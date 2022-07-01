import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1102   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雪拉扎德'),
    TXT(0x02, '奥利维尔'),
    TXT(0x03, '科洛丝'),
    TXT(0x04, '阿加特'),
    TXT(0x05, '提妲'),
    TXT(0x06, '金'),
    TXT(0x07, '乘客'),
    TXT(0x08, '乘客'),
    TXT(0x09, '乘客'),
    TXT(0x0A, '乘客'),
    TXT(0x0B, '乘客'),
    TXT(0x0C, '乘客'),
    TXT(0x0D, '奈尔'),
    TXT(0x0E, '朵洛希'),
    TXT(0x0F, '尤莉亚上尉'),
    TXT(0x10, '摩尔根将军'),
    TXT(0x11, '接待员泰德'),
    TXT(0x12, '拉克斯'),
    TXT(0x13, '诺尔姆'),
    TXT(0x14, '贝尔娜'),
    TXT(0x15, '阿尔丹'),
    TXT(0x16, '科尔娜'),
    TXT(0x17, '莫莉'),
    TXT(0x18, '赛希莉亚号乘客'),
    TXT(0x19, '赛希莉亚号乘客'),
    TXT(0x1A, '赛希莉亚号乘客'),
    TXT(0x1B, '赛希莉亚号乘客'),
    TXT(0x1C, '赛希莉亚号乘客'),
    TXT(0x1D, '佩特洛夫船长'),
    TXT(0x1E, '乘务员诺拉'),
    TXT(0x1F, '卡洛塔'),
    TXT(0x20, '沙库'),
    TXT(0x21, '飞艇'),
    TXT(0x22, '飞艇影'),
    TXT(0x23, '弗库利夫特'),
    TXT(0x24, '柏斯市·北街区'),
    TXT(0x25, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1102.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0x002B
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1102_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7FD0
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
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20129._CH', 'ED6_DT06/CH20129P._CP'),
        ('ED6_DT06/CH20051._CH', 'ED6_DT06/CH20051P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01453._CH', 'ED6_DT07/CH01453P._CP'),
        ('ED6_DT07/CH00051._CH', 'ED6_DT07/CH00051P._CP'),
        ('ED6_DT07/CH00061._CH', 'ED6_DT07/CH00061P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01440._CH', 'ED6_DT07/CH01440P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
    ]

# id: 0x10002 offset: 0x1BA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 46050,
            z                   = 0,
            y                   = 19400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 27300,
            z                   = -10000,
            y                   = 26800,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 48500,
            z                   = 1500,
            y                   = 36800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 51400,
            z                   = 0,
            y                   = 14100,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 51400,
            z                   = 1500,
            y                   = 47600,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 51400,
            z                   = 1500,
            y                   = 49740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 48340,
            z                   = 0,
            y                   = 12210,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 44940,
            z                   = 0,
            y                   = 15680,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 50290,
            z                   = 0,
            y                   = 16239,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 51900,
            z                   = 0,
            y                   = 13500,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 51890,
            z                   = 0,
            y                   = 14350,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 45050,
            z                   = 0,
            y                   = 11720,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 48780,
            z                   = 1500,
            y                   = 43400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 48140,
            z                   = 0,
            y                   = 18710,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 29420,
            z                   = -3000,
            y                   = 17280,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 50900,
            z                   = 0,
            y                   = 18020,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
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
            x                   = 48090,
            z                   = 3000,
            y                   = -20910,
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

# id: 0x10003 offset: 0x63A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x63A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 48000,
            y           = -2000,
            z           = 25600,
            range       = 52000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00006E8C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000017,
        ),
    )

# id: 0x10005 offset: 0x65A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 46070,
            triggerZ            = 0,
            triggerY            = 18140,
            triggerRange        = 600,
            actorX              = 46050,
            actorZ              = 1500,
            actorY              = 19400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 25480,
            triggerZ            = -3000,
            triggerY            = 11080,
            triggerRange        = 1600,
            actorX              = 25480,
            actorZ              = -1000,
            actorY              = 11080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 47780,
            triggerZ            = 0,
            triggerY            = 15880,
            triggerRange        = 800,
            actorX              = 47780,
            actorZ              = 2200,
            actorY              = 15880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0028,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 34950,
            triggerZ            = -10000,
            triggerY            = 24520,
            triggerRange        = 800,
            actorX              = 34950,
            actorZ              = -7800,
            actorY              = 24520,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0029,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 60000,
            triggerZ            = 0,
            triggerY            = 17090,
            triggerRange        = 800,
            actorX              = 60000,
            actorZ              = 1500,
            actorY              = 17090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x70E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_724',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0014)

    Jump('loc_77E')

    def _loc_724(): pass

    label('loc_724')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_743',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x65),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0019)

    Jump('loc_77E')

    def _loc_743(): pass

    label('loc_743')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_762',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 0x0024)

    Jump('loc_77E')

    def _loc_762(): pass

    label('loc_762')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_77E',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 0x0025)

    def _loc_77E(): pass

    label('loc_77E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_802',
    )

    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    SetChrPos(0x0019, 48770, 1500, 42170, 0)
    SetChrPos(0x001A, 31910, -10000, 26200, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7E9',
    )

    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    ClearChrFlags(0x0027, 0x0080)

    Jump('loc_7FF')

    def _loc_7E9(): pass

    label('loc_7E9')

    ClearChrFlags(0x001E, 0x0080)
    SetChrPos(0x0025, 51300, 1500, 35740, 96)

    def _loc_7FF(): pass

    label('loc_7FF')

    Jump('loc_8A4')

    def _loc_802(): pass

    label('loc_802')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_81B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_818',
    )

    ClearChrFlags(0x001D, 0x0080)

    def _loc_818(): pass

    label('loc_818')

    Jump('loc_8A4')

    def _loc_81B(): pass

    label('loc_81B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_836',
    )

    SetChrPos(0x001C, 46320, 3000, -1140, 0)

    Jump('loc_8A4')

    def _loc_836(): pass

    label('loc_836')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_867',
    )

    SetChrFlags(0x001C, 0x0080)
    SetChrPos(0x001A, 25620, -10000, 26830, 45)
    SetChrPos(0x001B, 25890, -3000, 17040, 0)

    Jump('loc_8A4')

    def _loc_867(): pass

    label('loc_867')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_89D',
    )

    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x0019, 0x0010)
    SetChrPos(0x0019, 27300, -10000, 26800, 0)
    SetChrPos(0x001A, 48500, 1500, 36800, 0)

    Jump('loc_8A4')

    def _loc_89D(): pass

    label('loc_89D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_8A4',
    )

    def _loc_8A4(): pass

    label('loc_8A4')

    Return()

# id: 0x0001 offset: 0x8A5
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE8518, 0xFFFE98A0, 0x00230042)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E5',
    )

    OP_B1('T1102_2')
    OP_72(0x0007, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_6F(0x0007, 410)

    Jump('loc_93D')

    def _loc_8E5(): pass

    label('loc_8E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_90C',
    )

    OP_B1('T1102_3')
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x0009, 0x0004)

    Jump('loc_93D')

    def _loc_90C(): pass

    label('loc_90C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_920',
    )

    OP_B1('T1102_2')

    Jump('loc_93D')

    def _loc_920(): pass

    label('loc_920')

    OP_B1('T1102_1')
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x0009, 0x0004)

    def _loc_93D(): pass

    label('loc_93D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_947',
    )

    Jump('loc_97E')

    def _loc_947(): pass

    label('loc_947')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_957',
    )

    OP_10(0x00, 0x00)
    OP_10(0x01, 0x01)

    Jump('loc_97E')

    def _loc_957(): pass

    label('loc_957')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_967',
    )

    OP_10(0x00, 0x00)
    OP_10(0x01, 0x01)

    Jump('loc_97E')

    def _loc_967(): pass

    label('loc_967')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_977',
    )

    OP_10(0x00, 0x00)
    OP_10(0x01, 0x01)

    Jump('loc_97E')

    def _loc_977(): pass

    label('loc_977')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_97E',
    )

    def _loc_97E(): pass

    label('loc_97E')

    OP_64(0x01, 0x0001)
    OP_A1(0x002A, 0x000D)
    SetChrPos(0x002A, 26510, -3000, 10000, 135)
    OP_72(0x000D, 0x0004)

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0078, 0x01, 0x0020)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0078, 0x01, 0x0040)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9C4',
    )

    OP_65(0x01, 0x0001)

    def _loc_9C4(): pass

    label('loc_9C4')

    Return()

# id: 0x0002 offset: 0x9C5
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9E8',
    )

    OP_8D(0x00FE, 45950, 15590, 50720, 11210, 1500)

    Jump('ReInit')

    def _loc_9E8(): pass

    label('loc_9E8')

    Return()

# id: 0x0003 offset: 0x9E9
@scena.Code('func_03_9E9')
def func_03_9E9():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x9EE
@scena.Code('func_04_9EE')
def func_04_9EE():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_AA9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A56',
    )

    ChrTalk(
        0x0018,
        (
            '那里的客人们……\n',
            '一直不肯离开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '这、这真是糟糕……\n',
            '船暂时无法出发……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_AA6')

    def _loc_A56(): pass

    label('loc_A56')

    ChrTalk(
        0x0018,
        (
            '嗯、一直在这里等\n',
            '我们也实在是为难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '也不知道什么时候\n',
            '才能恢复航行…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AA6(): pass

    label('loc_AA6')

    Jump('loc_1144')

    def _loc_AA9(): pass

    label('loc_AA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B16',
    )

    ChrTalk(
        0x0018,
        (
            '被滞留在这里的客人\n',
            '没有可去的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '现在准备把他们\n',
            '安排在酒店了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0018, 180, 400)
    SetChrFlags(0x0018, 0x0010)
    OP_A2(0x0000)

    Jump('loc_B5A')

    def _loc_B16(): pass

    label('loc_B16')

    ChrTalk(
        0x0018,
        (
            '已经安排各位\n',
            '住在旅馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '还要办理一些手续，\n',
            '请稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B5A(): pass

    label('loc_B5A')

    Jump('loc_1144')

    def _loc_B5D(): pass

    label('loc_B5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_C5E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_BBA',
    )

    ChrTalk(
        0x0018,
        (
            '听说捕获作战中\n',
            '游击士立下了大功呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '哈哈，现在协会\n',
            '一定很得意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C5B')

    def _loc_BBA(): pass

    label('loc_BBA')

    ChrTalk(
        0x0018,
        (
            '呀，各位，\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '听说捕获作战中\n',
            '游击士立下了大功呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '空贼事件时也是，\n',
            '这次已经是第二次让你们帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '哈哈，现在协会\n',
            '一定很得意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_C5B(): pass

    label('loc_C5B')

    Jump('loc_1144')

    def _loc_C5E(): pass

    label('loc_C5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_D34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_CB9',
    )

    ChrTalk(
        0x0018,
        (
            '『埃尔赛尤』的行动也\n',
            '开始紧张了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '捕获作战也\n',
            '进入佳境了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D31')

    def _loc_CB9(): pass

    label('loc_CB9')

    ChrTalk(
        0x0018,
        (
            '『埃尔赛尤』的行动也\n',
            '开始紧张了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '捕获作战也\n',
            '进入佳境了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '希望赶快解决它，\n',
            '然后解除飞行限制吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_D31(): pass

    label('loc_D31')

    Jump('loc_1144')

    def _loc_D34(): pass

    label('loc_D34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_E0D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_D8D',
    )

    ChrTalk(
        0x0018,
        (
            '军队的舰艇\n',
            '准备在这里着陆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '请各位在右手边\n',
            '的第一飞船坪等待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E0A')

    def _loc_D8D(): pass

    label('loc_D8D')

    OP_62(0x0018, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0018,
        (
            '啊……\n',
            '是各位游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '军队的舰艇\n',
            '准备在这里着陆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '请在右手边的\n',
            '的第一飞船坪等待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_E0A(): pass

    label('loc_E0A')

    Jump('loc_1144')

    def _loc_E0D(): pass

    label('loc_E0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_EBE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_E6E',
    )

    ChrTalk(
        0x0018,
        (
            '巨、巨大的影子\n',
            '向西北方飞去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '不过船没有撞上，\n',
            '就是不幸中的大幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EBB')

    def _loc_E6E(): pass

    label('loc_E6E')

    ChrTalk(
        0x0018,
        (
            '巨、巨大的影子\n',
            '从天上飞过去了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '那、那个\n',
            '难道就是传说中的龙？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_EBB(): pass

    label('loc_EBB')

    Jump('loc_1144')

    def _loc_EBE(): pass

    label('loc_EBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1144',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0348, 3, 0x1A43)),
            Expr.Return,
        ),
        'loc_1021',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FE0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_F2E',
    )

    ChrTalk(
        0x0018,
        (
            '最近定期船的航行也恢复了，\n',
            '真让人高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '政变之后，\n',
            '情况一直很稳定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FDD')

    def _loc_F2E(): pass

    label('loc_F2E')

    ChrTalk(
        0x0018,
        (
            '最近定期船的航行也恢复了，\n',
            '真让人高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '政变之后，\n',
            '情况一直很稳定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '听说空贼团把船\n',
            '夺走以后还很担心…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '不过之后他们就杳无音信了，\n',
            '大概是逃到国外了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_FDD(): pass

    label('loc_FDD')

    Jump('loc_101E')

    def _loc_FE0(): pass

    label('loc_FE0')

    ChrTalk(
        0x0018,
        (
            '阿加特先生\n',
            '好像总是很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '偶尔也好好\n',
            '休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_101E(): pass

    label('loc_101E')

    Jump('loc_1144')

    def _loc_1021(): pass

    label('loc_1021')

    ChrTurnDirection(0x0018, 0x0106, 0)

    ChrTalk(
        0x0018,
        (
            '啊，阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F哟，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '啊啊，是吗。\n',
            '好像刚回来啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '……今年也特意回乡看看吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#053F不，这次是为了工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#051F不过等解决之后\n',
            '也准备回去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '偶尔回去\n',
            '休息一下也不坏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '那么，要是有需要的话\n',
            '就再来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F啊，那先这样啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A43)
    OP_A2(0x0000)

    def _loc_1144(): pass

    label('loc_1144')

    TalkEnd(0x0018)

    Return()

# id: 0x0005 offset: 0x1148
@scena.Code('func_05_1148')
def func_05_1148():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_119B',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船的航行\n',
            '也恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '延期的旅行这下\n',
            '终于可以出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_146C')

    def _loc_119B(): pass

    label('loc_119B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1249',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_11E5',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船还没有恢复，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅行看来还是\n',
            '延期比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1246')

    def _loc_11E5(): pass

    label('loc_11E5')

    ChrTalk(
        0x00FE,
        (
            '定期船还没有恢复，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '军队的制度\n',
            '什么时候才能解除呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅行看来还是\n',
            '延期比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1246(): pass

    label('loc_1246')

    Jump('loc_146C')

    def _loc_1249(): pass

    label('loc_1249')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1336',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_129F',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～我本来想去旅行的，\n',
            '但定期船竟然停航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还真是不巧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1333')

    def _loc_129F(): pass

    label('loc_129F')

    ChrTalk(
        0x00FE,
        (
            '都是因为军队的制度，\n',
            '所以飞船才会停航。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～我本来想去旅行的，\n',
            '可为什么定期船会停航啊？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上次想要旅行的时候\n',
            '就遇到了空贼事件呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1333(): pass

    label('loc_1333')

    Jump('loc_146C')

    def _loc_1336(): pass

    label('loc_1336')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_138D',
    )

    ChrTalk(
        0x00FE,
        (
            '那、那是什么啊？！那个怪物！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从、从哪里冒出来的啊，\n',
            '那种东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_146C')

    def _loc_138D(): pass

    label('loc_138D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_146C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_13E6',
    )

    ChrTalk(
        0x00FE,
        (
            '明天要去王都，\n',
            '所以特意来定船票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以的话，想定\n',
            '下午的票呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_146C')

    def _loc_13E6(): pass

    label('loc_13E6')

    ChrTalk(
        0x00FE,
        (
            '明天要去王都，\n',
            '所以特意来定船票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前发生空贼事件的时候\n',
            '定期船就遇到了很大的麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从那以后，飞船\n',
            '就做了很多改变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_146C(): pass

    label('loc_146C')

    TalkEnd(0x001B)

    Return()

# id: 0x0006 offset: 0x1470
@scena.Code('func_06_1470')
def func_06_1470():
    TalkBegin(0x001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1579',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1500',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～飞船坪\n',
            '我可是每天都来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可为什么『埃尔赛尤』\n',
            '出现的时候我偏偏不在！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '笨蛋笨蛋！！我真是个笨蛋！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1576')

    def _loc_1500(): pass

    label('loc_1500')

    ChrTalk(
        0x00FE,
        (
            '今天早上本来想来\n',
            '拍摄飞船的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但因为心情不好\n',
            '就没有来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果没看到『埃尔赛尤』，\n',
            '真是大受打击啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_1576(): pass

    label('loc_1576')

    Jump('loc_17C8')

    def _loc_1579(): pass

    label('loc_1579')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1685',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0348, 6, 0x1A46)),
            Expr.Return,
        ),
        'loc_15CF',
    )

    ChrTalk(
        0x00FE,
        (
            '竟、竟然会错过\n',
            '埃尔赛尤号…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '笨蛋笨蛋！！我真是个笨蛋！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1682')

    def _loc_15CF(): pass

    label('loc_15CF')

    ChrTalk(
        0x00FE,
        (
            '喂、喂、你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '埃尔赛尤号\n',
            '在这里着陆是真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯、确实来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过已经飞走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(3000)

    OP_63(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#3S啊───────',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '错、错过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A46)

    def _loc_1682(): pass

    label('loc_1682')

    Jump('loc_17C8')

    def _loc_1685(): pass

    label('loc_1685')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_17C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1704',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然没有看到『埃尔赛尤』，\n',
            '但也是个不错的摄影旅行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是以后再遇到的话，\n',
            '一定把这次的也补拍回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17C8')

    def _loc_1704(): pass

    label('loc_1704')

    ChrTalk(
        0x00FE,
        (
            '呼～总算是\n',
            '回到柏斯了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我为了追随『埃尔赛尤』\n',
            '在蔡斯和王都之间东奔西走……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果还是没有遇到。\n',
            '不过这次的摄影旅行也算不错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好！下次有机会的话\n',
            '一定要拍到\n',
            '最完美的照片！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_17C8(): pass

    label('loc_17C8')

    TalkEnd(0x001C)

    Return()

# id: 0x0007 offset: 0x17CC
@scena.Code('func_07_17CC')
def func_07_17CC():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_18F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1898',
    )

    ChrTalk(
        0x00FE,
        (
            '『赛希莉亚号』的引擎\n',
            '没有发现任何异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各零件也没有任何损伤，\n',
            '简直就是完美无瑕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器无法运转的原因\n',
            '实在是不明白啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看见现在这种结果，\n',
            '真是让人抱有期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_18F4')

    def _loc_1898(): pass

    label('loc_1898')

    ChrTalk(
        0x00FE,
        (
            '『赛希莉亚号』的引擎\n',
            '没有发现任何异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各零件也没有任何损伤，\n',
            '简直就是完美无瑕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18F4(): pass

    label('loc_18F4')

    Jump('loc_1EBF')

    def _loc_18F7(): pass

    label('loc_18F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1A16',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19AD',
    )

    ChrTalk(
        0x00FE,
        (
            '慎重起见，还是再检查一次\n',
            '『赛希莉亚号』的引擎吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果和导力器瘫痪的理由相同的话，\n',
            '就要检查一下装置了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好好调查一下内部，\n',
            '确认一下停止时的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_1A13')

    def _loc_19AD(): pass

    label('loc_19AD')

    ChrTalk(
        0x00FE,
        (
            '慎重起见，还是再检查一次\n',
            '『赛希莉亚号』的引擎吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好好调查一下内部，\n',
            '确认一下停止时的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A13(): pass

    label('loc_1A13')

    Jump('loc_1EBF')

    def _loc_1A16(): pass

    label('loc_1A16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1AD0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1A7A',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来就是『林德号』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，这艘船的整备，\n',
            '我们也不会出现一分钟的误差。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1ACD')

    def _loc_1A7A(): pass

    label('loc_1A7A')

    ChrTalk(
        0x00FE,
        (
            '很好！\n',
            '接下来就是『林德号』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船通航以后，\n',
            '果然干劲就是不同了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1ACD(): pass

    label('loc_1ACD')

    Jump('loc_1EBF')

    def _loc_1AD0(): pass

    label('loc_1AD0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_1B30',
    )

    ChrTalk(
        0x00FE,
        (
            '噢，是你们啊。\n',
            '调查进行得怎么样了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不知道是什么事件，\n',
            '总之要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EBF')

    def _loc_1B30(): pass

    label('loc_1B30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1C71',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1B99',
    )

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤』是艘比\n',
            '传闻中更优秀的船啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不但性能优秀，\n',
            '整备性之高也非常了得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C6E')

    def _loc_1B99(): pass

    label('loc_1B99')

    ChrTalk(
        0x00FE,
        (
            '呼，『埃尔赛尤』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我是第一次对这艘船进行整备，\n',
            '不过确实是前所未见的好船啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不但性能优秀，\n',
            '整备性也非常高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '细微的检查整备\n',
            '是非常重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果在非常时期，\n',
            '就需要迅速调整状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1C6E(): pass

    label('loc_1C6E')

    Jump('loc_1EBF')

    def _loc_1C71(): pass

    label('loc_1C71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1D58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1CC0',
    )

    ChrTalk(
        0x00FE,
        (
            '军队的船\n',
            '马上要准备着陆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也要准备\n',
            '迎接才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D55')

    def _loc_1CC0(): pass

    label('loc_1CC0')

    ChrTalk(
        0x00FE,
        (
            '军队的船\n',
            '马上要准备着陆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也要准备\n',
            '迎接才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船都停止了，\n',
            '这次的战斗实在是不得了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但如今也\n',
            '只有祈祷努力有效果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1D55(): pass

    label('loc_1D55')

    Jump('loc_1EBF')

    def _loc_1D58(): pass

    label('loc_1D58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1E04',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1DAC',
    )

    ChrTalk(
        0x00FE,
        (
            '……古代龙吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那真是太危险了…\n',
            '这事情肯定会很严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E01')

    def _loc_1DAC(): pass

    label('loc_1DAC')

    ChrTalk(
        0x00FE,
        (
            '难道…\n',
            '刚才那东西…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……古代龙……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那真是太危险了…\n',
            '要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1E01(): pass

    label('loc_1E01')

    Jump('loc_1EBF')

    def _loc_1E04(): pass

    label('loc_1E04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1EBF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1E55',
    )

    ChrTalk(
        0x00FE,
        (
            '到『林德号』来之前\n',
            '还有些时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来检查一下\n',
            '材料吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EBF')

    def _loc_1E55(): pass

    label('loc_1E55')

    ChrTalk(
        0x00FE,
        (
            '好！『赛希莉亚号』\n',
            '没有问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到『林德号』来之前\n',
            '还有些时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁现在检查一下\n',
            '材料吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1EBF(): pass

    label('loc_1EBF')

    TalkEnd(0x0019)

    Return()

# id: 0x0008 offset: 0x1EC3
@scena.Code('func_08_1EC3')
def func_08_1EC3():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1FAD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F58',
    )

    ChrTalk(
        0x00FE,
        (
            '『赛希莉亚号』\n',
            '还和以前一样停在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连拉克斯主任\n',
            '好像也都很头疼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是第一次看到。\n',
            '主任一脸那种表情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_1FAA')

    def _loc_1F58(): pass

    label('loc_1F58')

    ChrTalk(
        0x00FE,
        (
            '连拉克斯主任\n',
            '好像也都很头疼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是第一次看到。\n',
            '主任一脸那种表情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FAA(): pass

    label('loc_1FAA')

    Jump('loc_24B7')

    def _loc_1FAD(): pass

    label('loc_1FAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_20DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2065',
    )

    ChrTalk(
        0x00FE,
        (
            '不只是『赛希莉亚号』，\n',
            '诱导灯和各种设施也都无法运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然以前也发生过类似故障，\n',
            '但从来都没有这么严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道说这也是因为\n',
            '昨天晚上异变的影响吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_20DB')

    def _loc_2065(): pass

    label('loc_2065')

    ChrTalk(
        0x00FE,
        (
            '不只是『赛希莉亚号』，\n',
            '诱导灯和各种设施也都无法运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然以前也发生过类似故障，\n',
            '但从来都没有这么严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20DB(): pass

    label('loc_20DB')

    Jump('loc_24B7')

    def _loc_20DE(): pass

    label('loc_20DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_21C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2147',
    )

    ChrTalk(
        0x00FE,
        (
            '托你们的福，\n',
            '定期船终于恢复航行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市也开始营业了，\n',
            '这下总算是回到正轨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21C0')

    def _loc_2147(): pass

    label('loc_2147')

    ChrTalk(
        0x00FE,
        (
            '托你们的福，\n',
            '定期船终于恢复航行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市也开始营业了，\n',
            '这下总算是回到正轨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好！我们也要加油工作啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_21C0(): pass

    label('loc_21C0')

    Jump('loc_24B7')

    def _loc_21C3(): pass

    label('loc_21C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_227E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_21FD',
    )

    ChrTalk(
        0x00FE,
        (
            '真没想到『埃尔赛尤』\n',
            '会在这着陆啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_227B')

    def _loc_21FD(): pass

    label('loc_21FD')

    ChrTalk(
        0x00FE,
        (
            '真，真没想到『埃尔赛尤』\n',
            '会在这着陆啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有些紧张，但现在\n',
            '还是要冷静工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也多亏拉克斯主任\n',
            '平时的指导啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_227B(): pass

    label('loc_227B')

    Jump('loc_24B7')

    def _loc_227E(): pass

    label('loc_227E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_232C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_22BE',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船停止航行了，\n',
            '不过王国军的飞船来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2329')

    def _loc_22BE(): pass

    label('loc_22BE')

    ChrTalk(
        0x00FE,
        (
            '定期船停止航行了，\n',
            '不过王国军的飞船来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然已经提前做了准备，\n',
            '但对定期船来说还是很麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_2329(): pass

    label('loc_2329')

    Jump('loc_24B7')

    def _loc_232C(): pass

    label('loc_232C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_23B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2366',
    )

    ChrTalk(
        0x00FE,
        (
            '刚、刚才飞过去\n',
            '的那个怪物是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B5')

    def _loc_2366(): pass

    label('loc_2366')

    ChrTalk(
        0x00FE,
        (
            '刚、刚才飞过去\n',
            '的那个怪物是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简、简直和定期船\n',
            '一样大啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_23B5(): pass

    label('loc_23B5')

    Jump('loc_24B7')

    def _loc_23B8(): pass

    label('loc_23B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_24B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2425',
    )

    ChrTalk(
        0x00FE,
        (
            '好，总算是把\n',
            '『赛希莉亚号』送上天了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船从着陆到出航\n',
            '的时间很短，真是麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B7')

    def _loc_2425(): pass

    label('loc_2425')

    ChrTalk(
        0x00FE,
        (
            '『赛希莉亚号』\n',
            '按原定时间出航……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各种设备没有异常…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好！这次也要\n',
            '准时起飞才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船从着陆到出航\n',
            '的时间很短，真是麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_24B7(): pass

    label('loc_24B7')

    TalkEnd(0x001A)

    Return()

# id: 0x0009 offset: 0x24BB
@scena.Code('func_09_24BB')
def func_09_24BB():
    TalkBegin(0x001D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_25FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2517',
    )

    ChrTalk(
        0x00FE,
        (
            '我以后也许\n',
            '还会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各位，如果方便的话，\n',
            '请代我向她问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25FA')

    def _loc_2517(): pass

    label('loc_2517')

    ChrTalk(
        0x00FE,
        (
            '啊，各位…\n',
            '谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊～莉拉的婶婶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '您要回自治州了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，虽然离开她有些寂寞，\n',
            '但我的目的已经达到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请代我向莉拉\n',
            '问好吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '也向您全家问好哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好的、那么再见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_25FA(): pass

    label('loc_25FA')

    TalkEnd(0x001D)

    Return()

# id: 0x000A offset: 0x25FE
@scena.Code('func_0A_25FE')
def func_0A_25FE():
    TalkBegin(0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2659',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，定期船\n',
            '到底什么时候才能起飞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～～已经等得\n',
            '急死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_2686')

    def _loc_2659(): pass

    label('loc_2659')

    ChrTalk(
        0x00FE,
        (
            '真是的，定期船\n',
            '到底什么时候才能起飞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2686(): pass

    label('loc_2686')

    TalkEnd(0x001E)

    Return()

# id: 0x000B offset: 0x268A
@scena.Code('func_0B_268A')
def func_0B_268A():
    TalkBegin(0x001F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_26D8',
    )

    ChrTalk(
        0x00FE,
        (
            '我就在这里一直等吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样要能起飞的话\n',
            '马上就可以知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2750')

    def _loc_26D8(): pass

    label('loc_26D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2750',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_272D',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '要等到什么时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可是急着\n',
            '要回卢安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_2750')

    def _loc_272D(): pass

    label('loc_272D')

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '要等到什么时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2750(): pass

    label('loc_2750')

    TalkEnd(0x001F)

    Return()

# id: 0x000C offset: 0x2754
@scena.Code('func_0C_2754')
def func_0C_2754():
    TalkBegin(0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27AE',
    )

    ChrTalk(
        0x00FE,
        (
            '似乎是原因不明的故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然使用了这么多年，\n',
            '但还是第一次遇到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_27F5')

    def _loc_27AE(): pass

    label('loc_27AE')

    ChrTalk(
        0x00FE,
        (
            '似乎是原因不明的故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器无法运转，\n',
            '或许也是同样原因吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27F5(): pass

    label('loc_27F5')

    TalkEnd(0x0020)

    Return()

# id: 0x000D offset: 0x27F9
@scena.Code('func_0D_27F9')
def func_0D_27F9():
    TalkBegin(0x0021)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2845',
    )

    ChrTalk(
        0x00FE,
        (
            '真头疼啊…\n',
            '竟然会被困在这种地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孩子也在一起…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_286C')

    def _loc_2845(): pass

    label('loc_2845')

    ChrTalk(
        0x00FE,
        (
            '真头疼啊…\n',
            '竟然会被困在这种地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_286C(): pass

    label('loc_286C')

    TalkEnd(0x0021)

    Return()

# id: 0x000E offset: 0x2870
@scena.Code('func_0E_2870')
def func_0E_2870():
    TalkBegin(0x0022)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28B4',
    )

    ChrTalk(
        0x00FE,
        (
            '喂、那船\n',
            '到底怎么了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么还不出发？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    Jump('loc_28D1')

    def _loc_28B4(): pass

    label('loc_28B4')

    ChrTalk(
        0x00FE,
        (
            '喂、那船\n',
            '到底怎么了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28D1(): pass

    label('loc_28D1')

    TalkEnd(0x0022)

    Return()

# id: 0x000F offset: 0x28D5
@scena.Code('func_0F_28D5')
def func_0F_28D5():
    TalkBegin(0x0023)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_292C',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到定期船\n',
            '它不能动了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是没办法，\n',
            '接下来还有工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    Jump('loc_2951')

    def _loc_292C(): pass

    label('loc_292C')

    ChrTalk(
        0x00FE,
        (
            '真是没办法，\n',
            '接下来还有工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2951(): pass

    label('loc_2951')

    TalkEnd(0x0023)

    Return()

# id: 0x0010 offset: 0x2955
@scena.Code('func_10_2955')
def func_10_2955():
    TalkBegin(0x0024)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2A51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29F0',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，和我想的一样，\n',
            '船没有任何异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '引擎停止运转\n',
            '也是和之前那些现象相同吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……完全束手无策了。\n',
            '我们什么也做不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    Jump('loc_2A4E')

    def _loc_29F0(): pass

    label('loc_29F0')

    ChrTalk(
        0x00FE,
        (
            '引擎停止运转\n',
            '也是和之前那些现象相同吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我们完全束手无策了。\n',
            '我们什么也做不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A4E(): pass

    label('loc_2A4E')

    Jump('loc_2B6D')

    def _loc_2A51(): pass

    label('loc_2A51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2B6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AF5',
    )

    ChrTalk(
        0x00FE,
        (
            '这次完全不是故障，\n',
            '以前的解决方法全都没用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里的梯子也准备了紧急时刻用的\n',
            '手摇伸缩设备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望客人们也能多了解\n',
            '一些导力原理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    Jump('loc_2B6D')

    def _loc_2AF5(): pass

    label('loc_2AF5')

    ChrTalk(
        0x00FE,
        (
            '呼，不管怎么说，\n',
            '故障在起飞前出现还算是幸运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果要是飞到一半时遇到这种情况的话，\n',
            '现在大家就都要去见女神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B6D(): pass

    label('loc_2B6D')

    TalkEnd(0x0024)

    Return()

# id: 0x0011 offset: 0x2B71
@scena.Code('func_11_2B71')
def func_11_2B71():
    TalkBegin(0x0025)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2C34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BD9',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船的恢复看来\n',
            '是个很麻烦的问题啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各位维修员也都\n',
            '在抱着头烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    Jump('loc_2C31')

    def _loc_2BD9(): pass

    label('loc_2BD9')

    ChrTalk(
        0x00FE,
        (
            '定期船的恢复看来\n',
            '是个很麻烦的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公社那边现在已经正在考虑\n',
            '什么对策了吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C31(): pass

    label('loc_2C31')

    Jump('loc_2D49')

    def _loc_2C34(): pass

    label('loc_2C34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2D49',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CF1',
    )

    ChrTalk(
        0x00FE,
        (
            '停在这里的是\n',
            '今天早上的航班…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果故障严重的话，\n',
            '就没法出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸好客人们都没受伤，\n',
            '还是值得高兴的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果起飞之后再遇到故障的话，\n',
            '那可就不得了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    Jump('loc_2D49')

    def _loc_2CF1(): pass

    label('loc_2CF1')

    ChrTalk(
        0x00FE,
        (
            '停在这里的是\n',
            '今天早上的航班…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '航行到底要到什么时候才能恢复，\n',
            '我们也不知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D49(): pass

    label('loc_2D49')

    TalkEnd(0x0025)

    Return()

# id: 0x0012 offset: 0x2D4D
@scena.Code('func_12_2D4D')
def func_12_2D4D():
    TalkBegin(0x0026)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DCD',
    )

    ChrTalk(
        0x00FE,
        (
            '定购的商品今天\n',
            '本来可以收到的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是定期船停运了。\n',
            '呼～真没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只能赶快去找替代用\n',
            '的商品了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000F)

    Jump('loc_2E17')

    def _loc_2DCD(): pass

    label('loc_2DCD')

    ChrTalk(
        0x00FE,
        (
            '定购的商品今天\n',
            '本来可以收到的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只能赶快去找替代用\n',
            '的商品了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E17(): pass

    label('loc_2E17')

    TalkEnd(0x0026)

    Return()

# id: 0x0013 offset: 0x2E1B
@scena.Code('func_13_2E1B')
def func_13_2E1B():
    TalkBegin(0x0027)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2ED0',
    )

    ChrTalk(
        0x00FE,
        (
            '呼呼……\n',
            '定期船停运了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器停了，\n',
            '船不能动也是当然的啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，真让人头疼啊。\n',
            '这样的话，就没办法做货物输出工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只能在当地\n',
            '找找买家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)

    Jump('loc_2F26')

    def _loc_2ED0(): pass

    label('loc_2ED0')

    ChrTalk(
        0x00FE,
        (
            '定期船无法航行了，\n',
            '货物输出工作也就没法做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在也只能在当地\n',
            '找找买家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F26(): pass

    label('loc_2F26')

    TalkEnd(0x0027)

    Return()

# id: 0x0014 offset: 0x2F2A
@scena.Code('func_14_2F2A')
def func_14_2F2A():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0101, 0x0080)
    OP_6D(76390, 30000, 24550, 0)
    OP_67(0, 45040, -55000, 0)
    OP_6B(900, 0)
    OP_6C(321000, 0)
    OP_6E(262, 0)
    OP_12(0x0000A410, 0x0003D090, 0x00000000)
    OP_A1(0x0028, 0x0007)
    OP_72(0x0007, 0x0004)
    OP_72(0x0007, 0x0020)
    SetChrPos(0x0028, 62250, 10650, 41990, 0)
    OP_6F(0x0007, 60)
    OP_A1(0x0029, 0x0008)
    OP_72(0x0008, 0x0004)
    SetChrPos(0x0029, 62250, 5650, 41990, 0)
    OP_72(0x000A, 0x0004)
    OP_6F(0x000A, 100)
    SetChrFlags(0x001A, 0x0080)
    OP_22(0x0079, 0x00, 0x64)
    CreateThread(0x0028, 0x00, 0x00, 0x0016)
    OP_C8(0x0200, 0x0046, 'C_PLAC15._CH', 0x00, 0x07D0)
    ShowPlaceName('柏斯')
    FadeIn(2000, 0)
    WaitForThreadExit(0x0028, 0x0000)
    Yield()
    Fade(1000)
    OP_12(0x0000A410, 0x000222E0, 0x00000000)
    OP_6D(55790, 1500, 37990, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(38000, 0)
    OP_6E(262, 0)
    OP_71(0x000B, 0x0004)
    OP_0D()
    OP_22(0x0006, 0x00, 0x64)
    OP_6F(0x0007, 411)
    OP_70(0x0007, 0x000001C2)
    OP_22(0x0006, 0x00, 0x64)
    OP_73(0x0007)
    CreateThread(0x000E, 0x01, 0x00, 0x0015)
    Sleep(800)

    CreateThread(0x000F, 0x01, 0x00, 0x0015)
    Sleep(1000)

    CreateThread(0x0010, 0x01, 0x00, 0x0015)
    Sleep(1000)

    CreateThread(0x0011, 0x01, 0x00, 0x0015)
    Sleep(1200)

    CreateThread(0x0012, 0x01, 0x00, 0x0015)
    Sleep(800)

    CreateThread(0x0013, 0x01, 0x00, 0x0015)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x00, 0x0015)
    Sleep(800)

    CreateThread(0x0008, 0x01, 0x00, 0x0015)
    Sleep(800)

    CreateThread(0x000B, 0x01, 0x00, 0x0015)
    Sleep(800)

    CreateThread(0x000C, 0x01, 0x00, 0x0015)
    Sleep(800)

    CreateThread(0x000A, 0x01, 0x00, 0x0015)
    Sleep(800)

    CreateThread(0x0009, 0x01, 0x00, 0x0015)
    Sleep(800)

    CreateThread(0x000D, 0x01, 0x00, 0x0015)
    Sleep(3000)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x3134
@scena.Code('func_15_3134')
def func_15_3134():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 62290, 1600, 42020, 180)
    OP_8E(0x00FE, 62290, 1500, 37870, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, 56690, 1500, 37870, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, 49400, 1500, 37870, 2000, 0x00)
    OP_8E(0x00FE, 49400, 0, 24600, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0016 offset: 0x31AF
@scena.Code('func_16_31AF')
def func_16_31AF():
    @scena.Lambda('lambda_31B5')
    def lambda_31B5():
        OP_8F(0x00FE, 62250, -5650, 41990, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_31B5)

    @scena.Lambda('lambda_31D0')
    def lambda_31D0():
        OP_8F(0x00FE, 62250, -5650, 41990, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_31D0)

    Sleep(100)

    @scena.Lambda('lambda_31F0')
    def lambda_31F0():
        OP_8F(0x00FE, 62250, -5650, 41990, 300, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_31F0)

    @scena.Lambda('lambda_320B')
    def lambda_320B():
        OP_8F(0x00FE, 62250, -5650, 41990, 300, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_320B)

    Sleep(100)

    @scena.Lambda('lambda_322B')
    def lambda_322B():
        OP_8F(0x00FE, 62250, -5650, 41990, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_322B)

    @scena.Lambda('lambda_3246')
    def lambda_3246():
        OP_8F(0x00FE, 62250, -5650, 41990, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_3246)

    Sleep(100)

    @scena.Lambda('lambda_3266')
    def lambda_3266():
        OP_6D(76390, 20000, 24550, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3266)

    Sleep(100)

    @scena.Lambda('lambda_3283')
    def lambda_3283():
        OP_8F(0x00FE, 62250, -5650, 41990, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_3283)

    @scena.Lambda('lambda_329E')
    def lambda_329E():
        OP_8F(0x00FE, 62250, -5650, 41990, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_329E)

    Sleep(100)

    @scena.Lambda('lambda_32BE')
    def lambda_32BE():
        OP_8F(0x00FE, 62250, -5650, 41990, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_32BE)

    @scena.Lambda('lambda_32D9')
    def lambda_32D9():
        OP_8F(0x00FE, 62250, -5650, 41990, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_32D9)

    Sleep(100)

    @scena.Lambda('lambda_32F9')
    def lambda_32F9():
        OP_8F(0x00FE, 62250, -5650, 41990, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_32F9)

    @scena.Lambda('lambda_3314')
    def lambda_3314():
        OP_8F(0x00FE, 62250, -5650, 41990, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_3314)

    Sleep(100)

    @scena.Lambda('lambda_3334')
    def lambda_3334():
        OP_8F(0x00FE, 62250, -5650, 41990, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_3334)

    @scena.Lambda('lambda_334F')
    def lambda_334F():
        OP_8F(0x00FE, 62250, -5650, 41990, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_334F)

    Sleep(100)

    @scena.Lambda('lambda_336F')
    def lambda_336F():
        OP_8F(0x00FE, 62250, -5650, 41990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_336F)

    @scena.Lambda('lambda_338A')
    def lambda_338A():
        OP_8F(0x00FE, 62250, -5650, 41990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_338A)

    Sleep(100)

    @scena.Lambda('lambda_33AA')
    def lambda_33AA():
        OP_8F(0x00FE, 62250, -5650, 41990, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_33AA)

    @scena.Lambda('lambda_33C5')
    def lambda_33C5():
        OP_8F(0x00FE, 62250, -5650, 41990, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_33C5)

    Sleep(100)

    @scena.Lambda('lambda_33E5')
    def lambda_33E5():
        OP_8F(0x00FE, 62250, -5650, 41990, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_33E5)

    Sleep(3200)

    @scena.Lambda('lambda_3405')
    def lambda_3405():
        OP_8F(0x00FE, 62250, -5650, 41990, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_3405)

    @scena.Lambda('lambda_3420')
    def lambda_3420():
        OP_8F(0x00FE, 62250, -5650, 41990, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_3420)

    Sleep(200)

    @scena.Lambda('lambda_3440')
    def lambda_3440():
        OP_8F(0x00FE, 62250, -5650, 41990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_3440)

    @scena.Lambda('lambda_345B')
    def lambda_345B():
        OP_8F(0x00FE, 62250, -5650, 41990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_345B)

    Sleep(200)

    @scena.Lambda('lambda_347B')
    def lambda_347B():
        OP_8F(0x00FE, 62250, -5650, 41990, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_347B)

    @scena.Lambda('lambda_3496')
    def lambda_3496():
        OP_8F(0x00FE, 62250, -5650, 41990, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_3496)

    Sleep(200)

    @scena.Lambda('lambda_34B6')
    def lambda_34B6():
        OP_8F(0x00FE, 62250, -5650, 41990, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_34B6)

    @scena.Lambda('lambda_34D1')
    def lambda_34D1():
        OP_8F(0x00FE, 62250, -5650, 41990, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_34D1)

    Sleep(200)

    @scena.Lambda('lambda_34F1')
    def lambda_34F1():
        OP_8F(0x00FE, 62250, -5650, 41990, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_34F1)

    @scena.Lambda('lambda_350C')
    def lambda_350C():
        OP_8F(0x00FE, 62250, -5650, 41990, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_350C)

    Sleep(200)

    @scena.Lambda('lambda_352C')
    def lambda_352C():
        OP_8F(0x00FE, 62250, -5650, 41990, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_352C)

    @scena.Lambda('lambda_3547')
    def lambda_3547():
        OP_8F(0x00FE, 62250, -5650, 41990, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_3547)

    Sleep(200)

    @scena.Lambda('lambda_3567')
    def lambda_3567():
        OP_8F(0x00FE, 62250, -5650, 41990, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_3567)

    @scena.Lambda('lambda_3582')
    def lambda_3582():
        OP_8F(0x00FE, 62250, -5650, 41990, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_3582)

    Sleep(200)

    @scena.Lambda('lambda_35A2')
    def lambda_35A2():
        OP_8F(0x00FE, 62250, -5650, 41990, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_35A2)

    @scena.Lambda('lambda_35BD')
    def lambda_35BD():
        OP_8F(0x00FE, 62250, -5650, 41990, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_35BD)

    Sleep(100)

    @scena.Lambda('lambda_35DD')
    def lambda_35DD():
        OP_8F(0x00FE, 62250, -5650, 41990, 400, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_35DD)

    @scena.Lambda('lambda_35F8')
    def lambda_35F8():
        OP_8F(0x00FE, 62250, -5650, 41990, 400, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_35F8)

    Sleep(100)

    @scena.Lambda('lambda_3618')
    def lambda_3618():
        OP_8F(0x00FE, 62250, -5650, 41990, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_3618)

    @scena.Lambda('lambda_3633')
    def lambda_3633():
        OP_8F(0x00FE, 62250, -5650, 41990, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_3633)

    WaitForThreadExit(0x0028, 0x0001)
    WaitForThreadExit(0x0029, 0x0001)
    OP_23(0x0079)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x00000064)
    SetChrPos(0x0028, 62250, -5650, 41990, 0)
    Sleep(1000)

    OP_22(0x0076, 0x00, 0x46)
    OP_B0(0x0007, 0x3C)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0x00000001)
    Sleep(1000)

    OP_22(0x0078, 0x00, 0x64)
    OP_6F(0x000A, 100)
    OP_70(0x000A, 0x000000C8)
    Sleep(2500)

    TerminateThread(0x0101, 0x01)

    Return()

# id: 0x0017 offset: 0x36BA
@scena.Code('func_17_36BA')
def func_17_36BA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_36C7',
    )

    Return()

    def _loc_36C7(): pass

    label('loc_36C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 5, 0x1A1D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C4A',
    )

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
        'loc_36F4',
    )

    Call(0, 0x0026)
    Call(0, 0x0027)
    FadeIn(0, 0)
    Sleep(200)

    def _loc_36F4(): pass

    label('loc_36F4')

    OP_A2(0x1A1D)
    Fade(1000)
    Call(0, 0x0022)
    OP_6D(48920, 1500, 32350, 0)
    OP_67(0, 7740, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(246000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 49200, 250, 25720, 0)
    SetChrPos(0x0103, 48730, 0, 24660, 0)
    SetChrPos(0x0105, 49640, 0, 24560, 0)
    SetChrPos(0x0108, 48740, 0, 23580, 0)
    SetChrPos(0x0104, 49910, 0, 23460, 0)

    @scena.Lambda('lambda_3798')
    def lambda_3798():
        OP_8E(0x00FE, 49200, 1500, 33570, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3798)

    Sleep(300)

    @scena.Lambda('lambda_37B8')
    def lambda_37B8():
        OP_8E(0x00FE, 48730, 1500, 32439, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_37B8)

    Sleep(70)

    @scena.Lambda('lambda_37D8')
    def lambda_37D8():
        OP_8E(0x00FE, 49900, 1500, 32470, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_37D8)

    Sleep(300)

    @scena.Lambda('lambda_37F8')
    def lambda_37F8():
        OP_8E(0x00FE, 48740, 1500, 31350, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_37F8)

    Sleep(80)

    @scena.Lambda('lambda_3818')
    def lambda_3818():
        OP_8E(0x00FE, 49910, 1500, 31330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_3818)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    OP_8C(0x0101, 270, 400)
    OP_12(0x0000A410, 0x00038270, 0x00001770)

    @scena.Lambda('lambda_3852')
    def lambda_3852():
        OP_6D(53530, 1500, 39100, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3852)

    @scena.Lambda('lambda_386A')
    def lambda_386A():
        OP_67(0, 8530, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_386A)

    @scena.Lambda('lambda_3882')
    def lambda_3882():
        OP_6B(4300, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3882)

    @scena.Lambda('lambda_3892')
    def lambda_3892():
        OP_6E(431, 6000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_3892)

    Sleep(1500)

    OP_8C(0x0101, 0, 400)
    OP_8C(0x0101, 90, 400)
    Sleep(1500)

    OP_8C(0x0101, 45, 400)
    Sleep(3000)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0103, 0x01)
    Fade(1000)
    OP_12(0x0000A410, 0x000222E0, 0x00000000)
    OP_6D(48920, 1500, 32350, 0)
    OP_67(0, 7740, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(246000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010310057V#1015F嗯～军队的飞艇\n',
            '好像还没来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_39C7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030310058V#020F想买东西的话\n',
            '现在倒是还有时间…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310059V怎么办呢？艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A8F')

    def _loc_39C7(): pass

    label('loc_39C7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3A37',
    )

    ChrTalk(
        0x0108,
        (
            '#0080310062V#070F想买东西的话\n',
            '现在倒是还有时间…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310063V怎么办？艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A8F')

    def _loc_3A37(): pass

    label('loc_3A37')

    ChrTalk(
        0x0103,
        (
            '#0030310058V#020F想买东西的话\n',
            '现在倒是还有时间…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310059V怎么办呢？艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A8F(): pass

    label('loc_3A8F')

    OP_8C(0x0101, 180, 400)
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
            TXT(0x00, '【等待军舰到来】\n'),
            TXT(0x01, '【先回到街上】\n'),
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
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BFE',
    )

    ChrTalk(
        0x0101,
        (
            '#0010310065V#1006F嗯～还是先回街上\n',
            '买些东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0023)
    OP_6D(50090, 0, 24550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 50090, 0, 24550, 180)
    SetChrPos(0x0103, 50090, 0, 24550, 180)
    SetChrPos(0x0104, 50090, 0, 24550, 180)
    SetChrPos(0x0105, 50090, 0, 24550, 180)
    SetChrPos(0x0108, 50090, 0, 24550, 180)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF9, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFF, 0xFF)
    OP_30(0x00)
    Sleep(500)

    FadeIn(1000, 0)

    Jump('loc_3C47')

    def _loc_3BFE(): pass

    label('loc_3BFE')

    ChrTalk(
        0x0101,
        (
            '#0010310069V#1006F那么，就在这里\n',
            '等军舰到来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    Call(0, 0x0018)

    def _loc_3C47(): pass

    label('loc_3C47')

    Jump('loc_3EDE')

    def _loc_3C4A(): pass

    label('loc_3C4A')

    EventBegin(0x02)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_3C68'),
        (0x00000002, 'loc_3CA0'),
        (0x00000003, 'loc_3CD4'),
        (0x00000004, 'loc_3D0C'),
        (0x00000007, 'loc_3D4D'),
        (-1, 'loc_3D89'),
    )

    def _loc_3C68(): pass

    label('loc_3C68')

    ChrTalk(
        0x0101,
        (
            '#0010310064V#1015F在１０点之前\n',
            '都算是空闲时间…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D89')

    def _loc_3CA0(): pass

    label('loc_3CA0')

    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030310066V#023F啊、还有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D89')

    def _loc_3CD4(): pass

    label('loc_3CD4')

    ChrTurnDirection(0x0104, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040310067V#033F啊、还有别的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D89')

    def _loc_3D0C(): pass

    label('loc_3D0C')

    ChrTurnDirection(0x0105, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x0105,
        (
            '#0060310070V#040F军舰马上就要来了，\n',
            '等等吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D89')

    def _loc_3D4D(): pass

    label('loc_3D4D')

    ChrTurnDirection(0x0108, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080310068V#073F喂，没有别的事情了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D89')

    def _loc_3D89(): pass

    label('loc_3D89')

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
            TXT(0x00, '【等待军舰到来】\n'),
            TXT(0x01, '【先回到街上】\n'),
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
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E8C',
    )

    FadeIn(300, 0)
    Sleep(300)

    Fade(500)
    OP_6D(50090, 0, 24550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 50090, 0, 24550, 180)
    SetChrPos(0x0103, 50090, 0, 24550, 180)
    SetChrPos(0x0104, 50090, 0, 24550, 180)
    SetChrPos(0x0105, 50090, 0, 24550, 180)
    SetChrPos(0x0108, 50090, 0, 24550, 180)
    OP_0D()

    Jump('loc_3EDE')

    def _loc_3E8C(): pass

    label('loc_3E8C')

    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010310069V#1006F那么，就在这里\n',
            '等军舰到来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    Call(0, 0x0018)

    def _loc_3EDE(): pass

    label('loc_3EDE')

    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x3EE1
@scena.Code('func_18_3EE1')
def func_18_3EE1():
    EventBegin(0x00)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_6D(50030, 1500, 34090, 0)
    OP_67(0, 6950, -10000, 0)
    OP_6B(3010, 0)
    OP_6C(107000, 0)
    OP_6E(282, 0)
    SetChrPos(0x0101, 51300, 1500, 34000, 270)
    SetChrPos(0x0008, 50450, 1500, 32850, 315)
    SetChrPos(0x000A, 50510, 1500, 35270, 225)
    SetChrPos(0x0009, 48710, 1500, 33730, 45)
    SetChrPos(0x000D, 48780, 1500, 35090, 135)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010310072V#1011F#5P来接我们的军用飞艇\n',
            '一定是艘很威风的装甲艇吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310073V#040F你是说警备飞艇吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310074V那是当然的，\n',
            '因为那是军队主力飞行舰艇啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030310075V#026F火力、装载量、机动性\n',
            '全都无比优秀的\n',
            '王国军用飞艇…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310076V#020F在１０年前开发出来之后\n',
            '也经过了多次改良，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310077V#047F是的，除了基本性能做了强化外，\n',
            '还追加了各种\n',
            '新装甲和武器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310078V#040F巡哨机、侦察机、攻击机……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310079V在不断的改进之下，\n',
            '如今已经组建了一支\n',
            '性能全面的舰队了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080310080V#070F#6P嗯……\n',
            '不愧是飞船的先进国家啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310081V#075F共和国虽然也有飞行舰队，\n',
            '不过完全就是纸老虎呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040310082V#035F呵呵，我们帝国也是一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310083V#030F虽然也有飞行舰队，\n',
            '但主力军毕竟还是战车部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x00A6, 0x00, 0x64)
    OP_20(0x00000BB8)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880310084V──王国军所属舰艇\n',
            '即将在第一飞船坪降落。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880310085V请无关人员\n',
            '迅速撤离。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010310086V#1006F喔！来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0125, 0x01, 0x14)
    Sleep(400)

    OP_24(0x0125, 0x1E)
    Sleep(400)

    OP_24(0x0125, 0x28)
    Sleep(400)

    OP_24(0x0125, 0x32)
    Sleep(400)

    OP_24(0x0125, 0x3C)
    Sleep(400)

    OP_24(0x0125, 0x46)
    Sleep(400)

    OP_24(0x0125, 0x50)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010310087V#1015F啊、那个？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310088V那种引擎的声音\n',
            '我好像从没听过呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310089V#044F这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4423')
    def lambda_4423():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4423)

    Sleep(100)

    @scena.Lambda('lambda_4436')
    def lambda_4436():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4436)

    Sleep(100)

    @scena.Lambda('lambda_4449')
    def lambda_4449():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4449)

    Sleep(100)

    @scena.Lambda('lambda_445C')
    def lambda_445C():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_445C)

    Sleep(100)

    OP_8C(0x000D, 45, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010310090V#1004F#4P啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMapFlags(0x00100000)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x44BD
@scena.Code('func_19_44BD')
def func_19_44BD():
    EventBegin(0x00)
    OP_DB()
    ClearMapFlags(0x00100000)
    OP_6D(76390, 30000, 28060, 0)
    OP_67(0, 45040, -55000, 0)
    OP_6B(900, 0)
    OP_6C(321000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 51120, 1800, 37530, 90)
    SetChrPos(0x0008, 49540, 1500, 37920, 90)
    SetChrPos(0x0009, 49180, 1500, 36690, 90)
    SetChrPos(0x000A, 50880, 1800, 38460, 90)
    SetChrPos(0x000D, 49140, 1500, 38860, 90)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    OP_E5(0x08, 0x00, 0x00)
    OP_E5(0x0A, 0x00, 0x00)
    OP_E5(0x0D, 0x00, 0x00)
    OP_E5(0x09, 0x00, 0x00)
    OP_12(0x0000A410, 0x0003D090, 0x00000000)
    OP_A1(0x0028, 0x0007)
    OP_72(0x0007, 0x0004)
    OP_72(0x0007, 0x0020)
    OP_6F(0x0007, 251)
    SetChrPos(0x0028, 62500, 17500, 44000, 0)
    OP_A1(0x0029, 0x0008)
    OP_72(0x0008, 0x0004)
    SetChrPos(0x0029, 62500, -2000, 44000, 0)
    OP_75(0x08, 0x00000000, 0x00)
    OP_74(0x0008, 0x00000000, 0x0000)
    OP_72(0x000A, 0x0004)
    OP_6F(0x000A, 100)
    OP_71(0x000B, 0x0004)
    FadeIn(1000, 0)
    Call(0, 0x0021)
    Fade(500)
    OP_6D(51270, 1800, 38190, 0)
    OP_67(0, 9040, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    OP_12(0x0000A410, 0x000222E0, 0x00000000)
    OP_E5(0x08, 0x00, 0x01)
    OP_E5(0x0A, 0x00, 0x01)
    OP_E5(0x0D, 0x00, 0x01)
    OP_E5(0x09, 0x00, 0x01)
    OP_0D()
    OP_22(0x0078, 0x00, 0x64)
    OP_6F(0x000A, 100)
    OP_70(0x000A, 0x000000C8)
    Sleep(2500)

    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010310091V#1008F#6P啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310092V我们要乘坐的飞船\n',
            '竟然是『埃尔赛尤』吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310093V#044F#6P昨天和尤莉亚联络的时候\n',
            '她并没有说过啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0014, 62300, 1500, 38740, 270)
    SetChrPos(0x0015, 62370, 1500, 40090, 270)
    SetChrChipByIndex(0x0015, 17)
    SetChrFlags(0x0014, 0x0004)
    SetChrFlags(0x0015, 0x0004)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)

    ExecExpressionWithValue(
        0x0014,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x006D, 0x00, 0x64)
    OP_6F(0x0007, 1888)
    OP_70(0x0007, 0x00000758)
    OP_73(0x0007)
    Sleep(500)

    NpcTalk(
        0x0014,
        '男人的声音',
        (
            '#0270310094V#3P哟～艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0015,
        '女孩的声音',
        (
            '#0280310095V#3P好久不见了～大家！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_4880')
    def lambda_4880():
        OP_6D(55520, 1500, 39550, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4880)

    @scena.Lambda('lambda_4898')
    def lambda_4898():
        OP_67(0, 5390, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4898)

    @scena.Lambda('lambda_48B0')
    def lambda_48B0():
        OP_6B(4040, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_48B0)

    @scena.Lambda('lambda_48C0')
    def lambda_48C0():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_48C0)

    @scena.Lambda('lambda_48D0')
    def lambda_48D0():
        OP_6E(236, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_48D0)

    @scena.Lambda('lambda_48E0')
    def lambda_48E0():
        ChrTurnDirection(0x00FE, 0x0014, 0)
        Yield()

        Jump('lambda_48E0')

    DispatchAsync2(0x0101, 0x0001, lambda_48E0)

    @scena.Lambda('lambda_48F1')
    def lambda_48F1():
        ChrTurnDirection(0x00FE, 0x0014, 0)
        Yield()

        Jump('lambda_48F1')

    DispatchAsync2(0x0008, 0x0001, lambda_48F1)

    @scena.Lambda('lambda_4902')
    def lambda_4902():
        ChrTurnDirection(0x00FE, 0x0014, 0)
        Yield()

        Jump('lambda_4902')

    DispatchAsync2(0x0009, 0x0001, lambda_4902)

    @scena.Lambda('lambda_4913')
    def lambda_4913():
        ChrTurnDirection(0x00FE, 0x0014, 0)
        Yield()

        Jump('lambda_4913')

    DispatchAsync2(0x000A, 0x0001, lambda_4913)

    @scena.Lambda('lambda_4924')
    def lambda_4924():
        ChrTurnDirection(0x00FE, 0x0014, 0)
        Yield()

        Jump('lambda_4924')

    DispatchAsync2(0x000D, 0x0001, lambda_4924)

    @scena.Lambda('lambda_4935')
    def lambda_4935():
        OP_8E(0x00FE, 59020, 1500, 38850, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_4935)

    Sleep(500)

    @scena.Lambda('lambda_4955')
    def lambda_4955():
        OP_8E(0x00FE, 59260, 1500, 39940, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_4955)

    WaitForThreadExit(0x0014, 0x0001)
    ChrTurnDirection(0x0014, 0x0101, 400)
    WaitForThreadExit(0x0015, 0x0001)
    ChrTurnDirection(0x0015, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000D, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010310096V#1020F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030310097V#023F#6P你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0270310098V#141F#2P嘿嘿，真是\n',
            '奇妙的再会啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0280310099V#151F#2P请多关照啊～\n',
            '艾丝蒂尔和大家！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310100V#1004F#6P为、为、为……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310101V为什么奈尔和朵洛希\n',
            '也会在埃尔赛尤号上！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0016, 62600, 1500, 42300, 180)

    ExecExpressionWithValue(
        0x0016,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0016, 0x0004)
    ClearChrFlags(0x0016, 0x0080)
    Sleep(500)

    NpcTalk(
        0x0016,
        '女性的声音',
        (
            '#0100310102V#7P……由我来\n',
            '做个说明吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4B1E')
    def lambda_4B1E():
        ChrTurnDirection(0x00FE, 0x0016, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4B1E)

    @scena.Lambda('lambda_4B2C')
    def lambda_4B2C():
        ChrTurnDirection(0x00FE, 0x0016, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4B2C)

    @scena.Lambda('lambda_4B3A')
    def lambda_4B3A():
        ChrTurnDirection(0x00FE, 0x0016, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_4B3A)

    @scena.Lambda('lambda_4B48')
    def lambda_4B48():
        ChrTurnDirection(0x00FE, 0x0016, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_4B48)

    @scena.Lambda('lambda_4B56')
    def lambda_4B56():
        ChrTurnDirection(0x00FE, 0x0016, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4B56)

    @scena.Lambda('lambda_4B64')
    def lambda_4B64():
        ChrTurnDirection(0x00FE, 0x0016, 0)
        Yield()

        Jump('lambda_4B64')

    DispatchAsync2(0x0101, 0x0001, lambda_4B64)

    @scena.Lambda('lambda_4B75')
    def lambda_4B75():
        ChrTurnDirection(0x00FE, 0x0016, 0)
        Yield()

        Jump('lambda_4B75')

    DispatchAsync2(0x000A, 0x0001, lambda_4B75)

    @scena.Lambda('lambda_4B86')
    def lambda_4B86():
        ChrTurnDirection(0x00FE, 0x0016, 0)
        Yield()

        Jump('lambda_4B86')

    DispatchAsync2(0x000D, 0x0001, lambda_4B86)

    @scena.Lambda('lambda_4B97')
    def lambda_4B97():
        ChrTurnDirection(0x00FE, 0x0016, 0)
        Yield()

        Jump('lambda_4B97')

    DispatchAsync2(0x0014, 0x0001, lambda_4B97)

    @scena.Lambda('lambda_4BA8')
    def lambda_4BA8():
        ChrTurnDirection(0x00FE, 0x0016, 0)
        Yield()

        Jump('lambda_4BA8')

    DispatchAsync2(0x0015, 0x0001, lambda_4BA8)

    SetChrSubChip(0x0014, 0)
    SetChrSubChip(0x0015, 0)
    OP_8E(0x0016, 62600, 1500, 39650, 2000, 0x00)
    OP_8E(0x0016, 59500, 1500, 37870, 2000, 0x00)
    OP_8E(0x0016, 57600, 1500, 37870, 2000, 0x00)
    ChrTurnDirection(0x0016, 0x0101, 400)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x0014, 0x01)
    TerminateThread(0x0015, 0x01)

    @scena.Lambda('lambda_4C1A')
    def lambda_4C1A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_4C1A)

    Sleep(100)

    @scena.Lambda('lambda_4C2D')
    def lambda_4C2D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_4C2D)

    ChrTalk(
        0x0101,
        (
            '#0010310103V#1004F#6P啊、尤莉亚小姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310104V#542F#6P尤莉亚……怎么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310105V你昨天也没有告诉过我\n',
            '埃尔赛尤号会来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0100310106V#171F#2P呵呵，为了给殿下一个惊喜，\n',
            '所以故意保密了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310107V还请您原谅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310108V#045F#6P尤莉亚……你真是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310109V#048F不过使用『埃尔赛尤』\n',
            '是祖母大人的意思吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0100310110V#170F#2P嗯，正是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310111V#1008F#6P啊……\n',
            '为什么女王陛下会……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0100310112V#176F#2P将知名的最新战舰投入使用的话，\n',
            '可以缓解人们因巨龙出现\n',
            '而产生的恐惧和不安…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310113V#170F正是出于这种考虑才会下达此决定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310114V#1006F#6P啊、原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040310115V#031F#6P呼，不愧是艾莉茜雅陛下啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310116V#030F那几位记者的同行\n',
            '也是因为这个理由吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0270310117V#141F#2P嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310118V这次龙的出现\n',
            '给大家带来的恐慌实在是非同寻常。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310119V所以要通过我们的报道来\n',
            '避免国民们的不安和动摇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0016, 0x0014, 400)

    ChrTalk(
        0x0016,
        (
            '#0100310120V#178F#6P奈尔先生、还请您……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0016, 400)
    Sleep(500)

    ChrTalk(
        0x0014,
        (
            '#0270310121V#147F#5P我知道啦～～\n',
            '机密的事情我是不会写出来的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310122V#140F不过，为了保证公正，\n',
            '还请让我进行深入些的调查啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0100310123V#176F#6P……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0017, 62600, 1500, 42300, 180)

    ExecExpressionWithValue(
        0x0017,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0017, 0x0004)
    ClearChrFlags(0x0017, 0x0080)

    NpcTalk(
        0x0017,
        '老人的声音',
        (
            '#0600310124V#7P呼……\n',
            '你们来得很准时啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0016, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000D, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0015, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0014, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_51BE')
    def lambda_51BE():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_51BE)

    @scena.Lambda('lambda_51CC')
    def lambda_51CC():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_51CC)

    @scena.Lambda('lambda_51DA')
    def lambda_51DA():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_51DA)

    @scena.Lambda('lambda_51E8')
    def lambda_51E8():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_51E8)

    @scena.Lambda('lambda_51F6')
    def lambda_51F6():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_51F6)

    @scena.Lambda('lambda_5204')
    def lambda_5204():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_5204)

    @scena.Lambda('lambda_5212')
    def lambda_5212():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_5212')

    DispatchAsync2(0x0101, 0x0001, lambda_5212)

    @scena.Lambda('lambda_5223')
    def lambda_5223():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_5223')

    DispatchAsync2(0x000A, 0x0001, lambda_5223)

    @scena.Lambda('lambda_5234')
    def lambda_5234():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_5234')

    DispatchAsync2(0x000D, 0x0001, lambda_5234)

    @scena.Lambda('lambda_5245')
    def lambda_5245():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_5245')

    DispatchAsync2(0x0014, 0x0001, lambda_5245)

    @scena.Lambda('lambda_5256')
    def lambda_5256():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_5256')

    DispatchAsync2(0x0015, 0x0001, lambda_5256)

    @scena.Lambda('lambda_5267')
    def lambda_5267():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_5267')

    DispatchAsync2(0x0016, 0x0001, lambda_5267)

    CreateThread(0x0017, 0x00, 0x00, 0x001B)
    Sleep(500)

    CreateThread(0x0016, 0x00, 0x00, 0x001C)
    WaitForThreadExit(0x0017, 0x0000)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x0014, 0x01)
    TerminateThread(0x0015, 0x01)
    TerminateThread(0x0016, 0x01)

    @scena.Lambda('lambda_52A0')
    def lambda_52A0():
        OP_8C(0x0014, 270, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_52A0)

    @scena.Lambda('lambda_52AE')
    def lambda_52AE():
        OP_8C(0x0015, 270, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_52AE)

    @scena.Lambda('lambda_52BC')
    def lambda_52BC():
        OP_8C(0x0016, 270, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_52BC)

    ChrTalk(
        0x0101,
        (
            '#0010310125V#1004F#6P啊、摩尔根将军……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030310126V#027F#6P您能允许我们同行，\n',
            '真是非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0600310127V#163F#2P哼，这也是女王陛下\n',
            '的意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310128V#160F为了不让你们误会，我话说在前。\n',
            '你们这次只不过\n',
            '是同行者而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310129V参加作战的基本还是我们，\n',
            '你们只要老老实实地旁观就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310130V#1006F#6P嗯，没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310131V如果军队能顺利完成任务的话，\n',
            '我们自然不会有什么意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080310132V#071F#6P让我们好好欣赏\n',
            '一场漂亮的战斗吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0600310133V#163F#2P呼……好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310134V#160F公主殿下，请到这边来。\n',
            '我来给您做向导。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310135V#043F#6P可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0600310136V#160F#2P这是王室的船，总不能让您\n',
            '以客人的身份乘坐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310137V那样会影响到大家的士气的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060310138V#047F#3P……我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x000A, 0x00, 0x00, 0x001D)
    Sleep(1000)

    @scena.Lambda('lambda_55DC')
    def lambda_55DC():
        OP_6D(56780, 1800, 39570, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_55DC)

    CreateThread(0x0017, 0x00, 0x00, 0x001E)

    @scena.Lambda('lambda_55FB')
    def lambda_55FB():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_55FB')

    DispatchAsync2(0x0014, 0x0001, lambda_55FB)

    @scena.Lambda('lambda_560C')
    def lambda_560C():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_560C')

    DispatchAsync2(0x0015, 0x0001, lambda_560C)

    @scena.Lambda('lambda_561D')
    def lambda_561D():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_561D')

    DispatchAsync2(0x0016, 0x0001, lambda_561D)

    Sleep(5000)

    ChrTalk(
        0x0101,
        (
            '#0010310139V#1007F#6P呼～将军还是\n',
            '和以前一个样子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310140V#1019F真是的，为什么就不能\n',
            '认同我们游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x0014, 0x01)
    TerminateThread(0x0015, 0x01)
    TerminateThread(0x0016, 0x01)
    OP_8C(0x0016, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0016,
        (
            '#0100310141V#171F#2P呵呵，那种顽固的老人家，\n',
            '要是态度突然转变了\n',
            '那才让人觉得奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310142V各位的向导\n',
            '就由我来担任吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0016, 315, 400)

    @scena.Lambda('lambda_5752')
    def lambda_5752():
        OP_6D(55700, 1500, 38800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5752)

    @scena.Lambda('lambda_576A')
    def lambda_576A():
        OP_6B(3800, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_576A)

    @scena.Lambda('lambda_577A')
    def lambda_577A():
        OP_8E(0x00FE, 57600, 1500, 37870, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_577A)

    Sleep(100)

    @scena.Lambda('lambda_579A')
    def lambda_579A():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_579A)

    Sleep(100)

    @scena.Lambda('lambda_57AD')
    def lambda_57AD():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_57AD)

    WaitForThreadExit(0x0016, 0x0001)
    OP_8C(0x0016, 270, 400)
    WaitForThreadExit(0x0101, 0x0002)
    SetChrChipByIndex(0x0016, 18)
    Sleep(100)

    OP_99(0x0016, 0x00, 0x01, 0x000005DC)
    Sleep(500)

    ChrTalk(
        0x0016,
        (
            '#0100310143V#178F#2P那么──\n',
            '欢迎你们！各位游击士！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310144V欢迎登上王室亲卫队所属的\n',
            '巡洋舰『埃尔赛尤』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_DB()
    OP_22(0x0075, 0x00, 0x64)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    OP_6F(0x0007, 1)
    OP_6D(61820, 6050, 54410, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(195000, 0)
    OP_6E(542, 0)
    FadeIn(1500, 0)
    OP_22(0x0078, 0x00, 0x64)
    OP_6F(0x000A, 200)
    OP_70(0x000A, 0x00000064)
    Sleep(2500)

    OP_23(0x0075)
    OP_22(0x0125, 0x00, 0x64)
    CreateThread(0x0028, 0x00, 0x00, 0x001A)
    Sleep(3000)

    OP_91(0x0028, 0, 500, 0, 400, 0x00)
    OP_91(0x0028, 0, 1000, 0, 800, 0x00)
    OP_91(0x0028, 0, 2000, 0, 1600, 0x00)
    OP_91(0x0028, 0, 500, 0, 800, 0x00)
    OP_91(0x0028, 0, 400, 0, 400, 0x00)

    @scena.Lambda('lambda_5982')
    def lambda_5982():
        OP_6D(59670, 1800, 67060, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5982)

    @scena.Lambda('lambda_599A')
    def lambda_599A():
        OP_67(0, 8260, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_599A)

    @scena.Lambda('lambda_59B2')
    def lambda_59B2():
        OP_6B(3830, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_59B2)

    @scena.Lambda('lambda_59C2')
    def lambda_59C2():
        OP_6C(204000, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_59C2)

    @scena.Lambda('lambda_59D2')
    def lambda_59D2():
        OP_6E(593, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_59D2)

    @scena.Lambda('lambda_59E2')
    def lambda_59E2():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_59E2)

    @scena.Lambda('lambda_59F8')
    def lambda_59F8():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_59F8)

    Sleep(400)

    @scena.Lambda('lambda_5A13')
    def lambda_5A13():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5A13)

    @scena.Lambda('lambda_5A29')
    def lambda_5A29():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5A29)

    Sleep(400)

    @scena.Lambda('lambda_5A44')
    def lambda_5A44():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5A44)

    @scena.Lambda('lambda_5A5A')
    def lambda_5A5A():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5A5A)

    Sleep(400)

    @scena.Lambda('lambda_5A75')
    def lambda_5A75():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5A75)

    @scena.Lambda('lambda_5A8B')
    def lambda_5A8B():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5A8B)

    Sleep(300)

    @scena.Lambda('lambda_5AA6')
    def lambda_5AA6():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5AA6)

    @scena.Lambda('lambda_5ABC')
    def lambda_5ABC():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5ABC)

    Sleep(300)

    @scena.Lambda('lambda_5AD7')
    def lambda_5AD7():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5AD7)

    @scena.Lambda('lambda_5AED')
    def lambda_5AED():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5AED)

    Sleep(300)

    @scena.Lambda('lambda_5B08')
    def lambda_5B08():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5B08)

    @scena.Lambda('lambda_5B1E')
    def lambda_5B1E():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5B1E)

    Sleep(300)

    @scena.Lambda('lambda_5B39')
    def lambda_5B39():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5B39)

    @scena.Lambda('lambda_5B4F')
    def lambda_5B4F():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5B4F)

    Sleep(200)

    @scena.Lambda('lambda_5B6A')
    def lambda_5B6A():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000032C8, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5B6A)

    @scena.Lambda('lambda_5B80')
    def lambda_5B80():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000514, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5B80)

    Sleep(200)

    @scena.Lambda('lambda_5B9B')
    def lambda_5B9B():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00003E80, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5B9B)

    @scena.Lambda('lambda_5BB1')
    def lambda_5BB1():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00003E80, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5BB1)

    Sleep(200)

    @scena.Lambda('lambda_5BCC')
    def lambda_5BCC():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00004A38, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5BCC)

    @scena.Lambda('lambda_5BE2')
    def lambda_5BE2():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00004A38, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5BE2)

    Sleep(200)

    @scena.Lambda('lambda_5BFD')
    def lambda_5BFD():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00005DC0, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5BFD)

    @scena.Lambda('lambda_5C13')
    def lambda_5C13():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00005DC0, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5C13)

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
    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    OP_6D(49170, 1500, 37540, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000B, 49530, 1500, 28520, 0)
    SetChrPos(0x000C, 48750, 1500, 28520, 0)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    OP_0D()
    OP_DC()

    NpcTalk(
        0x000B,
        '青年的声音',
        (
            '#0050310145V#3P来晚了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetChrChipByIndex(0x000B, 25)

    @scena.Lambda('lambda_5D3C')
    def lambda_5D3C():
        OP_8E(0x00FE, 49530, 1500, 37700, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_5D3C)

    Sleep(500)

    SetChrChipByIndex(0x000C, 26)

    @scena.Lambda('lambda_5D61')
    def lambda_5D61():
        OP_8E(0x000C, 48750, 1500, 37470, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_5D61)

    WaitForThreadExit(0x000B, 0x0001)
    SetChrChipByIndex(0x000B, 3)
    SetChrSubChip(0x000B, 0)
    WaitForThreadExit(0x000C, 0x0001)
    SetChrChipByIndex(0x000C, 4)
    SetChrSubChip(0x000C, 0)

    ChrTalk(
        0x000C,
        (
            '#0070310146V#065F已、已经飞走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050310147V#551F#5P可恶，要是再早点起床\n',
            '出发就好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310148V#051F没办法，龙的事\n',
            '就交给艾丝蒂尔她们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 90, 400)

    ChrTalk(
        0x000C,
        (
            '#0070310149V#560F#4P是、是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310150V#562F可是可是……呜呜呜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310151V人家好想坐一次\n',
            '『埃尔赛尤』呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 270, 400)

    ChrTalk(
        0x000B,
        (
            '#0050310152V#051F#5P怎么回事，\n',
            '机械瘾又发作了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070310153V#560F#4P可是…\n',
            '那上面有很多新型装备呢…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310154V可以容纳８个新型引擎的\n',
            '引擎管道…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310155V拥有高效率处理情报机能\n',
            '的次世代型运算器…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310156V#067F哈～真是好期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050310157V#551F#5P真是的……\n',
            '两只眼睛又开始发亮了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070310158V#067F#4P嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310159V#064F不过，阿加特哥哥，\n',
            '我们接下来该怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050310160V#053F#5P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310161V#051F那就先去找把\n',
            '替代用的重剑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070310162V#063F#4P啊、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310163V原来那把已经断成那样了，\n',
            '没办法修理了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050310164V#053F#5P嗯，所以只能重新买一把了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310165V#552F南街区的武器店\n',
            '应该就有那类武器吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0018, 49650, 1500, 28520, 0)
    ClearChrFlags(0x0018, 0x0080)
    OP_4A(0x0018, 255)

    NpcTalk(
        0x0018,
        '青年的声音',
        (
            '#1330310166V#3P阿加特！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_61E0')
    def lambda_61E0():
        OP_6D(49650, 1500, 35920, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_61E0)

    @scena.Lambda('lambda_61F8')
    def lambda_61F8():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_61F8)

    Sleep(50)

    @scena.Lambda('lambda_620B')
    def lambda_620B():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_620B)

    OP_8E(0x0018, 49300, 1500, 35390, 4000, 0x00)

    ChrTalk(
        0x000B,
        (
            '#0050310167V#052F#6P哟！泰德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070310168V#064F接待员哥哥……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1330310169V#2P啊～还好\n',
            '赶上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1330310170V#2P现在导力通信已经恢复了，\n',
            '你们要和『埃尔赛尤』联络吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050310171V#053F#6P啊……不用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310172V#051F不过、你是特意跑来\n',
            '确认我们是否登上船了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1330310173V#2P啊、其实是一半一半啦，因为……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1330310174V#2P昨天在整理最后一批包裹时\n',
            '发现了一个寄给阿加特你\n',
            '的快递包裹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050310175V#052F#6P给我的快递包裹？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1330310176V#2P嗯，是署名拉赛尔\n',
            '的小包裹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050310177V#055F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0070310178V#065F爷、爷爷寄来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_20(0x000005DC)
    OP_21()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/E0800._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x648B
@scena.Code('func_1A_648B')
def func_1A_648B():
    OP_22(0x0077, 0x00, 0x64)
    OP_6F(0x0007, 1)
    OP_70(0x0007, 0x00000096)
    OP_73(0x0007)
    OP_6F(0x0007, 151)
    OP_70(0x0007, 0x0000014A)
    Sleep(3300)

    OP_75(0x08, 0x00000000, 0x02)
    OP_22(0x00DD, 0x00, 0x64)
    OP_74(0x0008, 0x00000000, 0x0001)
    Sleep(250)

    OP_74(0x0008, 0x00000000, 0x0002)
    Sleep(250)

    OP_22(0x00DD, 0x00, 0x64)
    OP_74(0x0008, 0x00000000, 0x0003)
    Sleep(250)

    OP_74(0x0008, 0x00000000, 0x0004)
    Sleep(250)

    OP_22(0x00DD, 0x00, 0x64)
    OP_74(0x0008, 0x00000000, 0x0005)
    Sleep(250)

    OP_74(0x0008, 0x00000000, 0x0006)
    Sleep(250)

    OP_74(0x0008, 0x00000000, 0x0007)
    OP_73(0x0007)
    OP_71(0x0007, 0x0020)
    OP_6F(0x0007, 330)
    OP_70(0x0007, 0x000001AE)

    Return()

# id: 0x001B offset: 0x653E
@scena.Code('func_1B_653E')
def func_1B_653E():
    OP_8E(0x00FE, 62600, 1500, 40100, 2000, 0x00)
    OP_8E(0x00FE, 59670, 1500, 38090, 2000, 0x00)
    OP_8E(0x00FE, 57350, 1500, 37820, 2000, 0x00)

    Return()

# id: 0x001C offset: 0x657B
@scena.Code('func_1C_657B')
def func_1C_657B():
    OP_8E(0x00FE, 59010, 1500, 37910, 2000, 0x00)
    OP_8E(0x00FE, 59160, 1500, 37010, 2000, 0x00)

    Return()

# id: 0x001D offset: 0x65A4
@scena.Code('func_1D_65A4')
def func_1D_65A4():
    SetChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, 53790, 1500, 37940, 2000, 0x00)
    OP_8E(0x00FE, 59840, 1500, 38040, 2000, 0x00)
    OP_8E(0x00FE, 62090, 1500, 40060, 2000, 0x00)
    OP_8E(0x00FE, 62250, 1500, 41800, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001E offset: 0x65FF
@scena.Code('func_1E_65FF')
def func_1E_65FF():
    OP_8C(0x00FE, 90, 400)
    OP_8E(0x00FE, 59840, 1500, 38040, 2000, 0x00)
    OP_8E(0x00FE, 62090, 1500, 40060, 2000, 0x00)
    OP_8E(0x00FE, 62250, 1500, 41800, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001F offset: 0x6648
@scena.Code('func_1F_6648')
def func_1F_6648():
    OP_72(0x0007, 0x0020)
    OP_73(0x0007)
    OP_6F(0x0007, 600)
    OP_70(0x0007, 0x0000032A)

    Return()

# id: 0x0020 offset: 0x665F
@scena.Code('func_20_665F')
def func_20_665F():
    CreateThread(0x0101, 0x03, 0x00, 0x001F)
    OP_22(0x0079, 0x00, 0x64)

    @scena.Lambda('lambda_6671')
    def lambda_6671():
        OP_8F(0x00FE, 62500, -5100, 44000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_6671)

    @scena.Lambda('lambda_668C')
    def lambda_668C():
        OP_8F(0x00FE, 62500, 0, 44000, 100, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_668C)

    Sleep(100)

    @scena.Lambda('lambda_66AC')
    def lambda_66AC():
        OP_8F(0x00FE, 62500, 0, 44000, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_66AC)

    Sleep(100)

    @scena.Lambda('lambda_66CC')
    def lambda_66CC():
        OP_8F(0x00FE, 62500, 0, 44000, 300, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_66CC)

    Sleep(100)

    @scena.Lambda('lambda_66EC')
    def lambda_66EC():
        OP_8F(0x00FE, 62500, 0, 44000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_66EC)

    @scena.Lambda('lambda_6707')
    def lambda_6707():
        OP_6D(76390, 20000, 24550, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6707)

    Sleep(100)

    @scena.Lambda('lambda_6724')
    def lambda_6724():
        OP_8F(0x00FE, 62500, 0, 44000, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6724)

    Sleep(100)

    @scena.Lambda('lambda_6744')
    def lambda_6744():
        OP_8F(0x00FE, 62500, 0, 44000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6744)

    Sleep(100)

    @scena.Lambda('lambda_6764')
    def lambda_6764():
        OP_8F(0x00FE, 62500, 0, 44000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6764)

    Sleep(100)

    @scena.Lambda('lambda_6784')
    def lambda_6784():
        OP_8F(0x00FE, 62500, 0, 44000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6784)

    Sleep(100)

    @scena.Lambda('lambda_67A4')
    def lambda_67A4():
        OP_8F(0x00FE, 62500, 0, 44000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_67A4)

    Sleep(100)

    @scena.Lambda('lambda_67C4')
    def lambda_67C4():
        OP_8F(0x00FE, 62500, 0, 44000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_67C4)

    Sleep(100)

    @scena.Lambda('lambda_67E4')
    def lambda_67E4():
        OP_8F(0x00FE, 62500, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_67E4)

    Sleep(100)

    @scena.Lambda('lambda_6804')
    def lambda_6804():
        OP_8F(0x00FE, 62500, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6804)

    @scena.Lambda('lambda_681F')
    def lambda_681F():
        OP_8F(0x00FE, 62500, -5100, 44000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_681F)

    Sleep(3500)

    @scena.Lambda('lambda_683F')
    def lambda_683F():
        OP_8F(0x00FE, 62500, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_683F)

    Sleep(100)

    @scena.Lambda('lambda_685F')
    def lambda_685F():
        OP_8F(0x00FE, 62500, 0, 44000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_685F)

    Sleep(100)

    @scena.Lambda('lambda_687F')
    def lambda_687F():
        OP_8F(0x00FE, 62500, 0, 44000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_687F)

    Sleep(100)

    @scena.Lambda('lambda_689F')
    def lambda_689F():
        OP_8F(0x00FE, 62500, 0, 44000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_689F)

    Sleep(100)

    @scena.Lambda('lambda_68BF')
    def lambda_68BF():
        OP_8F(0x00FE, 62500, 0, 44000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_68BF)

    Sleep(100)

    @scena.Lambda('lambda_68DF')
    def lambda_68DF():
        OP_8F(0x00FE, 62500, 0, 44000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_68DF)

    Sleep(100)

    @scena.Lambda('lambda_68FF')
    def lambda_68FF():
        OP_8F(0x00FE, 62500, 0, 44000, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_68FF)

    Sleep(100)

    @scena.Lambda('lambda_691F')
    def lambda_691F():
        OP_8F(0x00FE, 62500, 0, 44000, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_691F)

    Sleep(100)

    @scena.Lambda('lambda_693F')
    def lambda_693F():
        OP_8F(0x00FE, 62500, 0, 44000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_693F)

    Sleep(100)

    @scena.Lambda('lambda_695F')
    def lambda_695F():
        OP_8F(0x00FE, 62500, 0, 44000, 400, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_695F)

    WaitForThreadExit(0x0028, 0x0001)
    OP_23(0x0079)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x00000064)
    SetChrPos(0x0028, 62500, 0, 44000, 0)
    TerminateThread(0x0101, 0x01)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(1000)

    Return()

# id: 0x0021 offset: 0x69B2
@scena.Code('func_21_69B2')
def func_21_69B2():
    CreateThread(0x0101, 0x03, 0x00, 0x001F)
    OP_22(0x0125, 0x00, 0x64)

    @scena.Lambda('lambda_69C4')
    def lambda_69C4():
        OP_8F(0x00FE, 62500, -5100, 44000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_69C4)

    @scena.Lambda('lambda_69DF')
    def lambda_69DF():
        OP_8F(0x00FE, 62500, 0, 44000, 100, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_69DF)

    Sleep(100)

    @scena.Lambda('lambda_69FF')
    def lambda_69FF():
        OP_8F(0x00FE, 62500, 0, 44000, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_69FF)

    Sleep(100)

    @scena.Lambda('lambda_6A1F')
    def lambda_6A1F():
        OP_8F(0x00FE, 62500, 0, 44000, 300, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6A1F)

    Sleep(100)

    @scena.Lambda('lambda_6A3F')
    def lambda_6A3F():
        OP_8F(0x00FE, 62500, 0, 44000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6A3F)

    @scena.Lambda('lambda_6A5A')
    def lambda_6A5A():
        OP_6D(76390, 20000, 24550, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6A5A)

    Sleep(100)

    @scena.Lambda('lambda_6A77')
    def lambda_6A77():
        OP_8F(0x00FE, 62500, 0, 44000, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6A77)

    Sleep(100)

    @scena.Lambda('lambda_6A97')
    def lambda_6A97():
        OP_8F(0x00FE, 62500, 0, 44000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6A97)

    Sleep(100)

    @scena.Lambda('lambda_6AB7')
    def lambda_6AB7():
        OP_8F(0x00FE, 62500, 0, 44000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6AB7)

    Sleep(100)

    @scena.Lambda('lambda_6AD7')
    def lambda_6AD7():
        OP_8F(0x00FE, 62500, 0, 44000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6AD7)

    Sleep(100)

    @scena.Lambda('lambda_6AF7')
    def lambda_6AF7():
        OP_8F(0x00FE, 62500, 0, 44000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6AF7)

    Sleep(100)

    @scena.Lambda('lambda_6B17')
    def lambda_6B17():
        OP_8F(0x00FE, 62500, 0, 44000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6B17)

    Sleep(100)

    @scena.Lambda('lambda_6B37')
    def lambda_6B37():
        OP_8F(0x00FE, 62500, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6B37)

    Sleep(100)

    @scena.Lambda('lambda_6B57')
    def lambda_6B57():
        OP_8F(0x00FE, 62500, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6B57)

    @scena.Lambda('lambda_6B72')
    def lambda_6B72():
        OP_8F(0x00FE, 62500, -5100, 44000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_6B72)

    Sleep(3500)

    @scena.Lambda('lambda_6B92')
    def lambda_6B92():
        OP_8F(0x00FE, 62500, 0, 44000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6B92)

    Sleep(100)

    @scena.Lambda('lambda_6BB2')
    def lambda_6BB2():
        OP_8F(0x00FE, 62500, 0, 44000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6BB2)

    Sleep(100)

    @scena.Lambda('lambda_6BD2')
    def lambda_6BD2():
        OP_8F(0x00FE, 62500, 0, 44000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6BD2)

    Sleep(100)

    @scena.Lambda('lambda_6BF2')
    def lambda_6BF2():
        OP_8F(0x00FE, 62500, 0, 44000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6BF2)

    Sleep(100)

    @scena.Lambda('lambda_6C12')
    def lambda_6C12():
        OP_8F(0x00FE, 62500, 0, 44000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6C12)

    Sleep(100)

    @scena.Lambda('lambda_6C32')
    def lambda_6C32():
        OP_8F(0x00FE, 62500, 0, 44000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6C32)

    Sleep(100)

    @scena.Lambda('lambda_6C52')
    def lambda_6C52():
        OP_8F(0x00FE, 62500, 0, 44000, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6C52)

    Sleep(100)

    @scena.Lambda('lambda_6C72')
    def lambda_6C72():
        OP_8F(0x00FE, 62500, 0, 44000, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6C72)

    Sleep(100)

    @scena.Lambda('lambda_6C92')
    def lambda_6C92():
        OP_8F(0x00FE, 62500, 0, 44000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6C92)

    Sleep(100)

    @scena.Lambda('lambda_6CB2')
    def lambda_6CB2():
        OP_8F(0x00FE, 62500, 0, 44000, 400, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_6CB2)

    WaitForThreadExit(0x0028, 0x0001)
    OP_23(0x0125)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x00000064)
    SetChrPos(0x0028, 62500, 0, 44000, 0)
    TerminateThread(0x0101, 0x01)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(1000)

    Return()

# id: 0x0022 offset: 0x6D05
@scena.Code('func_22_6D05')
def func_22_6D05():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6D4B',
    )

    FormationDelMember(0x02, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF9, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_6D4B(): pass

    label('loc_6D4B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6DA5',
    )

    FormationDelMember(0x03, 0xFF)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6D8D',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xF9, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_6DA5')

    def _loc_6D8D(): pass

    label('loc_6D8D')

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_6DA5(): pass

    label('loc_6DA5')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x4),
            Expr.Neq,
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6DFF',
    )

    FormationDelMember(0x04, 0xFF)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6DE7',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_6DFF')

    def _loc_6DE7(): pass

    label('loc_6DE7')

    FormationAddMember(ChrTable['科洛丝'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_6DFF(): pass

    label('loc_6DFF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Neq,
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6E31',
    )

    FormationDelMember(0x07, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_6E31(): pass

    label('loc_6E31')

    Return()

# id: 0x0023 offset: 0x6E32
@scena.Code('func_23_6E32')
def func_23_6E32():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_6E46',
    )

    FormationDelMember(0x02, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xFF, 0xFF)

    def _loc_6E46(): pass

    label('loc_6E46')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_6E5A',
    )

    FormationDelMember(0x03, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xFF, 0xFF)

    def _loc_6E5A(): pass

    label('loc_6E5A')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_6E6E',
    )

    FormationDelMember(0x04, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xFF, 0xFF)

    def _loc_6E6E(): pass

    label('loc_6E6E')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_6E82',
    )

    FormationDelMember(0x07, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFF, 0xFF)

    def _loc_6E82(): pass

    label('loc_6E82')

    Return()

# id: 0x0024 offset: 0x6E83
@scena.Code('func_24_6E83')
def func_24_6E83():
    EventBegin(0x00)
    OP_DB()
    OP_6D(66690, 9370, 39660, 0)
    OP_67(0, 45340, -55000, 0)
    OP_6B(900, 0)
    OP_6C(316000, 0)
    OP_6E(403, 0)
    OP_72(0x0007, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_6F(0x0007, 1)
    OP_75(0x08, 0x00000000, 0x00)
    OP_74(0x0008, 0x00000000, 0x0000)
    SetChrFlags(0x001A, 0x0080)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_6F02')
    def lambda_6F02():
        OP_6D(66900, 7780, 39660, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6F02)

    @scena.Lambda('lambda_6F1A')
    def lambda_6F1A():
        OP_67(0, 34090, -55000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6F1A)

    Sleep(1000)

    @scena.Lambda('lambda_6F37')
    def lambda_6F37():
        OP_6B(700, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6F37)

    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x02000000)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/E0311._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0025 offset: 0x6F6E
@scena.Code('func_25_6F6E')
def func_25_6F6E():
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
        'loc_6F85',
    )

    Call(0, 0x0026)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF8, 0xFF)

    def _loc_6F85(): pass

    label('loc_6F85')

    OP_6D(55720, 1500, 38000, 0)
    OP_67(0, 4310, -10000, 0)
    OP_6B(4370, 0)
    OP_6C(122000, 0)
    OP_6E(236, 0)
    OP_A1(0x0028, 0x0007)
    OP_72(0x0007, 0x0004)
    OP_72(0x0007, 0x0020)
    SetChrPos(0x0028, 62500, 0, 44000, 0)
    OP_6F(0x0007, 1)
    OP_A1(0x0029, 0x0008)
    OP_72(0x0008, 0x0004)
    SetChrPos(0x0029, 62500, -5100, 44000, 0)
    OP_75(0x08, 0x00000000, 0x00)
    OP_74(0x0008, 0x00000000, 0x0000)
    OP_72(0x000A, 0x0004)
    OP_6F(0x000A, 200)
    OP_71(0x000B, 0x0004)
    SetChrPos(0x0101, 51260, 1800, 37530, 90)
    SetChrPos(0x000B, 49290, 1500, 39050, 90)
    SetChrPos(0x000C, 49650, 1500, 40020, 135)
    SetChrPos(0x0108, 49230, 1500, 36580, 90)
    SetChrPos(0x0105, 51230, 1800, 38480, 90)
    SetChrPos(0x0103, 49640, 1500, 38070, 90)
    SetChrPos(0x0104, 48700, 1500, 37550, 90)
    SetChrPos(0x0017, 59050, 1500, 38120, 270)
    SetChrPos(0x0016, 59700, 1500, 38870, 270)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0004)
    SetChrFlags(0x0016, 0x0004)

    ExecExpressionWithValue(
        0x0017,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0105, 19)
    SetChrSubChip(0x0105, 1)
    SetChrFlags(0x001A, 0x0080)
    OP_22(0x0075, 0x01, 0x50)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0016,
        (
            '#0100310790V#176F接下来『埃尔赛尤』\n',
            '要在柏斯上空进行巡航。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310791V#170F找到龙的居所之后\n',
            '请马上和我们联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310792V#1006F嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060310793V#048F#6P找到龙的住处之后\n',
            '我们会马上让基库帮忙传达的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310794V我不在的时候\n',
            '你也要乖乖在艾丝蒂尔身边待着哦，\n',
            '拜托啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0105,
        '基库',
        (
            '#0060310795V#311F#5P啾⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0600310796V#163F殿下，如果您要同行的话，\n',
            '请一定要小心啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310797V#160F……艾丝蒂尔·布莱特。\n',
            '还有阿加特·科洛斯纳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310798V#1004F啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050310799V#052F#6P……怎么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0600310800V#163F如果龙从峡谷中逃脱的话，\n',
            '我们军队会负起责任做好最完善的处理的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310801V无论如何，我也不会让利贝尔的国民\n',
            '再受到第二次伤害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310802V#160F所以，你们不要害怕失败，\n',
            '照你们的意思去做吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310803V#1025F摩尔根将军……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050310804V#051F#6P……你竟然会\n',
            '说出这样的话来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310805V难道太阳从西边升起了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0600310806V#163F哼，这只是场面话而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0017, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0017,
        (
            '#0600310807V#160F#2P……上尉！出发了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0100310808V#171F是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_DB()
    Fade(1000)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)

    @scena.Lambda('lambda_752E')
    def lambda_752E():
        ChrTurnDirection(0x0101, 0x0028, 400)
        Yield()

        Jump('lambda_752E')

    DispatchAsync2(0x0103, 0x0002, lambda_752E)

    @scena.Lambda('lambda_753F')
    def lambda_753F():
        ChrTurnDirection(0x0103, 0x0028, 400)
        Yield()

        Jump('lambda_753F')

    DispatchAsync2(0x0103, 0x0003, lambda_753F)

    @scena.Lambda('lambda_7550')
    def lambda_7550():
        ChrTurnDirection(0x0105, 0x0028, 400)
        Yield()

        Jump('lambda_7550')

    DispatchAsync2(0x0105, 0x0003, lambda_7550)

    @scena.Lambda('lambda_7561')
    def lambda_7561():
        ChrTurnDirection(0x0108, 0x0028, 400)
        Yield()

        Jump('lambda_7561')

    DispatchAsync2(0x0108, 0x0003, lambda_7561)

    @scena.Lambda('lambda_7572')
    def lambda_7572():
        ChrTurnDirection(0x0104, 0x0028, 400)
        Yield()

        Jump('lambda_7572')

    DispatchAsync2(0x0104, 0x0003, lambda_7572)

    @scena.Lambda('lambda_7583')
    def lambda_7583():
        ChrTurnDirection(0x000B, 0x0028, 400)
        Yield()

        Jump('lambda_7583')

    DispatchAsync2(0x000B, 0x0003, lambda_7583)

    @scena.Lambda('lambda_7594')
    def lambda_7594():
        ChrTurnDirection(0x000C, 0x0028, 400)
        Yield()

        Jump('lambda_7594')

    DispatchAsync2(0x000C, 0x0003, lambda_7594)

    OP_6D(61820, 6050, 54410, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(195000, 0)
    OP_6E(542, 0)
    OP_0D()
    OP_22(0x0078, 0x00, 0x64)
    OP_6F(0x000A, 200)
    OP_70(0x000A, 0x00000064)
    Sleep(2500)

    OP_23(0x0075)
    OP_22(0x0125, 0x00, 0x64)
    CreateThread(0x0028, 0x00, 0x00, 0x001A)
    Sleep(3000)

    OP_91(0x0028, 0, 500, 0, 400, 0x00)
    OP_91(0x0028, 0, 1000, 0, 800, 0x00)
    OP_91(0x0028, 0, 2000, 0, 1600, 0x00)
    OP_91(0x0028, 0, 500, 0, 800, 0x00)
    OP_91(0x0028, 0, 400, 0, 400, 0x00)

    @scena.Lambda('lambda_7673')
    def lambda_7673():
        OP_6D(59670, 1800, 67060, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7673)

    @scena.Lambda('lambda_768B')
    def lambda_768B():
        OP_67(0, 8260, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_768B)

    @scena.Lambda('lambda_76A3')
    def lambda_76A3():
        OP_6B(3830, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_76A3)

    @scena.Lambda('lambda_76B3')
    def lambda_76B3():
        OP_6C(204000, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_76B3)

    @scena.Lambda('lambda_76C3')
    def lambda_76C3():
        OP_6E(593, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_76C3)

    @scena.Lambda('lambda_76D3')
    def lambda_76D3():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_76D3)

    @scena.Lambda('lambda_76E9')
    def lambda_76E9():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_76E9)

    Sleep(400)

    @scena.Lambda('lambda_7704')
    def lambda_7704():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_7704)

    @scena.Lambda('lambda_771A')
    def lambda_771A():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_771A)

    Sleep(400)

    @scena.Lambda('lambda_7735')
    def lambda_7735():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_7735)

    @scena.Lambda('lambda_774B')
    def lambda_774B():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_774B)

    Sleep(400)

    @scena.Lambda('lambda_7766')
    def lambda_7766():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_7766)

    @scena.Lambda('lambda_777C')
    def lambda_777C():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_777C)

    Sleep(300)

    @scena.Lambda('lambda_7797')
    def lambda_7797():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_7797)

    @scena.Lambda('lambda_77AD')
    def lambda_77AD():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_77AD)

    Sleep(300)

    @scena.Lambda('lambda_77C8')
    def lambda_77C8():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_77C8)

    @scena.Lambda('lambda_77DE')
    def lambda_77DE():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_77DE)

    Sleep(300)

    @scena.Lambda('lambda_77F9')
    def lambda_77F9():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_77F9)

    @scena.Lambda('lambda_780F')
    def lambda_780F():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_780F)

    Sleep(300)

    @scena.Lambda('lambda_782A')
    def lambda_782A():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_782A)

    @scena.Lambda('lambda_7840')
    def lambda_7840():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7840)

    Sleep(200)

    @scena.Lambda('lambda_785B')
    def lambda_785B():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x000032C8, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_785B)

    @scena.Lambda('lambda_7871')
    def lambda_7871():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00000514, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7871)

    Sleep(200)

    @scena.Lambda('lambda_788C')
    def lambda_788C():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00003E80, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_788C)

    @scena.Lambda('lambda_78A2')
    def lambda_78A2():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00003E80, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_78A2)

    Sleep(200)

    @scena.Lambda('lambda_78BD')
    def lambda_78BD():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00004A38, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_78BD)

    @scena.Lambda('lambda_78D3')
    def lambda_78D3():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00004A38, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_78D3)

    Sleep(200)

    @scena.Lambda('lambda_78EE')
    def lambda_78EE():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00005DC0, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_78EE)

    @scena.Lambda('lambda_7904')
    def lambda_7904():
        OP_94(0x01, 0x00FE, 0x0000, 0x00030D40, 0x00005DC0, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7904)

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
    WaitForThreadExit(0x0101, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0103, 0x02)
    TerminateThread(0x0103, 0x03)
    TerminateThread(0x0105, 0x03)
    TerminateThread(0x0108, 0x03)
    TerminateThread(0x0104, 0x03)
    TerminateThread(0x000B, 0x03)
    TerminateThread(0x000C, 0x03)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择固定队员外的一名同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0005,
            0x0006,
            0x00FF,
        ),
        (
            0x0002,
            0x0003,
            0x0004,
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
    OP_0D()
    Sleep(1000)

    SetMapFlags(0x02000000)
    OP_A2(0x1A24)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T1103._SN', 114, 0, 0)
    IdleLoop()

    Return()

# id: 0x0026 offset: 0x7A82
@scena.Code('func_26_7A82')
def func_26_7A82():
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
        (0x00000000, 'loc_7AFC'),
        (0x00000001, 'loc_7B02'),
        (-1, 'loc_7B08'),
    )

    def _loc_7AFC(): pass

    label('loc_7AFC')

    OP_A2(0x1200)

    Jump('loc_7B08')

    def _loc_7B02(): pass

    label('loc_7B02')

    OP_A2(0x1201)

    Jump('loc_7B08')

    def _loc_7B08(): pass

    label('loc_7B08')

    Return()

# id: 0x0027 offset: 0x7B09
@scena.Code('func_27_7B09')
def func_27_7B09():
    FadeOut(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x00FF,
            0x00FF,
        ),
        (
            0x0002,
            0x0003,
            0x0004,
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

    Sleep(100)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7BB9',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_7BB9(): pass

    label('loc_7BB9')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7C06',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BEE',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_7C06')

    def _loc_7BEE(): pass

    label('loc_7BEE')

    FormationAddMember(ChrTable['奥利维尔'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_7C06(): pass

    label('loc_7C06')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7C53',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C3B',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_7C53')

    def _loc_7C3B(): pass

    label('loc_7C3B')

    FormationAddMember(ChrTable['科洛丝'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_7C53(): pass

    label('loc_7C53')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7C78',
    )

    FormationAddMember(ChrTable['金'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_7C78(): pass

    label('loc_7C78')

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0028 offset: 0x7C8A
@scena.Code('func_28_7C8A')
def func_28_7C8A():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船飞船坪\n',
            '≡　前往洛连特市\n',
            '≡　前往卢安市\n',
            '≡　前往埃雷波尼亚帝国',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0029 offset: 0x7D00
@scena.Code('func_29_7D00')
def func_29_7D00():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

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

# id: 0x002A offset: 0x7D66
@scena.Code('func_2A_7D66')
def func_2A_7D66():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　飞船坪塔台　　　　\n',
            '　※无关人员禁止入内　　\n',
            '   『利贝尔飞船公社』　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x002B offset: 0x7DE2
@scena.Code('func_2B_7DE2')
def func_2B_7DE2():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x381),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7DEF',
    )

    Return()

    def _loc_7DEF(): pass

    label('loc_7DEF')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_7E01',
    )

    Return()

    def _loc_7E01(): pass

    label('loc_7E01')

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_CD(0x0018)"),
            Expr.Return,
        ),
        'loc_7E3C',
    )

    Call(0, 0x002C)

    Jump('loc_7EE1')

    def _loc_7E3C(): pass

    label('loc_7E3C')

    If(
        (
            (Expr.Eval, "OP_CD(0x03E8)"),
            Expr.Return,
        ),
        'loc_7E4B',
    )

    Call(0, 0x002C)

    Jump('loc_7EE1')

    def _loc_7E4B(): pass

    label('loc_7E4B')

    If(
        (
            (Expr.Eval, "OP_CD(0x00FF)"),
            Expr.Return,
        ),
        'loc_7EA3',
    )

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '试着出示了照片，\n',
            '但似乎没有见过的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_7EE1')

    def _loc_7EA3(): pass

    label('loc_7EA3')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近没有人可以确认照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_7EE1(): pass

    label('loc_7EE1')

    OP_0D()
    ClearMapFlags(0x00000080)

    Return()

# id: 0x002C offset: 0x7EE8
@scena.Code('func_2C_7EE8')
def func_2C_7EE8():
    TalkBegin(0x0018)

    ChrTalk(
        0x0018,
        (
            '嗯，照片上的小女孩\n',
            '已经想不起来是谁了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '很遗憾，大概和飞船坪中\n',
            '的客人们无关吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '可能已经有哪处的人家\n',
            '将她养育成人了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0018)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

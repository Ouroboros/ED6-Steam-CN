import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '爱娜'),
    TXT(0x02, '鲁克'),
    TXT(0x03, '帕特'),
    TXT(0x04, '克露莎'),
    TXT(0x05, '胡里奥'),
    TXT(0x06, '艾娅莉'),
    TXT(0x07, '阿鲁姆'),
    TXT(0x08, '艾娅莉'),
    TXT(0x09, '阿鲁姆'),
    TXT(0x0A, '尤妮'),
    TXT(0x0B, '卡雷尔'),
    TXT(0x0C, '拉德米拉'),
    TXT(0x0D, '伊娜'),
    TXT(0x0E, '安莉尔'),
    TXT(0x0F, '安莉尔'),
    TXT(0x10, '亚鲁瓦教授'),
    TXT(0x11, '奈尔'),
    TXT(0x12, '朵洛希'),
    TXT(0x13, '雪拉扎德'),
    TXT(0x14, '目标用摄像机'),
    TXT(0x15, '鸽子'),
    TXT(0x16, '鸽子'),
    TXT(0x17, '鸽子'),
    TXT(0x18, '鸽子'),
    TXT(0x19, '鸽子'),
    TXT(0x1A, '洛连特市长官邸'),
    TXT(0x1B, '洛连特飞艇坪'),
    TXT(0x1C, '艾利兹街道方向'),
    TXT(0x1D, '米尔西街道方向'),
    TXT(0x1E, '玛鲁加山道方向'),
    TXT(0x1F, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'rolent'
    header.mapModel       = 'T0100.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T0100._SN', 'ED6_DT01/T0100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA609
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x0000BF68,
            dword_04        = 0x00000000,
            dword_08        = 0x0000A028,
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
            word_3A         = 1,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x0000BF68,
            dword_04        = 0x00000000,
            dword_08        = 0x0000A028,
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
            word_3A         = 1,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x0000BF68,
            dword_04        = 0x00000000,
            dword_08        = 0x0000A028,
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
            word_3A         = 1,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0x130
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH02560._CH', 'ED6_DT07/CH02560P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01033._CH', 'ED6_DT07/CH01033P._CP'),
        ('ED6_DT07/CH01730._CH', 'ED6_DT07/CH01730P._CP'),
        ('ED6_DT07/CH01731._CH', 'ED6_DT07/CH01731P._CP'),
    ]

# id: 0x10002 offset: 0x1EA
@scena.NpcData('NpcData')
def NpcData():
    return (
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
            x                   = 49900,
            z                   = 0,
            y                   = 72100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 46900,
            z                   = 0,
            y                   = 74100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 30422,
            z                   = 0,
            y                   = 40087,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 51829,
            z                   = 0,
            y                   = 35208,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 29979,
            z                   = 0,
            y                   = 17921,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = 31832,
            z                   = 3250,
            y                   = 33000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 36305,
            z                   = 100,
            y                   = 46015,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 39160,
            z                   = 80,
            y                   = 47020,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 18,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 72160,
            z                   = 0,
            y                   = 18851,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 62400,
            z                   = 250,
            y                   = 22000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            x                   = 33500,
            z                   = 0,
            y                   = 45800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            x                   = 39420,
            z                   = 250,
            y                   = 51560,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 38700,
            z                   = 0,
            y                   = 50720,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 5488,
            z                   = 0,
            y                   = 16806,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 5488,
            z                   = 0,
            y                   = 16806,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 5488,
            z                   = 0,
            y                   = 16806,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 5488,
            z                   = 0,
            y                   = 16806,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 200,
            z                   = 0,
            y                   = 74200,
            direction           = 180,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34280,
            z                   = 430,
            y                   = 39120,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 90860,
            z                   = 0,
            y                   = 40240,
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
            x                   = 49150,
            z                   = 0,
            y                   = 95090,
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
            x                   = 48960,
            z                   = 0,
            y                   = 1120,
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
            x                   = 5400,
            z                   = 0,
            y                   = 39830,
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
            x                   = 28060,
            z                   = 0,
            y                   = 80870,
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

# id: 0x10003 offset: 0x5AA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x5AA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 44000,
            y           = 0,
            z           = 12250,
            range       = 54000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00002710,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000002B,
        ),
        ScenaEventData(
            x           = 18000,
            y           = 0,
            z           = 44000,
            range       = 19000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00009088,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000037,
        ),
        ScenaEventData(
            x           = 25000,
            y           = 0,
            z           = 72000,
            range       = 31000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00011364,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000040,
        ),
        ScenaEventData(
            x           = 55000,
            y           = -1000,
            z           = 57200,
            range       = 61500,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000DB88,
            dword_18    = 0x00010000,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = 42000,
            y           = -1000,
            z           = 34400,
            range       = 54000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00008278,
            dword_18    = 0x00010000,
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = 60900,
            y           = -1000,
            z           = 35800,
            range       = 61900,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000AFC8,
            dword_18    = 0x00010000,
            dword_1C    = 0x0000001F,
        ),
        ScenaEventData(
            x           = 61850,
            y           = -1000,
            z           = 30150,
            range       = 66550,
            dword_10    = 0x000007D0,
            dword_14    = 0x00007DC8,
            dword_18    = 0x00010000,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = 52800,
            y           = 0,
            z           = 18950,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004D,
        ),
        ScenaEventData(
            x           = 52800,
            y           = 0,
            z           = 29050,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004E,
        ),
        ScenaEventData(
            x           = 44700,
            y           = 0,
            z           = 33020,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004F,
        ),
        ScenaEventData(
            x           = 44700,
            y           = 0,
            z           = 21990,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000050,
        ),
        ScenaEventData(
            x           = 30900,
            y           = 0,
            z           = 47270,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000051,
        ),
        ScenaEventData(
            x           = 34300,
            y           = 0,
            z           = 52980,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000051,
        ),
        ScenaEventData(
            x           = 66000,
            y           = 0,
            z           = 52470,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000052,
        ),
        ScenaEventData(
            x           = 73000,
            y           = 0,
            z           = 34550,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000053,
        ),
        ScenaEventData(
            x           = 54800,
            y           = 0,
            z           = 49170,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000054,
        ),
    )

# id: 0x10005 offset: 0x7AA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 55000,
            triggerZ            = 0,
            triggerY            = 45300,
            triggerRange        = 1700,
            actorX              = 55000,
            actorZ              = 2500,
            actorY              = 45300,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 45000,
            triggerZ            = 0,
            triggerY            = 25400,
            triggerRange        = 500,
            actorX              = 45000,
            actorZ              = 0,
            actorY              = 25400,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 76980,
            triggerZ            = 0,
            triggerY            = 19020,
            triggerRange        = 800,
            actorX              = 76980,
            actorZ              = 0,
            actorY              = 19020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 44710,
            triggerZ            = 0,
            triggerY            = 70740,
            triggerRange        = 1500,
            actorX              = 44710,
            actorZ              = 1800,
            actorY              = 70740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x004B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 45280,
            triggerZ            = 0,
            triggerY            = 71310,
            triggerRange        = 1500,
            actorX              = 45280,
            actorZ              = 1800,
            actorY              = 71310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x004C,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x85E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_886',
    )

    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0008)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0008)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)

    Jump('loc_8DA')

    def _loc_886(): pass

    label('loc_886')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_8AE',
    )

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0008)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0008)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0008)

    Jump('loc_8DA')

    def _loc_8AE(): pass

    label('loc_8AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_8DA',
    )

    SetChrPos(0x000D, 32000, 0, 21020, 0)
    SetChrPos(0x000E, 31990, 0, 22540, 180)

    Jump('loc_8DA')

    def _loc_8DA(): pass

    label('loc_8DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_909',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0008)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0008)
    SetChrPos(0x0009, 48900, 0, 48800, 0)

    Jump('loc_A64')

    def _loc_909(): pass

    label('loc_909')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_93F',
    )

    SetChrPos(0x0009, 68600, 0, 42100, 0)
    SetChrPos(0x000A, 66000, 0, 40200, 225)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0008)

    Jump('loc_A64')

    def _loc_93F(): pass

    label('loc_93F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_975',
    )

    SetChrPos(0x0009, 48900, 0, 48800, 0)
    SetChrPos(0x000A, 34900, 0, 38200, 0)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0008)

    Jump('loc_A64')

    def _loc_975(): pass

    label('loc_975')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_9AB',
    )

    SetChrPos(0x0009, 70160, 0, 16850, 0)
    SetChrPos(0x000A, 72160, 0, 18850, 0)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0008)

    Jump('loc_A64')

    def _loc_9AB(): pass

    label('loc_9AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_9E8',
    )

    SetChrPos(0x0009, 70160, 0, 16850, 90)
    SetChrPos(0x000A, 71160, 0, 17850, 225)
    SetChrPos(0x0011, 72160, 0, 18850, 0)

    Jump('loc_A64')

    def _loc_9E8(): pass

    label('loc_9E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_A33',
    )

    SetChrPos(0x0011, 45200, 0, 42700, 0)
    SetChrPos(0x0009, 46900, 0, 74100, 0)
    CreateThread(0x0009, 0x00, 0x00, 0x0004)
    SetChrPos(0x000A, 49900, 0, 72100, 0)
    CreateThread(0x000A, 0x00, 0x00, 0x0003)

    Jump('loc_A64')

    def _loc_A33(): pass

    label('loc_A33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 6, 0x206)),
            Expr.Return,
        ),
        'loc_A64',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0009, 0x0008)
    SetChrFlags(0x000A, 0x0008)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0008)
    TerminateThread(0x0011, 0xFF)

    def _loc_A64(): pass

    label('loc_A64')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A6F',
    )

    def _loc_A6F(): pass

    label('loc_A6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 7, 0x217)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_A95',
    )

    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0012, 0x0008)
    SetChrFlags(0x0013, 0x0008)

    Jump('loc_B09')

    def _loc_A95(): pass

    label('loc_A95')

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_AB8',
    )

    SetChrPos(0x0012, 62400, 250, 22000, 270)
    ClearChrFlags(0x0012, 0x0080)

    Jump('loc_B09')

    def _loc_AB8(): pass

    label('loc_AB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_ADD',
    )

    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 32150, 0, 28000, 45)
    ClearChrFlags(0x0013, 0x0080)

    Jump('loc_B09')

    def _loc_ADD(): pass

    label('loc_ADD')

    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 45660, 0, 19400, 270)
    SetChrPos(0x0012, 62400, 250, 22000, 270)

    def _loc_B09(): pass

    label('loc_B09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 0, 0x258)),
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_B1A',
    )

    Jump('loc_B70')

    def _loc_B1A(): pass

    label('loc_B1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B51',
    )

    SetChrPos(0x0014, 36320, 0, 57180, 135)
    ClearChrFlags(0x0014, 0x0040)
    SetChrChipByIndex(0x0014, 19)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0015, 0x0008)

    Jump('loc_B70')

    def _loc_B51(): pass

    label('loc_B51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B70',
    )

    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0014, 0x0008)
    SetChrFlags(0x0015, 0x0008)

    Jump('loc_B70')

    def _loc_B70(): pass

    label('loc_B70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_B7E',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0047)

    def _loc_B7E(): pass

    label('loc_B7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_B95',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0048)

    def _loc_B95(): pass

    label('loc_B95')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_BB1'),
        (0x00000077, 'loc_BE9'),
        (0x0000006E, 'loc_C58'),
        (0x0000007A, 'loc_CC7'),
        (0x00000002, 'loc_CDD'),
        (-1, 'loc_D0A'),
    )

    def _loc_BB1(): pass

    label('loc_BB1')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0020)"),
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BD8',
    )

    OP_28(0x0009, 0x04, 0x10)
    Event(1, 0x0023)

    Jump('loc_BE6')

    def _loc_BD8(): pass

    label('loc_BD8')

    ClearMapFlags(0x00000001)
    SetMapFlags(0x00000080)
    Event(1, 0x0009)

    def _loc_BE6(): pass

    label('loc_BE6')

    Jump('loc_D0A')

    def _loc_BE9(): pass

    label('loc_BE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 2, 0x202)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BF4',
    )

    Jump('loc_D0A')

    def _loc_BF4(): pass

    label('loc_BF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 3, 0x203)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C55',
    )

    EventBegin(0x00)
    SetMapFlags(0x00400000)
    SetChrPos(0x0101, 48300, 0, 7432, 0)
    SetChrPos(0x0102, 49500, 0, 6573, 0)
    CameraMove(49336, 0, 72554, 0)
    OP_6C(36000, 0)
    CameraSetDistance(5000, 0)
    FadeIn(500, 0)
    Event(0, 0x0021)

    def _loc_C55(): pass

    label('loc_C55')

    Jump('loc_D0A')

    def _loc_C58(): pass

    label('loc_C58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 6, 0x206)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CC4',
    )

    ClearMapFlags(0x00000001)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    SetChrPos(0x0009, 57890, 0, 14350, 0)
    SetChrPos(0x000A, 57890, 0, 14350, 0)
    CameraMove(49800, 0, 18520, 0)
    OP_6C(33000, 0)
    FadeIn(500, 0)
    Event(0, 0x0025)

    def _loc_CC4(): pass

    label('loc_CC4')

    Jump('loc_D0A')

    def _loc_CC7(): pass

    label('loc_CC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 4, 0x264)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 3, 0x263)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CDA',
    )

    SetScenaFlags(ScenaFlag(0x004C, 4, 0x264))
    Event(0, 0x0015)

    def _loc_CDA(): pass

    label('loc_CDA')

    Jump('loc_D0A')

    def _loc_CDD(): pass

    label('loc_CDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_CEB',
    )

    Event(0, 0x001C)

    Jump('loc_D07')

    def _loc_CEB(): pass

    label('loc_CEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 7, 0x22F)),
            Expr.Return,
        ),
        'loc_CFE',
    )

    SetChrFlags(0x0011, 0x0080)
    Event(0, 0x001A)

    Jump('loc_D07')

    def _loc_CFE(): pass

    label('loc_CFE')

    SetChrFlags(0x0011, 0x0080)
    Event(0, 0x001B)

    def _loc_D07(): pass

    label('loc_D07')

    Jump('loc_D0A')

    def _loc_D0A(): pass

    label('loc_D0A')

    Return()

# id: 0x0001 offset: 0xD0B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D23',
    )

    OP_B1('t0100_y')

    Jump('loc_D2C')

    def _loc_D23(): pass

    label('loc_D23')

    OP_B1('t0100_n')

    def _loc_D2C(): pass

    label('loc_D2C')

    OP_16(0x02, 4000, -80000, -88000, 196609)

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x01, 0x0020)"),
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_D57',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_D69')

    def _loc_D57(): pass

    label('loc_D57')

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D69',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_D69')

    def _loc_D69(): pass

    label('loc_D69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 6, 0x206)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D75',
    )

    OP_64(0x02, 0x0001)

    def _loc_D75(): pass

    label('loc_D75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_D9B',
    )

    OP_6F(0x0025, 90)
    OP_6F(0x0027, 90)
    OP_6F(0x0029, 90)
    OP_6F(0x002B, 90)

    Jump('loc_E5F')

    def _loc_D9B(): pass

    label('loc_D9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 5, 0x22D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DC6',
    )

    OP_6F(0x0025, 100)
    OP_6F(0x0027, 100)
    OP_6F(0x0029, 100)
    OP_6F(0x002B, 100)

    Jump('loc_E5F')

    def _loc_DC6(): pass

    label('loc_DC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DF1',
    )

    OP_6F(0x0025, 50)
    OP_6F(0x0027, 50)
    OP_6F(0x0029, 50)
    OP_6F(0x002B, 50)

    Jump('loc_E5F')

    def _loc_DF1(): pass

    label('loc_DF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E1C',
    )

    OP_6F(0x0025, 30)
    OP_6F(0x0027, 30)
    OP_6F(0x0029, 30)
    OP_6F(0x002B, 30)

    Jump('loc_E5F')

    def _loc_E1C(): pass

    label('loc_E1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E43',
    )

    OP_6F(0x0025, 90)
    OP_6F(0x0027, 90)
    OP_6F(0x0029, 90)
    OP_6F(0x002B, 90)

    Jump('loc_E5F')

    def _loc_E43(): pass

    label('loc_E43')

    OP_6F(0x0025, 30)
    OP_6F(0x0027, 30)
    OP_6F(0x0029, 30)
    OP_6F(0x002B, 30)

    def _loc_E5F(): pass

    label('loc_E5F')

    Return()

# id: 0x0002 offset: 0xE60
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
        'loc_E85',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_FC7')

    def _loc_E85(): pass

    label('loc_E85')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E9E',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_FC7')

    def _loc_E9E(): pass

    label('loc_E9E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EB7',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_FC7')

    def _loc_EB7(): pass

    label('loc_EB7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ED0',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_FC7')

    def _loc_ED0(): pass

    label('loc_ED0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EE9',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_FC7')

    def _loc_EE9(): pass

    label('loc_EE9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F02',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_FC7')

    def _loc_F02(): pass

    label('loc_F02')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F1B',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_FC7')

    def _loc_F1B(): pass

    label('loc_F1B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F34',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_FC7')

    def _loc_F34(): pass

    label('loc_F34')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F4D',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_FC7')

    def _loc_F4D(): pass

    label('loc_F4D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F66',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_FC7')

    def _loc_F66(): pass

    label('loc_F66')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F7F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_FC7')

    def _loc_F7F(): pass

    label('loc_F7F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F98',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_FC7')

    def _loc_F98(): pass

    label('loc_F98')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FB1',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_FC7')

    def _loc_FB1(): pass

    label('loc_FB1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FC7',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_FC7(): pass

    label('loc_FC7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_FDC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_FC7')

    def _loc_FDC(): pass

    label('loc_FDC')

    Return()

# id: 0x0003 offset: 0xFDD
@scena.Code('func_03_FDD')
def func_03_FDD():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_100A',
    )

    def _loc_FE4(): pass

    label('loc_FE4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1007',
    )

    OP_8D(0x00FE, 47400, 52400, 50900, 47700, 3000)

    Jump('loc_FE4')

    def _loc_1007(): pass

    label('loc_1007')

    Jump('loc_1115')

    def _loc_100A(): pass

    label('loc_100A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_1037',
    )

    def _loc_1011(): pass

    label('loc_1011')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1034',
    )

    OP_8D(0x00FE, 64500, 43600, 73600, 38500, 3000)

    Jump('loc_1011')

    def _loc_1034(): pass

    label('loc_1034')

    Jump('loc_1115')

    def _loc_1037(): pass

    label('loc_1037')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1064',
    )

    def _loc_103E(): pass

    label('loc_103E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1061',
    )

    OP_8D(0x00FE, 47400, 52400, 50900, 47700, 3000)

    Jump('loc_103E')

    def _loc_1061(): pass

    label('loc_1061')

    Jump('loc_1115')

    def _loc_1064(): pass

    label('loc_1064')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1091',
    )

    def _loc_106B(): pass

    label('loc_106B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_108E',
    )

    OP_8D(0x00FE, 74178, 21340, 67183, 16526, 4000)

    Jump('loc_106B')

    def _loc_108E(): pass

    label('loc_108E')

    Jump('loc_1115')

    def _loc_1091(): pass

    label('loc_1091')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1115',
    )

    ChrWalkTo(0x00FE, 48900, 0, 42400, 6000, 0x00)
    ChrWalkTo(0x00FE, 58900, 0, 42400, 6000, 0x00)
    ChrWalkTo(0x00FE, 58900, 0, 60000, 6000, 0x00)
    ChrWalkTo(0x00FE, 57500, 0, 60000, 6000, 0x00)
    ChrWalkTo(0x00FE, 57500, 0, 71100, 6000, 0x00)
    ChrWalkTo(0x00FE, 48900, 0, 71100, 6000, 0x00)

    Jump('loc_1091')

    def _loc_1115(): pass

    label('loc_1115')

    Return()

# id: 0x0004 offset: 0x1116
@scena.Code('func_04_1116')
def func_04_1116():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_1143',
    )

    def _loc_111D(): pass

    label('loc_111D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1140',
    )

    OP_8D(0x00FE, 64500, 43600, 73600, 38500, 3000)

    Jump('loc_111D')

    def _loc_1140(): pass

    label('loc_1140')

    Jump('loc_124E')

    def _loc_1143(): pass

    label('loc_1143')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1170',
    )

    def _loc_114A(): pass

    label('loc_114A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_116D',
    )

    OP_8D(0x00FE, 31500, 36600, 36600, 40300, 3000)

    Jump('loc_114A')

    def _loc_116D(): pass

    label('loc_116D')

    Jump('loc_124E')

    def _loc_1170(): pass

    label('loc_1170')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_119D',
    )

    def _loc_1177(): pass

    label('loc_1177')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_119A',
    )

    OP_8D(0x00FE, 74178, 21340, 67183, 16526, 3000)

    Jump('loc_1177')

    def _loc_119A(): pass

    label('loc_119A')

    Jump('loc_124E')

    def _loc_119D(): pass

    label('loc_119D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_11CA',
    )

    def _loc_11A4(): pass

    label('loc_11A4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_11C7',
    )

    OP_8D(0x00FE, 74178, 21340, 67183, 16526, 3000)

    Jump('loc_11A4')

    def _loc_11C7(): pass

    label('loc_11C7')

    Jump('loc_124E')

    def _loc_11CA(): pass

    label('loc_11CA')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_124E',
    )

    ChrWalkTo(0x00FE, 48900, 0, 71100, 6000, 0x00)
    ChrWalkTo(0x00FE, 48900, 0, 42400, 6000, 0x00)
    ChrWalkTo(0x00FE, 58900, 0, 42400, 6000, 0x00)
    ChrWalkTo(0x00FE, 58900, 0, 60000, 6000, 0x00)
    ChrWalkTo(0x00FE, 57500, 0, 60000, 6000, 0x00)
    ChrWalkTo(0x00FE, 57500, 0, 71100, 6000, 0x00)

    Jump('loc_11CA')

    def _loc_124E(): pass

    label('loc_124E')

    Return()

# id: 0x0005 offset: 0x124F
@scena.Code('func_05_124F')
def func_05_124F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1272',
    )

    OP_8D(0x00FE, 25948, 43568, 37838, 41060, 3000)

    Jump('func_05_124F')

    def _loc_1272(): pass

    label('loc_1272')

    Return()

# id: 0x0006 offset: 0x1273
@scena.Code('func_06_1273')
def func_06_1273():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_12A0',
    )

    def _loc_127A(): pass

    label('loc_127A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_129D',
    )

    OP_8D(0x00FE, 74178, 21340, 67183, 16526, 4000)

    Jump('loc_127A')

    def _loc_129D(): pass

    label('loc_129D')

    Jump('loc_12F0')

    def _loc_12A0(): pass

    label('loc_12A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_12CD',
    )

    def _loc_12A7(): pass

    label('loc_12A7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12CA',
    )

    OP_8D(0x00FE, 43800, 43900, 47136, 39800, 4000)

    Jump('loc_12A7')

    def _loc_12CA(): pass

    label('loc_12CA')

    Jump('loc_12F0')

    def _loc_12CD(): pass

    label('loc_12CD')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12F0',
    )

    OP_8D(0x00FE, 74178, 21340, 67183, 16526, 4000)

    Jump('loc_12CD')

    def _loc_12F0(): pass

    label('loc_12F0')

    Return()

# id: 0x0007 offset: 0x12F1
@scena.Code('func_07_12F1')
def func_07_12F1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_131F',
    )

    def _loc_12F9(): pass

    label('loc_12F9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_131C',
    )

    OP_8D(0x00FE, 31735, 16555, 28343, 23211, 2000)

    Jump('loc_12F9')

    def _loc_131C(): pass

    label('loc_131C')

    Jump('loc_1334')

    def _loc_131F(): pass

    label('loc_131F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1334',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_131F')

    def _loc_1334(): pass

    label('loc_1334')

    Return()

# id: 0x0008 offset: 0x1335
@scena.Code('func_08_1335')
def func_08_1335():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_135C',
    )

    def _loc_1344(): pass

    label('loc_1344')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1359',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_1344')

    def _loc_1359(): pass

    label('loc_1359')

    Jump('loc_137F')

    def _loc_135C(): pass

    label('loc_135C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_137F',
    )

    OP_8D(0x00FE, 63200, 17400, 61600, 22900, 2000)

    Jump('loc_135C')

    def _loc_137F(): pass

    label('loc_137F')

    Return()

# id: 0x0009 offset: 0x1380
@scena.Code('func_09_1380')
def func_09_1380():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13AF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13AF',
    )

    def _loc_139A(): pass

    label('loc_139A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_13AF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_139A')

    def _loc_13AF(): pass

    label('loc_13AF')

    Return()

# id: 0x000A offset: 0x13B0
@scena.Code('func_0A_13B0')
def func_0A_13B0():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x00FE, 0x0040)
    OP_8D(0x00FE, 51380, 38050, 58760, 43900, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_13E4(): pass

    label('loc_13E4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_15B2',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x960),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_157B',
    )

    TerminateThread(0x00FE, 0x01)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_146B',
    )

    @scena.Lambda('lambda_144F')
    def lambda_144F():
        OP_97(0x00FE, 55000, 47140, 360000, 7000, 0x0001)
        Yield()

        Jump('lambda_144F')

    DispatchAsync2(0x00FE, 0x0001, lambda_144F)

    Jump('loc_148A')

    def _loc_146B(): pass

    label('loc_146B')

    @scena.Lambda('lambda_1471')
    def lambda_1471():
        OP_97(0x00FE, 55000, 47140, -360000, 7000, 0x0001)
        Yield()

        Jump('lambda_1471')

    DispatchAsync2(0x00FE, 0x0001, lambda_1471)

    def _loc_148A(): pass

    label('loc_148A')

    SetChrChipByIndex(0x00FE, 21)
    ClearChrFlags(0x00FE, 0x0400)
    SetChrFlags(0x00FE, 0x0004)
    def _loc_1499(): pass

    label('loc_1499')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_14D1',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0xC8),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x2),
            (Expr.PushLong, 0x2328),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_14C9',
    )

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 2000)

    Jump('loc_14D1')

    def _loc_14C9(): pass

    label('loc_14C9')

    Sleep(15)

    Jump('loc_1499')

    def _loc_14D1(): pass

    label('loc_14D1')

    SetChrFlags(0x00FE, 0x0080)
    TerminateThread(0x00FE, 0x01)
    ClearChrFlags(0x00FE, 0x0004)
    SetChrPos(0x00FE, 55000, 0, 47140, 74)
    def _loc_14F0(): pass

    label('loc_14F0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1578',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x61A8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x61A8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x61A8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x61A8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1570',
    )

    ClearChrFlags(0x00FE, 0x0080)
    SetChrChipByIndex(0x00FE, 22)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 0)
    ClearChrFlags(0x00FE, 0x0004)
    OP_8D(0x00FE, 51380, 38050, 58760, 43900, 0)

    Jump('loc_1578')

    def _loc_1570(): pass

    label('loc_1570')

    Sleep(500)

    Jump('loc_14F0')

    def _loc_1578(): pass

    label('loc_1578')

    Jump('loc_15AF')

    def _loc_157B(): pass

    label('loc_157B')

    Sleep(100)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x14),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15AF',
    )

    @scena.Lambda('lambda_1597')
    def lambda_1597():
        OP_8D(0x00FE, 51380, 38050, 58760, 43900, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1597)

    def _loc_15AF(): pass

    label('loc_15AF')

    Jump('loc_13E4')

    def _loc_15B2(): pass

    label('loc_15B2')

    Return()

# id: 0x000B offset: 0x15B3
@scena.Code('func_0B_15B3')
def func_0B_15B3():
    SetMapFlags(0x00000080)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１０７５年\n',
            '　由利贝尔王家、七耀教会\n',
            '　以及洛连特市共同建造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１１９２年\n',
            '　百日战役中，被围攻洛连特的\n',
            '　埃雷波尼亚帝国军队炮击而倒塌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１１９７年\n',
            '　在市民的协力下得以重建。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ClearMapFlags(0x00000080)

    Return()

# id: 0x000C offset: 0x16AB
@scena.Code('func_0C_16AB')
def func_0C_16AB():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1831',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17C6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '怎么了，艾丝蒂尔。\n',
            '你要出去旅行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F就算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我要暂时离开\n',
            '洛连特一段时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我不在的时候，\n',
            '你不要感到寂寞哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '傻、傻瓜啊你。\n',
            '谁会感到寂寞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……对了，你什么时候回来啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F唔……其实我也不清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_182E')

    def _loc_17C6(): pass

    label('loc_17C6')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……你要早点回来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呵呵，你刚才说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什、什么都没说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_182E(): pass

    label('loc_182E')

    Jump('loc_1D43')

    def _loc_1831(): pass

    label('loc_1831')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_1866',
    )

    ChrTalk(
        0x00FE,
        (
            '克劳斯爷爷家里\n',
            '是不是发生什么事了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D43')

    def _loc_1866(): pass

    label('loc_1866')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1935',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1900',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '记者好像是来采访\n',
            '卡西乌斯叔叔的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我老爸虽然是\n',
            '王国军的士兵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是和游击士比起来，\n',
            '就显得缺乏人情味又不引人注目了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1932')

    def _loc_1900(): pass

    label('loc_1900')

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '和士兵相比，\n',
            '果然还是游击士比较帅啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1932(): pass

    label('loc_1932')

    Jump('loc_1D43')

    def _loc_1935(): pass

    label('loc_1935')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_19B6',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～啊，好想快点变成大人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想做个游击士，\n',
            '然后大展拳脚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '居然被那个\n',
            '艾丝蒂尔抢先了，\n',
            '真是不甘心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D43')

    def _loc_19B6(): pass

    label('loc_19B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1B0A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AAA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '我上次看到\n',
            '克劳斯爷爷在钟楼周围\n',
            '专心致志地拔草呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长连这种事\n',
            '都要亲力亲为的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那是兴趣吧，\n',
            '都说他喜欢园艺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F所以他才会被叫作\n',
            '『克劳斯爷爷』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F呵呵，\n',
            '和蔼可亲的称呼也挺好的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B07')

    def _loc_1AAA(): pass

    label('loc_1AAA')

    ChrTalk(
        0x00FE,
        (
            '我上次看到\n',
            '克劳斯爷爷在钟楼周围\n',
            '专心致志地拔草呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长连这种事\n',
            '都要亲力亲为的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B07(): pass

    label('loc_1B07')

    Jump('loc_1D43')

    def _loc_1B0A(): pass

    label('loc_1B0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1B65',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    OP_4A(0x0009, 0)

    ChrTalk(
        0x0009,
        (
            '我就是卡西乌斯·布莱特！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x0009, 0)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '别跑，混帐魔兽，\n',
            '受死吧！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x0009, 0)

    Jump('loc_1D43')

    def _loc_1B65(): pass

    label('loc_1B65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1C8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C2F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0009,
        (
            '哼……\n',
            '还是要谢谢\n',
            '你们救了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '而且……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然不服气，\n',
            '但艾丝蒂尔你真的很厉害哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然还远远比不上\n',
            '卡西乌斯叔叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '决定了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我将来一定要\n',
            '成为一名游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C8A')

    def _loc_1C2F(): pass

    label('loc_1C2F')

    ChrTalk(
        0x0009,
        (
            '说起来，\n',
            '卡西乌斯叔叔\n',
            '真是太酷了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要当男子汉就是应该\n',
            '以卡西乌斯叔叔作为目标啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C8A(): pass

    label('loc_1C8A')

    Jump('loc_1D43')

    def _loc_1C8D(): pass

    label('loc_1C8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1CC5',
    )

    ChrTalk(
        0x0009,
        (
            '本应在翡翠之塔。\n',
            '看到我就说明发生了BUG。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D43')

    def _loc_1CC5(): pass

    label('loc_1CC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D1A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    OP_4A(0x0009, 0)

    ChrTalk(
        0x0009,
        (
            '嘿嘿，来追我呀，追我呀～～',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x0009, 0)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '你追不到我的啦～',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x0009, 0)

    Jump('loc_1D43')

    def _loc_1D1A(): pass

    label('loc_1D1A')

    OP_4A(0x0009, 0)

    ChrTalk(
        0x0009,
        (
            '但是～\n',
            '那可是我先发现的哦～',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x0009, 0)

    def _loc_1D43(): pass

    label('loc_1D43')

    TalkEnd(0x0009)

    Return()

# id: 0x000D offset: 0x1D47
@scena.Code('func_0D_1D47')
def func_0D_1D47():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_1D93',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才克劳斯爷爷\n',
            '急匆匆地跑了过去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2057')

    def _loc_1D93(): pass

    label('loc_1D93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1DF7',
    )

    ChrTalk(
        0x00FE,
        (
            '我老爸也一直在读\n',
            '《利贝尔通讯》这本杂志呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '封面上会刊登\n',
            '眼下风云人物的照片哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2057')

    def _loc_1DF7(): pass

    label('loc_1DF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1E55',
    )

    ChrTalk(
        0x00FE,
        (
            '最近在主日学校学了\n',
            '关于游击士协会的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士果然是\n',
            '让人神往的职业啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2057')

    def _loc_1E55(): pass

    label('loc_1E55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1EA7',
    )

    ChrTalk(
        0x00FE,
        (
            '市长家里的庭院\n',
            '真的很漂亮呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '克劳斯爷爷说\n',
            '那是他自己打理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2057')

    def _loc_1EA7(): pass

    label('loc_1EA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1EE2',
    )

    OP_4A(0x000A, 0)

    ChrTalk(
        0x000A,
        (
            '鲁克一点情面都不讲，\n',
            '我只好逃跑了。',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x000A, 0)

    Jump('loc_2057')

    def _loc_1EE2(): pass

    label('loc_1EE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1FEF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FA5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔姐姐，\n',
            '今天真是谢谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果姐姐你们\n',
            '没有来救我们的话，\n',
            '我们不知道会变成什么样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我想鲁克也会非常\n',
            '感谢姐姐你们的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '姐姐就别再生他的气了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FEC')

    def _loc_1FA5(): pass

    label('loc_1FA5')

    ChrTalk(
        0x000A,
        (
            '我想鲁克也会非常\n',
            '感谢姐姐你们的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '姐姐就别再生他的气了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FEC(): pass

    label('loc_1FEC')

    Jump('loc_2057')

    def _loc_1FEF(): pass

    label('loc_1FEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_202A',
    )

    ChrTalk(
        0x000A,
        (
            '应该在翡翠之塔的。\n',
            '如果看到了就请联系近藤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2057')

    def _loc_202A(): pass

    label('loc_202A')

    OP_4A(0x000A, 0)

    ChrTalk(
        0x000A,
        (
            '带我去嘛～！\n',
            '可是我提醒你的哦～',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x000A, 0)

    def _loc_2057(): pass

    label('loc_2057')

    TalkEnd(0x000A)

    Return()

# id: 0x000E offset: 0x205B
@scena.Code('func_0E_205B')
def func_0E_205B():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_2280',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2209',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔、约修亚。\n',
            '你们真的要去柏斯吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊哈哈……\n',
            '不愧是小克露莎啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '消息总是那么灵通。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们要调查一些事情，\n',
            '所以呢，要去柏斯那里才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不单是卡西乌斯叔叔，\n',
            '就连你们两人也不在了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……人家也要一起去，\n',
            '帮你们做采访。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '约修亚，把我也带上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F啊……这、这不好办哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我果然还是\n',
            '放不下这里发生的新闻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是让人烦恼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_227D')

    def _loc_2209(): pass

    label('loc_2209')

    ChrTalk(
        0x00FE,
        (
            '人家会乖乖地在这里等着，\n',
            '直到你们归来。\n',
            '所以你们要早点回来哦。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都不在的话，\n',
            '新闻的材料就少了很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_227D(): pass

    label('loc_227D')

    Jump('loc_377F')

    def _loc_2280(): pass

    label('loc_2280')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_23B1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2361',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x000B,
        (
            '啊，是艾丝蒂尔和约修亚！\n',
            '还有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0103, 400)
    OP_62(0x000B, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '呀，雪拉姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F你好啊，小克露莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '街上居然同时聚集了\n',
            '三位鼎鼎大名的游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哈，难道是有什么事件吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23AE')

    def _loc_2361(): pass

    label('loc_2361')

    ChrTalk(
        0x000B,
        (
            '街上居然同时聚集了\n',
            '三位鼎鼎大名的游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '难道是有什么事件吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23AE(): pass

    label('loc_23AE')

    Jump('loc_377F')

    def _loc_23B1(): pass

    label('loc_23B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_255E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2511',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x000B,
        (
            '艾丝蒂尔、约修亚㈱\n',
            '听说你们两人很活跃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '唔，\n',
            '在帕赛尔农场驱逐魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '在矿山救助矿工……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这次又要负责护送\n',
            '记者叔叔们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F知、知道得还真清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '嗯，还好啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '要是记者叔叔他们\n',
            '肯聘用人家就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '人家绝对\n',
            '是做记者的好料哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（嗯，\n',
            '　想来也的确挺适合的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（哈哈……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_255B')

    def _loc_2511(): pass

    label('loc_2511')

    ChrTalk(
        0x000B,
        (
            '要是记者叔叔他们\n',
            '肯聘用人家就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '人家绝对\n',
            '是做记者的好料哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_255B(): pass

    label('loc_255B')

    Jump('loc_377F')

    def _loc_255E(): pass

    label('loc_255E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_263A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2618',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x000B,
        (
            '上次我看见市长爷爷\n',
            '从游击士协会出来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '还有，最近经常在街上看见\n',
            '里农叔叔家的老婆婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不寻常呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '但是，到底要追哪一条线索呢，\n',
            '真是让人烦恼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2637')

    def _loc_2618(): pass

    label('loc_2618')

    ChrTalk(
        0x000B,
        (
            '啊啊，\n',
            '新闻在呼唤人家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2637(): pass

    label('loc_2637')

    Jump('loc_377F')

    def _loc_263A(): pass

    label('loc_263A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_26A7',
    )

    ChrTalk(
        0x000B,
        (
            '根据我的情报，\n',
            '帕赛尔农场那边\n',
            '好像有什么事要发生呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '要不要写份突击报道\n',
            '给爱娜姐姐呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_377F')

    def _loc_26A7(): pass

    label('loc_26A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_28A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2873',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x000B,
        (
            '对了， \n',
            '卡西乌斯叔叔上哪儿去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，因为工作的关系，\n',
            '他恐怕短期内不会回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '唔，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '卡西乌斯叔叔\n',
            '也是人家很关注的人呢。\n',
            '有点可惜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F小克露莎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我觉得卡西乌斯叔叔\n',
            '是个经得起考验的\n',
            '成熟男人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '他所表现出来的那种强大、\n',
            '不灭、独特的华丽，\n',
            '实在是让人无法抗拒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '他一定是很有影响力的游击士。\n',
            '嗯，卡西乌斯叔叔不错～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F……喂，\n',
            '小克露莎你几岁了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#019F哈哈，好早熟呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28A4')

    def _loc_2873(): pass

    label('loc_2873')

    ChrTalk(
        0x00FE,
        (
            '啊～啊，卡西乌斯叔叔不在，\n',
            '少了很多谈资呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28A4(): pass

    label('loc_28A4')

    Jump('loc_377F')

    def _loc_28A7(): pass

    label('loc_28A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_2EFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 5, 0x215)),
            Expr.Return,
        ),
        'loc_2982',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2948',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x000B,
        (
            '艾丝蒂尔和约修亚\n',
            '这么快就有表现了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '真不愧是人家\n',
            '关注的游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '继续好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '人家是你们\n',
            '忠实的崇拜者哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_297F')

    def _loc_2948(): pass

    label('loc_2948')

    ChrTalk(
        0x000B,
        (
            '继续好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '人家是你们\n',
            '忠实的崇拜者哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_297F(): pass

    label('loc_297F')

    Jump('loc_2EF8')

    def _loc_2982(): pass

    label('loc_2982')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 4, 0x214)),
            Expr.Return,
        ),
        'loc_2B3D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B00',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x000B,
        (
            '喂喂，\n',
            '艾丝蒂尔、约修亚。\n',
            '你们真的已经成为了游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F你的消息总是那么灵通啊～\n',
            '小克露莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '真不愧是克露莎\n',
            '看重的一对呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这下你们就可以大展拳脚了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '其实克露莎也\n',
            '喜欢有大人魅力的\n',
            '雪拉扎德姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '但是忍不住会偏袒\n',
            '艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#506F好、好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#019F多谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B3A')

    def _loc_2B00(): pass

    label('loc_2B00')

    ChrTalk(
        0x000B,
        (
            '一场划时代的大戏剧终于要开演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '人家好期待哦★',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B3A(): pass

    label('loc_2B3A')

    Jump('loc_2EF8')

    def _loc_2B3D(): pass

    label('loc_2B3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E61',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x000B,
        (
            '啊……\n',
            '艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '对了对了，\n',
            '你们两个成为游击士了，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是啊，\n',
            '为什么你会知道呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '因为因为，\n',
            '人家将来想成为一名记者嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '将来我会成为利贝尔通讯的女记者，\n',
            '发挥自己的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '可不要小看人家\n',
            '收集情报的能力哦。',
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
            '#506F是、是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '凭人家的直觉， \n',
            '你们两人肯定会成为风云人物的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F呵、呵呵，\n',
            '谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '因为爱而结合的你们，\n',
            '一定会成为坚守正义的游击士，\n',
            '这多美妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '感觉就像\n',
            '浪漫的舞台剧一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我和约修亚不是恋人，\n',
            '我们是家人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呵～\n',
            '艾丝蒂尔这你就不懂啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '约修亚是你们家的养子嘛，\n',
            '以后什么身份还说不定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '而且这样的故事\n',
            '读者也会很喜欢的。',
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
            '#019F读、读者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F唔……\n',
            '真是超乎我的想象呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '总之，\n',
            '我很期待你们的未来哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EF8')

    def _loc_2E61(): pass

    label('loc_2E61')

    ChrTalk(
        0x000B,
        (
            '相互信任守护着彼此，\n',
            '并尝试脱离险境的\n',
            '一对游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '啊，此时爱的种子\n',
            '就在他们的心中生根发芽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '多美妙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EF8(): pass

    label('loc_2EF8')

    Jump('loc_377F')

    def _loc_2EFB(): pass

    label('loc_2EFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_33D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 4, 0x214)),
            Expr.Return,
        ),
        'loc_307B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3050',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    SetScenaFlags(ScenaFlag(0x0042, 5, 0x215))

    ChrTalk(
        0x000B,
        (
            '喂喂，\n',
            '艾丝蒂尔、约修亚。\n',
            '你们真的已经成为了游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F你的消息总是那么灵通啊～\n',
            '小克露莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '真不愧是克露莎\n',
            '看重的一对呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这下你们就可以大展拳脚了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '其实克露莎\n',
            '也喜欢有大人魅力的\n',
            '雪拉扎德姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '但是忍不住会偏袒\n',
            '艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F好、好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#019F多谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3078')

    def _loc_3050(): pass

    label('loc_3050')

    ChrTalk(
        0x000B,
        (
            '好戏终于要开演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '好期待哦★',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3078(): pass

    label('loc_3078')

    Jump('loc_33D1')

    def _loc_307B(): pass

    label('loc_307B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3369',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    SetScenaFlags(ScenaFlag(0x0042, 5, 0x215))

    ChrTalk(
        0x000B,
        (
            '啊……\n',
            '艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '对了对了，\n',
            '你们两个成为游击士了，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是啊，\n',
            '为什么你会知道呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '因为我的目标\n',
            '是当记者嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我将来会加入利贝尔通讯社，\n',
            '当一名出色的女记者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '可不要小看我\n',
            '收集情报的能力哦。',
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
            '#506F是、是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '凭我的直觉， \n',
            '你们两人肯定会成为风云人物的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F呵、呵呵，\n',
            '谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '因为，彼此深爱的两位游击士\n',
            '共同坚守正义，\n',
            '这是多么美妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '感觉就像\n',
            '一场浪漫的爱情剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F我和约修亚不是恋人，\n',
            '是家人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呵～\n',
            '艾丝蒂尔这你就不懂啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '约修亚只是你们家的养子嘛，\n',
            '以后什么身份还说不定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '而且这样的故事\n',
            '读者也会很喜欢的。',
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
            '#019F读、读者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '总之，\n',
            '我很期待你们的未来哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33D1')

    def _loc_3369(): pass

    label('loc_3369')

    ChrTalk(
        0x000B,
        (
            '相互信任守护着彼此，\n',
            '并尝试脱离险境的\n',
            '一对游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '多美妙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33D1(): pass

    label('loc_33D1')

    Jump('loc_377F')

    def _loc_33D4(): pass

    label('loc_33D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36E8',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    SetScenaFlags(ScenaFlag(0x0042, 4, 0x214))

    ChrTalk(
        0x0101,
        (
            '#001F早上好呀，小克露莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '早上好。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '对了对了，\n',
            '你们两个成为游击士了，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F是啊，\n',
            '为什么你会知道呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '因为，我的目标\n',
            '是当记者嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我将来会加入利贝尔通讯社，\n',
            '当一名出色的女记者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '可不要小看我\n',
            '收集情报的能力哦。',
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
            '#506F是、是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '凭我的直觉， \n',
            '你们两人肯定会成为风云人物的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F呵、呵呵，\n',
            '谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '因为爱而结合的你们，\n',
            '一定会成为坚守正义的游击士，\n',
            '这多美妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '感觉就像\n',
            '浪漫的舞台剧一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F……啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我和约修亚不是恋人，\n',
            '我们是家人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呵～\n',
            '艾丝蒂尔这你就不懂啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '约修亚只是你们家的养子嘛，\n',
            '以后什么身份还说不定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '而且这样的故事\n',
            '读者也会很喜欢的。',
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
            '#019F读、读者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '总之，\n',
            '我很期待你们的未来哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_377F')

    def _loc_36E8(): pass

    label('loc_36E8')

    ChrTalk(
        0x000B,
        (
            '相互信任守护着彼此，\n',
            '并尝试脱离险境的\n',
            '一对游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '啊，此时爱的种子\n',
            '就在他们的心中生根发芽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '多美妙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_377F(): pass

    label('loc_377F')

    TalkEnd(0x000B)

    Return()

# id: 0x000F offset: 0x3783
@scena.Code('func_0F_3783')
def func_0F_3783():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_388D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_384B',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '最近，我的岳父\n',
            '在工作上给了我不少的建议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说我在林业\n',
            '这行业里做了很久，\n',
            '不过要学习的东西还有很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我以前的确是\n',
            '有点自高自大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我觉得有些羞愧呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_388A')

    def _loc_384B(): pass

    label('loc_384B')

    ChrTalk(
        0x00FE,
        (
            '我以前的确是\n',
            '有点自高自大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我觉得有些羞愧呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_388A(): pass

    label('loc_388A')

    Jump('loc_3D23')

    def _loc_388D(): pass

    label('loc_388D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_395B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3906',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '虽说工作挺顺利的，\n',
            '木材的销量也不断增加……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么说呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是没有得到\n',
            '岳父的认同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3958')

    def _loc_3906(): pass

    label('loc_3906')

    ChrTalk(
        0x00FE,
        (
            '虽说工作挺顺利的，\n',
            '木材的销量也不断增加……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是没有得到\n',
            '岳父的认同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3958(): pass

    label('loc_3958')

    Jump('loc_3D23')

    def _loc_395B(): pass

    label('loc_395B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_39DF',
    )

    ChrTalk(
        0x00FE,
        (
            '木材卖出去越多，\n',
            '我养家的自信和动力也\n',
            '源源不断地涌上来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事业上顺心顺境，\n',
            '我觉得自己的能力\n',
            '一点都不比岳父差。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D23')

    def _loc_39DF(): pass

    label('loc_39DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_3A3F',
    )

    ChrTalk(
        0x00FE,
        (
            '刚收到柏斯商人\n',
            '追加的木材订单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要继续加油，\n',
            '向其他地方推销自己的木材！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D23')

    def _loc_3A3F(): pass

    label('loc_3A3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_3B46',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3ADF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '我是为了\n',
            '能和妻子在一起， \n',
            '才承继了岳父的林业工作的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近好不容易\n',
            '才习惯了这份工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且感觉干劲和效率\n',
            '也提高了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B43')

    def _loc_3ADF(): pass

    label('loc_3ADF')

    ChrTalk(
        0x00FE,
        (
            '我是为了\n',
            '能和妻子在一起， \n',
            '才承继了岳父的林业工作的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近好不容易\n',
            '才习惯了这份工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B43(): pass

    label('loc_3B43')

    Jump('loc_3D23')

    def _loc_3B46(): pass

    label('loc_3B46')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_3B6C',
    )

    ChrTalk(
        0x000C,
        (
            '见到这个的你。\n',
            '是Bug。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D23')

    def _loc_3B6C(): pass

    label('loc_3B6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_3C31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BF3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x000C,
        (
            '虽然接受了商人的订货，\n',
            '不过木材好像还有些不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '为了我的妻子，为了得到岳父的承认，\n',
            '我一定要努力加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C2E')

    def _loc_3BF3(): pass

    label('loc_3BF3')

    ChrTalk(
        0x000C,
        (
            '为了我的妻子，为了得到岳父的承认，\n',
            '我一定要努力加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C2E(): pass

    label('loc_3C2E')

    Jump('loc_3D23')

    def _loc_3C31(): pass

    label('loc_3C31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CCB',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x000C,
        (
            '呼，\n',
            '今后的工作就得到\n',
            '南面的神秘森林去开展了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不久之后就会有\n',
            '柏斯的木材采购商来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '需要准备足够的木材\n',
            '供他们采购才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D23')

    def _loc_3CCB(): pass

    label('loc_3CCB')

    ChrTalk(
        0x000C,
        (
            '不久之后就会有\n',
            '柏斯的木材采购商来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '需要准备足够的木材\n',
            '供他们采购才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D23(): pass

    label('loc_3D23')

    TalkEnd(0x000C)

    Return()

# id: 0x0010 offset: 0x3D27
@scena.Code('func_10_3D27')
def func_10_3D27():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_3D78',
    )

    ChrTalk(
        0x0011,
        (
            '刚才克劳斯爷爷\n',
            '从这里走过哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '还好大声地和我\n',
            '打了招呼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EFD')

    def _loc_3D78(): pass

    label('loc_3D78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_3DC5',
    )

    ChrTalk(
        0x0011,
        (
            '鲁克真是的，\n',
            '从早上开始就一直那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '男孩子还真是单纯啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EFD')

    def _loc_3DC5(): pass

    label('loc_3DC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_3DFA',
    )

    ChrTalk(
        0x0011,
        (
            '鲁克和帕特他们\n',
            '究竟跑到哪里去了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EFD')

    def _loc_3DFA(): pass

    label('loc_3DFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3ED2',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x0011,
        (
            '呀，\n',
            '是艾丝蒂尔姐姐和约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F早上好啊，小尤妮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F今天怎么没有和\n',
            '鲁克、帕特在一起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '直到刚才\n',
            '还和他们在一起的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不过一眨眼的功夫他们两个\n',
            '就不知道跑到哪里去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EFD')

    def _loc_3ED2(): pass

    label('loc_3ED2')

    ChrTalk(
        0x0011,
        (
            '鲁克和帕特他们\n',
            '究竟跑到哪里去了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3EFD(): pass

    label('loc_3EFD')

    TalkEnd(0x0011)

    Return()

# id: 0x0011 offset: 0x3F01
@scena.Code('func_11_3F01')
def func_11_3F01():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_4018',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3FDC',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x000E,
        (
            '成功啦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '听我说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '她终于答应\n',
            '和我交往了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '啊啊，女神大人……\n',
            '一整天所做的努力终于没有白费啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（一、一整天？\n',
            '　唔……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（真是坚持不懈换来的胜利呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4015')

    def _loc_3FDC(): pass

    label('loc_3FDC')

    ChrTalk(
        0x000E,
        (
            '啊啊，女神大人……\n',
            '一整天所做的努力终于没有白费啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4015(): pass

    label('loc_4015')

    Jump('loc_412B')

    def _loc_4018(): pass

    label('loc_4018')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_40ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40AA',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x000E,
        (
            '唉～从早晨开始，\n',
            '我就告白好多次了，\n',
            '可她好像都不愿意接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '看起来她应该\n',
            '并不讨厌我呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我究竟应该怎么办啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40EA')

    def _loc_40AA(): pass

    label('loc_40AA')

    ChrTalk(
        0x000E,
        (
            '唉～从早晨开始，\n',
            '我就告白好多次了，\n',
            '可她好像都不愿意接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40EA(): pass

    label('loc_40EA')

    Jump('loc_412B')

    def _loc_40ED(): pass

    label('loc_40ED')

    ChrTalk(
        0x000E,
        (
            '啊……\n',
            '那个姑娘真可爱呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '鼓足勇气\n',
            '去和她打招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_412B(): pass

    label('loc_412B')

    TalkEnd(0x000E)

    Return()

# id: 0x0012 offset: 0x412F
@scena.Code('func_12_412F')
def func_12_412F():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_41D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41A8',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '成功啦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我约她一起去看女王的诞辰庆典，\n',
            '她真的答应了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要努力打工赚钱才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41CF')

    def _loc_41A8(): pass

    label('loc_41A8')

    ChrTalk(
        0x00FE,
        (
            '从现在起我要\n',
            '努力打工赚钱才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41CF(): pass

    label('loc_41CF')

    Jump('loc_4390')

    def _loc_41D2(): pass

    label('loc_41D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_42B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4269',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x0010,
        (
            '听说王都将举行\n',
            '女王的诞辰庆典呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '而且还会举办每年一度的武术大会，\n',
            '这还真是非常热闹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '我约了她一起去看诞辰庆典。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42B6')

    def _loc_4269(): pass

    label('loc_4269')

    ChrTalk(
        0x0010,
        (
            '我约了她到王都看女王的诞辰庆典。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呵呵呵，\n',
            '其实我想在那里向她表白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42B6(): pass

    label('loc_42B6')

    Jump('loc_4390')

    def _loc_42B9(): pass

    label('loc_42B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_4315',
    )

    ChrTalk(
        0x0010,
        (
            '每天和她见面的时候，\n',
            '不是聊天就是喝茶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '洛连特的约会场所\n',
            '实在是有限啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4390')

    def _loc_4315(): pass

    label('loc_4315')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_4360',
    )

    ChrTalk(
        0x0010,
        (
            '啊啊，真是幸福呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '每天都可以\n',
            '和自己喜欢的人一起度过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4390')

    def _loc_4360(): pass

    label('loc_4360')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_4390',
    )

    ChrTalk(
        0x0010,
        (
            '嗯呼呼呼，\n',
            '今天是我第一次的约会哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4390(): pass

    label('loc_4390')

    TalkEnd(0x0010)

    Return()

# id: 0x0013 offset: 0x4394
@scena.Code('func_13_4394')
def func_13_4394():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_44E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44BE',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x000D,
        (
            '星星开始闪烁的时候，\n',
            '他在塔上对我这么说——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '可以和我交往吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '嗯呵呵★',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这就是\n',
            '我梦寐以求的场景啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（唔，\n',
            '　的确是一个相当不错的地方……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F（不过为了听这句话\n',
            '　两个人特意跑上这里来？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（呵呵……\n',
            '　这要看当事人是怎么想的了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44E2')

    def _loc_44BE(): pass

    label('loc_44BE')

    ChrTalk(
        0x000D,
        (
            '呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '好·幸·福·呢★',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44E2(): pass

    label('loc_44E2')

    Jump('loc_475F')

    def _loc_44E5(): pass

    label('loc_44E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_4709',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4686',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x000D,
        (
            '哎～我该怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '那个人，他好像喜欢我。\n',
            '我虽然很乐意接受他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过这样的场景，\n',
            '跟我理想中的告白场景不太一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F唔……\n',
            '场景什么的真的那么重要吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '当然啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这有可能成为我\n',
            '一生难忘的回忆啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '当我变成老太婆的时候，\n',
            '临死前脑海里浮现的不也应该是\n',
            '现在这个最美妙的场景吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我不能在这个胡同里面\n',
            '接受表白啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呵呵……\n',
            '这个就是当事人的想法问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4706')

    def _loc_4686(): pass

    label('loc_4686')

    ChrTalk(
        0x000D,
        (
            '他，无论怎样热心地向我告白……\n',
            '我还是觉得跟我理想中的\n',
            '告白场景不太一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '要是他能在\n',
            '一个好点的场景\n',
            '说那番话就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4706(): pass

    label('loc_4706')

    Jump('loc_475F')

    def _loc_4709(): pass

    label('loc_4709')

    ChrTalk(
        0x000D,
        (
            '今天这么好的天气，\n',
            '真是让人神清气爽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我感觉今天似乎\n',
            '有什么好事要发生呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_475F(): pass

    label('loc_475F')

    TalkEnd(0x000D)

    Return()

# id: 0x0014 offset: 0x4763
@scena.Code('func_14_4763')
def func_14_4763():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_498A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4821',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '虽然有些犹豫，不过我还是决定\n',
            '和他一起去观看女王的诞辰庆典。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而我还是对妈妈说\n',
            '自己是和普通朋友一起去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是对不起，妈妈……\n',
            '不过我还是想和他一起去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4987')

    def _loc_4821(): pass

    label('loc_4821')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_496D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '王都这个地方，\n',
            '听说是个很繁华的大都会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '被传颂成为灯火辉煌的\n',
            '传统与美丽相融合的不夜城……\n',
            '伫立在湖畔的典雅的格兰赛尔城……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '络绎不绝往来穿梭的人群……\n',
            '各式各样的街市商店……\n',
            '还有诞辰庆典的盛装游行和烟花表演……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光是想想就已经很期待了。\n',
            '真是让人向往的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且还可以和他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4987')

    def _loc_496D(): pass

    label('loc_496D')

    ChrTalk(
        0x00FE,
        (
            '啊啊，我太激动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4987(): pass

    label('loc_4987')

    Jump('loc_4D04')

    def _loc_498A(): pass

    label('loc_498A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_4A96',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A2E',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x000F,
        (
            '他主动约我一起\n',
            '到王都观看女王的诞辰庆典呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '哎呀，有点犹豫呢。\n',
            '怎么和妈妈说才好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '要是到了王都之后\n',
            '他向我求婚的话那就太棒了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A93')

    def _loc_4A2E(): pass

    label('loc_4A2E')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x000F,
        (
            '他主动约我一起\n',
            '到王都观看女王的诞辰庆典呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '要是到了王都之后\n',
            '他向我求婚的话那就太棒了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A93(): pass

    label('loc_4A93')

    Jump('loc_4D04')

    def _loc_4A96(): pass

    label('loc_4A96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_4BBB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B62',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x000F,
        (
            '我觉得每天和他见面\n',
            '是一件开心的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '不过最近的约会地点\n',
            '已经有些千篇一律了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#502F嗯，现在才是\n',
            '考验男朋友真正价值的时候呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F（艾丝蒂尔，说的挺直接嘛……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BB8')

    def _loc_4B62(): pass

    label('loc_4B62')

    ChrTalk(
        0x000F,
        (
            '我觉得每天和他见面\n',
            '是一件开心的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '最近的约会地点\n',
            '已经有些千篇一律了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4BB8(): pass

    label('loc_4BB8')

    Jump('loc_4D04')

    def _loc_4BBB(): pass

    label('loc_4BBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_4BF6',
    )

    ChrTalk(
        0x000F,
        (
            '他这个人其实挺好的呢。\n',
            '希望他能永远疼爱我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D04')

    def _loc_4BF6(): pass

    label('loc_4BF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_4D04',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C9A',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x000F,
        (
            '呵呵，\n',
            '我们才刚刚开始交往呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '刚才看到什么东西闪了一闪呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '啊啊，\n',
            '这世界其实是如此的美丽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F（唔，二人世界呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D04')

    def _loc_4C9A(): pass

    label('loc_4C9A')

    ChrTalk(
        0x000F,
        (
            '呵呵，现在觉得什么都是新鲜美好的。\n',
            '刚才看到什么东西闪了一闪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '啊啊，\n',
            '这世界其实是如此的美丽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D04(): pass

    label('loc_4D04')

    TalkEnd(0x000F)

    Return()

# id: 0x0015 offset: 0x4D08
@scena.Code('func_15_4D08')
def func_15_4D08():
    EventBegin(0x00)
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    SetChrFlags(0x0020, 0x0080)
    SetChrPos(0x0000, 49730, 0, 79070, 180)
    SetChrPos(0x0001, 50770, 0, 79870, 180)
    SetChrPos(0x0002, 49620, 0, 80520, 180)
    SetChrPos(0x0019, 50932, 0, 42709, 270)
    SetChrPos(0x0018, 64013, 0, 42894, 270)
    OP_6C(45000, 0)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0019,
        '女孩的声音',
        (
            '#0280011197V前辈，太危险了啦！\n',
            '跑得那么快的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0018,
        '男人的声音',
        (
            '#0270011198V因、因为……\n',
            '不跑快点就赶不上啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearMapFlags(0x00000001)
    ChrTurnDirection(0x0019, 0x0018, 0)
    CameraMove(51350, 0, 43040, 3000)

    @scena.Lambda('lambda_4E24')
    def lambda_4E24():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_4E24')

    DispatchAsync2(0x0019, 0x0001, lambda_4E24)

    ChrWalkTo(0x0018, 57947, 0, 43302, 5000, 0x00)
    OP_62(0x0018, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x03)
    ChrMoveTo(0x0018, 56374, 0, 43102, 3000, 0x00)
    ChrMoveTo(0x0018, 55451, 0, 43402, 3000, 0x00)
    ChrMoveTo(0x0018, 54168, 0, 43002, 3000, 0x00)
    OP_62(0x0018, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x03)
    ChrMoveTo(0x0018, 52772, 0, 43302, 3000, 0x00)
    ChrMoveTo(0x0018, 51123, 0, 43680, 2000, 0x00)
    TerminateThread(0x0019, 0xFF)

    ChrTalk(
        0x0018,
        (
            '#0270011199V#145F#4P哈啊……呼呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270011200V#145F可、可恶……\n',
            '难道香烟也要少抽了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011201V#000F你们两位，在干什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrPos(0x0101, 50434, 0, 54609, 270)
    SetChrPos(0x0102, 48721, 0, 55602, 270)
    SetChrPos(0x0103, 51196, 0, 55910, 270)
    CreateThread(0x0101, 0x01, 0x00, 0x0016)
    CreateThread(0x0102, 0x01, 0x00, 0x0017)
    CreateThread(0x0103, 0x01, 0x00, 0x0018)
    CameraMove(51050, 0, 45160, 1000)
    ChrTurnDirection(0x0018, 0x0101, 400)
    ChrTurnDirection(0x0019, 0x0101, 400)
    Sleep(2000)

    ChrTalk(
        0x0018,
        (
            '#0270011202V#140F#4P哦哦，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270011203V#140F其实啊， \n',
            '我们现在正赶去柏斯啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011204V#010F可是，\n',
            '定期船好像还没有来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0270011205V#141F#4P啊，我知道。\n',
            '所以才打算从大道走过去啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270011206V#141F虽然要花不少时间，\n',
            '不过也不至于远到不能走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011207V#501F那真是辛苦你们了。\n',
            '难道发现了独家新闻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0270011208V#147F#4P没错，是非常棒的题材。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270011209V#144F不能再磨蹭了！\n',
            '今天之内必须要赶到柏斯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0018, 0x01, 0x00, 0x0019)
    ChrTurnDirection(0x0019, 0x0018, 0)
    OP_62(0x0018, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0018, 39307, 0, 40900, 6000, 0x00)
    TerminateThread(0x0018, 0xFF)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0018, 0x0008)

    ChrTalk(
        0x0019,
        (
            '#0280011210V#154F#4P前辈，真的不要紧吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0019, 0x0101, 400)
    ChrTurnDirection(0x0101, 0x0019, 400)
    ChrTurnDirection(0x0102, 0x0019, 400)
    ChrTurnDirection(0x0103, 0x0019, 400)

    ChrTalk(
        0x0019,
        (
            '#0280011211V#151F啊，那么再见了～！\n',
            '小艾，小约。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0019, 0x01, 0x00, 0x0019)
    OP_62(0x0019, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0019, 39307, 0, 40900, 6000, 0x00)
    TerminateThread(0x0019, 0xFF)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x0019, 0x0008)

    ChrTalk(
        0x0103,
        (
            '#0030011212V#020F真是活泼的组合呢。\n',
            '你们认识那两个人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011213V#000F就是那两个杂志的记者啊。\n',
            '之前我们还带他们去塔那边取材。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011214V#000F是不是发生了什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x52EE
@scena.Code('func_16_52EE')
def func_16_52EE():
    OP_92(0x0101, 0x0019, 2000, 3000, 0x00)

    Return()

# id: 0x0017 offset: 0x52FD
@scena.Code('func_17_52FD')
def func_17_52FD():
    OP_92(0x0102, 0x0019, 3000, 3000, 0x00)

    Return()

# id: 0x0018 offset: 0x530C
@scena.Code('func_18_530C')
def func_18_530C():
    OP_92(0x0103, 0x0019, 3500, 3000, 0x00)

    Return()

# id: 0x0019 offset: 0x531B
@scena.Code('func_19_531B')
def func_19_531B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5344',
    )

    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    ChrTurnDirection(0x0002, 0x00FE, 0)
    ChrTurnDirection(0x0019, 0x00FE, 0)
    Yield()

    Jump('func_19_531B')

    def _loc_5344(): pass

    label('loc_5344')

    Return()

# id: 0x001A offset: 0x5345
@scena.Code('func_1A_5345')
def func_1A_5345():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001A, 0x0008)
    SetChrPos(0x001A, 72905, 0, 18979, 90)
    SetChrPos(0x0102, 74801, 0, 19516, 225)
    SetChrPos(0x0101, 74801, 0, 18064, 315)
    OP_6F(0x002C, 30)
    CameraMove(74132, 0, 18793, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_28(0x000A, 0x04, 0x10)
    OP_28(0x000A, 0x01, 0x0004)

    ChrTalk(
        0x001A,
        (
            '#0030000605V#020F两人都辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000606V#020F那么按照规矩，\n',
            '我还是要确认一下搜索对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了２个',
            (TxtCtl.SetColor, 0x2),
            '小箱子',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(0x0373, 2)

    ChrTalk(
        0x001A,
        (
            '#0030000607V#020F……嗯，是真品。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000608V而且也没有打开过的痕迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000609V#007F（好、好险呢～～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000610V#015F（果然……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0030000611V#021F恭喜你们两人，\n',
            '实地研修考试合格了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000612V#502F哼哼，这种考试太轻松了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000613V#000F……对了，雪拉姐。\n',
            '那小箱子里面放的是什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0030000614V#020F这个暂时保密。\n',
            '等一下回到协会你们就知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000615V#020F好了，\n',
            '闲话就到此为止。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000616V#020F其实考试通过\n',
            '并不代表研修就这样结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000617V#004F咦，什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000618V#004F可是我们的考试不是都合格了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0030000619V#020F最后一样要做的\n',
            '就是关于你们的研修报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000620V#020F我知道你们已经很累了，\n',
            '不过现在要先回协会才行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000621V#505F呼，还要继续啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000622V#505F不过也没办法。\n',
            '才刚刚踏上游击士之路，不努力不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000623V#010F是啊。\n',
            '已经到这步了，再忍耐一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    NewScene('ED6_DT01/T0121._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x001B offset: 0x5776
@scena.Code('func_1B_5776')
def func_1B_5776():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001A, 0x0008)
    SetChrPos(0x001A, 72905, 0, 18979, 90)
    SetChrPos(0x0102, 74801, 0, 19516, 225)
    SetChrPos(0x0101, 74801, 0, 18064, 315)
    OP_6F(0x002C, 30)
    CameraMove(74132, 0, 18793, 0)
    OP_0D()
    OP_28(0x000A, 0x04, 0x04)
    OP_28(0x000A, 0x04, 0x08)
    OP_28(0x000A, 0x01, 0x0001)

    ChrTalk(
        0x001A,
        (
            '#0030000500V#020F终于到了研修最后也是最重要的一关了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000501V#020F现在就要开始进行你们两人的认定考试。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000502V#020F希望你们能把\n',
            '到目前为止学到的知识都发挥出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000503V#010F嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000504V#004F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 90, 400)
    Sleep(200)

    SetChrDirection(0x0101, 315, 400)
    Sleep(500)

    OP_62(0x0102, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020000505V#010F艾丝蒂尔，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000506V#505F……我说雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0030000507V#020F什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000508V#505F……难道，\n',
            '你说的考试不是笔试吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0030000509V#023F哈啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000510V艾丝蒂尔，\n',
            '你刚才不是看了公告板吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000511V#505F嗯，看是看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0030000512V#020F你还在手册上做了记录，\n',
            '难道又不记得了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000513V#020F公告板上不是写着搜索地下水路吗。\n',
            '那就是研修的最终考试哦。\n',
            '  ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000514V#004F………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000515V#007F哈啊～太好了～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 225, 400)
    PlaySE(137, 0x00, 0x64)
    OP_62(0x0101, 0x0000012C, 1600, 0x36, 0x39, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010000516V#001F啊啊，空之女神大人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000517V衷心感谢您为我们\n',
            '创造了地下水路这种东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000518V#018F难道……\n',
            '你一直以为那是笔试吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000519V所以刚才在工房一直闹着不肯走……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010000520V#502F呼，真怀念……现在想起来，\n',
            '研修还真是一段美好的回忆呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000521V#017F唉。\n',
            '我们真的能够毕业吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000522V#509F什么嘛～这样说算什么意思啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5C4D')
    def lambda_5C4D():
        ChrTurnDirection(0x00FE, 0x001A, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5C4D)

    @scena.Lambda('lambda_5C5B')
    def lambda_5C5B():
        ChrTurnDirection(0x00FE, 0x001A, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_5C5B)

    ChrTalk(
        0x001A,
        (
            '#0030000523V#022F好了好了，\n',
            '两人的闲聊到此为止。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000524V#022F都已经快考试了，\n',
            '至少也应该有点紧张感吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000525V#022F如果考试不合格，\n',
            '可就要接受严酷的补习哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000526V#001F嘿嘿，没问题啦㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000527V#001F好了，赶快开始考试吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0030000528V#026F嗯，这么有自信的话，\n',
            '就用结果来证明给我看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000529V#020F……回到正题。正如公告板写的那样，\n',
            '考试的题目是搜索地下水路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000530V#020F搜索对象是位于某处的宝箱，\n',
            '搜索目的是把藏在宝箱内的东西回收。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000531V#020F地下水路的构造很简单，\n',
            '所以你们不用担心会迷路……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000532V#020F但是里面到处都有真正的魔兽，\n',
            '大意的话可会吃苦头的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000533V#020F要是遭遇到危险的话，就用这个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了３个',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了 ',
            (TxtCtl.SetColor, 0x2),
            '魔兽手册',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    AddItem(0x01F5, 3)
    AddItem(0x020F, 1)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010000534V#505F嗯？这本手册是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0030000535V#020F这是魔兽手册，用来记录战斗过的\n',
            '对手的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000536V#020F一旦掌握了敌人的特点，就要马上\n',
            '记录到这本手册中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000537V#010F原来如此……\n',
            '知己知彼，才能百战百胜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000538V就是这个意思吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0030000539V#021F呵呵，正是。\n',
            '你懂得很多嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000540V#501F嘿，看来是件好东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000541V#001F谢啦，雪拉姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000542V#010F我们会充分利用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000543V#006F好～的！ \n',
            '约修亚，一鼓作气向前冲吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020000544V#010F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000545V#010F就把这当作实战，\n',
            '小心谨慎地行动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    NewScene('ED6_DT01/C0500._SN', 0, 0, 0)
    IdleLoop()
    SetMapFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x001C offset: 0x616A
@scena.Code('func_1C_616A')
def func_1C_616A():
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x0017, 0xFF)
    SetChrPos(0x0102, 29410, 0, 68310, 0)
    SetChrPos(0x0101, 30510, 0, 69400, 0)
    SetChrPos(0x0019, 31602, 0, 67448, 0)
    SetChrPos(0x0018, 32375, 0, 68461, 0)
    SetChrPos(0x0017, 33719, 0, 67665, 0)
    EventBegin(0x00)
    SetMapFlags(0x00400000)
    CameraMove(31270, 0, 68330, 0)
    CameraSetDistance(3000, 0)
    OP_6C(270000, 0)
    SetChrFlags(0x0019, 0x0040)
    SetChrFlags(0x0018, 0x0040)
    SetChrFlags(0x0017, 0x0040)
    ChrTurnDirection(0x0101, 0x0017, 0)
    ChrTurnDirection(0x0102, 0x0017, 0)
    ChrTurnDirection(0x0019, 0x0017, 0)
    ChrTurnDirection(0x0018, 0x0017, 0)
    ChrTurnDirection(0x0017, 0x0101, 0)
    SetScenaFlags(ScenaFlag(0x004B, 1, 0x259))
    OP_28(0x0019, 0x04, 0x10)
    OP_28(0x0019, 0x01, 0x0100)
    OP_28(0x0019, 0x01, 0x0200)
    OP_28(0x0005, 0x04, 0x40)
    OP_28(0x0009, 0x04, 0x40)

    If(
        (
            (Expr.PushValueByIndex, 0x17),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_6259',
    )

    def _loc_6259(): pass

    label('loc_6259')

    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0017,
        (
            '#0150010851V#130F——呀，回到城镇真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010852V#130F我还是第一次这么平安地从遗迹回来啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010853V#130F艾丝蒂尔、约修亚。\n',
            '该怎么感谢你们好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010854V#010F哪里，这是我们游击士应尽的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010855V#000F所以我就说嘛，\n',
            '下次调查的时候就请个游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0150010856V#130F哈哈，我要和钱包商量一下再说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150010857V#130F那么各位，我先告辞了……\n',
            '说不定以后还会有机会再见哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0017, 0x01, 0x00, 0x001E)
    SetChrDirection(0x0017, 90, 400)
    ChrWalkTo(0x0017, 43668, 0, 66724, 3000, 0x00)
    TerminateThread(0x0017, 0xFF)
    ChrTurnDirection(0x0101, 0x0019, 400)
    ChrTurnDirection(0x0102, 0x0018, 400)
    ChrTurnDirection(0x0019, 0x0101, 400)
    ChrTurnDirection(0x0018, 0x0101, 400)

    ChrTalk(
        0x0018,
        (
            '#0270010858V#141F那么……\n',
            '我们也就此告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010859V#141F一开始还不太放心，\n',
            '不过你们确实干得很不错啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010860V#147F总之谢谢你们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010861V#502F哼哼，这就是实力哦☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0270010862V#142F丫头，不要搞错了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010863V#142F和我认识的游击士比起来，\n',
            '你们还是乳臭未干的小鬼呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010864V#142F还需要不断努力才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010865V#007F唔……我会铭记在心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010866V#010F对了，\n',
            '你们两位这就打算回杂志社去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0270010867V#141F不，\n',
            '我想今天先呆在洛连特休息一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010868V#141F因为还得起稿写新闻嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0280010869V#151F而我就要去工房那儿\n',
            '把今天的照片冲洗出来～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010870V#151F那么，再见哦～！\n',
            '小艾，小约。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0019, 0x01, 0x00, 0x001D)
    CreateThread(0x0018, 0x01, 0x00, 0x001E)
    SetChrDirection(0x0018, 90, 400)
    ChrWalkTo(0x0018, 43668, 0, 66724, 3000, 0x00)
    TerminateThread(0x0018, 0xFF)

    ExecExpressionWithValue(
        0x001B,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001B,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001B,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x001B, 1000)
    ChrTurnDirection(0x0101, 0x0102, 400)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010871V#000F这下代替老爸去做的工作都完成了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010872V#000F嘿嘿～\n',
            '比想象中还要顺利呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010873V#010F嗯，对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010874V#010F而且，\n',
            '原来游击士的本职不只局限于战斗，\n',
            '现在我总算明白这道理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010875V#001F你又在装酷了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010876V#006F不过呢，嗯……\n',
            '我好像也有点明白了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010877V#019F前面还有很长的路要走啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010878V#019F总之，先回协会报告吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010879V#006F嗯，好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010880V#004F啊，你现在感觉怎么样？\n',
            '还会感到不舒服吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010881V#010F啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010882V好像已经完全好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    ClearMapFlags(0x00400000)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x0019, 0x0008)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0018, 0x0008)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0017, 0x0008)

    Return()

# id: 0x001D offset: 0x6912
@scena.Code('func_1D_6912')
def func_1D_6912():
    Sleep(500)

    SetChrDirection(0x0019, 90, 400)
    ChrWalkTo(0x0019, 43668, 0, 66724, 3000, 0x00)

    Return()

# id: 0x001E offset: 0x6933
@scena.Code('func_1E_6933')
def func_1E_6933():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_695C',
    )

    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    ChrTurnDirection(0x0019, 0x00FE, 0)
    ChrTurnDirection(0x0018, 0x00FE, 0)
    Yield()

    Jump('func_1E_6933')

    def _loc_695C(): pass

    label('loc_695C')

    Return()

# id: 0x001F offset: 0x695D
@scena.Code('func_1F_695D')
def func_1F_695D():
    CameraSetDistance(2800, 1300)

    Return()

# id: 0x0020 offset: 0x6967
@scena.Code('func_20_6967')
def func_20_6967():
    OP_6C(270000, 1300)

    Return()

# id: 0x0021 offset: 0x6971
@scena.Code('func_21_6971')
def func_21_6971():
    EventBegin(0x00)
    CreateThread(0x0101, 0x00, 0x00, 0x0022)
    CreateThread(0x0102, 0x00, 0x00, 0x0023)
    CreateThread(0x0000, 0x01, 0x00, 0x0024)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_12(0x00009470, 0x00030D40, 0x00000000)
    CameraMove(50063, 0, 24460, 8000)
    OP_A5(0x0000)
    OP_A5(0x0001)
    OP_A5(0x0002)
    Fade(1000)
    CameraMove(48500, 0, 16400, 0)
    CameraSetDistance(3000, 0)
    OP_6C(0, 0)
    OP_6E(261, 0)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020000232V#010F时间刚刚好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000233V既不是太早，又没有迟到。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_12(0x00009470, 0x000186A0, 0x00001F40)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010000234V#007F呜～\n',
            '明明刚从教会的主日学校毕业……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000235V为了当游击士，\n',
            '又要这么辛苦地学习，\n',
            '真是连做梦也没想到呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020000236V#010F今天不是到最后了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000237V为了自己憧憬的理想，\n',
            '付出这点辛苦也是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000238V#505F这样说也对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000239V#006F………好吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000240V既然到了最后关头，\n',
            '就鼓起干劲接受雪拉姐严格的训练吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000241V#019F好像已经干劲十足了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000242V那我们赶快到那边的游击士协会去吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    SetScenaFlags(ScenaFlag(0x0040, 3, 0x203))
    ClearMapFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0022 offset: 0x6C20
@scena.Code('func_22_6C20')
def func_22_6C20():
    OP_A6(0x0000)
    Sleep(5000)

    ChrWalkTo(0x00FE, 48300, 0, 15400, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0023 offset: 0x6C40
@scena.Code('func_23_6C40')
def func_23_6C40():
    OP_A6(0x0001)
    Sleep(5000)

    ChrWalkTo(0x00FE, 49500, 0, 15200, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0024 offset: 0x6C60
@scena.Code('func_24_6C60')
def func_24_6C60():
    OP_A6(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x0025 offset: 0x6C67
@scena.Code('func_25_6C67')
def func_25_6C67():
    EventBegin(0x00)
    CreateThread(0x0101, 0x00, 0x00, 0x0026)
    CreateThread(0x0102, 0x00, 0x00, 0x0027)
    CreateThread(0x0009, 0x00, 0x00, 0x0028)
    CreateThread(0x000A, 0x00, 0x00, 0x0029)
    CreateThread(0x0000, 0x01, 0x00, 0x002A)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_A5(0x0003)

    ChrTalk(
        0x0009,
        (
            '#0850000734V喂～快点过来啦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    Sleep(1500)

    ChrTalk(
        0x000A,
        (
            '#0860000735V等、等一下嘛～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A5(0x0004)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    CameraMove(49690, 0, 23330, 2500)
    OP_A5(0x0000)
    OP_A5(0x0001)
    OP_A5(0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010000736V#501F啊，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_A5(0x0003)
    SetChrName('鲁克')

    ChrTalk(
        0x0009,
        (
            '#0850000737V哎哎，艾丝蒂尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrName('帕特')

    ChrTalk(
        0x000A,
        (
            '#0860000738V啊，约修亚哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0101,
        (
            '#0010000739V#007F真没礼貌～\n',
            '那个『哎哎』是什么意思啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000740V#006F看你们急急忙忙的样子，\n',
            '要去哪里玩啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000741V#006F小孩子不要随处乱跑呢～\n',
            '外面的街道有很多魔兽在游荡哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0850000742V哼，真啰嗦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0850000743V男人要干大事，\n',
            '女人管那么多干嘛啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0850000744V又不是游击士，拽什么呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000745V#006F啧啧啧……\n',
            '太嫩了！　嫩得不得了呢，鲁克！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000746V#006F你简直比帕赛尔农场的蔬菜还要鲜嫩！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0850000747V咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0850000748V难、难道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000749V#502F嘿嘿，就在刚才，\n',
            '我已经得到游击士的资格啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000750V#502F现在的我可是如假包换的正牌游·击·士哦☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000751V#019F现在还不过是见习阶段，\n',
            '用不着在小孩子面前摆架子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000752V#509F喂，别给我泼冷水嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0860000753V哇，太羡慕了！\n',
            '姐姐，你们真的好了不起哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x000A, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000754V#001F呵呵，帕特真是个懂事的好孩子～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000755V和你那个又狂妄又任性的\n',
            '臭小子哥哥完全不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0850000756V什、什么呀……\n',
            '本来应该是我先当上游击士才对的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0850000757V约修亚哥哥倒也罢了，\n',
            '居然被艾丝蒂尔之类的抢先一步……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0009, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000758V#005F什么呀！\n',
            '那个『之类的』是什么意思！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000759V#005F首先，\n',
            '没到１６岁是不能成为游击士的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000760V#005F还在教会的主日学校学习的小孩就更不行了！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000761V#018F又这么孩子气了。\n',
            '怎么老是和小孩子认真计较……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0850000762V可恶～你给我记着！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0850000763V在秘密基地进行特训之后，\n',
            '很快我也能成为游击士的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000A, 500)

    ChrTalk(
        0x0009,
        (
            '#0850000764V帕特，我们走！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0009, 500)

    ChrTalk(
        0x000A,
        (
            '#0860000765V啊～嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0001, 0)

    ChrTalk(
        0x000A,
        (
            '#0860000766V哥哥姐姐，再见了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    @scena.Lambda('lambda_7331')
    def lambda_7331():
        CameraMove(49470, 0, 24950, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7331)

    @scena.Lambda('lambda_7349')
    def lambda_7349():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_7349)

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_A5(0x0000)
    OP_A5(0x0001)
    OP_A5(0x0003)
    OP_A5(0x0004)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0009, 0x0008)
    SetChrFlags(0x000A, 0x0008)

    ChrTalk(
        0x0101,
        (
            '#0010000767V#007F真是的，鲁克那小子……\n',
            '总是劈头就顶撞我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000768V#007F会不会是因为讨厌我啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020000769V#011F不，我觉得恰恰相反。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000770V#004F恰恰相反？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000771V#019F呵呵，因为是男孩子嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#0020000772V#013F话说回来，\n',
            '鲁克说的那个秘密基地……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000773V#001F嗯，\n',
            '是不是引起了共鸣呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000774V#001F约修亚小时候的纯真心灵被触动了吧……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0102,
        (
            '#0020000775V#018F什么呀。\n',
            '我想说的不是这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    SetScenaFlags(ScenaFlag(0x0040, 6, 0x206))
    EventEnd(0x00)

    Return()

# id: 0x0026 offset: 0x7583
@scena.Code('func_26_7583')
def func_26_7583():
    OP_A6(0x0000)
    ChrWalkTo(0x00FE, 51350, 0, 27630, 3000, 0x00)
    ChrWalkTo(0x00FE, 49650, 0, 24540, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0009, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    def _loc_75D2(): pass

    label('loc_75D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_75E4',
    )

    ChrTurnDirection(0x00FE, 0x0009, 0)
    Yield()

    Jump('loc_75D2')

    def _loc_75E4(): pass

    label('loc_75E4')

    Return()

# id: 0x0027 offset: 0x75E5
@scena.Code('func_27_75E5')
def func_27_75E5():
    OP_A6(0x0001)
    Sleep(1000)

    ChrWalkTo(0x00FE, 51350, 0, 27630, 3000, 0x00)
    ChrWalkTo(0x00FE, 50960, 0, 25150, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0009, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    def _loc_7622(): pass

    label('loc_7622')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7634',
    )

    ChrTurnDirection(0x00FE, 0x0009, 0)
    Yield()

    Jump('loc_7622')

    def _loc_7634(): pass

    label('loc_7634')

    Return()

# id: 0x0028 offset: 0x7635
@scena.Code('func_28_7635')
def func_28_7635():
    OP_A6(0x0003)
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 52200, 0, 14240, 5000, 0x00)
    ChrWalkTo(0x00FE, 50100, 0, 15710, 5000, 0x00)
    ChrWalkTo(0x00FE, 48940, 0, 22440, 5000, 0x00)
    SetChrDirection(0x00FE, 160, 400)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 1000, 8000)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 1000, 8000)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_A6(0x0003)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 2000, 8000)
    SetChrDirection(0x00FE, 0, 800)
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -500, 6000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_A6(0x0003)
    ChrWalkTo(0x00FE, 48500, 0, 24720, 7000, 0x00)
    ChrWalkTo(0x00FE, 48500, 0, 37720, 7000, 0x00)
    SetChrFlags(0x00FE, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x0029 offset: 0x771D
@scena.Code('func_29_771D')
def func_29_771D():
    OP_A6(0x0004)
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 52200, 0, 14240, 5000, 0x00)
    ChrWalkTo(0x00FE, 50100, 0, 15710, 5000, 0x00)
    ChrWalkTo(0x00FE, 49900, 0, 18470, 5000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_A6(0x0004)
    OP_6C(12000, 2500)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_A6(0x0004)
    ChrWalkTo(0x00FE, 49800, 0, 21520, 5000, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_A6(0x0004)
    Sleep(500)

    ChrWalkTo(0x00FE, 48500, 0, 24720, 7000, 0x00)
    ChrWalkTo(0x00FE, 48500, 0, 37720, 7000, 0x00)
    SetChrFlags(0x00FE, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

# id: 0x002A offset: 0x77D3
@scena.Code('func_2A_77D3')
def func_2A_77D3():
    OP_A6(0x0002)
    CameraMove(49800, 0, 19520, 3000)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x002B offset: 0x77EB
@scena.Code('func_2B_77EB')
def func_2B_77EB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 4, 0x264)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_77FE',
    )

    Call(0, 0x0036)

    Jump('loc_787E')

    def _loc_77FE(): pass

    label('loc_77FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_7808',
    )

    Jump('loc_787E')

    def _loc_7808(): pass

    label('loc_7808')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_781B',
    )

    Call(0, 0x0035)

    Jump('loc_787E')

    def _loc_781B(): pass

    label('loc_781B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_782E',
    )

    Call(0, 0x0034)

    Jump('loc_787E')

    def _loc_782E(): pass

    label('loc_782E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 4, 0x22C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_783C',
    )

    Jump('loc_787E')

    def _loc_783C(): pass

    label('loc_783C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_784A',
    )

    Call(0, 0x0033)

    Jump('loc_787E')

    def _loc_784A(): pass

    label('loc_784A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_7854',
    )

    Jump('loc_787E')

    def _loc_7854(): pass

    label('loc_7854')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 4, 0x20C)),
            Expr.Return,
        ),
        'loc_7862',
    )

    Call(0, 0x0032)

    Jump('loc_787E')

    def _loc_7862(): pass

    label('loc_7862')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 7, 0x207)),
            Expr.Return,
        ),
        'loc_7870',
    )

    Call(0, 0x002C)

    Jump('loc_787E')

    def _loc_7870(): pass

    label('loc_7870')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_787E',
    )

    Call(0, 0x0031)

    Jump('loc_787E')

    def _loc_787E(): pass

    label('loc_787E')

    Return()

# id: 0x002C offset: 0x787F
@scena.Code('func_2C_787F')
def func_2C_787F():
    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 51370, 0, 29175, 180)
    CreateThread(0x0101, 0x00, 0x00, 0x002D)
    CreateThread(0x0102, 0x00, 0x00, 0x002E)
    CreateThread(0x0008, 0x00, 0x00, 0x002F)
    CreateThread(0x0000, 0x01, 0x00, 0x0030)

    ChrTalk(
        0x0008,
        (
            '#0350000888V艾丝蒂尔、约修亚！\n',
            '还好找到你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    Fade(1000)
    SetChrPos(0x0101, 49700, 0, 15020, 315)
    SetChrPos(0x0102, 48380, 0, 15120, 0)
    SetChrPos(0x0008, 49950, 0, 25270, 180)
    CameraSetDistance(3000, 0)
    CameraMove(50250, 0, 16110, 0)
    OP_6C(156000, 0)
    OP_67(0, 7000, -10000, 0)
    OP_0D()
    ChrWalkTo(0x0008, 49200, 0, 19490, 5000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010000889V#004F哎呀，爱娜姐姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000890V#014F发生什么事了？\n',
            '这么着急的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350000891V#742F事情有点麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000892V我想问你们，\n',
            '今天卡西乌斯先生在家吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000893V#002F嗯，在啊。\n',
            '他说要在家整理书本的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000894V#002F嗯……发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350000895V#742F鲁克和帕特，你们认识吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000896V#002F当然了。\n',
            '刚才还见到他们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000897V#012F他们怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350000898V#742F其实……\n',
            '是尤妮告诉我的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000899V那两个孩子\n',
            '往北面郊外的『翡翠之塔』去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010000900V#004F『翡翠之塔』！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000901V#004F我记得那里好像已经变成魔兽的栖息地了呀！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350000902V#742F嗯，很有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000903V雪拉扎德还没回来，\n',
            '所以现在只能拜托卡西乌斯先生去保护他们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000904V#005F你在说什么呀，爱娜姐姐！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000905V#005F如果现在不赶快去追就麻烦啦！\n',
            '让我们去把他们带回来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350000906V#745F可是你们才刚刚成为游击士……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000907V#012F爱娜小姐，\n',
            '我觉得这次艾丝蒂尔说得对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000908V#012F现在赶去的话，\n',
            '说不定在他们到达塔之前就能追上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350000909V#744F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000910V#742F好吧，有什么责任由我来承担。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000911V这是游击士协会的紧急委托。\n',
            '一定要尽快确保孩子们的安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000912V#006F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000913V#012F知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350000914V#742F翡翠之塔就在通往玛鲁加山道途中\n',
            '往西拐的那个方向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000915V玛鲁加山道从城镇的北边出去就是了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000916V我在协会待命，\n',
            '如果有什么问题务必与我联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrWalkTo(0x0008, 49950, 0, 25270, 5000, 0x00)
    SetChrFlags(0x0008, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010000917V#002F这么快就接到第一份任务了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 0)

    ChrTalk(
        0x0101,
        (
            '#0010000918V#005F约修亚，我们快走！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020000919V#012F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    Fade(1000)
    SetChrPos(0x0101, 48920, 0, 15320, 0)
    SetChrPos(0x0102, 48920, 0, 15320, 0)
    OP_6C(0, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    SetScenaFlags(ScenaFlag(0x0041, 4, 0x20C))
    OP_28(0x0001, 0x01, 0x0001)
    OP_28(0x0001, 0x01, 0x0002)
    OP_28(0x0001, 0x04, 0x04)
    EventEnd(0x00)

    Return()

# id: 0x002D offset: 0x7F85
@scena.Code('func_2D_7F85')
def func_2D_7F85():
    OP_A6(0x0000)
    def _loc_7F88(): pass

    label('loc_7F88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7F9A',
    )

    ChrTurnDirection(0x00FE, 0x0008, 0)
    Yield()

    Jump('loc_7F88')

    def _loc_7F9A(): pass

    label('loc_7F9A')

    OP_A6(0x0000)
    def _loc_7F9D(): pass

    label('loc_7F9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7FAF',
    )

    ChrTurnDirection(0x00FE, 0x0008, 0)
    Yield()

    Jump('loc_7F9D')

    def _loc_7FAF(): pass

    label('loc_7FAF')

    OP_A6(0x0000)
    OP_92(0x00FE, 0x0000, 0, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x002E offset: 0x7FC4
@scena.Code('func_2E_7FC4')
def func_2E_7FC4():
    OP_A6(0x0001)
    def _loc_7FC7(): pass

    label('loc_7FC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7FD9',
    )

    ChrTurnDirection(0x00FE, 0x0008, 0)
    Yield()

    Jump('loc_7FC7')

    def _loc_7FD9(): pass

    label('loc_7FD9')

    OP_A6(0x0001)
    def _loc_7FDC(): pass

    label('loc_7FDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7FEE',
    )

    ChrTurnDirection(0x00FE, 0x0008, 0)
    Yield()

    Jump('loc_7FDC')

    def _loc_7FEE(): pass

    label('loc_7FEE')

    OP_A6(0x0001)
    OP_92(0x00FE, 0x0000, 0, 3000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x002F offset: 0x8003
@scena.Code('func_2F_8003')
def func_2F_8003():
    OP_A6(0x0005)
    ChrWalkTo(0x00FE, 49910, 0, 18690, 5000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    OP_A6(0x0005)
    ChrWalkTo(0x00FE, 51370, 0, 29175, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Return()

# id: 0x0030 offset: 0x8050
@scena.Code('func_30_8050')
def func_30_8050():
    OP_A6(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x0031 offset: 0x8057
@scena.Code('func_31_8057')
def func_31_8057():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020000776V#014F艾丝蒂尔，好像忘了一件事哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000777V今天早上老爸不是吩咐过\n',
            '我们到杂货铺买杂志的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000778V#008F啊，差点给忘了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0032 offset: 0x810D
@scena.Code('func_32_810D')
def func_32_810D():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020010067V#012F玛鲁加山道在城镇北面出口的方向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010068V#012F顺带说说，北面出口就是\n',
            '飞艇坪隔壁那个不起眼的小出口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010010069V#002F我、我知道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0033 offset: 0x81CE
@scena.Code('func_33_81CE')
def func_33_81CE():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020001313V#010F艾丝蒂尔，我们先到协会那里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001314V#010F先向爱娜小姐打听一下\n',
            '我们可以做些什么工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010001315V#000F嗯，说得对呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0034 offset: 0x8283
@scena.Code('func_34_8283')
def func_34_8283():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020010518V#010F可以不去工房吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010519V我们不是要去接杂志社的摄影师吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010010520V#000F啊，对啊。\n',
            '说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0035 offset: 0x8324
@scena.Code('func_35_8324')
def func_35_8324():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020000923V#015F要去『翡翠之塔』的话，\n',
            '要从城镇的北面出口走才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000924V#000F啊，没错呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000925V从飞艇坪旁边那个\n',
            '很小的出口出城就行了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0036 offset: 0x83E5
@scena.Code('func_36_83E5')
def func_36_83E5():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 2, 0x262)),
            Expr.Return,
        ),
        'loc_84CD',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_846F',
    )

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011149V#022F哎呀，我说你们想去哪儿？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011150V还是快点去飞艇坪那里吧。\n',
            '说不定现在还来得及呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84CA')

    def _loc_846F(): pass

    label('loc_846F')

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011151V#022F现在不是出城的时候，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011152V总之我们还是先到飞艇坪那里看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_84CA(): pass

    label('loc_84CA')

    Jump('loc_85AD')

    def _loc_84CD(): pass

    label('loc_84CD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_8548',
    )

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011133V#022F我说你们究竟想去哪啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011134V总之我们还是先去旅馆那里确认一下情况吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_85AD')

    def _loc_8548(): pass

    label('loc_8548')

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011135V#022F现在不是出城的时候，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011136V总之我们还是先去旅馆那里确认一下情况再说吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_85AD(): pass

    label('loc_85AD')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0037 offset: 0x85C9
@scena.Code('func_37_85C9')
def func_37_85C9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 4, 0x264)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_85DC',
    )

    Call(0, 0x003F)

    Jump('loc_8664')

    def _loc_85DC(): pass

    label('loc_85DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_85E6',
    )

    Jump('loc_8664')

    def _loc_85E6(): pass

    label('loc_85E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_85F9',
    )

    Call(0, 0x003E)

    Jump('loc_8664')

    def _loc_85F9(): pass

    label('loc_85F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_860C',
    )

    Call(0, 0x003D)

    Jump('loc_8664')

    def _loc_860C(): pass

    label('loc_860C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 4, 0x22C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_861A',
    )

    Jump('loc_8664')

    def _loc_861A(): pass

    label('loc_861A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_8628',
    )

    Call(0, 0x0038)

    Jump('loc_8664')

    def _loc_8628(): pass

    label('loc_8628')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_8636',
    )

    Call(0, 0x0038)

    Jump('loc_8664')

    def _loc_8636(): pass

    label('loc_8636')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 4, 0x20C)),
            Expr.Return,
        ),
        'loc_8644',
    )

    Call(0, 0x0038)

    Jump('loc_8664')

    def _loc_8644(): pass

    label('loc_8644')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 7, 0x207)),
            Expr.Return,
        ),
        'loc_8652',
    )

    Call(0, 0x0038)

    Jump('loc_8664')

    def _loc_8652(): pass

    label('loc_8652')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_8660',
    )

    Call(0, 0x0038)

    Jump('loc_8664')

    def _loc_8660(): pass

    label('loc_8660')

    Call(0, 0x0038)

    def _loc_8664(): pass

    label('loc_8664')

    Return()

# id: 0x0038 offset: 0x8665
@scena.Code('func_38_8665')
def func_38_8665():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_8708',
    )

    ChrTalk(
        0x0102,
        (
            '#0020001319V#010F艾丝蒂尔，我们先到协会那里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001320V#010F先向爱娜小姐打听一下\n',
            '我们可以做些什么工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010001321V#000F嗯，说得对呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8952')

    def _loc_8708(): pass

    label('loc_8708')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_878A',
    )

    ChrTalk(
        0x0102,
        (
            '#0020001065V#010F已经傍晚了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001066V#010F父亲还在等我们呢，\n',
            '我们还是早点回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001067V#000F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8952')

    def _loc_878A(): pass

    label('loc_878A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 4, 0x20C)),
            Expr.Return,
        ),
        'loc_8830',
    )

    ChrTalk(
        0x0102,
        (
            '#0020010067V#012F玛鲁加山道在城镇北面出口的方向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010068V#012F顺带说说，北面出口就是\n',
            '飞艇坪隔壁那个不起眼的小出口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010069V#002F我、我知道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8952')

    def _loc_8830(): pass

    label('loc_8830')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_88C7',
    )

    ChrTalk(
        0x0102,
        (
            '#0020000885V#010F艾丝蒂尔。\n',
            '总之我们还是先回家吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000886V#010F我们要把成为游击士的事告诉父亲呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000887V#000F嗯，那倒也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8952')

    def _loc_88C7(): pass

    label('loc_88C7')

    ChrTalk(
        0x0102,
        (
            '#0020000243V#010F艾丝蒂尔。\n',
            '很快就要开始研修了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000244V#010F我们还是先到\n',
            '南面的游击士协会再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000245V#007F哎～没办法啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8952(): pass

    label('loc_8952')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0039 offset: 0x896E
@scena.Code('func_39_896E')
def func_39_896E():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020000252V#010F艾丝蒂尔。\n',
            '很快就要开始研修了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000253V#010F我们还是先到\n',
            '南面的游击士协会再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000254V#007F哎～没办法啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0000, 22000, 0, 40000, 0)
    SetChrPos(0x0001, 22000, 0, 40000, 0)
    SetChrPos(0x0002, 22000, 0, 40000, 0)
    SetChrPos(0x0003, 22000, 0, 40000, 0)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    SetMapFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x003A offset: 0x8A66
@scena.Code('func_3A_8A66')
def func_3A_8A66():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020000876V#010F艾丝蒂尔。\n',
            '总之我们还是先回家吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000877V#010F我们要把成为游击士的事告诉父亲呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000878V#000F嗯，那倒也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0000, 22000, 0, 40000, 0)
    SetChrPos(0x0001, 22000, 0, 40000, 0)
    SetChrPos(0x0002, 22000, 0, 40000, 0)
    SetChrPos(0x0003, 22000, 0, 40000, 0)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    SetMapFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x003B offset: 0x8B60
@scena.Code('func_3B_8B60')
def func_3B_8B60():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010067V#012F玛鲁加山道在城镇北面出口的方向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010068V#012F顺带说说，北面出口就是\n',
            '飞艇坪隔壁那个不起眼的小出口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010069V#002F我、我知道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0000, 22000, 0, 40000, 0)
    SetChrPos(0x0001, 22000, 0, 40000, 0)
    SetChrPos(0x0002, 22000, 0, 40000, 0)
    SetChrPos(0x0003, 22000, 0, 40000, 0)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    SetMapFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x003C offset: 0x8C69
@scena.Code('func_3C_8C69')
def func_3C_8C69():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001068V#010F已经傍晚了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001069V#010F父亲还在等我们呢，\n',
            '我们还是早点回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001070V#000F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0000, 22000, 0, 40000, 0)
    SetChrPos(0x0001, 22000, 0, 40000, 0)
    SetChrPos(0x0002, 22000, 0, 40000, 0)
    SetChrPos(0x0003, 22000, 0, 40000, 0)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    SetMapFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x003D offset: 0x8D4E
@scena.Code('func_3D_8D4E')
def func_3D_8D4E():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020010518V#010F可以不去工房吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010519V我们不是要去接杂志社的摄影师吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010010520V#000F啊，对啊。\n',
            '说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x003E offset: 0x8DEF
@scena.Code('func_3E_8DEF')
def func_3E_8DEF():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020000926V#015F要去『翡翠之塔』的话，\n',
            '要从城镇的北面出口走才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000927V#000F啊，没错呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000928V从飞艇坪旁边那个\n',
            '很小的出口出城就行了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x003F offset: 0x8EB0
@scena.Code('func_3F_8EB0')
def func_3F_8EB0():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 2, 0x262)),
            Expr.Return,
        ),
        'loc_8F98',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_8F3A',
    )

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011149V#022F哎呀，我说你们想去哪儿？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011150V还是快点去飞艇坪那里吧。\n',
            '说不定现在还来得及呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8F95')

    def _loc_8F3A(): pass

    label('loc_8F3A')

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011151V#022F现在不是出城的时候，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011152V总之我们还是先到飞艇坪那里看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8F95(): pass

    label('loc_8F95')

    Jump('loc_9074')

    def _loc_8F98(): pass

    label('loc_8F98')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_9013',
    )

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011133V#022F我说你们究竟想去哪啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011134V总之我们还是先去旅馆那里确认一下情况吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9074')

    def _loc_9013(): pass

    label('loc_9013')

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011135V#022F现在不是出城的时候，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011136V总之我们还是先去旅馆那里确认一下情况吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9074(): pass

    label('loc_9074')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0040 offset: 0x9090
@scena.Code('func_40_9090')
def func_40_9090():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 4, 0x264)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_90A3',
    )

    Call(0, 0x0046)

    Jump('loc_9114')

    def _loc_90A3(): pass

    label('loc_90A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_90AD',
    )

    Jump('loc_9114')

    def _loc_90AD(): pass

    label('loc_90AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_90C0',
    )

    Call(0, 0x0045)

    Jump('loc_9114')

    def _loc_90C0(): pass

    label('loc_90C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 4, 0x22C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_90CE',
    )

    Jump('loc_9114')

    def _loc_90CE(): pass

    label('loc_90CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_90DC',
    )

    Call(0, 0x0041)

    Jump('loc_9114')

    def _loc_90DC(): pass

    label('loc_90DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_90EA',
    )

    Call(0, 0x0041)

    Jump('loc_9114')

    def _loc_90EA(): pass

    label('loc_90EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 4, 0x20C)),
            Expr.Return,
        ),
        'loc_90F4',
    )

    Jump('loc_9114')

    def _loc_90F4(): pass

    label('loc_90F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 7, 0x207)),
            Expr.Return,
        ),
        'loc_9102',
    )

    Call(0, 0x0041)

    Jump('loc_9114')

    def _loc_9102(): pass

    label('loc_9102')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_9110',
    )

    Call(0, 0x0041)

    Jump('loc_9114')

    def _loc_9110(): pass

    label('loc_9110')

    Call(0, 0x0041)

    def _loc_9114(): pass

    label('loc_9114')

    Return()

# id: 0x0041 offset: 0x9115
@scena.Code('func_41_9115')
def func_41_9115():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_91B8',
    )

    ChrTalk(
        0x0102,
        (
            '#0020001316V#010F艾丝蒂尔，我们先到协会那里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001317V#010F先向爱娜小姐打听一下\n',
            '我们可以做些什么工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010001318V#000F嗯，说得对呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9353')

    def _loc_91B8(): pass

    label('loc_91B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_923A',
    )

    ChrTalk(
        0x0102,
        (
            '#0020001062V#010F已经傍晚了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001063V#010F父亲还在等我们呢，\n',
            '我们还是早点回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001064V#000F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9353')

    def _loc_923A(): pass

    label('loc_923A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 4, 0x20C)),
            Expr.Return,
        ),
        'loc_9244',
    )

    Jump('loc_9353')

    def _loc_9244(): pass

    label('loc_9244')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_92DB',
    )

    ChrTalk(
        0x0102,
        (
            '#0020000882V#010F艾丝蒂尔。\n',
            '总之我们还是先回家吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000883V#010F我们要把成为游击士的事告诉父亲呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000884V#000F嗯，那倒也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9353')

    def _loc_92DB(): pass

    label('loc_92DB')

    ChrTalk(
        0x0102,
        (
            '#0020000246V#010F艾丝蒂尔。\n',
            '很快就要开始研修了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000247V#010F我们快点去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000248V#007F哎～没办法啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9353(): pass

    label('loc_9353')

    ChrMoveToRelative(0x0000, 0, 0, -1000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0042 offset: 0x936F
@scena.Code('func_42_936F')
def func_42_936F():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020000249V#010F艾丝蒂尔。\n',
            '很快就要开始研修了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000250V#010F我们快点去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000251V#007F哎～没办法啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0000, 32000, 0, 67800, 90)
    SetChrPos(0x0001, 32000, 0, 67800, 90)
    SetChrPos(0x0002, 32000, 0, 67800, 90)
    SetChrPos(0x0003, 32000, 0, 67800, 90)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    SetMapFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x0043 offset: 0x9454
@scena.Code('func_43_9454')
def func_43_9454():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020000879V#010F艾丝蒂尔。\n',
            '总之我们还是先回家吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000880V#010F我们要把成为游击士的事告诉父亲呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000881V#000F嗯，那倒也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0000, 32000, 0, 67800, 90)
    SetChrPos(0x0001, 32000, 0, 67800, 90)
    SetChrPos(0x0002, 32000, 0, 67800, 90)
    SetChrPos(0x0003, 32000, 0, 67800, 90)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    SetMapFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x0044 offset: 0x954E
@scena.Code('func_44_954E')
def func_44_954E():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020000779V#010F艾丝蒂尔，等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000780V#010F我们还没到里农先生那里\n',
            '买《利贝尔通讯》呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000781V#000F啊，忘了忘了。\n',
            '那我们快点去杂货铺吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6C(300000, 0)
    SetChrPos(0x0000, 32000, 0, 67800, 90)
    SetChrPos(0x0001, 32000, 0, 67800, 90)
    SetChrPos(0x0002, 32000, 0, 67800, 90)
    SetChrPos(0x0003, 32000, 0, 67800, 90)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    SetMapFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x0045 offset: 0x9656
@scena.Code('func_45_9656')
def func_45_9656():
    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#0020010518V#010F可以不去工房吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010519V我们不是要去接杂志社的摄影师吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010520V#000F啊，对啊。\n',
            '说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0046 offset: 0x96F0
@scena.Code('func_46_96F0')
def func_46_96F0():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 2, 0x262)),
            Expr.Return,
        ),
        'loc_97D8',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_977A',
    )

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011149V#022F哎呀，我说你们想去哪儿？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011150V还是快点去飞艇坪那里吧。\n',
            '说不定现在还来得及呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_97D5')

    def _loc_977A(): pass

    label('loc_977A')

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011151V#022F现在不是出城的时候，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011152V总之我们还是先到飞艇坪那里看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_97D5(): pass

    label('loc_97D5')

    Jump('loc_98B8')

    def _loc_97D8(): pass

    label('loc_97D8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_9853',
    )

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011133V#022F我说你们究竟想去哪啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011134V总之我们还是先去旅馆那里确认一下情况吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_98B8')

    def _loc_9853(): pass

    label('loc_9853')

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011135V#022F现在不是出城的时候，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011136V总之我们还是先去旅馆那里确认一下情况再说吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_98B8(): pass

    label('loc_98B8')

    ChrMoveToRelative(0x0000, 0, 0, -1000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0047 offset: 0x98D4
@scena.Code('func_47_98D4')
def func_47_98D4():
    EventBegin(0x00)
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    SetChrFlags(0x0020, 0x0080)
    SetChrPos(0x0102, 54640, 0, 43670, 0)
    SetChrPos(0x0101, 55690, 0, 43940, 0)
    CameraMove(55160, 1000, 47020, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(314000, 0)
    OP_6E(261, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_995D')
    def lambda_995D():
        CameraMove(55160, 9000, 47020, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_995D)

    OP_6C(44000, 7000)
    Fade(1000)
    CameraMove(55310, 0, 45740, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    Sleep(1500)

    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１０７５年\n',
            '　由利贝尔王家、七耀教会\n',
            '　以及洛连特市共同建造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１１９２年\n',
            '　百日战役中，被围攻洛连特的\n',
            '　埃雷波尼亚帝国军队炮击而倒塌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１１９７年\n',
            '　在市民的协力下得以重建。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020020127V#010F#3P每次看到这座钟楼，\n',
            '我都会这样想……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020128V在战争中被破坏之后，\n',
            '还能修复到如此程度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020129V洛连特市民的气概真是令人赞叹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020130V#500F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020131V#014F#3P艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020132V#501F#2P……我说，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020133V在雪拉姐来之前，\n',
            '我们上去看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020134V#014F#3P到钟楼上面？\n',
            '我倒是没什么意见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020135V#000F#2P那我们就上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0060, 0, 0x300))
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T0133._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0048 offset: 0x9C61
@scena.Code('func_48_9C61')
def func_48_9C61():
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    SetChrFlags(0x0020, 0x0080)
    FormationAddMember(0x02, 0xFF)
    SetScenaFlags(ScenaFlag(0x0060, 1, 0x301))
    EventBegin(0x00)
    SetMapFlags(0x00000001)
    SetChrPos(0x0102, 51920, 0, 49090, 180)
    SetChrPos(0x0101, 53010, 0, 50110, 270)
    SetChrPos(0x0103, 56060, 0, 43300, 270)
    OP_6C(45000, 0)
    OP_6A(0x0102)
    FadeIn(2000, 0)
    CreateThread(0x0101, 0x00, 0x00, 0x004A)
    ChrWalkTo(0x0102, 51730, 0, 44190, 3000, 0x00)
    ClearMapFlags(0x00000001)
    CreateThread(0x0102, 0x00, 0x00, 0x0049)
    CameraMove(55290, 0, 43570, 1500)
    OP_6A(0x0000)
    ClearMapFlags(0x00000001)

    ChrTalk(
        0x0103,
        (
            '#0030020207V#021F嘿嘿，你们两个。\n',
            '刚才的气氛真不错嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020208V姐姐我啊～\n',
            '都觉得不好意思了呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020020209V#014F#4P哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020210V#014F难、难道刚才在偷看……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020211V#027F什么呀，说得这么难听。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020212V只不过是仰头看时间的时候\n',
            '不小心瞥见了而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020213V#021F啊～要是身上带有\n',
            '导力照相机的话那就更完美了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020214V#018F#4P呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020215V#001F真是的～在说什么呀。\n',
            '不过是单纯的肢体接触而已嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020216V和被喝醉了的雪拉姐抱着\n',
            '是一样的感觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1300)

    ChrTalk(
        0x0102,
        (
            '#0020020217V#017F#4P………呼……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(300)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010020218V#501F嗯？怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020219V#025F唉，你这孩子啊，\n',
            '真是一点也不好玩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020220V#020F算了。\n',
            '你已经和莱娜小姐打了招呼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020221V#000F……嗯。\n',
            '我向她许了愿呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020222V祈愿她守护着老爸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020223V#021F那么，这样就一定没问题的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020224V莱娜小姐的保佑\n',
            '可以和空之女神相媲美呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020225V卡西乌斯老师\n',
            '一定会平安无事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020226V#008F啊哈哈，\n',
            '我觉得这样说好像有点太夸张了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020227V#010F#4P那样说的话，\n',
            '雪拉姐姐曾经见过\n',
            '艾丝蒂尔的母亲是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020228V#020F是的……\n',
            '我小时候还受过她很多照顾呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020229V那是我还在剧团里的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020230V#014F#4P剧团？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020231V#000F是巡回马戏团的剧团哦。\n',
            '雪拉姐是舞者呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020232V很久以前来洛连特\n',
            '巡回演出的时候和我们认识的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020233V#020F准确地说是１２年前。\n',
            '那时我１１岁，艾丝蒂尔４岁。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020234V可能是缘分吧，后来我成为游击士的时候，\n',
            '就被卡西乌斯老师收做徒弟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020235V#010F#4P原来是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020236V#020F好了，\n',
            '这些闲话等到以后再慢慢聊吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020237V咱们也该起程去柏斯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020238V因为定期船停航，\n',
            '要去柏斯就不得不走陆路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020239V首先，我们先去\n',
            '通往柏斯地区的边界关所威尔特桥吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020240V#010F#4P是西边的米尔西街道的终点对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020241V#006F那么，我们出发吧～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0052, 0x04, 0x02)
    OP_28(0x0052, 0x04, 0x04)
    OP_28(0x0052, 0x01, 0x0001)
    RemoveItem(0x032A, 1)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00400000)
    OP_20(0x000003E8)
    EventEnd(0x00)
    PlayBGM(10)

    Return()

# id: 0x0049 offset: 0xA42B
@scena.Code('func_49_A42B')
def func_49_A42B():
    ChrWalkTo(0x0102, 54540, 0, 42640, 3000, 0x00)
    SetChrDirection(0x0102, 45, 400)

    Return()

# id: 0x004A offset: 0xA447
@scena.Code('func_4A_A447')
def func_4A_A447():
    SetChrFlags(0x0101, 0x0004)
    ChrWalkTo(0x0101, 51640, 0, 50280, 3000, 0x00)
    ChrWalkTo(0x0101, 51960, 0, 44180, 3000, 0x00)
    ChrWalkTo(0x0101, 54300, 0, 43910, 3000, 0x00)
    ClearChrFlags(0x0101, 0x0004)
    ChrTurnDirection(0x0101, 0x0103, 400)

    Return()

# id: 0x004B offset: 0xA495
@scena.Code('func_4B_A495')
def func_4B_A495():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　玛鲁加山道一侧出口',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x004C offset: 0xA4DE
@scena.Code('func_4C_A4DE')
def func_4C_A4DE():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　洛连特飞艇坪',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x004D offset: 0xA521
@scena.Code('func_4D_A521')
def func_4D_A521():
    OP_13(0x0004)

    Return()

# id: 0x004E offset: 0xA525
@scena.Code('func_4E_A525')
def func_4E_A525():
    OP_13(0x0002)

    Return()

# id: 0x004F offset: 0xA529
@scena.Code('func_4F_A529')
def func_4F_A529():
    OP_13(0x0006)

    Return()

# id: 0x0050 offset: 0xA52D
@scena.Code('func_50_A52D')
def func_50_A52D():
    OP_13(0x0005)

    Return()

# id: 0x0051 offset: 0xA531
@scena.Code('func_51_A531')
def func_51_A531():
    OP_13(0x0007)

    Return()

# id: 0x0052 offset: 0xA535
@scena.Code('func_52_A535')
def func_52_A535():
    OP_13(0x0008)

    Return()

# id: 0x0053 offset: 0xA539
@scena.Code('func_53_A539')
def func_53_A539():
    OP_13(0x0003)

    Return()

# id: 0x0054 offset: 0xA53D
@scena.Code('func_54_A53D')
def func_54_A53D():
    OP_13(0x000A)

    Return()

# id: 0x0055 offset: 0xA541
@scena.Code('func_55_A541')
def func_55_A541():
    OP_13(0x000C)

    Return()

# id: 0x0056 offset: 0xA545
@scena.Code('func_56_A545')
def func_56_A545():
    OP_13(0x0009)

    Return()

# id: 0x0057 offset: 0xA549
@scena.Code('func_57_A549')
def func_57_A549():
    OP_13(0x0015)

    Return()

# id: 0x0058 offset: 0xA54D
@scena.Code('func_58_A54D')
def func_58_A54D():
    OP_13(0x0016)

    Return()

# id: 0x0059 offset: 0xA551
@scena.Code('func_59_A551')
def func_59_A551():
    OP_13(0x0017)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

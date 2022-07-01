import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0032_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0032   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, 'CH02350克劳斯市长'),
    TXT(0x02, 'CH02360梅贝尔市长'),
    TXT(0x03, 'CH02370莉拉'),
    TXT(0x04, 'CH02380卢格兰老人'),
    TXT(0x05, 'CH02390乔儿'),
    TXT(0x06, 'CH02400嘉恩'),
    TXT(0x07, 'CH02410戴尔蒙市长'),
    TXT(0x08, 'CH02420基尔巴特'),
    TXT(0x09, 'CH02430麻绪婆婆'),
    TXT(0x0A, 'CH02440格斯塔夫维修长'),
    TXT(0x0B, 'CH02450希德少校'),
    TXT(0x0C, 'CH02460希尔丹夫人'),
    TXT(0x0D, 'CH02470管家菲利普'),
    TXT(0x0E, 'CH02480缇欧'),
    TXT(0x0F, 'CH02490伊莉莎'),
    TXT(0x10, 'CH02500波利'),
    TXT(0x11, 'CH02510迪恩'),
    TXT(0x12, 'CH02520雷斯'),
    TXT(0x13, 'CH02530洛克'),
    TXT(0x14, 'CH02540特斯'),
    TXT(0x15, 'CH02550汉斯'),
    TXT(0x16, 'CH02560爱娜'),
    TXT(0x17, 'CH02570特蕾莎院长'),
    TXT(0x18, 'CH02580艾南'),
    TXT(0x19, 'CH02590克拉姆'),
    TXT(0x1A, 'CH02600科林兹校长'),
    TXT(0x1B, 'CH02610雾香'),
    TXT(0x1C, 'CH02620玛多克工房长'),
    TXT(0x1D, 'CH02630玛丽'),
    TXT(0x1E, 'CH02640达尼艾尔'),
    TXT(0x1F, 'CH01600王国军将校Ｂ'),
    TXT(0x20, 'CH01610特务兵Ｂ'),
    TXT(0x21, 'CH01620男游击士２'),
    TXT(0x22, 'CH01630女游击士２'),
    TXT(0x23, 'CH01640王国军兵士'),
    TXT(0x24, 'CH01650王国军兵士'),
    TXT(0x25, 'CH01660男性学者３'),
    TXT(0x26, 'CH01670年轻神父'),
    TXT(0x27, 'CH01680街中年男２'),
    TXT(0x28, 'CH01690街中年女２'),
    TXT(0x29, 'CH01700猫'),
    TXT(0x2A, 'CH01710牛'),
    TXT(0x2B, 'CH01720鸡'),
    TXT(0x2C, 'CH01730鸽子'),
    TXT(0x2D, 'CH01740海鸥'),
    TXT(0x2E, 'CH01750男游击士３'),
    TXT(0x2F, 'CH01760男游击士４'),
    TXT(0x30, 'CH01770侍应１'),
    TXT(0x31, 'CH01780侍应２'),
    TXT(0x32, 'CH01790特务兵Ｃ中队长'),
    TXT(0x33, 'CH20020 0'),
    TXT(0x34, 'CH20020 1'),
    TXT(0x35, 'CH20020 2'),
    TXT(0x36, 'CH20020 3'),
    TXT(0x37, 'CH20020 4'),
    TXT(0x38, 'CH20020 5'),
    TXT(0x39, 'CH20020 6'),
    TXT(0x3A, 'CH20020 7'),
    TXT(0x3B, 'CH20020 8'),
    TXT(0x3C, 'CH20020 9'),
    TXT(0x3D, 'CH20020 10'),
    TXT(0x3E, 'CH20020 11'),
    TXT(0x3F, 'CH20020 12'),
    TXT(0x40, 'CH20020 13'),
    TXT(0x41, 'CH20020 14'),
    TXT(0x42, 'CH20020 15'),
    TXT(0x43, 'CH20020 16'),
    TXT(0x44, 'CH20020 17'),
    TXT(0x45, 'CH20020 18'),
    TXT(0x46, 'CH20020 19'),
    TXT(0x47, 'CH20020 20'),
    TXT(0x48, 'CH20020 21'),
    TXT(0x49, 'CH20020 22'),
    TXT(0x4A, 'CH20020 23'),
    TXT(0x4B, 'CH20020 24'),
    TXT(0x4C, 'CH20020 25'),
    TXT(0x4D, 'CH20020 26'),
    TXT(0x4E, 'CH20020 27'),
    TXT(0x4F, 'CH20020 28'),
    TXT(0x50, 'CH20020 29'),
    TXT(0x51, 'CH20020 30'),
    TXT(0x52, 'CH20020 31'),
    TXT(0x53, 'CH20021 0'),
    TXT(0x54, 'CH20021 1'),
    TXT(0x55, 'CH20021 2'),
    TXT(0x56, 'CH20021 3'),
    TXT(0x57, 'CH20021 4'),
    TXT(0x58, 'CH20021 5'),
    TXT(0x59, 'CH20021 6'),
    TXT(0x5A, 'CH20021 7'),
    TXT(0x5B, 'CH20021 8'),
    TXT(0x5C, 'CH20021 9'),
    TXT(0x5D, 'CH20021 10'),
    TXT(0x5E, 'CH20021 11'),
    TXT(0x5F, 'CH20021 12'),
    TXT(0x60, 'CH20021 13'),
    TXT(0x61, 'CH20021 14'),
    TXT(0x62, 'CH20021 15'),
    TXT(0x63, 'CH20021 16'),
    TXT(0x64, 'CH20021 17'),
    TXT(0x65, 'CH20021 18'),
    TXT(0x66, 'CH20021 19'),
    TXT(0x67, 'CH20021 20'),
    TXT(0x68, 'CH20021 21'),
    TXT(0x69, 'CH20021 22'),
    TXT(0x6A, 'CH20021 23'),
    TXT(0x6B, 'CH20021 24'),
    TXT(0x6C, 'CH20021 25'),
    TXT(0x6D, 'CH20021 26'),
    TXT(0x6E, 'CH20021 27'),
    TXT(0x6F, 'CH20021 28'),
    TXT(0x70, 'CH20021 29'),
    TXT(0x71, 'CH20021 30'),
    TXT(0x72, 'CH20021 31'),
    TXT(0x73, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map1'
    header.mapModel       = 'T0030.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1A80
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
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0005,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
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
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH02380._CH', 'ED6_DT07/CH02380P._CP'),
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02400._CH', 'ED6_DT07/CH02400P._CP'),
        ('ED6_DT07/CH02410._CH', 'ED6_DT07/CH02410P._CP'),
        ('ED6_DT07/CH02420._CH', 'ED6_DT07/CH02420P._CP'),
        ('ED6_DT07/CH02430._CH', 'ED6_DT07/CH02430P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT07/CH02450._CH', 'ED6_DT07/CH02450P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH02520._CH', 'ED6_DT07/CH02520P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH02560._CH', 'ED6_DT07/CH02560P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02580._CH', 'ED6_DT07/CH02580P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
        ('ED6_DT07/CH02610._CH', 'ED6_DT07/CH02610P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01670._CH', 'ED6_DT07/CH01670P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH01710._CH', 'ED6_DT07/CH01710P._CP'),
        ('ED6_DT07/CH01720._CH', 'ED6_DT07/CH01720P._CP'),
        ('ED6_DT07/CH01730._CH', 'ED6_DT07/CH01730P._CP'),
        ('ED6_DT07/CH01740._CH', 'ED6_DT07/CH01740P._CP'),
        ('ED6_DT07/CH01750._CH', 'ED6_DT07/CH01750P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
        ('ED6_DT07/CH01780._CH', 'ED6_DT07/CH01780P._CP'),
        ('ED6_DT07/CH01790._CH', 'ED6_DT07/CH01790P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10002 offset: 0x24A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
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
            x                   = 8000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 40000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 45,
            chipIndex           = 45,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 40000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 46,
            chipIndex           = 46,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 40000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 47,
            chipIndex           = 47,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 40000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 48,
            chipIndex           = 48,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 40000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 49,
            chipIndex           = 49,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 50,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65586,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131122,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 196658,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262194,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327730,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 393266,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458802,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524338,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589874,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 22000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 655410,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 720946,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 26000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 786482,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 852018,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 30000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 917554,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 48000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983090,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048626,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1114162,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179698,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245234,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1310770,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1376306,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1441842,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1507378,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572914,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638450,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 22000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703986,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1769522,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 26000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835058,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1900594,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 30000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966130,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 50000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2031666,
            chipIndex           = 50,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 51,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65587,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131123,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 196659,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262195,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327731,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 393267,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458803,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524339,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589875,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 22000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 655411,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 720947,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 26000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 786483,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 852019,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 30000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 917555,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 52000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983091,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048627,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1114163,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179699,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245235,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1310771,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1376307,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1441843,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1507379,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572915,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638451,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 22000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703987,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1769523,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 26000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835059,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1900595,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 30000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966131,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 54000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2031667,
            chipIndex           = 51,
            npcIndex            = 0x0142,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
    )

# id: 0x10003 offset: 0x108A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x108A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x108A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x108A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x108B
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x108C
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_10A1',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_10A1(): pass

    label('loc_10A1')

    Return()

# id: 0x0003 offset: 0x10A2
@scena.Code('func_03_10A2')
def func_03_10A2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_10B7',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

    Jump('func_03_10A2')

    def _loc_10B7(): pass

    label('loc_10B7')

    Return()

# id: 0x0004 offset: 0x10B8
@scena.Code('func_04_10B8')
def func_04_10B8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_10CD',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000578)

    Jump('func_04_10B8')

    def _loc_10CD(): pass

    label('loc_10CD')

    Return()

# id: 0x0005 offset: 0x10CE
@scena.Code('func_05_10CE')
def func_05_10CE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_10F1',
    )

    OP_8D(0x00FE, 4000, 20000, 24000, 30000, 1500)

    Jump('func_05_10CE')

    def _loc_10F1(): pass

    label('loc_10F1')

    Return()

# id: 0x0006 offset: 0x10F2
@scena.Code('func_06_10F2')
def func_06_10F2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1115',
    )

    OP_8D(0x00FE, 22000, 20000, 42000, 30000, 1500)

    Jump('func_06_10F2')

    def _loc_1115(): pass

    label('loc_1115')

    Return()

# id: 0x0007 offset: 0x1116
@scena.Code('func_07_1116')
def func_07_1116():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#600F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#601F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#602F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#603F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#604F慌张',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1168
@scena.Code('func_08_1168')
def func_08_1168():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#610F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#611F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#612F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#613F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#614F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#615F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#616F叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#617F困扰的笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x11ED
@scena.Code('func_09_11ED')
def func_09_11ED():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#620F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#621F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#622F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#623F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#624F盯视',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x123F
@scena.Code('func_0A_123F')
def func_0A_123F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#630F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#631F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#632F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#633F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#634F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1291
@scena.Code('func_0B_1291')
def func_0B_1291():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#640F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#641F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#642F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#643F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#644F自信',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#645F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#646F唔',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#647F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#648F抛媚眼',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#649F调戏',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#659F诡笑（…会用吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x134B
@scena.Code('func_0C_134B')
def func_0C_134B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#650F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#651F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#652F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#653F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#654F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x139D
@scena.Code('func_0D_139D')
def func_0D_139D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#660F通常（表）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#661F笑容（表）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#662F认真（表里兼用）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#663F惊愕１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#664F瞑目（表里兼用）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#665F叫喊（表里兼用）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#666F唔（里）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#667F笑容（里）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#668F惊愕２',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1469
@scena.Code('func_0E_1469')
def func_0E_1469():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#670F通常（表）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#671F认真（表里兼用）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#672F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#673F瞑目（表里兼用）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#674F叫喊（表里兼用）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#675F笑容（里）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#676F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#677F叫喊２（受伤）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x1522
@scena.Code('func_0F_1522')
def func_0F_1522():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#680F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#681F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#682F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#683F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#684F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1574
@scena.Code('func_10_1574')
def func_10_1574():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#690F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#691F笑容１',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#692F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#693F笑容２',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x15BB
@scena.Code('func_11_15BB')
def func_11_15BB():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#700F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#701F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#702F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#703F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#704F叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x160D
@scena.Code('func_12_160D')
def func_12_160D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#710F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#711F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#712F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#713F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x1650
@scena.Code('func_13_1650')
def func_13_1650():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#720F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#721F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#722F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#723F叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x1693
@scena.Code('func_14_1693')
def func_14_1693():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '没有表情',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x16A8
@scena.Code('func_15_16A8')
def func_15_16A8():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '没有表情',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x16BD
@scena.Code('func_16_16BD')
def func_16_16BD():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '没有表情',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x16D2
@scena.Code('func_17_16D2')
def func_17_16D2():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '没有表情',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x16E7
@scena.Code('func_18_16E7')
def func_18_16E7():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '没有表情',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x16FC
@scena.Code('func_19_16FC')
def func_19_16FC():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '没有表情',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x1711
@scena.Code('func_1A_1711')
def func_1A_1711():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '没有表情',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x1726
@scena.Code('func_1B_1726')
def func_1B_1726():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#730F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#731F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#732F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#733F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#734F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x1778
@scena.Code('func_1C_1778')
def func_1C_1778():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#740F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#741F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#742F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#743F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#744F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#745F叹息',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x17D9
@scena.Code('func_1D_17D9')
def func_1D_17D9():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#750F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#751F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#752F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#753F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#754F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#755F叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#756F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#757F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#758F高兴的哭泣',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001E offset: 0x186D
@scena.Code('func_1E_186D')
def func_1E_186D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#760F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#761F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#762F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#763F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#764F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001F offset: 0x18BF
@scena.Code('func_1F_18BF')
def func_1F_18BF():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#770F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#771F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#772F认真',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#773F悲哀',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#774F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#775F困惑',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#776F发怒',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#777F哭泣',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#778F叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0020 offset: 0x194D
@scena.Code('func_20_194D')
def func_20_194D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#780F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#781F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#782F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x1981
@scena.Code('func_21_1981')
def func_21_1981():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#790F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#791F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#792F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0022 offset: 0x19B5
@scena.Code('func_22_19B5')
def func_22_19B5():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#800F通常',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#801F笑容',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#802F惊愕',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#803F瞑目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#804F叫喊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#805F慌张',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#806F远目',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0023 offset: 0x1A25
@scena.Code('func_23_1A25')
def func_23_1A25():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呜喵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

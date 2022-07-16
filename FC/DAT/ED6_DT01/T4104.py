import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4104_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4104   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '金'),
    TXT(0x02, '卡露娜'),
    TXT(0x03, '亚妮拉丝'),
    TXT(0x04, '库拉茨'),
    TXT(0x05, '克鲁茨'),
    TXT(0x06, '空贼'),
    TXT(0x07, '多伦'),
    TXT(0x08, '吉尔'),
    TXT(0x09, '乔丝特'),
    TXT(0x0A, '不良青年'),
    TXT(0x0B, '迪恩'),
    TXT(0x0C, '雷斯'),
    TXT(0x0D, '洛克'),
    TXT(0x0E, '士兵'),
    TXT(0x0F, '士兵'),
    TXT(0x10, '士兵'),
    TXT(0x11, '士兵'),
    TXT(0x12, '莱尔中尉'),
    TXT(0x13, '贝伦中尉'),
    TXT(0x14, '迪鲁队长'),
    TXT(0x15, '特务兵'),
    TXT(0x16, '特务兵'),
    TXT(0x17, '特务兵'),
    TXT(0x18, '洛伦斯少尉'),
    TXT(0x19, '管家菲利普'),
    TXT(0x1A, '杜南公爵'),
    TXT(0x1B, '亚鲁瓦教授'),
    TXT(0x1C, '朵洛希'),
    TXT(0x1D, '裁判'),
    TXT(0x1E, '不良青年'),
    TXT(0x1F, '不良青年'),
    TXT(0x20, '不良青年'),
    TXT(0x21, '凯诺娜上尉'),
    TXT(0x22, '理查德上校'),
    TXT(0x23, '芭蒂'),
    TXT(0x24, '拉尔夫'),
    TXT(0x25, '蒂库'),
    TXT(0x26, '拉尔斯'),
    TXT(0x27, '托伊'),
    TXT(0x28, '克劳斯市长'),
    TXT(0x29, '观众'),
    TXT(0x2A, '观众'),
    TXT(0x2B, '观众'),
    TXT(0x2C, '观众'),
    TXT(0x2D, '观众'),
    TXT(0x2E, '观众'),
    TXT(0x2F, '观众'),
    TXT(0x30, '观众'),
    TXT(0x31, '观众'),
    TXT(0x32, '观众'),
    TXT(0x33, '观众'),
    TXT(0x34, '观众'),
    TXT(0x35, '观众'),
    TXT(0x36, '观众'),
    TXT(0x37, '观众'),
    TXT(0x38, '观众'),
    TXT(0x39, '观众'),
    TXT(0x3A, '观众'),
    TXT(0x3B, '观众'),
    TXT(0x3C, '观众'),
    TXT(0x3D, '观众'),
    TXT(0x3E, '观众'),
    TXT(0x3F, '观众'),
    TXT(0x40, '观众'),
    TXT(0x41, '观众'),
    TXT(0x42, '观众'),
    TXT(0x43, '观众'),
    TXT(0x44, '观众'),
    TXT(0x45, '观众'),
    TXT(0x46, '观众'),
    TXT(0x47, '观众'),
    TXT(0x48, '观众'),
    TXT(0x49, '观众'),
    TXT(0x4A, '观众'),
    TXT(0x4B, '观众'),
    TXT(0x4C, '观众'),
    TXT(0x4D, '观众'),
    TXT(0x4E, '观众'),
    TXT(0x4F, '观众'),
    TXT(0x50, '观众'),
    TXT(0x51, '观众'),
    TXT(0x52, '观众'),
    TXT(0x53, '观众'),
    TXT(0x54, '观众'),
    TXT(0x55, '观众'),
    TXT(0x56, '观众'),
    TXT(0x57, '观众'),
    TXT(0x58, '观众'),
    TXT(0x59, '观众'),
    TXT(0x5A, '观众'),
    TXT(0x5B, '观众'),
    TXT(0x5C, '观众'),
    TXT(0x5D, '观众'),
    TXT(0x5E, '观众'),
    TXT(0x5F, '观众'),
    TXT(0x60, '观众'),
    TXT(0x61, '观众'),
    TXT(0x62, '观众'),
    TXT(0x63, '观众'),
    TXT(0x64, '观众'),
    TXT(0x65, '观众'),
    TXT(0x66, '观众'),
    TXT(0x67, '观众'),
    TXT(0x68, '观众'),
    TXT(0x69, '观众'),
    TXT(0x6A, '观众'),
    TXT(0x6B, '观众'),
    TXT(0x6C, '观众'),
    TXT(0x6D, '观众'),
    TXT(0x6E, '观众'),
    TXT(0x6F, '观众'),
    TXT(0x70, '观众'),
    TXT(0x71, '观众'),
    TXT(0x72, '观众'),
    TXT(0x73, '观众'),
    TXT(0x74, '观众'),
    TXT(0x75, '观众'),
    TXT(0x76, '观众'),
    TXT(0x77, '观众'),
    TXT(0x78, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4104.x'
    header.mapIndex       = 1
    header.bgm            = 18
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T4104._SN', 'ED6_DT01/T4104_1._SN', 'ED6_DT01/T4104_2._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x943C
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
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH01390._CH', 'ED6_DT07/CH01390P._CP'),
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH02520._CH', 'ED6_DT07/CH02520P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT06/CH20123._CH', 'ED6_DT06/CH20123P._CP'),
        ('ED6_DT06/CH20124._CH', 'ED6_DT06/CH20124P._CP'),
        ('ED6_DT06/CH20125._CH', 'ED6_DT06/CH20125P._CP'),
        ('ED6_DT06/CH20126._CH', 'ED6_DT06/CH20126P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT06/CH20088._CH', 'ED6_DT06/CH20088P._CP'),
    ]

# id: 0x10002 offset: 0x1B2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0025,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0024,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002B,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002E,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002D,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002C,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
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
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
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
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -12680,
            z                   = 4700,
            y                   = -4790,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            x                   = -12660,
            z                   = 4700,
            y                   = -3750,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            x                   = -14750,
            z                   = 5200,
            y                   = 3290,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131099,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            x                   = -14750,
            z                   = 5200,
            y                   = 3960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65564,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            x                   = -14750,
            z                   = 5200,
            y                   = 4700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196634,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 393244,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = -14740,
            z                   = 5200,
            y                   = -13430,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65563,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            x                   = -15730,
            z                   = 5450,
            y                   = -5010,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0001,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = 3270,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            x                   = -15820,
            z                   = 5450,
            y                   = -9240,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -15850,
            z                   = 5450,
            y                   = 1890,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = -6590,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -12680,
            z                   = 4700,
            y                   = -17670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -14720,
            z                   = 5200,
            y                   = -3720,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 458778,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = 1670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262171,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -13710,
            z                   = 4950,
            y                   = -13580,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -14750,
            z                   = 5200,
            y                   = -8060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327707,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -14720,
            z                   = 5200,
            y                   = 510,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -12660,
            z                   = 4700,
            y                   = -9280,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -13750,
            z                   = 4950,
            y                   = 4710,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -13770,
            z                   = 4950,
            y                   = -6540,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196636,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -14850,
            z                   = 5200,
            y                   = -15970,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262172,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = -13490,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327708,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = -15610,
            z                   = 5450,
            y                   = -17700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -15900,
            z                   = 5450,
            y                   = -14800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = -16640,
            z                   = 5700,
            y                   = -13560,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393242,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -13720,
            z                   = 4950,
            y                   = -9500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = -13810,
            z                   = 4950,
            y                   = -4800,
            direction           = 91,
            word_0E             = 0,
            dword_10            = 196635,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = -14870,
            z                   = 5200,
            y                   = -4980,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = -15810,
            z                   = 5450,
            y                   = -6530,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327706,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = -15850,
            z                   = 5450,
            y                   = 3270,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327707,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = 520,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65563,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = -13720,
            z                   = 4950,
            y                   = 3330,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262171,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = -14730,
            z                   = 5200,
            y                   = 1860,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = -13780,
            z                   = 4950,
            y                   = -8039,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 458779,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = -15680,
            z                   = 5450,
            y                   = 550,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            x                   = -12660,
            z                   = 4700,
            y                   = 4760,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393242,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            x                   = -13930,
            z                   = 4950,
            y                   = -3700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            x                   = -16620,
            z                   = 5700,
            y                   = -3710,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = -15860,
            z                   = 5450,
            y                   = 4750,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196636,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            x                   = -12730,
            z                   = 4700,
            y                   = -8010,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131100,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            x                   = -16720,
            z                   = 5700,
            y                   = -13930,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262172,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -13800,
            z                   = 4950,
            y                   = -14740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327708,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -14800,
            z                   = 5200,
            y                   = -14740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -15640,
            z                   = 5450,
            y                   = -15910,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -15790,
            z                   = 5450,
            y                   = -13450,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393242,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -16820,
            z                   = 5700,
            y                   = -17670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -16710,
            z                   = 5700,
            y                   = -16280,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196635,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -16710,
            z                   = 5700,
            y                   = -14840,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -15840,
            z                   = 5450,
            y                   = -16740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327706,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -14720,
            z                   = 5200,
            y                   = -16740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327707,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -14860,
            z                   = 5200,
            y                   = -14050,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65563,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -12700,
            z                   = 4700,
            y                   = -14100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262171,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -14670,
            z                   = 5200,
            y                   = -9220,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -15900,
            z                   = 5450,
            y                   = -7990,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 458779,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -14820,
            z                   = 5200,
            y                   = -6520,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -15740,
            z                   = 5450,
            y                   = -3710,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393242,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -14700,
            z                   = 5200,
            y                   = -7290,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -13790,
            z                   = 4950,
            y                   = -5620,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262172,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -16740,
            z                   = 5700,
            y                   = -5620,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196636,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -16690,
            z                   = 5700,
            y                   = -8690,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131100,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -15800,
            z                   = 5450,
            y                   = -5790,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = -5670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = -7390,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 458778,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -14700,
            z                   = 5200,
            y                   = -4400,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262171,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -16690,
            z                   = 5700,
            y                   = -7210,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -13760,
            z                   = 4950,
            y                   = -8770,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 327707,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -13760,
            z                   = 4950,
            y                   = 530,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -13760,
            z                   = 4950,
            y                   = 1760,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -15870,
            z                   = 5450,
            y                   = 1130,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -13900,
            z                   = 4950,
            y                   = 2470,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -12680,
            z                   = 4700,
            y                   = 4050,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65563,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -15780,
            z                   = 5450,
            y                   = 4019,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -14710,
            z                   = 5200,
            y                   = 2590,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4950,
            y                   = 1110,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 393243,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -12650,
            z                   = 4700,
            y                   = 2550,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 14670,
            z                   = 4700,
            y                   = 1910,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 262172,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 14660,
            z                   = 4700,
            y                   = 680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 327708,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 15770,
            z                   = 4950,
            y                   = 680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 16860,
            z                   = 5200,
            y                   = 680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 131098,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 17850,
            z                   = 5450,
            y                   = 680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 393242,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 18800,
            z                   = 5700,
            y                   = 680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 15910,
            z                   = 4950,
            y                   = 1830,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 196635,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 16760,
            z                   = 5200,
            y                   = 1830,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 262170,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 17780,
            z                   = 5450,
            y                   = 1990,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 327706,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1092
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1092
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1092
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1092
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 6, 0x3FE)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 7, 0x3FF)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 0, 0x3F0)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 1, 0x3F1)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 2, 0x3F2)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 3, 0x3F3)),
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1224',
    )

    ClearChrFlags(0x0053, 0x0080)
    ClearChrFlags(0x0054, 0x0080)
    ClearChrFlags(0x0055, 0x0080)
    ClearChrFlags(0x0056, 0x0080)
    ClearChrFlags(0x0057, 0x0080)
    ClearChrFlags(0x0058, 0x0080)
    ClearChrFlags(0x0059, 0x0080)
    ClearChrFlags(0x005A, 0x0080)
    ClearChrFlags(0x005B, 0x0080)
    ClearChrFlags(0x005C, 0x0080)
    ClearChrFlags(0x005D, 0x0080)
    ClearChrFlags(0x005E, 0x0080)
    ClearChrFlags(0x005F, 0x0080)
    ClearChrFlags(0x0060, 0x0080)
    ClearChrFlags(0x0061, 0x0080)
    ClearChrFlags(0x0062, 0x0080)
    ClearChrFlags(0x0063, 0x0080)
    ClearChrFlags(0x0064, 0x0080)
    ClearChrFlags(0x0065, 0x0080)
    ClearChrFlags(0x0066, 0x0080)
    ClearChrFlags(0x0067, 0x0080)
    ClearChrFlags(0x0068, 0x0080)
    ClearChrFlags(0x0069, 0x0080)
    ClearChrFlags(0x006A, 0x0080)
    ClearChrFlags(0x006B, 0x0080)
    ClearChrFlags(0x006C, 0x0080)
    ClearChrFlags(0x006D, 0x0080)
    ClearChrFlags(0x006E, 0x0080)
    ClearChrFlags(0x006F, 0x0080)
    ClearChrFlags(0x0070, 0x0080)
    ClearChrFlags(0x0071, 0x0080)
    ClearChrFlags(0x0072, 0x0080)
    ClearChrFlags(0x0073, 0x0080)
    ClearChrFlags(0x0074, 0x0080)
    ClearChrFlags(0x0075, 0x0080)
    ClearChrFlags(0x0030, 0x0080)
    ClearChrFlags(0x0031, 0x0080)
    ClearChrFlags(0x0032, 0x0080)
    ClearChrFlags(0x0033, 0x0080)
    ClearChrFlags(0x0034, 0x0080)
    ClearChrFlags(0x0035, 0x0080)
    ClearChrFlags(0x0036, 0x0080)
    ClearChrFlags(0x0037, 0x0080)
    ClearChrFlags(0x0038, 0x0080)
    ClearChrFlags(0x0039, 0x0080)
    ClearChrFlags(0x003A, 0x0080)
    ClearChrFlags(0x003B, 0x0080)
    ClearChrFlags(0x003C, 0x0080)
    ClearChrFlags(0x003D, 0x0080)
    ClearChrFlags(0x003E, 0x0080)
    ClearChrFlags(0x003F, 0x0080)
    ClearChrFlags(0x0040, 0x0080)
    ClearChrFlags(0x0041, 0x0080)
    ClearChrFlags(0x0042, 0x0080)
    ClearChrFlags(0x0043, 0x0080)
    ClearChrFlags(0x0044, 0x0080)
    ClearChrFlags(0x0045, 0x0080)
    ClearChrFlags(0x0046, 0x0080)
    ClearChrFlags(0x0047, 0x0080)
    ClearChrFlags(0x0048, 0x0080)
    ClearChrFlags(0x0049, 0x0080)
    ClearChrFlags(0x004A, 0x0080)
    ClearChrFlags(0x004B, 0x0080)
    ClearChrFlags(0x004C, 0x0080)
    ClearChrFlags(0x004D, 0x0080)
    ClearChrFlags(0x004E, 0x0080)
    ClearChrFlags(0x004F, 0x0080)
    ClearChrFlags(0x0050, 0x0080)
    ClearChrFlags(0x0051, 0x0080)
    ClearChrFlags(0x0052, 0x0080)

    def _loc_1224(): pass

    label('loc_1224')

    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0015, 17290, 9500, -4880, 270)
    SetChrPos(0x0016, 17290, 9500, -8150, 270)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_125E',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0003)

    def _loc_125E(): pass

    label('loc_125E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_126C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0004)

    def _loc_126C(): pass

    label('loc_126C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_127A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x0005)

    def _loc_127A(): pass

    label('loc_127A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_1288',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, 0x0007)

    def _loc_1288(): pass

    label('loc_1288')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 6, 0x3FE)),
            Expr.Return,
        ),
        'loc_1296',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 6, 0x3FE))
    Event(0, 0x0008)

    def _loc_1296(): pass

    label('loc_1296')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 7, 0x3FF)),
            Expr.Return,
        ),
        'loc_12A4',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    Event(0, 0x0009)

    def _loc_12A4(): pass

    label('loc_12A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 0, 0x3F0)),
            Expr.Return,
        ),
        'loc_12B2',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    Event(0, 0x000A)

    def _loc_12B2(): pass

    label('loc_12B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 1, 0x3F1)),
            Expr.Return,
        ),
        'loc_12C0',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 1, 0x3F1))
    Event(0, 0x000C)

    def _loc_12C0(): pass

    label('loc_12C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 2, 0x3F2)),
            Expr.Return,
        ),
        'loc_12CE',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 2, 0x3F2))
    Event(0, 0x000D)

    def _loc_12CE(): pass

    label('loc_12CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 3, 0x3F3)),
            Expr.Return,
        ),
        'loc_12DC',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 3, 0x3F3))
    Event(0, 0x000E)

    def _loc_12DC(): pass

    label('loc_12DC')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_12F0'),
        (0x00000064, 'loc_12F0'),
        (0x00000067, 'loc_1306'),
        (-1, 'loc_1342'),
    )

    def _loc_12F0(): pass

    label('loc_12F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 6, 0x60E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 5, 0x60D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1303',
    )

    SetScenaFlags(ScenaFlag(0x00C1, 6, 0x60E))
    Event(0, 0x0002)

    def _loc_1303(): pass

    label('loc_1303')

    Jump('loc_1342')

    def _loc_1306(): pass

    label('loc_1306')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 6, 0x636)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1319',
    )

    SetScenaFlags(ScenaFlag(0x00C6, 7, 0x637))
    Event(0, 0x000F)

    def _loc_1319(): pass

    label('loc_1319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_132C',
    )

    SetScenaFlags(ScenaFlag(0x00C3, 6, 0x61E))
    Event(0, 0x0006)

    def _loc_132C(): pass

    label('loc_132C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 5, 0x625)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_133F',
    )

    SetScenaFlags(ScenaFlag(0x00C4, 6, 0x626))
    Event(0, 0x000B)

    def _loc_133F(): pass

    label('loc_133F')

    Jump('loc_1342')

    def _loc_1342(): pass

    label('loc_1342')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 0, 0x638)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13D2',
    )

    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x0022, -17490, 5950, -9620, 90)
    SetChrPos(0x0023, -10510, 4200, -6570, 90)
    SetChrPos(0x0009, -12660, 4700, -16340, 90)
    SetChrPos(0x000A, -12670, 4700, -15020, 90)
    SetChrPos(0x000B, -13760, 4950, -17160, 90)
    SetChrPos(0x000C, -14580, 5200, -17680, 90)

    def _loc_13D2(): pass

    label('loc_13D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_13DC',
    )

    Jump('loc_154E')

    def _loc_13DC(): pass

    label('loc_13DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_13E6',
    )

    Jump('loc_154E')

    def _loc_13E6(): pass

    label('loc_13E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_13F0',
    )

    Jump('loc_154E')

    def _loc_13F0(): pass

    label('loc_13F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_13FA',
    )

    Jump('loc_154E')

    def _loc_13FA(): pass

    label('loc_13FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_149E',
    )

    ClearChrFlags(0x002A, 0x0080)
    ClearChrFlags(0x002B, 0x0080)
    ClearChrFlags(0x002C, 0x0080)
    ClearChrFlags(0x002D, 0x0080)
    ClearChrFlags(0x002E, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 5, 0x635)),
            Expr.Return,
        ),
        'loc_1437',
    )

    ClearChrFlags(0x002F, 0x0080)
    SetChrPos(0x002F, -14380, 5200, 4380, 98)

    def _loc_1437(): pass

    label('loc_1437')

    ClearChrFlags(0x003F, 0x0080)
    ClearChrFlags(0x0040, 0x0080)
    ClearChrFlags(0x0041, 0x0080)
    ClearChrFlags(0x0042, 0x0080)
    ClearChrFlags(0x0043, 0x0080)
    ClearChrFlags(0x0044, 0x0080)
    ClearChrFlags(0x0045, 0x0080)
    ClearChrFlags(0x0046, 0x0080)
    ClearChrFlags(0x0047, 0x0080)
    ClearChrFlags(0x0048, 0x0080)
    ClearChrFlags(0x0049, 0x0080)
    ClearChrFlags(0x004A, 0x0080)
    ClearChrFlags(0x004B, 0x0080)
    ClearChrFlags(0x004C, 0x0080)
    ClearChrFlags(0x004D, 0x0080)
    ClearChrFlags(0x004E, 0x0080)
    ClearChrFlags(0x004F, 0x0080)
    ClearChrFlags(0x0050, 0x0080)
    ClearChrFlags(0x0051, 0x0080)
    ClearChrFlags(0x0052, 0x0080)

    Jump('loc_154E')

    def _loc_149E(): pass

    label('loc_149E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_14A8',
    )

    Jump('loc_154E')

    def _loc_14A8(): pass

    label('loc_14A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_14FA',
    )

    ClearChrFlags(0x002A, 0x0080)
    SetChrPos(0x002A, -14850, 5200, 4019, 90)
    ClearChrFlags(0x0035, 0x0080)
    ClearChrFlags(0x0036, 0x0080)
    ClearChrFlags(0x0037, 0x0080)
    ClearChrFlags(0x0038, 0x0080)
    ClearChrFlags(0x0039, 0x0080)
    ClearChrFlags(0x003A, 0x0080)
    ClearChrFlags(0x003B, 0x0080)
    ClearChrFlags(0x003C, 0x0080)
    ClearChrFlags(0x003D, 0x0080)
    ClearChrFlags(0x003E, 0x0080)

    Jump('loc_154E')

    def _loc_14FA(): pass

    label('loc_14FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1504',
    )

    Jump('loc_154E')

    def _loc_1504(): pass

    label('loc_1504')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_153D',
    )

    ClearChrFlags(0x002A, 0x0080)
    SetChrPos(0x002A, -12690, 4700, -4810, 90)
    ClearChrFlags(0x0030, 0x0080)
    ClearChrFlags(0x0031, 0x0080)
    ClearChrFlags(0x0032, 0x0080)
    ClearChrFlags(0x0033, 0x0080)
    ClearChrFlags(0x0034, 0x0080)

    Jump('loc_154E')

    def _loc_153D(): pass

    label('loc_153D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1547',
    )

    Jump('loc_154E')

    def _loc_1547(): pass

    label('loc_1547')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_154E',
    )

    def _loc_154E(): pass

    label('loc_154E')

    Return()

# id: 0x0001 offset: 0x154F
@scena.Code('Init')
def Init():
    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)

    Return()

# id: 0x0002 offset: 0x155A
@scena.Code('ReInit')
def ReInit():
    ClearChrFlags(0x0053, 0x0080)
    ClearChrFlags(0x0054, 0x0080)
    ClearChrFlags(0x0055, 0x0080)
    ClearChrFlags(0x0056, 0x0080)
    ClearChrFlags(0x0057, 0x0080)
    ClearChrFlags(0x0058, 0x0080)
    ClearChrFlags(0x0059, 0x0080)
    ClearChrFlags(0x005A, 0x0080)
    ClearChrFlags(0x005B, 0x0080)
    ClearChrFlags(0x005C, 0x0080)
    ClearChrFlags(0x005D, 0x0080)
    ClearChrFlags(0x005E, 0x0080)
    ClearChrFlags(0x005F, 0x0080)
    ClearChrFlags(0x0060, 0x0080)
    ClearChrFlags(0x0061, 0x0080)
    ClearChrFlags(0x0062, 0x0080)
    ClearChrFlags(0x0063, 0x0080)
    ClearChrFlags(0x0064, 0x0080)
    ClearChrFlags(0x0065, 0x0080)
    ClearChrFlags(0x0066, 0x0080)
    ClearChrFlags(0x0067, 0x0080)
    ClearChrFlags(0x0068, 0x0080)
    ClearChrFlags(0x0069, 0x0080)
    ClearChrFlags(0x006A, 0x0080)
    ClearChrFlags(0x006B, 0x0080)
    ClearChrFlags(0x006C, 0x0080)
    ClearChrFlags(0x006D, 0x0080)
    ClearChrFlags(0x006E, 0x0080)
    ClearChrFlags(0x006F, 0x0080)
    ClearChrFlags(0x0070, 0x0080)
    ClearChrFlags(0x0071, 0x0080)
    ClearChrFlags(0x0072, 0x0080)
    ClearChrFlags(0x0073, 0x0080)
    ClearChrFlags(0x0074, 0x0080)
    ClearChrFlags(0x0075, 0x0080)
    ClearChrFlags(0x0030, 0x0080)
    ClearChrFlags(0x0031, 0x0080)
    ClearChrFlags(0x0032, 0x0080)
    ClearChrFlags(0x0033, 0x0080)
    ClearChrFlags(0x0034, 0x0080)
    ClearChrFlags(0x0035, 0x0080)
    ClearChrFlags(0x0036, 0x0080)
    ClearChrFlags(0x0037, 0x0080)
    ClearChrFlags(0x0038, 0x0080)
    ClearChrFlags(0x0039, 0x0080)
    ClearChrFlags(0x003A, 0x0080)
    ClearChrFlags(0x003B, 0x0080)
    ClearChrFlags(0x003C, 0x0080)
    ClearChrFlags(0x003D, 0x0080)
    ClearChrFlags(0x003E, 0x0080)
    ClearChrFlags(0x003F, 0x0080)
    ClearChrFlags(0x0040, 0x0080)
    ClearChrFlags(0x0041, 0x0080)
    ClearChrFlags(0x0042, 0x0080)
    ClearChrFlags(0x0043, 0x0080)
    ClearChrFlags(0x0044, 0x0080)
    ClearChrFlags(0x0045, 0x0080)
    ClearChrFlags(0x0046, 0x0080)
    ClearChrFlags(0x0047, 0x0080)
    ClearChrFlags(0x0048, 0x0080)
    ClearChrFlags(0x0049, 0x0080)
    ClearChrFlags(0x004A, 0x0080)
    ClearChrFlags(0x004B, 0x0080)
    ClearChrFlags(0x004C, 0x0080)
    ClearChrFlags(0x004D, 0x0080)
    ClearChrFlags(0x004E, 0x0080)
    ClearChrFlags(0x004F, 0x0080)
    ClearChrFlags(0x0050, 0x0080)
    ClearChrFlags(0x0051, 0x0080)
    ClearChrFlags(0x0052, 0x0080)
    SetChrPos(0x0053, -13710, 4950, -16760, 90)
    SetChrPos(0x005D, -12690, 4700, -15820, 90)
    SetChrPos(0x0035, -14950, 5200, 4040, 90)
    SetChrPos(0x0068, -12650, 4700, -3710, 90)
    SetChrPos(0x0069, -16730, 5700, 2520, 90)
    ClearChrFlags(0x0076, 0x0080)
    ClearChrFlags(0x0077, 0x0080)
    ClearChrFlags(0x0078, 0x0080)
    ClearChrFlags(0x0079, 0x0080)
    ClearChrFlags(0x007A, 0x0080)
    ClearChrFlags(0x007B, 0x0080)
    ClearChrFlags(0x007C, 0x0080)
    ClearChrFlags(0x007D, 0x0080)
    ClearChrFlags(0x007E, 0x0080)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)
    ClearChrFlags(0x0021, 0x0080)
    SetChrFlags(0x0021, 0x0004)
    SetChrChipByIndex(0x0021, 32)
    SetChrPos(0x0021, 13860, 9850, -6510, 270)
    ClearChrFlags(0x0020, 0x0080)
    SetChrPos(0x0020, 14630, 9750, -5420, 270)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17A8',
    )

    SetChrPos(0x0102, -10510, 4200, 5460, 270)
    SetChrPos(0x0101, -10500, 4200, 4210, 270)

    Jump('loc_17CA')

    def _loc_17A8(): pass

    label('loc_17A8')

    SetChrPos(0x0101, -10510, 4200, -16790, 270)
    SetChrPos(0x0102, -10510, 4200, -17970, 270)

    def _loc_17CA(): pass

    label('loc_17CA')

    CameraMove(12190, 5450, -6580, 0)
    OP_67(0, 5170, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(180000, 0)
    OP_6E(441, 0)
    OP_66(0x0000)

    @scena.Lambda('lambda_1810')
    def lambda_1810():
        CameraMove(-4240, 7800, 50, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1810)

    Sleep(6000)

    Fade(1000)
    OP_66(0x0001)
    Yield()

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1859',
    )

    CameraMove(-10980, 4200, 5030, 0)
    OP_6C(315000, 0)

    Jump('loc_1873')

    def _loc_1859(): pass

    label('loc_1859')

    CameraMove(-10520, 4200, -17340, 0)
    OP_6C(224000, 0)

    def _loc_1873(): pass

    label('loc_1873')

    OP_67(0, 6050, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6E(262, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010100898V#004F哇……\n',
            '这么多人啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100899V#010F嗯……大家的热情很高啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100900V预选赛都有这么多人来看，\n',
            '这个大会的规模可想而知了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_192E')
    def lambda_192E():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_192E)

    Sleep(200)

    SetChrDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100901V#006F预选赛，进行到什么阶段了呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200100902V',
            (TxtCtl.SetColor, 0x5),
            '让大家久等了。\n',
            '接下来开始第七场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100903V#006F啊……好像开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100904V#010F那么，\n',
            '我们赶快找个空位坐下来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    SetChrPos(0x0102, -12660, 4700, -6310, 90)
    SetChrPos(0x0101, -12650, 4700, -7170, 90)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1000, 0, -6610, 0)
    OP_67(0, 18930, -27990, 0)
    CameraSetDistance(700, 0)
    OP_6C(90000, 0)
    OP_6E(532, 0)
    OP_66(0x0000)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200100905V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100906V',
            (TxtCtl.SetColor, 0x5),
            '国境警卫队第２连队所属，\n',
            '帕乌尔少尉等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrPos(0x0019, 2260, 120, -24190, 0)
    SetChrPos(0x0015, 1380, 120, -24190, 0)
    SetChrPos(0x0016, 300, 120, -24190, 0)
    SetChrPos(0x0017, -560, 120, -24190, 0)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    CameraMove(1200, 0, -21730, 2000)
    OP_70(0x0000, 100)
    OP_73(0x0000)
    Sleep(500)

    PlaySE(175, 0x00, 0x64)

    @scena.Lambda('lambda_1BA0')
    def lambda_1BA0():
        ChrWalkTo(0x00FE, 2260, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1BA0)

    Sleep(300)

    @scena.Lambda('lambda_1BC0')
    def lambda_1BC0():
        ChrWalkTo(0x00FE, -560, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_1BC0)

    Sleep(50)

    @scena.Lambda('lambda_1BE0')
    def lambda_1BE0():
        ChrWalkTo(0x00FE, 1380, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_1BE0)

    Sleep(50)

    @scena.Lambda('lambda_1C00')
    def lambda_1C00():
        ChrWalkTo(0x00FE, 300, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_1C00)

    CameraMove(1000, 0, -6610, 6000)

    ChrTalk(
        0x0101,
        (
            '#0010100907V#004F咦……\n',
            '比赛不是一对一吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100908V#012F嗯，看起来好像是团体赛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100909V根据我的记忆，\n',
            '应该是个人赛没错啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200100910V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100911V',
            (TxtCtl.SetColor, 0x5),
            '游击士协会格兰赛尔支部，\n',
            '克鲁茨选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010100912V#501F啊，是卡露娜姐姐他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100913V#010F差一点就错过了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, 2260, 120, 11000, 180)
    SetChrPos(0x000A, 1380, 120, 11000, 180)
    SetChrPos(0x000B, 300, 120, 11000, 180)
    SetChrPos(0x000C, -560, 120, 11000, 180)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    CameraMove(880, 0, 8980, 2000)
    OP_70(0x0001, 100)
    OP_73(0x0001)
    Sleep(500)

    PlaySE(175, 0x00, 0x64)

    @scena.Lambda('lambda_1DEF')
    def lambda_1DEF():
        ChrWalkTo(0x00FE, 2260, 0, -5460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1DEF)

    @scena.Lambda('lambda_1E0A')
    def lambda_1E0A():
        ChrWalkTo(0x00FE, 300, 0, -5460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1E0A)

    Sleep(60)

    @scena.Lambda('lambda_1E2A')
    def lambda_1E2A():
        ChrWalkTo(0x00FE, -560, 0, -5460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1E2A)

    Sleep(100)

    @scena.Lambda('lambda_1E4A')
    def lambda_1E4A():
        ChrWalkTo(0x00FE, 1380, 0, -5460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1E4A)

    CameraMove(1000, 0, -6610, 6000)
    Sleep(500)

    ChrWalkTo(0x0024, 2900, 0, -6480, 3000, 0x00)

    ChrTalk(
        0x0024,
        (
            '#2210100914V马上开始武术大会\n',
            '预选赛第７场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1EE9')
    def lambda_1EE9():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1EE9')

    DispatchAsync2(0x0019, 0x0001, lambda_1EE9)

    @scena.Lambda('lambda_1EFA')
    def lambda_1EFA():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1EFA')

    DispatchAsync2(0x0017, 0x0001, lambda_1EFA)

    @scena.Lambda('lambda_1F0B')
    def lambda_1F0B():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1F0B')

    DispatchAsync2(0x0015, 0x0001, lambda_1F0B)

    @scena.Lambda('lambda_1F1C')
    def lambda_1F1C():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1F1C')

    DispatchAsync2(0x0016, 0x0001, lambda_1F1C)

    @scena.Lambda('lambda_1F2D')
    def lambda_1F2D():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_1F2D)

    Sleep(200)

    @scena.Lambda('lambda_1F4D')
    def lambda_1F4D():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_1F4D)

    @scena.Lambda('lambda_1F68')
    def lambda_1F68():
        ChrWalkTo(0x00FE, 2580, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_1F68)

    @scena.Lambda('lambda_1F83')
    def lambda_1F83():
        ChrWalkTo(0x00FE, -350, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_1F83)

    @scena.Lambda('lambda_1F9E')
    def lambda_1F9E():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_1F9E')

    DispatchAsync2(0x000B, 0x0001, lambda_1F9E)

    @scena.Lambda('lambda_1FAF')
    def lambda_1FAF():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_1FAF')

    DispatchAsync2(0x000A, 0x0001, lambda_1FAF)

    @scena.Lambda('lambda_1FC0')
    def lambda_1FC0():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_1FC0')

    DispatchAsync2(0x0009, 0x0001, lambda_1FC0)

    @scena.Lambda('lambda_1FD1')
    def lambda_1FD1():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_1FD1')

    DispatchAsync2(0x000C, 0x0001, lambda_1FD1)

    @scena.Lambda('lambda_1FE2')
    def lambda_1FE2():
        ChrWalkTo(0x00FE, 390, 0, -1720, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1FE2)

    @scena.Lambda('lambda_1FFD')
    def lambda_1FFD():
        ChrWalkTo(0x00FE, 1430, 0, -1790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1FFD)

    @scena.Lambda('lambda_2018')
    def lambda_2018():
        ChrWalkTo(0x00FE, 2260, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2018)

    @scena.Lambda('lambda_2033')
    def lambda_2033():
        ChrWalkTo(0x00FE, -560, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2033)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    SetChrChipByIndex(0x0019, 29)
    SetChrChipByIndex(0x0015, 29)
    SetChrChipByIndex(0x0016, 29)
    SetChrChipByIndex(0x0017, 29)
    SetChrFlags(0x0019, 0x0002)
    SetChrFlags(0x0015, 0x0002)
    SetChrFlags(0x0016, 0x0002)
    SetChrFlags(0x0017, 0x0002)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x34),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000B, 29)
    SetChrChipByIndex(0x000A, 29)
    SetChrChipByIndex(0x0009, 29)
    SetChrChipByIndex(0x000C, 29)
    SetChrFlags(0x000B, 0x0002)
    SetChrFlags(0x000A, 0x0002)
    SetChrFlags(0x0009, 0x0002)
    SetChrFlags(0x000C, 0x0002)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000C, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BB9, 0x00100002, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)
    SetChrPos(0x0019, 670, 0, -8630, 0)
    SetChrPos(0x0015, 2400, 0, -9100, 0)
    SetChrPos(0x0016, -120, 0, -9870, 0)
    SetChrPos(0x0017, -1110, 0, -8890, 0)
    SetChrPos(0x000B, 1480, 0, -4830, 180)
    SetChrPos(0x000A, -1050, 0, -4440, 180)
    SetChrPos(0x0009, 80, 0, -3240, 180)
    SetChrPos(0x000C, 2650, 0, -3550, 180)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x35),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrDirection(0x0019, 0, 0)
    SetChrDirection(0x0015, 45, 0)
    SetChrDirection(0x0016, 315, 0)
    SetChrDirection(0x0017, 45, 0)
    SetChrPos(0x0102, -12660, 4700, -6310, 90)
    SetChrPos(0x0101, -12650, 4700, -7170, 90)
    OP_66(0x0000)
    CameraMove(1000, 0, -6610, 0)
    OP_67(-26990, 18930, -7100, 0)
    CameraSetDistance(790, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210100918V胜负已分！\n',
            '红之组，克鲁茨小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_66(0x0001)
    CameraMove(-12660, 4700, -6670, 0)
    OP_67(0, 4970, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000C, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010100919V#001F太好了～～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100920V卡露娜姐姐他们真厉害！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100921V#010F嗯，真是精彩的比赛啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100922V军队一方虽然打得也不错，\n',
            '但是进攻配合和角色分工方面\n',
            '和游击士组相比还是差了不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100923V#006F嗯嗯，\n',
            '可以作为我们战斗的参考呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100924V#506F哎呀，该怎么说呢，\n',
            '我身体里武术家的血液已经沸腾起来了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100925V早知道就先不去王城，\n',
            '来这里从头开始看比赛了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100926V#019F哈哈，我很理解你的心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100927V不过如果连这个也忍耐不了的话，\n',
            '就没办法成为独当一面的游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100928V#009F哼，\n',
            '反正我只是个半吊子嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200100929V',
            (TxtCtl.SetColor, 0x5),
            '……接下来\n',
            '要进行的是第八场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100930V',
            (TxtCtl.SetColor, 0x5),
            '这场比赛之后，\n',
            '预选赛就全部结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(1000)

    Fade(1000)
    SetChrPos(0x0102, -12660, 4700, -6310, 90)
    SetChrPos(0x0101, -12650, 4700, -7170, 90)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1000, 0, -6610, 0)
    OP_67(0, 18930, -27990, 0)
    CameraSetDistance(700, 0)
    OP_6C(90000, 0)
    OP_6E(532, 0)
    OP_66(0x0000)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200100905V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100932V',
            (TxtCtl.SetColor, 0x5),
            '『渡鸦帮』所属，\n',
            '贝尔夫选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrPos(0x0011, 2260, 120, -24190, 0)
    SetChrPos(0x0025, 1380, 120, -24190, 0)
    SetChrPos(0x0026, 300, 120, -24190, 0)
    SetChrPos(0x0027, -560, 120, -24190, 0)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    ClearChrFlags(0x0027, 0x0080)
    CameraMove(1200, 0, -21730, 2000)
    OP_70(0x0000, 100)
    OP_73(0x0000)
    Sleep(500)

    PlaySE(175, 0x00, 0x64)

    @scena.Lambda('lambda_2772')
    def lambda_2772():
        ChrWalkTo(0x00FE, -560, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_2772)

    Sleep(50)

    @scena.Lambda('lambda_2792')
    def lambda_2792():
        ChrWalkTo(0x00FE, 1380, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_2792)

    Sleep(50)

    @scena.Lambda('lambda_27B2')
    def lambda_27B2():
        ChrWalkTo(0x00FE, 300, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_27B2)

    @scena.Lambda('lambda_27CD')
    def lambda_27CD():
        ChrWalkTo(0x00FE, 2260, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_27CD)

    CameraMove(1000, 0, -6610, 6000)

    ChrTalk(
        0x0101,
        (
            '#0010100933V#005F那、那些家伙！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100934V#014F是卢安仓库那些流氓的成员。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100935V原来如此，\n',
            '大会对普通人也是开放的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100936V#007F唉，他们是不是来错地方了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100937V这里聚集的都是战斗和武术的高手，\n',
            '那些家伙们怎么可能打得过嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200100910V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100939V',
            (TxtCtl.SetColor, 0x5),
            '来自邻国卡尔瓦德共和国的武术家，\n',
            '金选手单人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010100940V#004F金、金先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100941V#014F又是熟人啊……\n',
            '这世界还真是狭小呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100942V#012F不过，只有一个人出场的话，\n',
            '情况会不会有所不利呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100943V#002F就是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100944V就算对手都是小混混，\n',
            '被包围起来也会很难办的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0008, 2260, 120, 11000, 180)
    ClearChrFlags(0x0008, 0x0080)
    CameraMove(880, 0, 8980, 2000)
    OP_70(0x0001, 100)
    OP_73(0x0001)
    Sleep(500)

    PlaySE(175, 0x00, 0x64)

    @scena.Lambda('lambda_2A88')
    def lambda_2A88():
        ChrWalkTo(0x00FE, 850, 0, -5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2A88)

    CameraMove(1000, 0, -6610, 6000)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200100945V',
            (TxtCtl.SetColor, 0x5),
            '这次的预选赛\n',
            '金选手没有任何队友陪同，\n',
            '所以只有他一个人出场应战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100946V',
            (TxtCtl.SetColor, 0x5),
            '虽然条件对他很不利，\n',
            '但根据他本人的强烈要求，\n',
            '主办方同意在这种情况下进行比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100947V',
            (TxtCtl.SetColor, 0x5),
            '特此声明，请大家理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetChrPos(0x0024, 5550, 0, -6570, 270)
    ChrWalkTo(0x0024, 2900, 0, -6480, 3000, 0x00)

    ChrTalk(
        0x0024,
        (
            '#2210100948V马上开始武术大会\n',
            '预选赛第八场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2C2B')
    def lambda_2C2B():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2C2B')

    DispatchAsync2(0x0011, 0x0001, lambda_2C2B)

    @scena.Lambda('lambda_2C3C')
    def lambda_2C3C():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2C3C')

    DispatchAsync2(0x0025, 0x0001, lambda_2C3C)

    @scena.Lambda('lambda_2C4D')
    def lambda_2C4D():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2C4D')

    DispatchAsync2(0x0026, 0x0001, lambda_2C4D)

    @scena.Lambda('lambda_2C5E')
    def lambda_2C5E():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2C5E')

    DispatchAsync2(0x0027, 0x0001, lambda_2C5E)

    @scena.Lambda('lambda_2C6F')
    def lambda_2C6F():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2C6F)

    Sleep(200)

    @scena.Lambda('lambda_2C8F')
    def lambda_2C8F():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0002, lambda_2C8F)

    @scena.Lambda('lambda_2CAA')
    def lambda_2CAA():
        ChrWalkTo(0x00FE, 2580, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_2CAA)

    @scena.Lambda('lambda_2CC5')
    def lambda_2CC5():
        ChrWalkTo(0x00FE, -350, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0002, lambda_2CC5)

    @scena.Lambda('lambda_2CE0')
    def lambda_2CE0():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_2CE0')

    DispatchAsync2(0x0008, 0x0001, lambda_2CE0)

    @scena.Lambda('lambda_2CF1')
    def lambda_2CF1():
        ChrWalkTo(0x00FE, 760, 0, -700, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2CF1)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    SetChrChipByIndex(0x0011, 29)
    SetChrChipByIndex(0x0025, 29)
    SetChrChipByIndex(0x0026, 29)
    SetChrChipByIndex(0x0027, 29)
    SetChrFlags(0x0011, 0x0002)
    SetChrFlags(0x0025, 0x0002)
    SetChrFlags(0x0026, 0x0002)
    SetChrFlags(0x0027, 0x0002)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x08,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x08,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x08,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 25)
    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0025, 0xFF)
    TerminateThread(0x0026, 0xFF)
    TerminateThread(0x0027, 0xFF)
    TerminateThread(0x0008, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBA, 0x00100003, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x11),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x08,
        (
            (Expr.PushLong, 0x11),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x08,
        (
            (Expr.PushLong, 0x11),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x08,
        (
            (Expr.PushLong, 0x11),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0011, 1870, 0, -9140, 0)
    SetChrPos(0x0025, -60, 0, -9780, 0)
    SetChrPos(0x0026, 1090, 0, -10320, 0)
    SetChrPos(0x0027, 2720, 0, -10150, 0)
    SetChrPos(0x0008, 1120, 0, -4070, 180)
    SetChrPos(0x0102, -12660, 4700, -6310, 90)
    SetChrPos(0x0101, -12650, 4700, -7170, 90)
    OP_66(0x0000)
    CameraMove(1000, 0, -6610, 0)
    OP_67(-26990, 18930, -7100, 0)
    CameraSetDistance(790, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210100952V胜负已分！\n',
            '红之组，金选手胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(176, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_66(0x0001)
    CameraMove(-12660, 4700, -6670, 0)
    OP_67(0, 4970, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0025, 0x0080)
    SetChrFlags(0x0026, 0x0080)
    SetChrFlags(0x0027, 0x0080)
    SetChrFlags(0x0008, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010100953V#001F呀嗬～～～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100954V不愧是金先生，完全一边倒嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100955V#019F看起来我们的担心是多余的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100956V虽然那么巨大的身体，\n',
            '但速度却很快，招式也相当厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100957V#010F不过，我觉得到了正式赛的时候，\n',
            '一对四还是会很困难的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100958V#007F嗯，确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200100959V',
            (TxtCtl.SetColor, 0x5),
            '经过刚才的一番竞逐，\n',
            '预选赛已经全部结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100960V',
            (TxtCtl.SetColor, 0x5),
            '在正式赛里出场的队伍一共八支。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100961V',
            (TxtCtl.SetColor, 0x5),
            '从明天开始连续三天，\n',
            '以淘汰赛的方式决定冠军所属。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200100962V',
            (TxtCtl.SetColor, 0x5),
            '那么最后，\n',
            '请大会的主办者杜南公爵发表致词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_66(0x0001)
    CameraMove(7100, 10100, -6310, 0)
    OP_67(0, 4570, -10000, 0)
    CameraSetDistance(1160, 0)
    OP_6C(306000, 0)
    OP_6E(823, 0)
    SetChrChipByIndex(0x0021, 18)
    SetChrPos(0x0021, 11990, 9750, -6500, 270)
    SetChrPos(0x0020, 14000, 9750, -7520, 270)
    OP_0D()

    ChrTalk(
        0x0021,
        (
            '#0640100963V#225F#2P咳咳！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100964V#220F啊～～各位亲爱的市民，\n',
            '今天特意来看比赛，真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100965V很遗憾，因为我忙于政务，\n',
            '错过了今天前半部分的比赛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100966V#221F不过后半部分的比赛都很精彩，\n',
            '我感到非常的满足，特别的兴奋！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(274, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0021,
        (
            '#0640100967V#225F#2P最近接连发生了恐怖事件，\n',
            '陛下龙体欠佳等不好的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100968V#220F不过，请各位放心！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100969V作为陛下托付政务的本人——\n',
            '杜南·冯·奥赛雷丝，\n',
            '粉身碎骨也要不负各位的期待！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100970V希望借助本次武术大会如此活跃的气氛，\n',
            '能够让大家的心情好起来！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100971V#221F敬请期待明天开始的正式赛！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_66(0x0001)
    CameraMove(-12660, 4700, -6670, 0)
    OP_67(0, 4970, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010100972V#509F这、这段话对那个公爵来说，\n',
            '也太过诚恳了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100973V#015F很可能是情报部的人帮他起草的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_66(0x0001)
    CameraMove(7100, 10100, -6310, 0)
    OP_67(0, 4570, -10000, 0)
    CameraSetDistance(1160, 0)
    OP_6C(306000, 0)
    OP_6E(823, 0)
    SetChrChipByIndex(0x0021, 18)
    SetChrPos(0x0021, 11990, 9750, -6500, 270)
    OP_0D()

    ChrTalk(
        0x0021,
        (
            '#0640100974V#221F#2P哈、哈、哈……哦，对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100975V#220F这次大会的冠军，除了得到奖金以外，\n',
            '我本人还准备了其他丰厚的礼物！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0020, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0020, 0x0021, 400)

    ChrTalk(
        0x0020,
        (
            '#0660100976V#721F（公、公爵大人……\n',
            '　这样做真的妥当吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0021, 0x0020, 400)

    ChrTalk(
        0x0021,
        (
            '#0640100977V#222F#5P（真烦人，给我闭嘴。\n',
            '　这是让大家了解我优点的大好机会。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0021, 270, 400)
    SetChrDirection(0x0020, 270, 400)

    ChrTalk(
        0x0021,
        (
            '#0640100978V#225F#2P这个礼物就是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100979V#224F三天后在格兰赛尔城举行的\n',
            '宫廷晚宴的请柬！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(176, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0021,
        (
            '#0640100980V#221F#2P很遗憾虽然陛下无法出席，\n',
            '不过这可是齐集各界名流的高级晚餐会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100981V还可以品尝到只能由王公贵族享用的，\n',
            '称得上为王国最高级的料理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100982V今天胜出的各位选手，\n',
            '为了得到我的请柬也请加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    FadeOut(1500, 0, -1)
    OP_0D()
    ChrTurnDirection(0x0101, 0x0102, 0)
    ChrTurnDirection(0x0102, 0x0101, 0)
    OP_66(0x0001)
    CameraMove(-12660, 4700, -6880, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2350, 0)
    OP_6C(134000, 0)
    OP_6E(261, 0)
    OP_23(0x00AE)
    Sleep(3000)

    SetChrFlags(0x0053, 0x0080)
    SetChrFlags(0x0054, 0x0080)
    SetChrFlags(0x0055, 0x0080)
    SetChrFlags(0x0056, 0x0080)
    SetChrFlags(0x0057, 0x0080)
    SetChrFlags(0x0058, 0x0080)
    SetChrFlags(0x0059, 0x0080)
    SetChrFlags(0x005A, 0x0080)
    SetChrFlags(0x005B, 0x0080)
    SetChrFlags(0x005C, 0x0080)
    SetChrFlags(0x005D, 0x0080)
    SetChrFlags(0x005E, 0x0080)
    SetChrFlags(0x005F, 0x0080)
    SetChrFlags(0x0060, 0x0080)
    SetChrFlags(0x0061, 0x0080)
    SetChrFlags(0x0062, 0x0080)
    SetChrFlags(0x0063, 0x0080)
    SetChrFlags(0x0064, 0x0080)
    SetChrFlags(0x0065, 0x0080)
    SetChrFlags(0x0066, 0x0080)
    SetChrFlags(0x0067, 0x0080)
    SetChrFlags(0x0068, 0x0080)
    SetChrFlags(0x0069, 0x0080)
    SetChrFlags(0x006A, 0x0080)
    SetChrFlags(0x006B, 0x0080)
    SetChrFlags(0x006C, 0x0080)
    SetChrFlags(0x006D, 0x0080)
    SetChrFlags(0x006E, 0x0080)
    SetChrFlags(0x006F, 0x0080)
    SetChrFlags(0x0070, 0x0080)
    SetChrFlags(0x0071, 0x0080)
    SetChrFlags(0x0072, 0x0080)
    SetChrFlags(0x0073, 0x0080)
    SetChrFlags(0x0074, 0x0080)
    SetChrFlags(0x0075, 0x0080)
    SetChrFlags(0x0030, 0x0080)
    SetChrFlags(0x0031, 0x0080)
    SetChrFlags(0x0032, 0x0080)
    SetChrFlags(0x0033, 0x0080)
    SetChrFlags(0x0034, 0x0080)
    SetChrFlags(0x0035, 0x0080)
    SetChrFlags(0x0036, 0x0080)
    SetChrFlags(0x0037, 0x0080)
    SetChrFlags(0x0038, 0x0080)
    SetChrFlags(0x0039, 0x0080)
    SetChrFlags(0x003A, 0x0080)
    SetChrFlags(0x003B, 0x0080)
    SetChrFlags(0x003C, 0x0080)
    SetChrFlags(0x003D, 0x0080)
    SetChrFlags(0x003E, 0x0080)
    SetChrFlags(0x003F, 0x0080)
    SetChrFlags(0x0040, 0x0080)
    SetChrFlags(0x0041, 0x0080)
    SetChrFlags(0x0042, 0x0080)
    SetChrFlags(0x0043, 0x0080)
    SetChrFlags(0x0044, 0x0080)
    SetChrFlags(0x0045, 0x0080)
    SetChrFlags(0x0046, 0x0080)
    SetChrFlags(0x0047, 0x0080)
    SetChrFlags(0x0048, 0x0080)
    SetChrFlags(0x0049, 0x0080)
    SetChrFlags(0x004A, 0x0080)
    SetChrFlags(0x004B, 0x0080)
    SetChrFlags(0x004C, 0x0080)
    SetChrFlags(0x004D, 0x0080)
    SetChrFlags(0x004E, 0x0080)
    SetChrFlags(0x004F, 0x0080)
    SetChrFlags(0x0050, 0x0080)
    SetChrFlags(0x0051, 0x0080)
    SetChrFlags(0x0052, 0x0080)
    SetChrFlags(0x0076, 0x0080)
    SetChrFlags(0x0077, 0x0080)
    SetChrFlags(0x0078, 0x0080)
    SetChrFlags(0x0079, 0x0080)
    SetChrFlags(0x007A, 0x0080)
    SetChrFlags(0x007B, 0x0080)
    SetChrFlags(0x007C, 0x0080)
    SetChrFlags(0x007D, 0x0080)
    SetChrFlags(0x007E, 0x0080)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010100983V#003F喂，约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100984V不如我们去找卡露娜姐姐他们吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100985V#015F嗯，我也是这么想的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100986V如果他们能够获胜，\n',
            '就可以堂堂正正地进入格兰赛尔城了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100987V借此良机，\n',
            '能把那件事传达给女王也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100988V#010F你是这个意思吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100989V#003F嗯……虽然我不太情愿\n',
            '把博士的委托交给别人去做……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100990V不过这可不是固执的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100991V#010F我没什么意见哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100992V他们可能还没回去，\n',
            '我们去选手休息室看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100993V#000F嗯，好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100994V嗯……刚才卡露娜姐姐他们\n',
            '好像是从北边的大门出去的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100995V#010F嗯，如果在的话，\n',
            '肯定是在北边的休息室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00C1, 6, 0x60E))
    SetScenaFlags(ScenaFlag(0x00C1, 7, 0x60F))
    OP_28(0x0045, 0x01, 0x1000)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x3C46
@scena.Code('func_03_3C46')
def func_03_3C46():
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)
    SetChrPos(0x002A, -12650, 4700, -3680, 90)
    SetChrPos(0x0053, -12650, 4700, -16700, 90)
    SetChrPos(0x005E, -12650, 4700, -14700, 90)
    SetChrPos(0x006A, -13730, 4950, -16780, 90)
    SetChrPos(0x0074, -12660, 4700, -15720, 90)
    SetChrPos(0x006F, -14780, 5200, 3980, 90)
    SetChrPos(0x005D, -13830, 4950, -15790, 90)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0108, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    ChrSetRGBAMask(0x0021, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0020, 255, 255, 255, 0, 0)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    SetChrFlags(0x0021, 0x0004)
    SetChrFlags(0x0020, 0x0004)
    SetChrPos(0x0021, 19870, 9500, -6460, 270)
    SetChrPos(0x0020, 20800, 9500, -5950, 270)
    CameraMove(-9450, 0, -6730, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(500, 0)

    @scena.Lambda('lambda_3D67')
    def lambda_3D67():
        OP_6E(339, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3D67)

    @scena.Lambda('lambda_3D77')
    def lambda_3D77():
        OP_6C(90000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3D77)

    @scena.Lambda('lambda_3D87')
    def lambda_3D87():
        CameraMove(13540, 9750, -6540, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3D87)

    FadeIn(2000, 0)
    Sleep(3500)

    SetChrPos(0x0030, 14650, 4700, 250, 270)
    SetChrPos(0x0031, 15730, 4950, 250, 270)
    SetChrPos(0x0032, 16860, 5200, 250, 270)
    SetChrPos(0x0033, 17850, 5450, 250, 270)
    SetChrPos(0x0034, 18880, 5700, 250, 270)
    SetChrPos(0x0035, 19640, 5950, 250, 270)
    SetChrPos(0x0036, 14650, 4700, 1200, 270)
    SetChrPos(0x0037, 15730, 4950, 1200, 270)
    SetChrPos(0x0038, 16860, 5200, 1200, 270)
    SetChrPos(0x0039, 17850, 5450, 1200, 270)
    SetChrPos(0x003A, 18880, 5700, 1200, 270)
    SetChrPos(0x003B, 19640, 5950, 1200, 270)
    SetChrPos(0x003C, 14650, 4700, 2390, 270)
    SetChrPos(0x003D, 15730, 4950, 2390, 270)
    SetChrPos(0x003E, 16860, 5200, 2390, 270)
    SetChrPos(0x003F, 17850, 5450, 2390, 270)
    SetChrPos(0x0040, 18880, 5700, 2390, 270)
    SetChrPos(0x0041, 19640, 5950, 2390, 270)
    SetChrPos(0x0042, 14650, 4700, 3550, 270)
    SetChrPos(0x0043, 15730, 4950, 3550, 270)
    SetChrPos(0x0044, 16860, 5200, 3550, 270)
    SetChrPos(0x0045, 17850, 5450, 3550, 270)
    SetChrPos(0x0046, 18880, 5700, 3550, 270)
    SetChrPos(0x0047, 19640, 5950, 3550, 270)
    SetChrPos(0x0048, 14650, 4700, 4830, 270)
    SetChrPos(0x0049, 15730, 4950, 4830, 270)
    SetChrPos(0x004A, 16860, 5200, 4830, 270)
    SetChrPos(0x004B, 17850, 5450, 4830, 270)
    SetChrPos(0x004C, 18880, 5700, 4830, 270)
    SetChrPos(0x004D, 19640, 5950, 4830, 270)
    SetChrPos(0x004E, 14650, 4700, -13300, 270)
    SetChrPos(0x004F, 15730, 4950, -13300, 270)
    SetChrPos(0x0050, 16860, 5200, -13300, 270)
    SetChrPos(0x0051, 17850, 5450, -13300, 270)
    SetChrPos(0x0052, 18880, 5700, -13300, 270)
    SetChrPos(0x0053, 19640, 5950, -13300, 270)
    SetChrPos(0x0054, 14650, 4700, -14500, 270)
    SetChrPos(0x0055, 15730, 4950, -14500, 270)
    SetChrPos(0x0056, 16860, 5200, -14500, 270)
    SetChrPos(0x0057, 17850, 5450, -14500, 270)
    SetChrPos(0x0058, 18880, 5700, -14500, 270)
    SetChrPos(0x0059, 19640, 5950, -14500, 270)
    SetChrPos(0x005A, 14650, 4700, -15600, 270)
    SetChrPos(0x005B, 15730, 4950, -15600, 270)
    SetChrPos(0x005C, 16860, 5200, -15600, 270)
    SetChrPos(0x005D, 17850, 5450, -15600, 270)
    SetChrPos(0x005E, 18880, 5700, -15600, 270)
    SetChrPos(0x005F, 19640, 5950, -15600, 270)
    SetChrPos(0x0060, 14650, 4700, -16920, 270)
    SetChrPos(0x0061, 15730, 4950, -16920, 270)
    SetChrPos(0x0062, 16860, 5200, -16920, 270)
    SetChrPos(0x0063, 17850, 5450, -16920, 270)
    SetChrPos(0x0064, 18880, 5700, -16920, 270)
    SetChrPos(0x0065, 19640, 5950, -16920, 270)
    SetChrPos(0x0066, 14650, 4700, -18030, 270)
    SetChrPos(0x0067, 15730, 4950, -18030, 270)
    SetChrPos(0x0068, 16860, 5200, -18030, 270)
    SetChrPos(0x0069, 17850, 5450, -18030, 270)
    SetChrPos(0x006A, 18880, 5700, -18030, 270)
    SetChrPos(0x006B, 19640, 5950, -18030, 270)
    Sleep(6000)

    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 60)
    Sleep(1000)

    @scena.Lambda('lambda_41C6')
    def lambda_41C6():
        ChrWalkTo(0x00FE, 10890, 9500, -6410, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_41C6)

    @scena.Lambda('lambda_41E1')
    def lambda_41E1():
        ChrWalkTo(0x00FE, 10890, 9500, -6410, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_41E1)

    @scena.Lambda('lambda_41FC')
    def lambda_41FC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0021, 0x0002, lambda_41FC)

    @scena.Lambda('lambda_420E')
    def lambda_420E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_420E)

    Sleep(500)

    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x4237
@scena.Code('func_04_4237')
def func_04_4237():
    EventBegin(0x00)
    PlaySE(174, 0x00, 0x64)
    FormationAddMember(0x01, 0xFF)
    FormationAddMember(0x03, 0xFF)
    FormationAddMember(0x07, 0xFF)
    CameraMove(810, 0, -6480, 0)
    OP_67(0, 15230, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(269000, 0)
    OP_6E(96, 0)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, -4240, 0, -6480, 0)

    @scena.Lambda('lambda_42A0')
    def lambda_42A0():
        OP_6C(90000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_42A0)

    @scena.Lambda('lambda_42B0')
    def lambda_42B0():
        OP_6E(524, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_42B0)

    @scena.Lambda('lambda_42C0')
    def lambda_42C0():
        OP_67(0, 8010, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_42C0)

    @scena.Lambda('lambda_42D8')
    def lambda_42D8():
        ChrWalkTo(0x00FE, 5940, 0, -6480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_42D8)

    WaitForThreadExit(0x0024, 0x0001)
    SetChrDirection(0x0024, 270, 400)
    WaitForThreadExit(0x0101, 0x0002)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200110182V',
            (TxtCtl.SetColor, 0x5),
            '那么接下来，\n',
            '我们马上来公布\n',
            '有幸参加揭幕战的小组吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110183V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组——\n',
            '游击士协会格兰赛尔支部，\n',
            '克鲁茨选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110184V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组——\n',
            '王国军突击骑兵队所属，\n',
            '杰多中尉等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x43F7
@scena.Code('func_05_43F7')
def func_05_43F7():
    EventBegin(0x00)
    PlaySE(174, 0x00, 0x64)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0019, 2260, 0, -5460, 180)
    SetChrPos(0x0015, 300, 0, -5460, 180)
    SetChrPos(0x0016, -560, 0, -5460, 180)
    SetChrPos(0x0017, 1380, 0, -5460, 180)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0009, 2260, 0, -7590, 0)
    SetChrPos(0x000B, 1380, 0, -7590, 0)
    SetChrPos(0x000C, 300, 0, -7590, 0)
    SetChrPos(0x000A, -560, 0, -7590, 0)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210110191V马上开始武术大会\n',
            '正式赛第一场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x0019, 0x0040)
    SetChrFlags(0x0017, 0x0040)
    SetChrFlags(0x0015, 0x0040)
    SetChrFlags(0x0016, 0x0040)

    @scena.Lambda('lambda_458E')
    def lambda_458E():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_458E')

    DispatchAsync2(0x000B, 0x0001, lambda_458E)

    @scena.Lambda('lambda_459F')
    def lambda_459F():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_459F')

    DispatchAsync2(0x000A, 0x0001, lambda_459F)

    @scena.Lambda('lambda_45B0')
    def lambda_45B0():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_45B0')

    DispatchAsync2(0x0009, 0x0001, lambda_45B0)

    @scena.Lambda('lambda_45C1')
    def lambda_45C1():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_45C1')

    DispatchAsync2(0x000C, 0x0001, lambda_45C1)

    @scena.Lambda('lambda_45D2')
    def lambda_45D2():
        ChrWalkTo(0x00FE, 2350, 0, -13170, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_45D2)

    Sleep(100)

    @scena.Lambda('lambda_45F2')
    def lambda_45F2():
        ChrWalkTo(0x00FE, -170, 0, -13170, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_45F2)

    Sleep(200)

    @scena.Lambda('lambda_4612')
    def lambda_4612():
        ChrWalkTo(0x00FE, 1570, 0, -11430, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_4612)

    @scena.Lambda('lambda_462D')
    def lambda_462D():
        ChrWalkTo(0x00FE, 390, 0, -11390, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_462D)

    @scena.Lambda('lambda_4648')
    def lambda_4648():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_4648')

    DispatchAsync2(0x0019, 0x0001, lambda_4648)

    @scena.Lambda('lambda_4659')
    def lambda_4659():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_4659')

    DispatchAsync2(0x0017, 0x0001, lambda_4659)

    @scena.Lambda('lambda_466A')
    def lambda_466A():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_466A')

    DispatchAsync2(0x0015, 0x0001, lambda_466A)

    @scena.Lambda('lambda_467B')
    def lambda_467B():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_467B')

    DispatchAsync2(0x0016, 0x0001, lambda_467B)

    @scena.Lambda('lambda_468C')
    def lambda_468C():
        ChrWalkTo(0x00FE, 1080, 0, 680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_468C)

    Sleep(200)

    @scena.Lambda('lambda_46AC')
    def lambda_46AC():
        ChrWalkTo(0x00FE, -310, 0, -290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_46AC)

    Sleep(100)

    @scena.Lambda('lambda_46CC')
    def lambda_46CC():
        ChrWalkTo(0x00FE, 2670, 0, -320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_46CC)

    Sleep(200)

    @scena.Lambda('lambda_46EC')
    def lambda_46EC():
        ChrWalkTo(0x00FE, 1080, 0, -1960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_46EC)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    SetChrChipByIndex(0x0019, 29)
    SetChrChipByIndex(0x0015, 29)
    SetChrChipByIndex(0x0016, 29)
    SetChrChipByIndex(0x0017, 29)
    SetChrFlags(0x0019, 0x0002)
    SetChrFlags(0x0015, 0x0002)
    SetChrFlags(0x0016, 0x0002)
    SetChrFlags(0x0017, 0x0002)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x36),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x32),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x32),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x32),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000B, 29)
    SetChrChipByIndex(0x000A, 29)
    SetChrChipByIndex(0x0009, 29)
    SetChrChipByIndex(0x000C, 29)
    SetChrFlags(0x000B, 0x0002)
    SetChrFlags(0x000A, 0x0002)
    SetChrFlags(0x0009, 0x0002)
    SetChrFlags(0x000C, 0x0002)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000C, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBB, 0x00100004, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x37),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x33),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x33),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x33),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x000B, 1570, 0, -9320, 0)
    SetChrPos(0x000A, -10, 0, -9870, 0)
    SetChrPos(0x0009, 2360, 0, -10500, 0)
    SetChrPos(0x000C, -1470, 0, -9110, 0)
    SetChrPos(0x0019, 1690, 0, -4090, 180)
    SetChrPos(0x0015, 20, 0, -3980, 180)
    SetChrPos(0x0016, 2390, 0, -2970, 180)
    SetChrPos(0x0017, -970, 0, -2780, 180)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110195V胜负已分！\n',
            '苍之组，克鲁茨小组获胜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x49A0
@scena.Code('func_06_49A0')
def func_06_49A0():
    EventBegin(0x00)
    PlaySE(174, 0x00, 0x64)
    SetMapFlags(0x00100000)
    OP_66(0x0000)
    CameraMove(1450, 0, -21650, 0)
    OP_67(-6800, 5030, -14300, 0)
    CameraSetDistance(1530, 0)
    OP_6C(229000, 0)
    OP_6E(733, 0)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 5550, 0, -6570, 270)
    SetChrPos(0x0011, 2260, 0, -5460, 180)
    SetChrPos(0x0013, 300, 0, -5460, 180)
    SetChrPos(0x0014, -560, 0, -5460, 180)
    SetChrPos(0x0012, 1380, 0, -5460, 180)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    FadeIn(2000, 0)
    SetChrPos(0x0108, 2260, 0, -24190, 0)
    SetChrPos(0x0101, 1380, 0, -24190, 0)
    SetChrPos(0x0102, 300, 0, -24190, 0)
    SetChrPos(0x0104, -560, 0, -24190, 0)
    OP_70(0x0000, 100)
    OP_73(0x0000)
    OP_66(0x0000)

    @scena.Lambda('lambda_4ABA')
    def lambda_4ABA():
        CameraMove(1160, 0, -6810, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4ABA)

    Sleep(500)

    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)

    @scena.Lambda('lambda_4AE1')
    def lambda_4AE1():
        ChrWalkTo(0x00FE, 2260, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_4AE1)

    Sleep(300)

    @scena.Lambda('lambda_4B01')
    def lambda_4B01():
        ChrWalkTo(0x00FE, -560, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_4B01)

    Sleep(50)

    @scena.Lambda('lambda_4B21')
    def lambda_4B21():
        ChrWalkTo(0x00FE, 1380, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4B21)

    Sleep(50)

    @scena.Lambda('lambda_4B41')
    def lambda_4B41():
        ChrWalkTo(0x00FE, 300, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4B41)

    Sleep(6000)

    OP_66(0x0001)
    Fade(1000)
    CameraMove(1130, 0, -6520, 0)
    OP_67(0, 5770, -10000, 0)
    CameraSetDistance(3320, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0012,
        (
            '#0450110212V嘿嘿……\n',
            '这么快复仇的机会就来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0470110213V偶尔女神也会\n',
            '照顾我们一次嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0460110214V#6P之前发生的事情，\n',
            '让我们认识到自己的力量太弱小了，\n',
            '因此我们进行了地狱般的特训……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0460110215V#6P就让你们看看我们的修炼成果吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110216V#006F哼哼，这种劲头很好嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110217V我们也会拼尽全力，\n',
            '决不会手下留情的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110218V#031F#2P（呵呵，艾丝蒂尔今天怎么这么来劲呢，\n',
            '　真是难得一见哦。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110219V（该说她是假小子呢还是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110220V#017F（这句话被艾丝蒂尔听见的话，\n',
            '　你肯定又会挨打的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110221V#070F#2P那么，也差不多该开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210110222V马上开始武术大会\n',
            '正式赛第二场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    SetChrFlags(0x0108, 0x0040)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0102, 0x0040)
    SetChrFlags(0x0104, 0x0040)
    SetChrFlags(0x0012, 0x0040)
    SetChrFlags(0x0013, 0x0040)
    SetChrFlags(0x0014, 0x0040)
    SetChrFlags(0x0011, 0x0040)

    @scena.Lambda('lambda_4E93')
    def lambda_4E93():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_4E93')

    DispatchAsync2(0x0108, 0x0001, lambda_4E93)

    @scena.Lambda('lambda_4EA4')
    def lambda_4EA4():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_4EA4')

    DispatchAsync2(0x0101, 0x0001, lambda_4EA4)

    @scena.Lambda('lambda_4EB5')
    def lambda_4EB5():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_4EB5')

    DispatchAsync2(0x0102, 0x0001, lambda_4EB5)

    @scena.Lambda('lambda_4EC6')
    def lambda_4EC6():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_4EC6')

    DispatchAsync2(0x0104, 0x0001, lambda_4EC6)

    @scena.Lambda('lambda_4ED7')
    def lambda_4ED7():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_4ED7)

    Sleep(200)

    @scena.Lambda('lambda_4EF7')
    def lambda_4EF7():
        ChrWalkTo(0x00FE, 2580, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_4EF7)

    @scena.Lambda('lambda_4F12')
    def lambda_4F12():
        ChrWalkTo(0x00FE, -350, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_4F12)

    Sleep(200)

    @scena.Lambda('lambda_4F32')
    def lambda_4F32():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4F32)

    @scena.Lambda('lambda_4F4D')
    def lambda_4F4D():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4F4D')

    DispatchAsync2(0x0012, 0x0001, lambda_4F4D)

    @scena.Lambda('lambda_4F5E')
    def lambda_4F5E():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4F5E')

    DispatchAsync2(0x0013, 0x0001, lambda_4F5E)

    @scena.Lambda('lambda_4F6F')
    def lambda_4F6F():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4F6F')

    DispatchAsync2(0x0014, 0x0001, lambda_4F6F)

    @scena.Lambda('lambda_4F80')
    def lambda_4F80():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4F80')

    DispatchAsync2(0x0011, 0x0001, lambda_4F80)

    @scena.Lambda('lambda_4F91')
    def lambda_4F91():
        ChrWalkTo(0x00FE, 1080, 0, 680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_4F91)

    Sleep(200)

    @scena.Lambda('lambda_4FB1')
    def lambda_4FB1():
        ChrWalkTo(0x00FE, -310, 0, -800, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_4FB1)

    @scena.Lambda('lambda_4FCC')
    def lambda_4FCC():
        ChrWalkTo(0x00FE, 2670, 0, -800, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_4FCC)

    Sleep(200)

    @scena.Lambda('lambda_4FEC')
    def lambda_4FEC():
        ChrWalkTo(0x00FE, 1080, 0, -1960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_4FEC)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    SetChrChipByIndex(0x0012, 29)
    SetChrChipByIndex(0x0013, 29)
    SetChrChipByIndex(0x0014, 29)
    SetChrChipByIndex(0x0011, 29)
    SetChrFlags(0x0012, 0x0002)
    SetChrFlags(0x0013, 0x0002)
    SetChrFlags(0x0014, 0x0002)
    SetChrFlags(0x0011, 0x0002)

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x16),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x08,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x08,
        (
            (Expr.PushLong, 0x1E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x12),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0108, 25)
    SetChrChipByIndex(0x0101, 22)
    SetChrChipByIndex(0x0102, 23)
    SetChrChipByIndex(0x0104, 24)
    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0104, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x0000039D, 0x00000000, 0x00, 0x0000, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x17),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x08,
        (
            (Expr.PushLong, 0x1B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x08,
        (
            (Expr.PushLong, 0x1F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x13),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0101, 1100, 0, -8740, 0)
    SetChrPos(0x0102, -160, 0, -9400, 0)
    SetChrPos(0x0108, 2380, 0, -9800, 0)
    SetChrPos(0x0104, 1070, 0, -10590, 0)
    SetChrPos(0x0012, 1830, 0, -3910, 180)
    SetChrPos(0x0013, 900, 0, -2670, 180)
    SetChrPos(0x0014, 320, 0, -3480, 180)
    SetChrPos(0x0011, 2610, 0, -2850, 180)
    OP_66(0x0000)
    CameraMove(2410, 0, -7040, 0)
    OP_67(-26990, 18930, -7100, 0)
    CameraSetDistance(660, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110226V胜负已分！\n',
            '苍之组，金小组获胜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0012,
        (
            '#0450110227V#5P哈啊……哈啊……\n',
            '最后还是输了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0470110228V#5P真、真是厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0460110229V#5P可恶，可恶可恶可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110230V#506F#2P好啦好啦……\n',
            '不要那么沮丧嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110231V#006F说实话，我真是吃了一惊呢。\n',
            '你们现在居然能变得这么强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110232V#010F#2P我也这么觉得。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110233V比在灯塔交手的时候要强得多了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0450110234V#5P是、是吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0470110235V#5P那个时候的事情，\n',
            '我们已经不太记得了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110236V#071F#2P虽然我不太明白是怎么一回事，\n',
            '不过我们都已拼尽全力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110237V大家就挺起胸膛回休息室去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 6, 0x3FE))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x5467
@scena.Code('func_07_5467')
def func_07_5467():
    EventBegin(0x00)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0019, 2260, 0, -7590, 0)
    SetChrPos(0x0015, 300, 0, -7590, 0)
    SetChrPos(0x0016, -560, 0, -7590, 0)
    SetChrPos(0x0017, 1380, 0, -7590, 0)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1000, 0, -6610, 0)
    OP_67(0, 18930, -27990, 0)
    CameraSetDistance(700, 0)
    OP_6C(90000, 0)
    OP_6E(532, 0)
    OP_66(0x0000)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0108, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    SetChrPos(0x000D, 2260, 120, 11000, 180)
    SetChrPos(0x000E, 1380, 120, 11000, 180)
    SetChrPos(0x000F, 300, 120, 11000, 180)
    SetChrPos(0x0010, -560, 120, 11000, 180)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    CameraMove(880, 0, 8980, 2000)
    OP_70(0x0001, 100)
    OP_73(0x0001)
    Sleep(500)

    PlaySE(176, 0x00, 0x64)

    @scena.Lambda('lambda_55AE')
    def lambda_55AE():
        ChrWalkTo(0x00FE, 1380, 0, -5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_55AE)

    Sleep(50)

    @scena.Lambda('lambda_55CE')
    def lambda_55CE():
        ChrWalkTo(0x00FE, -560, 0, -5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_55CE)

    Sleep(50)

    @scena.Lambda('lambda_55EE')
    def lambda_55EE():
        ChrWalkTo(0x00FE, 300, 0, -5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_55EE)

    Sleep(50)

    @scena.Lambda('lambda_560E')
    def lambda_560E():
        ChrWalkTo(0x00FE, 2260, 0, -5500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_560E)

    @scena.Lambda('lambda_5629')
    def lambda_5629():
        CameraMove(1000, 0, -6610, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5629)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200110259V',
            (TxtCtl.SetColor, 0x5),
            '嗯，那个……\n',
            '我来说明一下这件事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110260V',
            (TxtCtl.SetColor, 0x5),
            '我想很多人也知道，\n',
            '他们是曾在柏斯地区作乱的\n',
            '空贼团『卡普亚一家』的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110261V',
            (TxtCtl.SetColor, 0x5),
            '他们希望能堂堂正正地战斗，\n',
            '给武术大会增添热闹的气氛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110262V',
            (TxtCtl.SetColor, 0x5),
            '同时也是为了向\n',
            '曾经受过困扰的王国人民谢罪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110263V',
            (TxtCtl.SetColor, 0x5),
            '为了这个目的，\n',
            '他们强烈希望参加这次的武术大会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110264V',
            (TxtCtl.SetColor, 0x5),
            '因为在服刑期间态度良好，\n',
            '又得到了主办者杜南公爵的同意，\n',
            '所以他们今天得以在这里出场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110265V',
            (TxtCtl.SetColor, 0x5),
            '请大家给予理解和支持。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x5839
@scena.Code('func_08_5839')
def func_08_5839():
    EventBegin(0x00)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0108, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x0019, 2260, 0, -7590, 0)
    SetChrPos(0x0015, 1380, 0, -7590, 0)
    SetChrPos(0x0016, 300, 0, -7590, 0)
    SetChrPos(0x0017, -560, 0, -7590, 0)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x000D, 2260, 0, -5460, 180)
    SetChrPos(0x000F, 300, 0, -5460, 180)
    SetChrPos(0x0010, -560, 0, -5460, 180)
    SetChrPos(0x000E, 1380, 0, -5460, 180)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110271V各位，请安静！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210110272V马上开始武术大会\n',
            '正式赛第三场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000E, 0x0040)
    SetChrFlags(0x000F, 0x0040)
    SetChrFlags(0x0010, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x0019, 0x0040)
    SetChrFlags(0x0017, 0x0040)
    SetChrFlags(0x0015, 0x0040)
    SetChrFlags(0x0016, 0x0040)

    @scena.Lambda('lambda_59FF')
    def lambda_59FF():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_59FF')

    DispatchAsync2(0x000E, 0x0001, lambda_59FF)

    @scena.Lambda('lambda_5A10')
    def lambda_5A10():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_5A10')

    DispatchAsync2(0x000F, 0x0001, lambda_5A10)

    @scena.Lambda('lambda_5A21')
    def lambda_5A21():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_5A21')

    DispatchAsync2(0x0010, 0x0001, lambda_5A21)

    @scena.Lambda('lambda_5A32')
    def lambda_5A32():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_5A32')

    DispatchAsync2(0x000D, 0x0001, lambda_5A32)

    @scena.Lambda('lambda_5A43')
    def lambda_5A43():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_5A43)

    Sleep(200)

    @scena.Lambda('lambda_5A63')
    def lambda_5A63():
        ChrWalkTo(0x00FE, 2580, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_5A63)

    @scena.Lambda('lambda_5A7E')
    def lambda_5A7E():
        ChrWalkTo(0x00FE, -350, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_5A7E)

    Sleep(200)

    @scena.Lambda('lambda_5A9E')
    def lambda_5A9E():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_5A9E)

    @scena.Lambda('lambda_5AB9')
    def lambda_5AB9():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_5AB9')

    DispatchAsync2(0x0019, 0x0001, lambda_5AB9)

    @scena.Lambda('lambda_5ACA')
    def lambda_5ACA():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_5ACA')

    DispatchAsync2(0x0017, 0x0001, lambda_5ACA)

    @scena.Lambda('lambda_5ADB')
    def lambda_5ADB():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_5ADB')

    DispatchAsync2(0x0015, 0x0001, lambda_5ADB)

    @scena.Lambda('lambda_5AEC')
    def lambda_5AEC():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_5AEC')

    DispatchAsync2(0x0016, 0x0001, lambda_5AEC)

    @scena.Lambda('lambda_5AFD')
    def lambda_5AFD():
        ChrWalkTo(0x00FE, 2260, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_5AFD)

    @scena.Lambda('lambda_5B18')
    def lambda_5B18():
        ChrWalkTo(0x00FE, -560, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_5B18)

    Sleep(200)

    @scena.Lambda('lambda_5B38')
    def lambda_5B38():
        ChrWalkTo(0x00FE, 390, 0, -1720, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_5B38)

    @scena.Lambda('lambda_5B53')
    def lambda_5B53():
        ChrWalkTo(0x00FE, 1430, 0, -1790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_5B53)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    SetChrChipByIndex(0x0019, 29)
    SetChrChipByIndex(0x0015, 29)
    SetChrChipByIndex(0x0016, 29)
    SetChrChipByIndex(0x0017, 29)
    SetChrFlags(0x0019, 0x0002)
    SetChrFlags(0x0015, 0x0002)
    SetChrFlags(0x0016, 0x0002)
    SetChrFlags(0x0017, 0x0002)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x34),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000E, 29)
    SetChrChipByIndex(0x000F, 29)
    SetChrChipByIndex(0x0010, 29)
    SetChrChipByIndex(0x000D, 29)
    SetChrFlags(0x000E, 0x0002)
    SetChrFlags(0x000F, 0x0002)
    SetChrFlags(0x0010, 0x0002)
    SetChrFlags(0x000D, 0x0002)

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x2A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x26),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x22),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x000D, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBC, 0x00100005, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x35),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0019, 1260, 0, -8950, 0)
    SetChrPos(0x0015, 320, 0, -9900, 0)
    SetChrPos(0x0016, 2130, 0, -10270, 0)
    SetChrPos(0x0017, 2940, 0, -9340, 0)
    SetChrPos(0x000E, 40, 0, -2660, 180)
    SetChrPos(0x000F, 1100, 0, -3990, 180)
    SetChrPos(0x0010, 2230, 0, -2600, 180)
    SetChrPos(0x000D, 2040, 0, -3690, 180)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110276V胜负已分！\n',
            '红之组，多伦小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x5E05
@scena.Code('func_09_5E05')
def func_09_5E05():
    EventBegin(0x00)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x001C, 2260, 0, -5460, 180)
    SetChrPos(0x001D, 300, 0, -5460, 180)
    SetChrPos(0x001E, -560, 0, -5460, 180)
    SetChrPos(0x001F, 1380, 0, -5460, 180)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0019, 2260, 0, -7590, 0)
    SetChrPos(0x0015, 1380, 0, -7590, 0)
    SetChrPos(0x0016, 300, 0, -7590, 0)
    SetChrPos(0x0017, -560, 0, -7590, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110303V马上开始武术大会\n',
            '正式赛第四场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0019, 0x0040)
    SetChrFlags(0x0015, 0x0040)
    SetChrFlags(0x0016, 0x0040)
    SetChrFlags(0x0017, 0x0040)
    SetChrFlags(0x001C, 0x0040)
    SetChrFlags(0x001D, 0x0040)
    SetChrFlags(0x001E, 0x0040)
    SetChrFlags(0x001F, 0x0040)

    @scena.Lambda('lambda_5F9C')
    def lambda_5F9C():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_5F9C')

    DispatchAsync2(0x0019, 0x0001, lambda_5F9C)

    @scena.Lambda('lambda_5FAD')
    def lambda_5FAD():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_5FAD')

    DispatchAsync2(0x0015, 0x0001, lambda_5FAD)

    @scena.Lambda('lambda_5FBE')
    def lambda_5FBE():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_5FBE')

    DispatchAsync2(0x0016, 0x0001, lambda_5FBE)

    @scena.Lambda('lambda_5FCF')
    def lambda_5FCF():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_5FCF')

    DispatchAsync2(0x0017, 0x0001, lambda_5FCF)

    @scena.Lambda('lambda_5FE0')
    def lambda_5FE0():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_5FE0)

    Sleep(200)

    @scena.Lambda('lambda_6000')
    def lambda_6000():
        ChrWalkTo(0x00FE, 2580, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_6000)

    @scena.Lambda('lambda_601B')
    def lambda_601B():
        ChrWalkTo(0x00FE, -350, 0, -12760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_601B)

    Sleep(200)

    @scena.Lambda('lambda_603B')
    def lambda_603B():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_603B)

    @scena.Lambda('lambda_6056')
    def lambda_6056():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_6056')

    DispatchAsync2(0x001C, 0x0001, lambda_6056)

    @scena.Lambda('lambda_6067')
    def lambda_6067():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_6067')

    DispatchAsync2(0x001D, 0x0001, lambda_6067)

    @scena.Lambda('lambda_6078')
    def lambda_6078():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_6078')

    DispatchAsync2(0x001E, 0x0001, lambda_6078)

    @scena.Lambda('lambda_6089')
    def lambda_6089():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_6089')

    DispatchAsync2(0x001F, 0x0001, lambda_6089)

    @scena.Lambda('lambda_609A')
    def lambda_609A():
        ChrWalkTo(0x00FE, 1080, 0, 680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_609A)

    Sleep(200)

    @scena.Lambda('lambda_60BA')
    def lambda_60BA():
        ChrWalkTo(0x00FE, -310, 0, -290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0002, lambda_60BA)

    @scena.Lambda('lambda_60D5')
    def lambda_60D5():
        ChrWalkTo(0x00FE, 2670, 0, -320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_60D5)

    Sleep(200)

    @scena.Lambda('lambda_60F5')
    def lambda_60F5():
        ChrWalkTo(0x00FE, 1080, 0, -1960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_60F5)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    SetChrChipByIndex(0x0019, 29)
    SetChrChipByIndex(0x0015, 29)
    SetChrChipByIndex(0x0016, 29)
    SetChrChipByIndex(0x0017, 29)
    SetChrFlags(0x0019, 0x0002)
    SetChrFlags(0x0015, 0x0002)
    SetChrFlags(0x0016, 0x0002)
    SetChrFlags(0x0017, 0x0002)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x34),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x001C, 29)
    SetChrChipByIndex(0x001D, 29)
    SetChrChipByIndex(0x001E, 29)
    SetChrChipByIndex(0x001F, 29)
    SetChrFlags(0x001C, 0x0002)
    SetChrFlags(0x001D, 0x0002)
    SetChrFlags(0x001E, 0x0002)
    SetChrFlags(0x001F, 0x0002)

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x001F, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBD, 0x00100006, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x35),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x08,
        (
            (Expr.PushLong, 0x31),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0019, 320, 0, -9150, 0)
    SetChrPos(0x0015, 3630, 0, -8680, 0)
    SetChrPos(0x0016, 1900, 0, -10130, 0)
    SetChrPos(0x0017, -1110, 0, -10190, 0)
    SetChrPos(0x001C, 790, 0, -2710, 180)
    SetChrPos(0x001D, -400, 0, -3530, 180)
    SetChrPos(0x001E, 2470, 0, -3700, 180)
    SetChrPos(0x001F, 940, 0, -4430, 180)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110307V胜负已分！\n',
            '红之组，洛伦斯小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007E, 1, 0x3F1))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x63A9
@scena.Code('func_0A_63A9')
def func_0A_63A9():
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)
    CameraMove(-13010, 4700, -19290, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(1830, 0)
    OP_6C(190000, 0)
    OP_6E(620, 0)
    SetChrPos(0x0053, -12650, 4700, -16700, 90)
    SetChrPos(0x005E, -12650, 4700, -14700, 90)
    SetChrPos(0x006A, -13730, 4950, -16780, 90)
    SetChrPos(0x0074, -12660, 4700, -15720, 90)
    SetChrPos(0x006F, -14780, 5200, 3980, 90)
    SetChrPos(0x005D, -13830, 4950, -15790, 90)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)

    @scena.Lambda('lambda_646D')
    def lambda_646D():
        CameraMove(-13480, 4950, 3760, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_646D)

    OP_6C(315000, 6000)
    SetMapFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007E, 2, 0x3F2))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x649A
@scena.Code('func_0B_649A')
def func_0B_649A():
    EventBegin(0x00)
    PlaySE(174, 0x00, 0x64)
    SetMapFlags(0x00100000)
    CameraMove(-6270, 0, -6280, 0)
    OP_67(0, 11870, -10000, 0)
    CameraSetDistance(3320, 0)
    OP_6C(90000, 0)
    OP_6E(505, 0)
    SetChrPos(0x0053, -12650, 4700, -16700, 90)
    SetChrPos(0x005E, -12650, 4700, -14700, 90)
    SetChrPos(0x006A, -13730, 4950, -16780, 90)
    SetChrPos(0x0074, -12660, 4700, -15720, 90)
    SetChrPos(0x006F, -14780, 5200, 3980, 90)
    SetChrPos(0x005D, -13830, 4950, -15790, 90)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_6558')
    def lambda_6558():
        CameraMove(1840, 0, -7130, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6558)

    @scena.Lambda('lambda_6570')
    def lambda_6570():
        OP_67(0, 5770, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6570)

    @scena.Lambda('lambda_6588')
    def lambda_6588():
        OP_6C(135000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6588)

    @scena.Lambda('lambda_6598')
    def lambda_6598():
        OP_6E(262, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6598)

    SetChrPos(0x0108, 2260, 0, -7590, 0)
    SetChrPos(0x0101, 1380, 0, -7590, 0)
    SetChrPos(0x0102, 300, 0, -7590, 0)
    SetChrPos(0x0104, -560, 0, -7590, 0)
    SetChrPos(0x0009, 2260, 0, -5460, 180)
    SetChrPos(0x000A, 1380, 0, -5460, 180)
    SetChrPos(0x000B, 300, 0, -5460, 180)
    SetChrPos(0x000C, -560, 0, -5460, 180)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 5550, 0, -6570, 270)
    Sleep(5000)

    ChrTalk(
        0x0009,
        (
            '#0320110800V#6P来了吗。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0120110801V#6P两位新人，呀嗬～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110802V#506F#2P嘿嘿……\n',
            '各位前辈，你们好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110803V#010F#2P还请各位前辈手下留情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0310110804V#822F#6P『不动金』……\n',
            '一直想向您讨教呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310110805V#6P到底有多厉害，\n',
            '就由这把剑来检验一下吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110806V#070F#2P哼哼，可以啊。\n',
            '我也会全力以赴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0330110807V#845F#6P哈哈，如果可以的话，\n',
            '真的希望是在决赛中碰面呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330110808V#6P在这里遇见也是命运的安排吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110809V#030F#2P一方是经验丰富的游击士集团。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110810V一方是令人注目的新人组合——\n',
            '武术家游击士和天才演奏家的混合小组。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110811V#035F哪一方会获胜，\n',
            '只有女神才会知道吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0024, 2900, 0, -6480, 3000, 0x00)

    ChrTalk(
        0x0024,
        (
            '#2210110812V马上开始武术大会\n',
            '正式赛第五场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    SetChrFlags(0x0108, 0x0040)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0102, 0x0040)
    SetChrFlags(0x0104, 0x0040)
    SetChrFlags(0x0012, 0x0040)
    SetChrFlags(0x0013, 0x0040)
    SetChrFlags(0x0014, 0x0040)
    SetChrFlags(0x0011, 0x0040)

    @scena.Lambda('lambda_69A0')
    def lambda_69A0():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_69A0')

    DispatchAsync2(0x0108, 0x0001, lambda_69A0)

    @scena.Lambda('lambda_69B1')
    def lambda_69B1():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_69B1')

    DispatchAsync2(0x0101, 0x0001, lambda_69B1)

    @scena.Lambda('lambda_69C2')
    def lambda_69C2():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_69C2')

    DispatchAsync2(0x0102, 0x0001, lambda_69C2)

    @scena.Lambda('lambda_69D3')
    def lambda_69D3():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_69D3')

    DispatchAsync2(0x0104, 0x0001, lambda_69D3)

    @scena.Lambda('lambda_69E4')
    def lambda_69E4():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_69E4)

    Sleep(200)

    @scena.Lambda('lambda_6A04')
    def lambda_6A04():
        ChrWalkTo(0x00FE, 2580, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_6A04)

    @scena.Lambda('lambda_6A1F')
    def lambda_6A1F():
        ChrWalkTo(0x00FE, -350, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6A1F)

    Sleep(200)

    @scena.Lambda('lambda_6A3F')
    def lambda_6A3F():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6A3F)

    @scena.Lambda('lambda_6A5A')
    def lambda_6A5A():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_6A5A')

    DispatchAsync2(0x000B, 0x0001, lambda_6A5A)

    @scena.Lambda('lambda_6A6B')
    def lambda_6A6B():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_6A6B')

    DispatchAsync2(0x000A, 0x0001, lambda_6A6B)

    @scena.Lambda('lambda_6A7C')
    def lambda_6A7C():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_6A7C')

    DispatchAsync2(0x0009, 0x0001, lambda_6A7C)

    @scena.Lambda('lambda_6A8D')
    def lambda_6A8D():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_6A8D')

    DispatchAsync2(0x000C, 0x0001, lambda_6A8D)

    @scena.Lambda('lambda_6A9E')
    def lambda_6A9E():
        ChrWalkTo(0x00FE, 390, 0, -1720, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_6A9E)

    @scena.Lambda('lambda_6AB9')
    def lambda_6AB9():
        ChrWalkTo(0x00FE, 1430, 0, -1790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_6AB9)

    @scena.Lambda('lambda_6AD4')
    def lambda_6AD4():
        ChrWalkTo(0x00FE, 2260, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_6AD4)

    @scena.Lambda('lambda_6AEF')
    def lambda_6AEF():
        ChrWalkTo(0x00FE, -560, 0, -440, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_6AEF)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    SetChrChipByIndex(0x0108, 25)
    SetChrChipByIndex(0x0101, 22)
    SetChrChipByIndex(0x0102, 23)
    SetChrChipByIndex(0x0104, 24)
    SetChrChipByIndex(0x000B, 29)
    SetChrChipByIndex(0x000A, 29)
    SetChrChipByIndex(0x0009, 29)
    SetChrChipByIndex(0x000C, 29)
    SetChrFlags(0x000B, 0x0002)
    SetChrFlags(0x000A, 0x0002)
    SetChrFlags(0x0009, 0x0002)
    SetChrFlags(0x000C, 0x0002)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0104, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000C, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x0000039E, 0x00000000, 0x00, 0x0000, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0101, 1100, 0, -8740, 0)
    SetChrPos(0x0102, -160, 0, -9400, 0)
    SetChrPos(0x0108, 2380, 0, -9800, 0)
    SetChrPos(0x0104, 1070, 0, -10590, 0)
    SetChrPos(0x000B, 2540, 0, -4780, 180)
    SetChrPos(0x000A, -970, 0, -4310, 180)
    SetChrPos(0x0009, 20, 0, -3500, 180)
    SetChrPos(0x000C, 1670, 0, -3790, 180)
    OP_66(0x0000)
    CameraMove(2410, 0, -7040, 0)
    OP_67(-26990, 18930, -7100, 0)
    CameraSetDistance(660, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110816V#5P胜负已分！\n',
            '苍之组，金小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#0330110817V#5P唔……干得漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0310110818V#5P『不动金』……\n',
            '没想到会是如此厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110819V#070F#2P过奖了，你们也相当的强哦。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110820V如果没有艾丝蒂尔他们帮忙的话，\n',
            '我一个人肯定没有胜算的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110821V#007F#2P哈啊哈啊……\n',
            '我们，赢了吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110822V#019F#2P嗯，怎么说呢……\n',
            '没有拖后腿就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0320110823V#835F#5P呵呵……\n',
            '不要太谦虚啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320110824V#5P金大人就不用说了，\n',
            '你们两个也很厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0120110825V#856F#5P呼，不愧是雪拉前辈\n',
            '教导出来的孩子啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120110826V#854F#5P而且，没想到那一位小哥\n',
            '也能有如此漂亮的表现……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110827V#035F#2P呵呵……\n',
            '小姐你也让我很着迷呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110828V不介意的话，\n',
            '比赛之后我们去干杯庆祝一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110829V#509F#2P给我适可而止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0048, 0x01, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007E, 3, 0x3F3))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x7013
@scena.Code('func_0C_7013')
def func_0C_7013():
    EventBegin(0x00)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 5550, 0, -6570, 270)
    CameraMove(1130, 0, -5670, 0)
    OP_67(0, 5770, -10000, 0)
    CameraSetDistance(3320, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x001C, 2260, 0, -5460, 180)
    SetChrPos(0x001D, 300, 0, -5460, 180)
    SetChrPos(0x001E, -560, 0, -5460, 180)
    SetChrPos(0x001F, 1380, 0, -5460, 180)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000E, 2260, 0, -7590, 0)
    SetChrPos(0x000F, 1380, 0, -7590, 0)
    SetChrPos(0x0010, 300, 0, -7590, 0)
    SetChrPos(0x000D, -560, 0, -7590, 0)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#0300110856V#190F#4P哟，带面具的小哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110857V我已经等这个复仇机会很久了！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0290110858V#200F#4P嘿嘿，这得感谢那个胖公爵啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140110859V#280F#5P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0090110860V#214F#4P有、有什么好笑的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140110861V#280F#5P埃雷波尼亚的没落贵族，\n',
            '卡普亚男爵家的各位孤儿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140110862V被恶德商人霸占了领地，\n',
            '为了家业复兴而干起空贼的行当……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140110863V真是可歌可泣的故事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0300110864V#196F#4P#3S你、你！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0290110865V#201F#4P你怎么会知道的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140110866V#280F#5P别忘了，\n',
            '我们所属的可是『情报部』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140110867V你们还是放弃向我们复仇的念头，\n',
            '老老实实地服刑比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140110868V因为你们并不是什么穷凶极恶的坏人。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0090110869V#216F#4P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0290110870V#204F#4P哼，看来你不单会耍手段，\n',
            '连嘴上功夫也有两下子的嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0300110871V#196F哼，马上就让你们\n',
            '成为我导力炮下的食物！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0024, 2900, 0, -6480, 3000, 0x00)

    ChrTalk(
        0x0024,
        (
            '#2210110872V马上开始武术大会\n',
            '正式赛第六场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100915V请两队队员\n',
            '分别站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    SetChrFlags(0x000E, 0x0040)
    SetChrFlags(0x000F, 0x0040)
    SetChrFlags(0x0010, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x001C, 0x0040)
    SetChrFlags(0x001D, 0x0040)
    SetChrFlags(0x001E, 0x0040)
    SetChrFlags(0x001F, 0x0040)

    @scena.Lambda('lambda_758B')
    def lambda_758B():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_758B')

    DispatchAsync2(0x000E, 0x0001, lambda_758B)

    @scena.Lambda('lambda_759C')
    def lambda_759C():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_759C')

    DispatchAsync2(0x000F, 0x0001, lambda_759C)

    @scena.Lambda('lambda_75AD')
    def lambda_75AD():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_75AD')

    DispatchAsync2(0x0010, 0x0001, lambda_75AD)

    @scena.Lambda('lambda_75BE')
    def lambda_75BE():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_75BE')

    DispatchAsync2(0x000D, 0x0001, lambda_75BE)

    @scena.Lambda('lambda_75CF')
    def lambda_75CF():
        ChrWalkTo(0x00FE, 2350, 0, -13170, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_75CF)

    @scena.Lambda('lambda_75EA')
    def lambda_75EA():
        ChrWalkTo(0x00FE, -170, 0, -13170, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_75EA)

    Sleep(200)

    @scena.Lambda('lambda_760A')
    def lambda_760A():
        ChrWalkTo(0x00FE, 1570, 0, -11430, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_760A)

    @scena.Lambda('lambda_7625')
    def lambda_7625():
        ChrWalkTo(0x00FE, 390, 0, -11390, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_7625)

    @scena.Lambda('lambda_7640')
    def lambda_7640():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_7640')

    DispatchAsync2(0x001C, 0x0001, lambda_7640)

    @scena.Lambda('lambda_7651')
    def lambda_7651():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_7651')

    DispatchAsync2(0x001D, 0x0001, lambda_7651)

    @scena.Lambda('lambda_7662')
    def lambda_7662():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_7662')

    DispatchAsync2(0x001E, 0x0001, lambda_7662)

    @scena.Lambda('lambda_7673')
    def lambda_7673():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_7673')

    DispatchAsync2(0x001F, 0x0001, lambda_7673)

    @scena.Lambda('lambda_7684')
    def lambda_7684():
        ChrWalkTo(0x00FE, 1080, 0, 680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_7684)

    Sleep(200)

    @scena.Lambda('lambda_76A4')
    def lambda_76A4():
        ChrWalkTo(0x00FE, -310, 0, -290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0002, lambda_76A4)

    @scena.Lambda('lambda_76BF')
    def lambda_76BF():
        ChrWalkTo(0x00FE, 2670, 0, -320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_76BF)

    Sleep(200)

    @scena.Lambda('lambda_76DF')
    def lambda_76DF():
        ChrWalkTo(0x00FE, 1080, 0, -1960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_76DF)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    SetChrChipByIndex(0x000E, 29)
    SetChrChipByIndex(0x000F, 29)
    SetChrChipByIndex(0x0010, 29)
    SetChrChipByIndex(0x000D, 29)
    SetChrFlags(0x000E, 0x0002)
    SetChrFlags(0x000F, 0x0002)
    SetChrFlags(0x0010, 0x0002)
    SetChrFlags(0x000D, 0x0002)

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x28),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x24),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x20),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x001C, 29)
    SetChrChipByIndex(0x001D, 29)
    SetChrChipByIndex(0x001E, 29)
    SetChrChipByIndex(0x001F, 29)
    SetChrFlags(0x001C, 0x0002)
    SetChrFlags(0x001D, 0x0002)
    SetChrFlags(0x001E, 0x0002)
    SetChrFlags(0x001F, 0x0002)

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x001F, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00000BBE, 0x00100007, 0x00, 0x0200, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x29),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x25),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x000E, 1540, 0, -9380, 0)
    SetChrPos(0x000F, -170, 0, -9030, 0)
    SetChrPos(0x0010, 730, 0, -10360, 0)
    SetChrPos(0x000D, 2770, 0, -8750, 0)
    SetChrPos(0x001C, 790, 0, -2710, 180)
    SetChrPos(0x001D, -400, 0, -3530, 180)
    SetChrPos(0x001E, 2470, 0, -3700, 180)
    SetChrPos(0x001F, 940, 0, -4430, 180)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110307V胜负已分！\n',
            '红之组，洛伦斯小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007E, 4, 0x3F4))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x7993
@scena.Code('func_0D_7993')
def func_0D_7993():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    PlaySE(174, 0x00, 0x64)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0108, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    ChrSetRGBAMask(0x0021, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0020, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0029, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0028, 255, 255, 255, 0, 0)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0029, 0x0080)
    ClearChrFlags(0x0028, 0x0080)
    SetChrFlags(0x0021, 0x0004)
    SetChrFlags(0x0020, 0x0004)
    SetChrFlags(0x0029, 0x0004)
    SetChrFlags(0x0028, 0x0004)
    SetChrPos(0x0021, 19870, 9500, -6460, 270)
    SetChrPos(0x0020, 20800, 9500, -5950, 270)
    SetChrPos(0x0029, 20290, 9750, -7200, 270)
    SetChrPos(0x0028, 21100, 9500, -6600, 270)
    CameraMove(1210, 11600, -6480, 0)
    OP_67(0, 3630, -10000, 0)
    CameraSetDistance(2870, 0)
    OP_6C(269000, 0)
    OP_6E(428, 0)

    @scena.Lambda('lambda_7A93')
    def lambda_7A93():
        OP_6C(90000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7A93)

    FadeIn(2000, 0)
    Sleep(4000)

    SetChrPos(0x0030, 14650, 4700, 250, 270)
    SetChrPos(0x0031, 15730, 4950, 250, 270)
    SetChrPos(0x0032, 16860, 5200, 250, 270)
    SetChrPos(0x0033, 17850, 5450, 250, 270)
    SetChrPos(0x0034, 18880, 5700, 250, 270)
    SetChrPos(0x0035, 19640, 5950, 250, 270)
    SetChrPos(0x0036, 14650, 4700, 1200, 270)
    SetChrPos(0x0037, 15730, 4950, 1200, 270)
    SetChrPos(0x0038, 16860, 5200, 1200, 270)
    SetChrPos(0x0039, 17850, 5450, 1200, 270)
    SetChrPos(0x003A, 18880, 5700, 1200, 270)
    SetChrPos(0x003B, 19640, 5950, 1200, 270)
    SetChrPos(0x003C, 14650, 4700, 2390, 270)
    SetChrPos(0x003D, 15730, 4950, 2390, 270)
    SetChrPos(0x003E, 16860, 5200, 2390, 270)
    SetChrPos(0x003F, 17850, 5450, 2390, 270)
    SetChrPos(0x0040, 18880, 5700, 2390, 270)
    SetChrPos(0x0041, 19640, 5950, 2390, 270)
    SetChrPos(0x0042, 14650, 4700, 3550, 270)
    SetChrPos(0x0043, 15730, 4950, 3550, 270)
    SetChrPos(0x0044, 16860, 5200, 3550, 270)
    SetChrPos(0x0045, 17850, 5450, 3550, 270)
    SetChrPos(0x0046, 18880, 5700, 3550, 270)
    SetChrPos(0x0047, 19640, 5950, 3550, 270)
    SetChrPos(0x0048, 14650, 4700, 4830, 270)
    SetChrPos(0x0049, 15730, 4950, 4830, 270)
    SetChrPos(0x004A, 16860, 5200, 4830, 270)
    SetChrPos(0x004B, 17850, 5450, 4830, 270)
    SetChrPos(0x004C, 18880, 5700, 4830, 270)
    SetChrPos(0x004D, 19640, 5950, 4830, 270)
    SetChrPos(0x004E, 14650, 4700, -13300, 270)
    SetChrPos(0x004F, 15730, 4950, -13300, 270)
    SetChrPos(0x0050, 16860, 5200, -13300, 270)
    SetChrPos(0x0051, 17850, 5450, -13300, 270)
    SetChrPos(0x0052, 18880, 5700, -13300, 270)
    SetChrPos(0x0053, 19640, 5950, -13300, 270)
    SetChrPos(0x0054, 14650, 4700, -14500, 270)
    SetChrPos(0x0055, 15730, 4950, -14500, 270)
    SetChrPos(0x0056, 16860, 5200, -14500, 270)
    SetChrPos(0x0057, 17850, 5450, -14500, 270)
    SetChrPos(0x0058, 18880, 5700, -14500, 270)
    SetChrPos(0x0059, 19640, 5950, -14500, 270)
    SetChrPos(0x005A, 14650, 4700, -15600, 270)
    SetChrPos(0x005B, 15730, 4950, -15600, 270)
    SetChrPos(0x005C, 16860, 5200, -15600, 270)
    SetChrPos(0x005D, 17850, 5450, -15600, 270)
    SetChrPos(0x005E, 18880, 5700, -15600, 270)
    SetChrPos(0x005F, 19640, 5950, -15600, 270)
    SetChrPos(0x0060, 14650, 4700, -16920, 270)
    SetChrPos(0x0061, 15730, 4950, -16920, 270)
    SetChrPos(0x0062, 16860, 5200, -16920, 270)
    SetChrPos(0x0063, 17850, 5450, -16920, 270)
    SetChrPos(0x0064, 18880, 5700, -16920, 270)
    SetChrPos(0x0065, 19640, 5950, -16920, 270)
    SetChrPos(0x0066, 14650, 4700, -18030, 270)
    SetChrPos(0x0067, 15730, 4950, -18030, 270)
    SetChrPos(0x0068, 16860, 5200, -18030, 270)
    SetChrPos(0x0069, 17850, 5450, -18030, 270)
    SetChrPos(0x006A, 18880, 5700, -18030, 270)
    SetChrPos(0x006B, 19640, 5950, -18030, 270)
    Sleep(5000)

    @scena.Lambda('lambda_7EB2')
    def lambda_7EB2():
        CameraMove(9560, 14150, -6480, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7EB2)

    @scena.Lambda('lambda_7ECA')
    def lambda_7ECA():
        OP_67(0, 6940, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7ECA)

    @scena.Lambda('lambda_7EE2')
    def lambda_7EE2():
        OP_6E(314, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7EE2)

    Sleep(1500)

    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 60)
    Sleep(2000)

    @scena.Lambda('lambda_7F0F')
    def lambda_7F0F():
        ChrWalkTo(0x00FE, 10890, 9500, -6410, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_7F0F)

    @scena.Lambda('lambda_7F2A')
    def lambda_7F2A():
        ChrWalkTo(0x00FE, 10890, 9500, -6410, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_7F2A)

    @scena.Lambda('lambda_7F45')
    def lambda_7F45():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0021, 0x0002, lambda_7F45)

    @scena.Lambda('lambda_7F57')
    def lambda_7F57():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_7F57)

    Sleep(300)

    @scena.Lambda('lambda_7F6E')
    def lambda_7F6E():
        ChrWalkTo(0x00FE, 3830, 9750, -7250, 1100, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7F6E)

    @scena.Lambda('lambda_7F89')
    def lambda_7F89():
        ChrWalkTo(0x00FE, 3830, 9750, -7250, 1100, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_7F89)

    @scena.Lambda('lambda_7FA4')
    def lambda_7FA4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0029, 0x0002, lambda_7FA4)

    @scena.Lambda('lambda_7FB6')
    def lambda_7FB6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0028, 0x0002, lambda_7FB6)

    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007E, 6, 0x3F6))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x7FE4
@scena.Code('func_0E_7FE4')
def func_0E_7FE4():
    EventBegin(0x00)
    CameraMove(-4350, 1700, -6590, 0)
    OP_67(0, 9590, -10000, 0)
    CameraSetDistance(3970, 0)
    OP_6C(90000, 0)
    OP_6E(389, 0)
    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 870, 0, -6590, 0)

    @scena.Lambda('lambda_803F')
    def lambda_803F():
        CameraSetDistance(2940, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_803F)

    @scena.Lambda('lambda_804F')
    def lambda_804F():
        CameraMove(1020, 0, -6570, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_804F)

    @scena.Lambda('lambda_8067')
    def lambda_8067():
        ChrWalkTo(0x00FE, 5940, 0, -6480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_8067)

    WaitForThreadExit(0x0024, 0x0001)
    SetChrDirection(0x0024, 270, 400)
    WaitForThreadExit(0x0101, 0x0002)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200111743V',
            (TxtCtl.SetColor, 0x5),
            '武术大会从预选赛开始\n',
            '已经经过了一个星期的时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200111744V',
            (TxtCtl.SetColor, 0x5),
            '今天终于迎来了\n',
            '最后一场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200111745V',
            (TxtCtl.SetColor, 0x5),
            '到底哪一支队伍会\n',
            '获得胜利和荣耀呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200111746V',
            (TxtCtl.SetColor, 0x5),
            '那么下面公布参加决赛的\n',
            '对阵的双方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110206V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组——\n',
            '来自卡尔瓦德共和国的武术家。\n',
            '金选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110847V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组——\n',
            '王国军情报部，特务部队所属。\n',
            '洛伦斯少尉等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007E, 7, 0x3F7))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x8226
@scena.Code('func_0F_8226')
def func_0F_8226():
    EventBegin(0x00)
    SetMapFlags(0x00100000)
    PlaySE(174, 0x00, 0x64)
    CameraMove(1010, 0, -20480, 0)
    OP_67(0, 2060, -10000, 0)
    CameraSetDistance(3640, 0)
    OP_6C(180000, 0)
    OP_6E(316, 0)
    OP_71(0x0001, 0x0004)
    FadeOut(0, 0, -1)

    @scena.Lambda('lambda_8284')
    def lambda_8284():
        CameraSetDistance(1380, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8284)

    @scena.Lambda('lambda_8294')
    def lambda_8294():
        OP_6E(840, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8294)

    ClearChrFlags(0x0024, 0x0080)
    SetChrPos(0x0024, 5550, 0, -6570, 270)
    Sleep(500)

    FadeIn(2000, 0)
    SetChrPos(0x0108, 2260, 0, -24190, 0)
    SetChrPos(0x0101, 1380, 0, -24190, 0)
    SetChrPos(0x0102, 300, 0, -24190, 0)
    SetChrPos(0x0104, -560, 0, -24190, 0)
    SetChrPos(0x001C, 2260, 0, 11000, 180)
    SetChrPos(0x001D, 1380, 0, 11000, 180)
    SetChrPos(0x001E, 300, 0, 11000, 180)
    SetChrPos(0x001F, -560, 0, 11000, 180)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    Sleep(2000)

    OP_70(0x0000, 100)
    OP_70(0x0001, 100)
    Sleep(3000)

    @scena.Lambda('lambda_837C')
    def lambda_837C():
        CameraMove(1650, 0, -6810, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_837C)

    @scena.Lambda('lambda_8394')
    def lambda_8394():
        OP_6C(134000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8394)

    @scena.Lambda('lambda_83A4')
    def lambda_83A4():
        OP_67(0, 5420, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_83A4)

    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)

    @scena.Lambda('lambda_83C6')
    def lambda_83C6():
        ChrWalkTo(0x00FE, 2260, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_83C6)

    Sleep(300)

    @scena.Lambda('lambda_83E6')
    def lambda_83E6():
        ChrWalkTo(0x00FE, -560, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_83E6)

    Sleep(50)

    @scena.Lambda('lambda_8406')
    def lambda_8406():
        ChrWalkTo(0x00FE, 1380, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8406)

    Sleep(50)

    @scena.Lambda('lambda_8426')
    def lambda_8426():
        ChrWalkTo(0x00FE, 300, 0, -7590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8426)

    SetChrPos(0x001C, 2260, 0, -5460, 180)
    SetChrPos(0x001D, 1380, 0, -5460, 180)
    SetChrPos(0x001E, 300, 0, -5460, 180)
    SetChrPos(0x001F, -560, 0, -5460, 180)
    OP_72(0x0001, 0x0004)
    Sleep(6000)

    Fade(1000)
    CameraSetDistance(1020, 0)
    OP_6C(45000, 0)
    CameraMove(910, 0, -6640, 0)
    OP_0D()

    ChrTalk(
        0x001C,
        (
            '#2620111754V（果然比至今为止碰到的家伙\n',
            '　看起来都要厉害得多……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111755V（可是，队伍的一半\n',
            '　只是稚气未脱的少年少女啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111756V（总之根本不是我们的对手嘛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140111757V#280F（哼哼，不要轻敌。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140111758V（那些小孩是游击士协会的人哦。）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#2620111759V（哎……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111760V（难道是报告中的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140111761V#281F（有这种可能。\n',
            '　一定不要放松警惕啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#2620111762V（……是！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111763V（明白了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111764V#509F#4P喂喂～怎么叽叽咕咕的～\n',
            '你们在偷偷摸摸说些什么呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111765V#035F#4P呵，艾丝蒂尔君。\n',
            '不要和那些人介意啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111766V带着那样的面具，\n',
            '肯定是对自己的脸没有信心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111767V因为嫉妒我这艺术般的美貌，\n',
            '偷偷地说些坏话也是没有办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#2620111768V你、你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111769V不要随便乱解释！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111770V#012F#4P那个……\n',
            '您是叫洛伦斯少尉吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140111771V#281F怎么了，这位黑发少年？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111772V#004F#4P约修亚……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111773V#013F#4P你的剑法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111774V#015F…………………………\n',
            '不……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111775V#012F总之请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140111776V#280F哼……\n',
            '彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111777V#505F#4P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111778V#070F#4P好了，谈话就到这里为止吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111779V差不多该开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210111780V马上开始武术大会的决赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210111781V请两队队员站在初始位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(1900, 0, -6510, 0)
    OP_67(0, 19660, -27990, 0)
    CameraSetDistance(910, 0)
    OP_6C(90000, 0)
    OP_6E(407, 0)
    SetChrFlags(0x0108, 0x0040)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0102, 0x0040)
    SetChrFlags(0x0104, 0x0040)
    SetChrFlags(0x001C, 0x0040)
    SetChrFlags(0x001D, 0x0040)
    SetChrFlags(0x001E, 0x0040)
    SetChrFlags(0x001F, 0x0040)

    @scena.Lambda('lambda_89B7')
    def lambda_89B7():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_89B7')

    DispatchAsync2(0x0108, 0x0001, lambda_89B7)

    @scena.Lambda('lambda_89C8')
    def lambda_89C8():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_89C8')

    DispatchAsync2(0x0101, 0x0001, lambda_89C8)

    @scena.Lambda('lambda_89D9')
    def lambda_89D9():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_89D9')

    DispatchAsync2(0x0102, 0x0001, lambda_89D9)

    @scena.Lambda('lambda_89EA')
    def lambda_89EA():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_89EA')

    DispatchAsync2(0x0104, 0x0001, lambda_89EA)

    @scena.Lambda('lambda_89FB')
    def lambda_89FB():
        ChrWalkTo(0x00FE, 1030, 0, -13650, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_89FB)

    Sleep(200)

    @scena.Lambda('lambda_8A1B')
    def lambda_8A1B():
        ChrWalkTo(0x00FE, 2580, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_8A1B)

    @scena.Lambda('lambda_8A36')
    def lambda_8A36():
        ChrWalkTo(0x00FE, -350, 0, -12560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_8A36)

    Sleep(200)

    @scena.Lambda('lambda_8A56')
    def lambda_8A56():
        ChrWalkTo(0x00FE, 1020, 0, -11320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8A56)

    @scena.Lambda('lambda_8A71')
    def lambda_8A71():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_8A71')

    DispatchAsync2(0x001C, 0x0001, lambda_8A71)

    @scena.Lambda('lambda_8A82')
    def lambda_8A82():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_8A82')

    DispatchAsync2(0x001D, 0x0001, lambda_8A82)

    @scena.Lambda('lambda_8A93')
    def lambda_8A93():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_8A93')

    DispatchAsync2(0x001E, 0x0001, lambda_8A93)

    @scena.Lambda('lambda_8AA4')
    def lambda_8AA4():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_8AA4')

    DispatchAsync2(0x001F, 0x0001, lambda_8AA4)

    @scena.Lambda('lambda_8AB5')
    def lambda_8AB5():
        ChrWalkTo(0x00FE, 1080, 0, 680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_8AB5)

    Sleep(200)

    @scena.Lambda('lambda_8AD5')
    def lambda_8AD5():
        ChrWalkTo(0x00FE, -310, 0, -290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0002, lambda_8AD5)

    @scena.Lambda('lambda_8AF0')
    def lambda_8AF0():
        ChrWalkTo(0x00FE, 2670, 0, -320, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_8AF0)

    Sleep(200)

    @scena.Lambda('lambda_8B10')
    def lambda_8B10():
        ChrWalkTo(0x00FE, 1080, 0, -1960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_8B10)

    Sleep(100)

    ChrMoveTo(0x0024, 6410, 0, -6500, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0024,
        (
            '#2210111782V在空之女神的见证下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#2210100916V双方，准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    SetChrChipByIndex(0x001C, 29)
    SetChrChipByIndex(0x001D, 29)
    SetChrChipByIndex(0x001E, 29)
    SetChrChipByIndex(0x001F, 29)
    SetChrFlags(0x001C, 0x0002)
    SetChrFlags(0x001D, 0x0002)
    SetChrFlags(0x001E, 0x0002)
    SetChrFlags(0x001F, 0x0002)

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x3A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0108, 25)
    SetChrChipByIndex(0x0101, 22)
    SetChrChipByIndex(0x0102, 23)
    SetChrChipByIndex(0x0104, 24)
    Sleep(2000)

    ChrTalk(
        0x0024,
        (
            '#2210100917V比赛开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x001F, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0104, 0xFF)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_23(0x00AE)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x0000039F, 0x00000000, 0x00, 0x0000, 0xFF)
    PlaySE(174, 0x00, 0x64)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x3B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x3B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x3B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x3F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0101, 1100, 0, -8740, 0)
    SetChrPos(0x0102, -160, 0, -9400, 0)
    SetChrPos(0x0108, 2380, 0, -9800, 0)
    SetChrPos(0x0104, 1070, 0, -10590, 0)
    SetChrPos(0x001C, 790, 0, -2710, 180)
    SetChrPos(0x001D, -400, 0, -3530, 180)
    SetChrPos(0x001E, 2470, 0, -3700, 180)
    SetChrPos(0x001F, 940, 0, -4430, 180)
    OP_66(0x0000)
    CameraMove(2410, 0, -7040, 0)
    OP_67(-26990, 18930, -7100, 0)
    CameraSetDistance(660, 0)
    OP_6C(90000, 0)
    OP_6E(462, 0)
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0024,
        (
            '#2210110816V#5P胜负已分！\n',
            '苍之组金小组胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#2620111786V#5P不、不可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2630111787V#5P代表精英的特务部队的我们\n',
            '竟然输掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0140111788V#280F#5P哼……还是有两下子嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010111789V#001F#2P#5S太好啦～～～！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111790V#014F#2P赢了……我们赢了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111791V#034F#2P哈啊哈啊……\n',
            '真、真是累啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111792V#072F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_66(0x0001)
    CameraMove(860, 0, -6420, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0024, 0x0080)
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    SetChrPos(0x0020, 5470, 0, -6520, 270)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    SetChrPos(0x0019, 3500, 0, -5190, 270)
    SetChrPos(0x001B, 3500, 0, -7920, 270)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    SetChrChipByIndex(0x0104, 65535)
    SetChrPos(0x0020, 3290, 0, -7050, 270)
    SetChrPos(0x0021, 2500, 0, -6550, 270)
    SetChrPos(0x0101, -1310, 0, -5190, 90)
    SetChrPos(0x0102, -1310, 0, -6120, 90)
    SetChrPos(0x0108, -1310, 0, -6940, 90)
    SetChrPos(0x0104, -1310, 0, -7920, 90)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200111793V',
            (TxtCtl.SetColor, 0x5),
            '那么，接下来请杜南公爵\n',
            '为优胜小组送上祝福的讲话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

    Talk(
        (
            '#2200111794V',
            (TxtCtl.SetColor, 0x5),
            '代表，金·瓦赛克选手！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200111795V',
            (TxtCtl.SetColor, 0x5),
            '请上前来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0108,
        (
            '#0080111796V#070F好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_90DE')
    def lambda_90DE():
        CameraMove(1860, 0, -6420, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_90DE)

    ChrWalkTo(0x0108, 930, 0, -6580, 1000, 0x00)
    ChrTurnDirection(0x0108, 0x0021, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0021,
        (
            '#0640111797V#223F#5P哦哦……\n',
            '走近了看还真是大块头啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640111798V你们东方人都是这么大的体型吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111799V#070F#4P不，只是我自己特殊而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111800V从小的时候养成良好的饮食和作息习惯，\n',
            '经常锻炼，自然就成这样了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111801V本性不会对事情深入考虑，\n',
            '所以只是体格变大了而已吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#0640111802V#221F#5P哈哈哈，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640111803V#220F嗯！\n',
            '我很欣赏你，金选手！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640111804V现在给你颁发奖金１０万米拉\n',
            '和晚宴的邀请函！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111805V#074F#4P十分荣幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0021, 1900, 0, -6550, 1000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '晚宴请帖',
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
            '得到奖金',
            (TxtCtl.SetColor, 0x4),
            '１０００００',
            (TxtCtl.SetColor, 0x0),
            '米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddMira(50000)
    AddMira(50000)
    ChrMoveTo(0x0021, 2500, 0, -6550, 2000, 0x00)
    RemoveItem(0x0375, 1)
    RemoveItem(0x0372, 1)

    ChrTalk(
        0x0021,
        (
            '#0640111806V#220F#5P愿这位选手和他的同伴\n',
            '得到空之女神的祝福和光荣！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640111807V#221F那么，各位亲爱的市民！\n',
            '请给优胜者最热烈的鼓掌和喝彩！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    OP_28(0x0049, 0x01, 0x0020)
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 0, 0x3F8))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

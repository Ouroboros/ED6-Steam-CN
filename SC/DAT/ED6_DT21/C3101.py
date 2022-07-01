import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3101   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '卡西乌斯'),
    TXT(0x02, '尤莉亚上尉'),
    TXT(0x03, '摩尔根将军'),
    TXT(0x04, '希德中校'),
    TXT(0x05, '格斯塔夫维修长'),
    TXT(0x06, '士兵'),
    TXT(0x07, '士兵'),
    TXT(0x08, '士兵'),
    TXT(0x09, '士兵'),
    TXT(0x0A, '士兵'),
    TXT(0x0B, '士兵'),
    TXT(0x0C, '士兵'),
    TXT(0x0D, '士兵'),
    TXT(0x0E, '士兵'),
    TXT(0x0F, '士兵'),
    TXT(0x10, '士兵'),
    TXT(0x11, '士兵'),
    TXT(0x12, '士兵'),
    TXT(0x13, '士兵'),
    TXT(0x14, '士兵'),
    TXT(0x15, '士兵'),
    TXT(0x16, '亲卫队'),
    TXT(0x17, '亲卫队'),
    TXT(0x18, '亲卫队'),
    TXT(0x19, '亲卫队'),
    TXT(0x1A, '亲卫队'),
    TXT(0x1B, '亲卫队'),
    TXT(0x1C, '王国军士官'),
    TXT(0x1D, '目标用照相机'),
    TXT(0x1E, '贝尔克副队长'),
    TXT(0x1F, '士兵'),
    TXT(0x20, '士兵'),
    TXT(0x21, '士兵'),
    TXT(0x22, '士兵'),
    TXT(0x23, '士兵'),
    TXT(0x24, '士兵'),
    TXT(0x25, '士兵'),
    TXT(0x26, '士兵'),
    TXT(0x27, '士兵'),
    TXT(0x28, '士兵'),
    TXT(0x29, '士兵'),
    TXT(0x2A, '士兵'),
    TXT(0x2B, '士兵'),
    TXT(0x2C, '士兵'),
    TXT(0x2D, '士兵'),
    TXT(0x2E, '士兵'),
    TXT(0x2F, '士兵'),
    TXT(0x30, '士兵'),
    TXT(0x31, '士兵'),
    TXT(0x32, '士兵'),
    TXT(0x33, '士兵'),
    TXT(0x34, '士兵'),
    TXT(0x35, '士兵'),
    TXT(0x36, '士兵'),
    TXT(0x37, '士兵'),
    TXT(0x38, '士兵'),
    TXT(0x39, '士兵'),
    TXT(0x3A, '士兵'),
    TXT(0x3B, '士兵'),
    TXT(0x3C, '士兵'),
    TXT(0x3D, '士兵'),
    TXT(0x3E, '士兵'),
    TXT(0x3F, '王国军士官'),
    TXT(0x40, '王国军士官'),
    TXT(0x41, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3101.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/C3101._SN', 'ED6_DT21/C3101_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6B60
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
        ('ED6_DT27/CH03670._CH', 'ED6_DT27/CH03670P._CP'),
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT27/CH03590._CH', 'ED6_DT27/CH03590P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH00322._CH', 'ED6_DT07/CH00322P._CP'),
        ('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04004P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00124._CH', 'ED6_DT07/CH00124P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00134._CH', 'ED6_DT07/CH00134P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00144._CH', 'ED6_DT07/CH00144P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00154P._CP'),
        ('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP'),
        ('ED6_DT07/CH00324._CH', 'ED6_DT07/CH00324P._CP'),
        ('ED6_DT07/CH00330._CH', 'ED6_DT07/CH00330P._CP'),
        ('ED6_DT07/CH00334._CH', 'ED6_DT07/CH00334P._CP'),
        ('ED6_DT07/CH00137._CH', 'ED6_DT07/CH00137P._CP'),
        ('ED6_DT26/CH20290._CH', 'ED6_DT26/CH20290P._CP'),
        ('ED6_DT26/CH20307._CH', 'ED6_DT26/CH20307P._CP'),
        ('ED6_DT26/CH20296._CH', 'ED6_DT26/CH20296P._CP'),
        ('ED6_DT26/CH20297._CH', 'ED6_DT26/CH20297P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH00331._CH', 'ED6_DT07/CH00331P._CP'),
        ('ED6_DT27/CH04590._CH', 'ED6_DT27/CH04590P._CP'),
        ('ED6_DT27/CH04594._CH', 'ED6_DT27/CH04594P._CP'),
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x9BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x9BA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x9BA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x9BA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_9D0',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x000B)

    Jump('loc_9FD')

    def _loc_9D0(): pass

    label('loc_9D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_9EF',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0002)

    Jump('loc_9FD')

    def _loc_9EF(): pass

    label('loc_9EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_9FD',
    )

    OP_A3(0x10F2)
    Event(1, 0x0000)

    def _loc_9FD(): pass

    label('loc_9FD')

    Return()

# id: 0x0001 offset: 0x9FE
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x9FF
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0023, -850, 0, 30150, 180)
    SetChrPos(0x000D, -2850, 0, 28150, 90)
    SetChrPos(0x000E, 1250, 0, 28150, 270)
    SetChrPos(0x000F, -2850, 0, 26150, 90)
    SetChrPos(0x0010, 1250, 0, 26150, 270)
    SetChrPos(0x0011, -2850, 0, 24150, 90)
    SetChrPos(0x0012, 1250, 0, 24150, 270)
    SetChrChipByIndex(0x000D, 9)
    SetChrChipByIndex(0x000E, 9)
    SetChrChipByIndex(0x000F, 9)
    SetChrChipByIndex(0x0010, 9)
    SetChrChipByIndex(0x0011, 9)
    SetChrChipByIndex(0x0012, 9)
    OP_6D(-980, 0, 27500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    CreateThread(0x000D, 0x01, 0x00, 0x0004)
    Sleep(50)

    CreateThread(0x000F, 0x01, 0x00, 0x0004)
    Sleep(50)

    CreateThread(0x000E, 0x01, 0x00, 0x0004)
    Sleep(50)

    CreateThread(0x0011, 0x01, 0x00, 0x0004)
    Sleep(50)

    CreateThread(0x0010, 0x01, 0x00, 0x0004)
    Sleep(50)

    CreateThread(0x0012, 0x01, 0x00, 0x0004)
    FadeIn(2000, 0)
    Sleep(3500)

    OP_22(0x0085, 0x00, 0x64)

    @scena.Lambda('lambda_0B66')
    def lambda_0B66():
        OP_7C(0x000000C8, 0x00000000, 0x000007D0, 0x00000BB8)
        Yield()

        Jump('lambda_0B66')

    DispatchAsync2(0x0101, 0x0003, lambda_0B66)

    Sleep(500)

    OP_A2(0x0000)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0023, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#2450230722V什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2460230723V敌、敌人的轰炸！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    OP_62(0x000F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    OP_62(0x0011, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    OP_62(0x0012, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x000D, 0x01, 0x00, 0x0005)
    CreateThread(0x000E, 0x01, 0x00, 0x0006)
    CreateThread(0x000F, 0x01, 0x00, 0x0007)
    CreateThread(0x0010, 0x01, 0x00, 0x0008)
    CreateThread(0x0011, 0x01, 0x00, 0x0009)
    CreateThread(0x0012, 0x01, 0x00, 0x000A)
    CreateThread(0x0023, 0x01, 0x00, 0x0003)
    Sleep(1000)

    OP_62(0x0023, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)

    ChrTalk(
        0x0023,
        (
            '#2440230724V#5P冷、冷静一点！\n',
            '只是地震！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2440230725V#5P别乱了阵型，原地待命！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C3110._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0xDAC
@scena.Code('func_03_DAC')
def func_03_DAC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DD0',
    )

    OP_8C(0x00FE, 225, 400)
    Sleep(500)

    OP_8C(0x00FE, 135, 400)
    Sleep(500)

    Jump('func_03_DAC')

    def _loc_DD0(): pass

    label('loc_DD0')

    Return()

# id: 0x0004 offset: 0xDD1
@scena.Code('func_04_DD1')
def func_04_DD1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DF8',
    )

    OP_99(0x00FE, 0x00, 0x04, 0x00000A28)
    Sleep(500)

    OP_99(0x00FE, 0x04, 0x00, 0x00000A28)
    Sleep(1500)

    Jump('func_04_DD1')

    def _loc_DF8(): pass

    label('loc_DF8')

    Return()

# id: 0x0005 offset: 0xDF9
@scena.Code('func_05_DF9')
def func_05_DF9():
    SetChrChipByIndex(0x00FE, 10)
    def _loc_DFE(): pass

    label('loc_DFE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E32',
    )

    OP_90(0x00FE, -500, 0, 500, 4100, 0x00)
    OP_90(0x00FE, 500, 0, -500, 4200, 0x00)

    Jump('loc_DFE')

    def _loc_E32(): pass

    label('loc_E32')

    Return()

# id: 0x0006 offset: 0xE33
@scena.Code('func_06_E33')
def func_06_E33():
    SetChrChipByIndex(0x00FE, 10)
    Sleep(50)

    def _loc_E3D(): pass

    label('loc_E3D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E71',
    )

    OP_90(0x00FE, -800, 0, -800, 4200, 0x00)
    OP_90(0x00FE, 800, 0, 800, 4300, 0x00)

    Jump('loc_E3D')

    def _loc_E71(): pass

    label('loc_E71')

    Return()

# id: 0x0007 offset: 0xE72
@scena.Code('func_07_E72')
def func_07_E72():
    SetChrChipByIndex(0x00FE, 10)
    Sleep(50)

    def _loc_E7C(): pass

    label('loc_E7C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EB0',
    )

    OP_90(0x00FE, -1000, 0, 0, 3800, 0x00)
    OP_90(0x00FE, 1000, 0, 0, 3900, 0x00)

    Jump('loc_E7C')

    def _loc_EB0(): pass

    label('loc_EB0')

    Return()

# id: 0x0008 offset: 0xEB1
@scena.Code('func_08_EB1')
def func_08_EB1():
    SetChrChipByIndex(0x00FE, 10)
    def _loc_EB6(): pass

    label('loc_EB6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EDE',
    )

    OP_8C(0x00FE, 90, 400)
    OP_8C(0x00FE, 0, 400)
    OP_8C(0x00FE, 270, 400)
    OP_8C(0x00FE, 180, 400)

    Jump('loc_EB6')

    def _loc_EDE(): pass

    label('loc_EDE')

    Return()

# id: 0x0009 offset: 0xEDF
@scena.Code('func_09_EDF')
def func_09_EDF():
    SetChrChipByIndex(0x00FE, 10)
    Sleep(50)

    def _loc_EE9(): pass

    label('loc_EE9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F1D',
    )

    OP_90(0x00FE, 500, 0, -500, 4000, 0x00)
    OP_90(0x00FE, -500, 0, 500, 4100, 0x00)

    Jump('loc_EE9')

    def _loc_F1D(): pass

    label('loc_F1D')

    Return()

# id: 0x000A offset: 0xF1E
@scena.Code('func_0A_F1E')
def func_0A_F1E():
    SetChrChipByIndex(0x00FE, 10)
    Sleep(50)

    def _loc_F28(): pass

    label('loc_F28')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F5C',
    )

    OP_90(0x00FE, 0, 0, -1000, 4200, 0x00)
    OP_90(0x00FE, 0, 0, 1000, 4300, 0x00)

    Jump('loc_F28')

    def _loc_F5C(): pass

    label('loc_F5C')

    Return()

# id: 0x000B offset: 0xF5D
@scena.Code('func_0B_F5D')
def func_0B_F5D():
    EventBegin(0x00)
    ClearMapFlags(0x00000010)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    SetChrPos(0x0008, -2300, 0, 17510, 0)
    SetChrPos(0x0009, -2300, 0, 24240, 180)
    SetChrPos(0x000A, -4980, 0, 20880, 90)
    SetChrPos(0x000D, -12080, 0, 15010, 90)
    SetChrPos(0x000E, -12900, 0, 16840, 90)
    SetChrPos(0x000F, -13490, 0, 18730, 90)
    SetChrPos(0x0010, -14010, 0, 15710, 90)
    SetChrPos(0x0011, -14670, 0, 17570, 90)
    SetChrPos(0x0012, -15200, 0, 19820, 90)
    SetChrPos(0x001D, -13510, 0, 22660, 90)
    SetChrPos(0x001E, -12880, 0, 24340, 90)
    SetChrPos(0x001F, -11920, 0, 26130, 90)
    SetChrPos(0x0020, -15170, 0, 22090, 90)
    SetChrPos(0x0021, -14580, 0, 23690, 90)
    SetChrPos(0x0022, -13960, 0, 25780, 90)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 1)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 6)
    LoadEffect(0x00, 'map\\\\mp009_00.eff')
    OP_6D(-16450, 0, 14000, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(247000, 0)
    OP_6E(316, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_1136')
    def lambda_1136():
        OP_6D(-16450, 0, 28000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1136)

    @scena.Lambda('lambda_114E')
    def lambda_114E():
        OP_6C(310000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_114E)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_1163')
    def lambda_1163():
        OP_6D(-2680, 0, 21130, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1163)

    @scena.Lambda('lambda_117B')
    def lambda_117B():
        OP_67(0, 4810, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_117B)

    @scena.Lambda('lambda_1193')
    def lambda_1193():
        OP_6B(2760, 4500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_1193)

    @scena.Lambda('lambda_11A3')
    def lambda_11A3():
        OP_6C(296000, 4500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_11A3)

    @scena.Lambda('lambda_11B3')
    def lambda_11B3():
        OP_6E(443, 4500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_11B3)

    WaitForThreadExit(0x0009, 0x0001)
    Fade(500)
    OP_6D(-5790, 0, 20930, 0)
    OP_67(0, 4810, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(271000, 0)
    OP_6E(443, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0600240024V#163F#5P双方，预备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0600240025V#162F#5P#5S开始！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    OP_59()

    ExecExpressionWithValue(
        0x0024,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0024,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0024,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_12CE')
    def lambda_12CE():
        OP_8F(0x00FE, -11340, 0, 20880, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_12CE)

    OP_DB()
    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0009, 0x0020)
    SetChrFlags(0x0009, 0x0040)

    @scena.Lambda('lambda_12FE')
    def lambda_12FE():
        OP_6D(-2710, 0, 25430, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_12FE)

    @scena.Lambda('lambda_1316')
    def lambda_1316():
        OP_6B(1740, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1316)

    @scena.Lambda('lambda_1326')
    def lambda_1326():
        OP_6C(336000, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1326)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 7)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0009,
        (
            '#0100240026V#177F#2P#8A──呀啊啊啊啊啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1388')
    def lambda_1388():
        OP_6D(-3520, 0, 18740, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1388)

    @scena.Lambda('lambda_13A0')
    def lambda_13A0():
        OP_6B(1840, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13A0)

    @scena.Lambda('lambda_13B0')
    def lambda_13B0():
        OP_6C(296000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_13B0)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)

    @scena.Lambda('lambda_13CA')
    def lambda_13CA():
        OP_8E(0x00FE, -2300, 0, 20800, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_13CA)

    WaitForThreadExit(0x0009, 0x0000)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 1)

    @scena.Lambda('lambda_13FE')
    def lambda_13FE():
        OP_8F(0x00FE, -2300, 0, 19020, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_13FE)

    @scena.Lambda('lambda_1419')
    def lambda_1419():
        OP_99(0x00FE, 0x04, 0x06, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1419)

    @scena.Lambda('lambda_1429')
    def lambda_1429():
        OP_8F(0x00FE, -2300, 0, 17210, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1429)

    WaitForThreadExit(0x0009, 0x0000)
    PlayEffect(0x00, 0xFF, 0x0008, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(400)

    @scena.Lambda('lambda_1491')
    def lambda_1491():
        OP_6C(278000, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1491)

    @scena.Lambda('lambda_14A1')
    def lambda_14A1():
        OP_6B(2040, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14A1)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 5)

    @scena.Lambda('lambda_14BB')
    def lambda_14BB():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x0000544C, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_14BB)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 7)
    Sleep(200)

    @scena.Lambda('lambda_14F2')
    def lambda_14F2():
        OP_6D(-3520, 0, 18250, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_14F2)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)

    @scena.Lambda('lambda_151D')
    def lambda_151D():
        OP_8E(0x00FE, -2300, 0, 20240, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_151D)

    WaitForThreadExit(0x0009, 0x0000)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 9)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 7)

    @scena.Lambda('lambda_1551')
    def lambda_1551():
        OP_8F(0x00FE, -2300, 0, 18920, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1551)

    @scena.Lambda('lambda_156C')
    def lambda_156C():
        OP_99(0x00FE, 0x09, 0x0A, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_156C)

    @scena.Lambda('lambda_157C')
    def lambda_157C():
        OP_8F(0x00FE, -2300, 0, 16910, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_157C)

    PlayEffect(0x00, 0xFF, 0x0008, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(400)

    @scena.Lambda('lambda_15DF')
    def lambda_15DF():
        OP_6D(-3520, 0, 15920, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_15DF)

    @scena.Lambda('lambda_15F7')
    def lambda_15F7():
        OP_6C(226000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_15F7)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 7)
    Sleep(300)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 2)

    @scena.Lambda('lambda_1629')
    def lambda_1629():
        OP_8F(0x00FE, -2300, 0, 17920, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1629)

    @scena.Lambda('lambda_1644')
    def lambda_1644():
        OP_99(0x00FE, 0x07, 0x08, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1644)

    @scena.Lambda('lambda_1654')
    def lambda_1654():
        OP_8F(0x00FE, -2300, 0, 16110, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1654)

    OP_23(0x00D6)
    PlayEffect(0x00, 0xFF, 0x0008, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    @scena.Lambda('lambda_16BA')
    def lambda_16BA():
        OP_6D(-3520, 0, 16120, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_16BA)

    @scena.Lambda('lambda_16D2')
    def lambda_16D2():
        OP_6B(1840, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16D2)

    @scena.Lambda('lambda_16E2')
    def lambda_16E2():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_16E2)

    @scena.Lambda('lambda_16FC')
    def lambda_16FC():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_16FC)

    @scena.Lambda('lambda_1716')
    def lambda_1716():
        OP_8F(0x00FE, -2300, 0, 16560, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1716)

    Sleep(150)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 1)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 7)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 6)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 4)

    @scena.Lambda('lambda_1771')
    def lambda_1771():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00003E6C, 0x00000190, 0x00004E20)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1771)

    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_1799')
    def lambda_1799():
        OP_99(0x00FE, 0x06, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1799)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 3)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_17FB')
    def lambda_17FB():
        OP_6D(-2750, 0, 20070, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_17FB)

    @scena.Lambda('lambda_1813')
    def lambda_1813():
        OP_6C(192000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1813)

    @scena.Lambda('lambda_1823')
    def lambda_1823():
        OP_67(0, 7000, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1823)

    @scena.Lambda('lambda_183B')
    def lambda_183B():
        OP_6B(1840, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_183B)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 6)

    @scena.Lambda('lambda_1855')
    def lambda_1855():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x000056EA, 0x00000320, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1855)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 5)

    @scena.Lambda('lambda_1887')
    def lambda_1887():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00005D98, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1887)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 7)
    Sleep(1000)

    @scena.Lambda('lambda_18BE')
    def lambda_18BE():
        OP_6D(-2470, 0, 19840, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_18BE)

    @scena.Lambda('lambda_18D6')
    def lambda_18D6():
        OP_6C(184000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18D6)

    @scena.Lambda('lambda_18E6')
    def lambda_18E6():
        OP_67(0, 3850, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_18E6)

    @scena.Lambda('lambda_18FE')
    def lambda_18FE():
        OP_6B(1720, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_18FE)

    Sleep(200)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)
    Sleep(200)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1949')
    def lambda_1949():
        OP_6D(-2280, 0, 18410, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1949)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)

    @scena.Lambda('lambda_196B')
    def lambda_196B():
        OP_8E(0x00FE, -2300, 0, 18130, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_196B)

    Sleep(200)

    SetChrPos(0x0009, -2300, 0, 23960, 180)

    @scena.Lambda('lambda_199C')
    def lambda_199C():
        OP_8E(0x00FE, -2300, 0, 18130, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_199C)

    OP_6D(-2250, 0, 22320, 0)
    OP_67(0, 3850, -10000, 0)
    OP_6B(1660, 0)
    OP_6C(1000, 0)
    OP_6E(443, 0)

    @scena.Lambda('lambda_19F4')
    def lambda_19F4():
        OP_6D(-2250, 0, 19120, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_19F4)

    WaitForThreadExit(0x0009, 0x0000)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 0)

    @scena.Lambda('lambda_1A1B')
    def lambda_1A1B():
        OP_8F(0x00FE, -2300, 0, 17020, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1A1B)

    @scena.Lambda('lambda_1A36')
    def lambda_1A36():
        OP_99(0x00FE, 0x00, 0x01, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1A36)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 1)
    OP_8C(0x0008, 45, 0)

    @scena.Lambda('lambda_1A57')
    def lambda_1A57():
        OP_8F(0x00FE, -3010, 0, 15680, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1A57)

    Sleep(100)

    OP_22(0x0084, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0009, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 2)
    OP_8C(0x0009, 225, 0)
    Sleep(200)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1AB3')
    def lambda_1AB3():
        OP_6D(-3820, 0, 16950, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1AB3)

    @scena.Lambda('lambda_1ACB')
    def lambda_1ACB():
        OP_6C(315000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1ACB)

    @scena.Lambda('lambda_1ADB')
    def lambda_1ADB():
        OP_8F(0x00FE, -2620, 0, 16329, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1ADB)

    @scena.Lambda('lambda_1AF6')
    def lambda_1AF6():
        OP_99(0x00FE, 0x02, 0x03, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1AF6)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 6)
    OP_8C(0x0008, 0, 0)

    @scena.Lambda('lambda_1B17')
    def lambda_1B17():
        OP_8F(0x00FE, -2430, 0, 14840, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1B17)

    Sleep(200)

    OP_22(0x0084, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0009, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    @scena.Lambda('lambda_1B54')
    def lambda_1B54():
        OP_6D(-3120, 0, 16810, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1B54)

    @scena.Lambda('lambda_1B6C')
    def lambda_1B6C():
        OP_67(0, 4680, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B6C)

    @scena.Lambda('lambda_1B84')
    def lambda_1B84():
        OP_6B(2200, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1B84)

    OP_8C(0x0009, 0, 1000)
    OP_8C(0x0009, 90, 1000)

    @scena.Lambda('lambda_1BA2')
    def lambda_1BA2():
        OP_8C(0x00FE, 180, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1BA2)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 9)

    @scena.Lambda('lambda_1BBA')
    def lambda_1BBA():
        OP_96(0x00FE, 0xFFFFF81C, 0x00000000, 0x00004CEA, 0x000007D0, 0x00001770)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1BBA)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x0009, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)

    @scena.Lambda('lambda_1BFB')
    def lambda_1BFB():
        OP_8F(0x00FE, -2020, 0, 12920, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1BFB)

    @scena.Lambda('lambda_1C16')
    def lambda_1C16():
        OP_99(0x00FE, 0x04, 0x06, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1C16)

    OP_22(0x00A3, 0x00, 0x64)
    Sleep(100)

    OP_22(0x0084, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 4)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(600)

    @scena.Lambda('lambda_1C62')
    def lambda_1C62():
        OP_6D(-3120, 0, 19040, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1C62)

    @scena.Lambda('lambda_1C7A')
    def lambda_1C7A():
        OP_6C(270000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C7A)

    @scena.Lambda('lambda_1C8A')
    def lambda_1C8A():
        OP_6B(1820, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1C8A)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 7)
    OP_8C(0x0009, 90, 1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1CB4')
    def lambda_1CB4():
        OP_8C(0x00FE, 0, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1CB4)

    @scena.Lambda('lambda_1CC2')
    def lambda_1CC2():
        OP_8F(0x00FE, -2020, 0, 16020, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1CC2)

    WaitForThreadExit(0x0009, 0x0000)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)
    WaitForThreadExit(0x0009, 0x0001)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)

    @scena.Lambda('lambda_1CFB')
    def lambda_1CFB():
        OP_8F(0x00FE, -2020, 0, 17540, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1CFB)

    @scena.Lambda('lambda_1D16')
    def lambda_1D16():
        OP_99(0x00FE, 0x04, 0x06, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1D16)

    Sleep(100)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 5)

    @scena.Lambda('lambda_1D35')
    def lambda_1D35():
        OP_8F(0x00FE, -1920, 0, 19690, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1D35)

    WaitForThreadExit(0x0009, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayEffect(0x00, 0xFF, 0x0008, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)

    @scena.Lambda('lambda_1D98')
    def lambda_1D98():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1D98)

    Sleep(600)

    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_1DBC')
    def lambda_1DBC():
        OP_6D(-3120, 0, 15960, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1DBC)

    @scena.Lambda('lambda_1DD4')
    def lambda_1DD4():
        OP_6C(235000, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1DD4)

    @scena.Lambda('lambda_1DE4')
    def lambda_1DE4():
        OP_6B(2240, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1DE4)

    ChrTurnDirection(0x0008, 0x0009, 0)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 4)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 7)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1E18')
    def lambda_1E18():
        OP_8F(0x00FE, -1920, 0, 18710, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1E18)

    WaitForThreadExit(0x0008, 0x0000)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 5)
    Sleep(100)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x0209, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 6)

    @scena.Lambda('lambda_1E5F')
    def lambda_1E5F():
        OP_8F(0x00FE, -1920, 0, 13930, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1E5F)

    WaitForThreadExit(0x0009, 0x0000)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 4)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 6)

    @scena.Lambda('lambda_1E93')
    def lambda_1E93():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1E93)

    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x0009,
        (
            '#0100240027V#172F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160240028V#1126F#6P怎么回事！？\n',
            '行动太过直线化！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240029V你用的是细剑，就应该使出\n',
            '流畅的进攻套路！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240030V想想我教过你的东西！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100240031V#173F#5P是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100240032V#177F……是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    Fade(250)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)
    OP_0D()

    @scena.Lambda('lambda_1FCA')
    def lambda_1FCA():
        OP_6D(-3120, 0, 12880, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1FCA)

    @scena.Lambda('lambda_1FE2')
    def lambda_1FE2():
        OP_6B(1940, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FE2)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1FFC')
    def lambda_1FFC():
        OP_6D(-2360, 0, 19240, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1FFC)

    @scena.Lambda('lambda_2014')
    def lambda_2014():
        OP_6C(322000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2014)

    @scena.Lambda('lambda_2024')
    def lambda_2024():
        OP_6B(2440, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2024)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)
    OP_7D(0x00, 0x0009, 0x0032, 0x01F4)

    @scena.Lambda('lambda_2046')
    def lambda_2046():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2046')

    DispatchAsync2(0x0009, 0x0003, lambda_2046)

    @scena.Lambda('lambda_2057')
    def lambda_2057():
        OP_96(0x00FE, 0x00000BFE, 0x00000000, 0x000048BC, 0x00000190, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2057)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_207F')
    def lambda_207F():
        OP_96(0x00FE, 0xFFFFF880, 0x00000000, 0x00005A82, 0x00000190, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_207F)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_20A7')
    def lambda_20A7():
        OP_96(0x00FE, 0xFFFFE4DA, 0x00000000, 0x000048BC, 0x00000190, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_20A7)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0009, 0x0000, 0x0000)
    TerminateThread(0x0009, 0x03)
    Fade(500)
    OP_8C(0x0009, 79, 0)
    OP_6D(-7350, 0, 21010, 0)
    OP_67(0, 2370, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(304000, 0)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 7)
    Sleep(400)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)

    @scena.Lambda('lambda_213D')
    def lambda_213D():
        OP_6D(-5290, 0, 21010, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_213D)

    @scena.Lambda('lambda_2155')
    def lambda_2155():
        OP_8F(0x00FE, -4320, 0, 18620, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2155)

    WaitForThreadExit(0x0009, 0x0000)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)

    @scena.Lambda('lambda_217F')
    def lambda_217F():
        OP_8F(0x00FE, -3170, 0, 18620, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_217F)

    @scena.Lambda('lambda_219A')
    def lambda_219A():
        OP_99(0x00FE, 0x04, 0x06, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_219A)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 1)
    OP_8C(0x0008, 349, 0)

    @scena.Lambda('lambda_21BB')
    def lambda_21BB():
        OP_8F(0x00FE, -860, 0, 18160, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_21BB)

    Sleep(100)

    OP_22(0x0084, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0000)
    WaitForThreadExit(0x0008, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(400)

    @scena.Lambda('lambda_21F8')
    def lambda_21F8():
        OP_6D(-4680, 0, 19770, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_21F8)

    @scena.Lambda('lambda_2210')
    def lambda_2210():
        OP_67(0, 4800, -10000, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2210)

    @scena.Lambda('lambda_2228')
    def lambda_2228():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_2228')

    DispatchAsync2(0x0008, 0x0003, lambda_2228)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 5)

    @scena.Lambda('lambda_2243')
    def lambda_2243():
        OP_96(0x00FE, 0xFFFFEA0C, 0x00000000, 0x000048BC, 0x00000190, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2243)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 7)
    TerminateThread(0x0008, 0x03)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)

    @scena.Lambda('lambda_2283')
    def lambda_2283():
        OP_6D(-4690, 0, 18490, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2283)

    @scena.Lambda('lambda_229B')
    def lambda_229B():
        OP_6C(270000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_229B)

    @scena.Lambda('lambda_22AB')
    def lambda_22AB():
        OP_67(0, 3680, -10000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_22AB)

    OP_7D(0x00, 0x0009, 0x0032, 0x00C8)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)

    @scena.Lambda('lambda_22D5')
    def lambda_22D5():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_22D5')

    DispatchAsync2(0x0009, 0x0003, lambda_22D5)

    @scena.Lambda('lambda_22E6')
    def lambda_22E6():
        OP_8F(0x00FE, -3510, 0, 20880, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_22E6)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0009, 0x0000, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x0009, 0x03)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 2)

    @scena.Lambda('lambda_232A')
    def lambda_232A():
        OP_96(0x00FE, 0xFFFFF862, 0x00000000, 0x00004B5A, 0x00000320, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_232A)

    OP_8C(0x0009, 214, 2000)
    OP_8C(0x0009, 304, 2000)
    OP_8C(0x0009, 34, 2000)
    OP_8C(0x0009, 124, 2000)
    WaitForThreadExit(0x0009, 0x0000)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 3)
    PlayEffect(0x00, 0xFF, 0x0008, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 7)
    OP_8C(0x0008, 315, 0)

    @scena.Lambda('lambda_23BE')
    def lambda_23BE():
        OP_8F(0x00FE, 380, 0, 17540, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_23BE)

    WaitForThreadExit(0x0008, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 5)

    @scena.Lambda('lambda_23F6')
    def lambda_23F6():
        OP_96(0x00FE, 0xFFFFF218, 0x00000000, 0x00004F88, 0x00000258, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_23F6)

    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0000)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)

    @scena.Lambda('lambda_2428')
    def lambda_2428():
        OP_6D(-370, 0, 16280, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2428)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)
    OP_7D(0x00, 0x0009, 0x0032, 0x01F4)

    @scena.Lambda('lambda_2452')
    def lambda_2452():
        OP_96(0x00FE, 0x00001068, 0x00000000, 0x000039E4, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2452)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x00A3, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0009, 0x0000, 0x0000)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_24AB')
    def lambda_24AB():
        OP_6D(-2090, 0, 18000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_24AB)

    @scena.Lambda('lambda_24C3')
    def lambda_24C3():
        OP_6C(258000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_24C3)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)

    @scena.Lambda('lambda_24DD')
    def lambda_24DD():
        OP_8F(0x00FE, 1920, 0, 16390, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_24DD)

    @scena.Lambda('lambda_24F8')
    def lambda_24F8():
        OP_99(0x00FE, 0x04, 0x06, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_24F8)

    @scena.Lambda('lambda_2508')
    def lambda_2508():
        OP_8C(0x00FE, 306, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2508)

    Sleep(100)

    OP_22(0x0084, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 9)

    @scena.Lambda('lambda_252A')
    def lambda_252A():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_252A)

    @scena.Lambda('lambda_2538')
    def lambda_2538():
        OP_96(0x00FE, 0xFFFFF3F8, 0x00000000, 0x00004EC0, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2538)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 3)
    WaitForThreadExit(0x0008, 0x0000)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x0008, 0x03)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 4)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_259C')
    def lambda_259C():
        OP_6D(-3700, 0, 19950, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_259C)

    @scena.Lambda('lambda_25B4')
    def lambda_25B4():
        OP_6C(282000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_25B4)

    @scena.Lambda('lambda_25C4')
    def lambda_25C4():
        OP_6B(2000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_25C4)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)
    OP_7D(0x00, 0x0009, 0x0032, 0x00C8)

    @scena.Lambda('lambda_25E6')
    def lambda_25E6():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_25E6')

    DispatchAsync2(0x0009, 0x0003, lambda_25E6)

    @scena.Lambda('lambda_25F7')
    def lambda_25F7():
        OP_8F(0x00FE, -1090, 0, 18620, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_25F7)

    WaitForThreadExit(0x0009, 0x0000)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)

    @scena.Lambda('lambda_2621')
    def lambda_2621():
        OP_6D(-5530, 0, 18670, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2621)

    @scena.Lambda('lambda_2639')
    def lambda_2639():
        OP_96(0x00FE, 0xFFFFF02E, 0x00000000, 0x00003FF2, 0x00000258, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2639)

    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0000)
    TerminateThread(0x0009, 0x03)
    OP_7D(0x01, 0x0009, 0x0000, 0x0000)

    @scena.Lambda('lambda_266D')
    def lambda_266D():
        OP_6D(-4720, 0, 20630, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_266D)

    @scena.Lambda('lambda_2685')
    def lambda_2685():
        OP_67(0, 3060, -10000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2685)

    @scena.Lambda('lambda_269D')
    def lambda_269D():
        OP_6C(258000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_269D)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 12)

    @scena.Lambda('lambda_26B7')
    def lambda_26B7():
        OP_96(0x00FE, 0xFFFFF3B2, 0x00000000, 0x000049FC, 0x00000578, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_26B7)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x00A4, 0x00, 0x64)
    Sleep(100)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 0)
    WaitForThreadExit(0x0009, 0x0000)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 1)
    PlayEffect(0x00, 0xFF, 0x0008, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 2)
    OP_8C(0x0008, 213, 0)

    @scena.Lambda('lambda_2759')
    def lambda_2759():
        OP_8F(0x00FE, -1940, 0, 22640, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2759)

    @scena.Lambda('lambda_2774')
    def lambda_2774():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2774)

    WaitForThreadExit(0x0008, 0x0000)
    Sleep(200)

    @scena.Lambda('lambda_2798')
    def lambda_2798():
        OP_6D(-3540, 0, 21820, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2798)

    @scena.Lambda('lambda_27B0')
    def lambda_27B0():
        OP_67(0, 4059, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_27B0)

    @scena.Lambda('lambda_27C8')
    def lambda_27C8():
        OP_6C(234000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_27C8)

    @scena.Lambda('lambda_27D8')
    def lambda_27D8():
        OP_6B(2400, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_27D8)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 3)

    @scena.Lambda('lambda_27F2')
    def lambda_27F2():
        OP_96(0x00FE, 0xFFFFFCFE, 0x00000000, 0x000065FE, 0x00000258, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_27F2)

    @scena.Lambda('lambda_2810')
    def lambda_2810():
        OP_8C(0x00FE, 189, 200)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2810)

    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 4)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    Sleep(200)

    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0008,
        (
            '#0160240033V#1125F#6P这就对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240034V#1122F那么，接招吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    OP_8C(0x0009, 9, 0)
    OP_8C(0x0008, 189, 0)

    @scena.Lambda('lambda_28D3')
    def lambda_28D3():
        OP_6D(-2150, 0, 25310, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_28D3)

    @scena.Lambda('lambda_28EB')
    def lambda_28EB():
        OP_67(0, 3360, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_28EB)

    @scena.Lambda('lambda_2903')
    def lambda_2903():
        OP_6B(1800, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2903)

    Fade(250)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 8)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(400)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_2940')
    def lambda_2940():
        OP_6D(-5080, 0, 19800, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2940)

    @scena.Lambda('lambda_2958')
    def lambda_2958():
        OP_6C(270000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2958)

    @scena.Lambda('lambda_2968')
    def lambda_2968():
        OP_6B(2200, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2968)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 9)
    SetChrFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_2987')
    def lambda_2987():
        OP_96(0x00FE, 0xFFFFF3B2, 0x000000C8, 0x00004F38, 0x00000960, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2987)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x00A3, 0x00, 0x64)
    Sleep(250)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 4)

    @scena.Lambda('lambda_29C4')
    def lambda_29C4():
        OP_99(0x00FE, 0x04, 0x05, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_29C4)

    WaitForThreadExit(0x0008, 0x0000)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 2)

    @scena.Lambda('lambda_2A1D')
    def lambda_2A1D():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x00000258, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2A1D)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    @scena.Lambda('lambda_2A45')
    def lambda_2A45():
        OP_6D(-5080, 0, 23430, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2A45)

    @scena.Lambda('lambda_2A5D')
    def lambda_2A5D():
        OP_67(0, 4360, -10000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A5D)

    @scena.Lambda('lambda_2A75')
    def lambda_2A75():
        OP_6C(315000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A75)

    @scena.Lambda('lambda_2A85')
    def lambda_2A85():
        OP_8F(0x00FE, -3150, 0, 18440, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2A85)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 3)
    ClearChrFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_2AAF')
    def lambda_2AAF():
        OP_96(0x00FE, 0xFFFFF3B2, 0x00000000, 0x00005D02, 0x000007D0, 0x00001388)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2AAF)

    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 4)
    Sleep(200)

    @scena.Lambda('lambda_2AF1')
    def lambda_2AF1():
        OP_6D(-4860, 0, 20850, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2AF1)

    @scena.Lambda('lambda_2B09')
    def lambda_2B09():
        OP_6B(1960, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2B09)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 9)

    @scena.Lambda('lambda_2B2C')
    def lambda_2B2C():
        OP_8F(0x00FE, -3150, 0, 21180, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2B2C)

    WaitForThreadExit(0x0008, 0x0000)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 0)
    Sleep(100)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 1)

    @scena.Lambda('lambda_2B65')
    def lambda_2B65():
        OP_8F(0x00FE, -3150, 0, 19960, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2B65)

    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 3)

    @scena.Lambda('lambda_2BC4')
    def lambda_2BC4():
        OP_8F(0x00FE, -3150, 0, 17870, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2BC4)

    @scena.Lambda('lambda_2BDF')
    def lambda_2BDF():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2BDF)

    Sleep(200)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 0)
    Sleep(200)

    @scena.Lambda('lambda_2C16')
    def lambda_2C16():
        OP_6D(-4860, 0, 19860, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2C16)

    @scena.Lambda('lambda_2C2E')
    def lambda_2C2E():
        OP_6B(1760, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2C2E)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 1)

    @scena.Lambda('lambda_2C51')
    def lambda_2C51():
        OP_8F(0x00FE, -3150, 0, 19050, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2C51)

    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 3)

    @scena.Lambda('lambda_2CB0')
    def lambda_2CB0():
        OP_8F(0x00FE, -3150, 0, 16960, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2CB0)

    @scena.Lambda('lambda_2CCB')
    def lambda_2CCB():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2CCB)

    Sleep(200)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 0)
    Sleep(150)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 5)

    @scena.Lambda('lambda_2D0C')
    def lambda_2D0C():
        OP_96(0x00FE, 0xFFFFE7C8, 0x00000000, 0x00003C64, 0x00000258, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2D0C)

    WaitForThreadExit(0x0008, 0x0000)
    Sleep(50)

    @scena.Lambda('lambda_2D34')
    def lambda_2D34():
        OP_6D(-4860, 0, 18870, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2D34)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 1)

    @scena.Lambda('lambda_2D56')
    def lambda_2D56():
        OP_8F(0x00FE, -3150, 0, 18140, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2D56)

    OP_22(0x0084, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_2D7B')
    def lambda_2D7B():
        OP_6D(-4860, 0, 17620, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2D7B)

    @scena.Lambda('lambda_2D93')
    def lambda_2D93():
        OP_6B(2060, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D93)

    @scena.Lambda('lambda_2DA3')
    def lambda_2DA3():
        OP_67(0, 3360, -10000, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DA3)

    @scena.Lambda('lambda_2DBB')
    def lambda_2DBB():
        OP_6C(304000, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2DBB)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 6)
    OP_7D(0x00, 0x0008, 0x0014, 0x00C8)
    OP_8C(0x0008, 259, 0)

    @scena.Lambda('lambda_2DE4')
    def lambda_2DE4():
        OP_96(0x00FE, 0xFFFFE7C8, 0x00000000, 0x00004204, 0x00000190, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2DE4)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 2)
    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0008, 0x0000, 0x0000)
    OP_8C(0x0008, 214, 800)
    OP_8C(0x0008, 169, 800)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 7)

    @scena.Lambda('lambda_2E40')
    def lambda_2E40():
        OP_6D(-7640, 0, 14240, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2E40)

    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 6)

    @scena.Lambda('lambda_2E9C')
    def lambda_2E9C():
        OP_96(0x00FE, 0xFFFFE7C8, 0x00000000, 0x0000328C, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2E9C)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_2EC4')
    def lambda_2EC4():
        OP_96(0x00FE, 0xFFFFE7C8, 0x00000000, 0x00002738, 0x00000258, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2EC4)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 3)

    @scena.Lambda('lambda_2EEC')
    def lambda_2EEC():
        OP_96(0x00FE, 0xFFFFE7C8, 0x00000000, 0x00004FD8, 0x00000190, 0x00001388)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2EEC)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 4)
    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 4)
    Sleep(200)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 9)

    @scena.Lambda('lambda_2F4A')
    def lambda_2F4A():
        OP_8F(0x00FE, -6200, 0, 12180, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2F4A)

    Sleep(200)

    SetChrPos(0x0008, -6200, 0, 20440, 180)

    @scena.Lambda('lambda_2F7B')
    def lambda_2F7B():
        OP_8F(0x00FE, -6200, 0, 12180, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2F7B)

    Fade(500)
    OP_6D(-7500, 0, 12160, 0)
    OP_6C(220000, 0)
    OP_6E(443, 0)

    @scena.Lambda('lambda_2FBE')
    def lambda_2FBE():
        OP_6D(-7460, 0, 9900, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2FBE)

    @scena.Lambda('lambda_2FD6')
    def lambda_2FD6():
        OP_6B(1800, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FD6)

    Sleep(100)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 11)
    WaitForThreadExit(0x0008, 0x0000)

    @scena.Lambda('lambda_3003')
    def lambda_3003():
        OP_6D(-7460, 0, 10900, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3003)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 10)

    @scena.Lambda('lambda_3025')
    def lambda_3025():
        OP_8F(0x00FE, -6200, 0, 11140, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3025)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 6)
    OP_7D(0x00, 0x0008, 0x0014, 0x00C8)

    @scena.Lambda('lambda_3052')
    def lambda_3052():
        OP_8F(0x00FE, -7160, 0, 13750, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3052)

    WaitForThreadExit(0x0008, 0x0000)
    OP_7D(0x01, 0x0008, 0x0000, 0x0000)
    OP_22(0x0084, 0x00, 0x64)
    Sleep(300)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_308D')
    def lambda_308D():
        OP_6D(-5960, 0, 10310, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_308D)

    @scena.Lambda('lambda_30A5')
    def lambda_30A5():
        OP_6B(2060, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_30A5)

    @scena.Lambda('lambda_30B5')
    def lambda_30B5():
        OP_67(0, 4360, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_30B5)

    @scena.Lambda('lambda_30CD')
    def lambda_30CD():
        OP_6C(110000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_30CD)

    @scena.Lambda('lambda_30DD')
    def lambda_30DD():
        OP_8F(0x00FE, -8220, 0, 10800, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_30DD)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 2)

    @scena.Lambda('lambda_3102')
    def lambda_3102():
        OP_8C(0x00FE, 245, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3102)

    OP_8C(0x0008, 90, 1500)
    OP_8C(0x0008, 0, 1500)
    OP_8C(0x0008, 270, 1500)
    OP_8C(0x0008, 180, 1500)
    OP_8C(0x0008, 90, 1500)
    OP_8C(0x0008, 66, 1500)
    WaitForThreadExit(0x0008, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 7)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 6)

    @scena.Lambda('lambda_31A5')
    def lambda_31A5():
        OP_96(0x00FE, 0xFFFFFE5C, 0x00000000, 0x00003458, 0x00000960, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_31A5)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    @scena.Lambda('lambda_31D3')
    def lambda_31D3():
        OP_6D(-1220, 0, 8000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_31D3)

    @scena.Lambda('lambda_31EB')
    def lambda_31EB():
        OP_67(0, 3400, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_31EB)

    @scena.Lambda('lambda_3203')
    def lambda_3203():
        OP_6C(154000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3203)

    @scena.Lambda('lambda_3213')
    def lambda_3213():
        OP_6B(2320, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3213)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 9)

    @scena.Lambda('lambda_322D')
    def lambda_322D():
        OP_96(0x00FE, 0xFFFFFE5C, 0x00000000, 0x00003458, 0x000007D0, 0x00001770)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_322D)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x00A3, 0x00, 0x64)
    Sleep(100)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 4)

    @scena.Lambda('lambda_326A')
    def lambda_326A():
        OP_99(0x00FE, 0x04, 0x05, 0x00000708)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_326A)

    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0009, 0x00)

    @scena.Lambda('lambda_3287')
    def lambda_3287():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3287)

    OP_22(0x0209, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(200)

    WaitForThreadExit(0x0009, 0x0000)

    @scena.Lambda('lambda_32C4')
    def lambda_32C4():
        OP_6D(-2640, 0, 11340, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_32C4)

    @scena.Lambda('lambda_32DC')
    def lambda_32DC():
        OP_67(0, 6180, -10000, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_32DC)

    @scena.Lambda('lambda_32F4')
    def lambda_32F4():
        OP_6C(130000, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_32F4)

    @scena.Lambda('lambda_3304')
    def lambda_3304():
        OP_96(0x00FE, 0x00000D0C, 0x00000000, 0x00003480, 0x000007D0, 0x00002328)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3304)

    @scena.Lambda('lambda_3322')
    def lambda_3322():
        OP_96(0x00FE, 0xFFFFDF44, 0x00000000, 0x00002C74, 0x000007D0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3322)

    Sleep(100)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 3)
    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_3364')
    def lambda_3364():
        OP_6D(-710, 0, 11560, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3364)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 9)

    @scena.Lambda('lambda_3386')
    def lambda_3386():
        OP_96(0x00FE, 0xFFFFEBA6, 0x00000000, 0x00002E72, 0x00000190, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3386)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 4)
    ClearChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_33CD')
    def lambda_33CD():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_33CD)

    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0003)
    OP_DC()

    ChrTalk(
        0x0009,
        (
            '#0100240035V#175F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0009, 0x0001)
    Fade(500)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0160240036V#1127F#6P防守基本相同！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240037V注意对方动作的意图，\n',
            '同时想好攻守的步骤！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100240038V#178F#5P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()

    @scena.Lambda('lambda_34BF')
    def lambda_34BF():
        OP_6D(1340, 0, 10040, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_34BF)

    @scena.Lambda('lambda_34D7')
    def lambda_34D7():
        OP_67(0, 2660, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_34D7)

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0100240039V#177F#5P#3S#15A哈啊啊啊啊啊啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 7)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(500)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)
    OP_7D(0x00, 0x0009, 0x0032, 0x01F4)

    @scena.Lambda('lambda_3577')
    def lambda_3577():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_3577')

    DispatchAsync2(0x0009, 0x0003, lambda_3577)

    @scena.Lambda('lambda_3588')
    def lambda_3588():
        OP_96(0x00FE, 0x0000067C, 0x00000000, 0x00003F01, 0x00000190, 0x00001388)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3588)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_35B0')
    def lambda_35B0():
        OP_8F(0x00FE, -2180, 0, 13710, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_35B0)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_35D5')
    def lambda_35D5():
        OP_96(0x00FE, 0xFFFFFD3A, 0x00000000, 0x00002530, 0x00000190, 0x00001388)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_35D5)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0009, 0x0000, 0x0000)
    TerminateThread(0x0009, 0x03)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_3612')
    def lambda_3612():
        OP_6D(-2540, 0, 11300, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3612)

    @scena.Lambda('lambda_362A')
    def lambda_362A():
        OP_67(0, 4420, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_362A)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 12)

    @scena.Lambda('lambda_364C')
    def lambda_364C():
        OP_96(0x00FE, 0xFFFFF218, 0x00000000, 0x00002954, 0x00000640, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_364C)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 0)
    Sleep(200)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 3)

    @scena.Lambda('lambda_3693')
    def lambda_3693():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_3693')

    DispatchAsync2(0x0008, 0x0003, lambda_3693)

    @scena.Lambda('lambda_36A4')
    def lambda_36A4():
        OP_96(0x00FE, 0xFFFFEACA, 0x00000000, 0x00003DFE, 0x00000258, 0x00001388)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_36A4)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x0084, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 1)
    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 4)
    Sleep(100)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_3703')
    def lambda_3703():
        OP_6D(-5430, 0, 14290, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3703)

    @scena.Lambda('lambda_371B')
    def lambda_371B():
        OP_6C(190000, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_371B)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 3)

    @scena.Lambda('lambda_3735')
    def lambda_3735():
        OP_96(0x00FE, 0xFFFFEA02, 0x00000000, 0x00004C36, 0x00000190, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3735)

    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 4)
    Sleep(100)

    TerminateThread(0x0008, 0x03)

    @scena.Lambda('lambda_3770')
    def lambda_3770():
        OP_6D(-6870, 0, 16030, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3770)

    @scena.Lambda('lambda_3788')
    def lambda_3788():
        OP_67(0, 3360, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3788)

    @scena.Lambda('lambda_37A0')
    def lambda_37A0():
        OP_6C(238000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_37A0)

    @scena.Lambda('lambda_37B0')
    def lambda_37B0():
        OP_6B(2180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_37B0)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)
    OP_7D(0x00, 0x0009, 0x0032, 0x01F4)
    ChrTurnDirection(0x0009, 0x0008, 0)

    @scena.Lambda('lambda_37D9')
    def lambda_37D9():
        OP_8F(0x00FE, -4740, 0, 16079, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_37D9)

    Sleep(100)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 0)
    Sleep(200)

    OP_7D(0x01, 0x0009, 0x0000, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_3819')
    def lambda_3819():
        OP_8F(0x00FE, -5320, 0, 18230, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3819)

    WaitForThreadExit(0x0009, 0x0000)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 3)
    WaitForThreadExit(0x0008, 0x0000)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 1)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    @scena.Lambda('lambda_389A')
    def lambda_389A():
        OP_6D(-6250, 0, 15120, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_389A)

    @scena.Lambda('lambda_38B2')
    def lambda_38B2():
        OP_6B(1980, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38B2)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 0)
    Sleep(400)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_38DA')
    def lambda_38DA():
        OP_8F(0x00FE, -4990, 0, 17180, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_38DA)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 1)

    @scena.Lambda('lambda_38FF')
    def lambda_38FF():
        OP_8F(0x00FE, -4040, 0, 15260, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_38FF)

    WaitForThreadExit(0x0008, 0x0000)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    @scena.Lambda('lambda_3967')
    def lambda_3967():
        OP_6D(-5360, 0, 13720, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3967)

    @scena.Lambda('lambda_397F')
    def lambda_397F():
        OP_6C(236000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_397F)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 5)

    @scena.Lambda('lambda_39AC')
    def lambda_39AC():
        OP_96(0x00FE, 0xFFFFF650, 0x00000000, 0x00002C10, 0x00000258, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_39AC)

    Sleep(400)

    @scena.Lambda('lambda_39CF')
    def lambda_39CF():
        OP_8F(0x00FE, -4540, 0, 16200, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_39CF)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 1)
    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 5)

    @scena.Lambda('lambda_3A08')
    def lambda_3A08():
        OP_8F(0x00FE, -3220, 0, 13030, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3A08)

    WaitForThreadExit(0x0008, 0x0000)
    PlayEffect(0x00, 0xFF, 0x0008, 0, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    @scena.Lambda('lambda_3A70')
    def lambda_3A70():
        OP_6B(1780, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3A70)

    @scena.Lambda('lambda_3A80')
    def lambda_3A80():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3A80)

    @scena.Lambda('lambda_3A9A')
    def lambda_3A9A():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3A9A)

    WaitForThreadExit(0x0101, 0x0000)
    PlayEffect(0x00, 0xFF, 0x0008, 0, 500, -2000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 2000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)

    @scena.Lambda('lambda_3B28')
    def lambda_3B28():
        OP_6D(-3420, 0, 13940, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3B28)

    @scena.Lambda('lambda_3B40')
    def lambda_3B40():
        OP_67(0, 6500, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3B40)

    @scena.Lambda('lambda_3B58')
    def lambda_3B58():
        OP_6C(148000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3B58)

    @scena.Lambda('lambda_3B68')
    def lambda_3B68():
        OP_6B(2180, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3B68)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 2)
    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 3)
    CreateThread(0x0008, 0x03, 0x00, 0x000D)

    @scena.Lambda('lambda_3B93')
    def lambda_3B93():
        OP_96(0x00FE, 0xFFFFECC8, 0x00000000, 0x00002B84, 0x000004B0, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3B93)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0009, 0x03, 0x00, 0x000E)

    @scena.Lambda('lambda_3BC3')
    def lambda_3BC3():
        OP_96(0x00FE, 0xFFFFF542, 0x00000000, 0x00004862, 0x000004B0, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3BC3)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)
    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)
    Sleep(200)

    @scena.Lambda('lambda_3C2F')
    def lambda_3C2F():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x00000258, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3C2F)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_3C57')
    def lambda_3C57():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x00000320, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3C57)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x00, 0x0009, 0x0032, 0x01F4)

    @scena.Lambda('lambda_3C87')
    def lambda_3C87():
        OP_6D(-3810, 0, 12730, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3C87)

    @scena.Lambda('lambda_3C9F')
    def lambda_3C9F():
        OP_67(0, 4600, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C9F)

    @scena.Lambda('lambda_3CB7')
    def lambda_3CB7():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_3CB7')

    DispatchAsync2(0x0009, 0x0003, lambda_3CB7)

    @scena.Lambda('lambda_3CC8')
    def lambda_3CC8():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_3CC8')

    DispatchAsync2(0x0008, 0x0003, lambda_3CC8)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)

    @scena.Lambda('lambda_3CE3')
    def lambda_3CE3():
        OP_96(0x00FE, 0xFFFFF164, 0x00000000, 0x00003B38, 0x00000320, 0x00001388)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3CE3)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_3D0B')
    def lambda_3D0B():
        OP_6C(204000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3D0B)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)

    @scena.Lambda('lambda_3D25')
    def lambda_3D25():
        OP_96(0x00FE, 0xFFFFF7A4, 0x00000000, 0x00002E40, 0x00000320, 0x00001388)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3D25)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 5)

    @scena.Lambda('lambda_3D57')
    def lambda_3D57():
        OP_96(0x00FE, 0xFFFFFA2E, 0x00000000, 0x00003A34, 0x00000320, 0x00001388)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3D57)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_3D7F')
    def lambda_3D7F():
        OP_6C(122000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3D7F)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)

    @scena.Lambda('lambda_3D99')
    def lambda_3D99():
        OP_96(0x00FE, 0xFFFFEFE8, 0x00000000, 0x0000367E, 0x00000320, 0x00001388)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3D99)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_3DC1')
    def lambda_3DC1():
        OP_6D(-3690, 0, 10320, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3DC1)

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 5)

    @scena.Lambda('lambda_3DE3')
    def lambda_3DE3():
        OP_96(0x00FE, 0xFFFFE994, 0x00000000, 0x00003D40, 0x00000320, 0x00001388)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3DE3)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 8)

    @scena.Lambda('lambda_3E15')
    def lambda_3E15():
        OP_96(0x00FE, 0xFFFFE1A6, 0x00000000, 0x00003340, 0x00000320, 0x00001388)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3E15)

    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0009, 0x0000, 0x0000)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 7)
    TerminateThread(0x0009, 0x03)
    TerminateThread(0x0008, 0x03)
    Sleep(200)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_3E65')
    def lambda_3E65():
        OP_6D(-400, 0, 8240, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3E65)

    @scena.Lambda('lambda_3E7D')
    def lambda_3E7D():
        OP_67(0, 3300, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3E7D)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)

    @scena.Lambda('lambda_3E9F')
    def lambda_3E9F():
        OP_8F(0x00FE, -1590, 0, 8990, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3E9F)

    @scena.Lambda('lambda_3EBA')
    def lambda_3EBA():
        OP_99(0x00FE, 0x04, 0x06, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3EBA)

    Sleep(100)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 2)
    OP_8C(0x0008, 205, 0)

    @scena.Lambda('lambda_3EE0')
    def lambda_3EE0():
        OP_8F(0x00FE, -3890, 0, 12700, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3EE0)

    @scena.Lambda('lambda_3EFB')
    def lambda_3EFB():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3EFB)

    PlayEffect(0x00, 0xFF, 0x0008, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0000)
    WaitForThreadExit(0x0008, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_3F70')
    def lambda_3F70():
        OP_6D(-1000, 0, 11820, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3F70)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)

    @scena.Lambda('lambda_3F92')
    def lambda_3F92():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x00000258, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3F92)

    CreateThread(0x0009, 0x03, 0x00, 0x0010)
    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_3FC6')
    def lambda_3FC6():
        OP_8F(0x00FE, -6490, 0, 16110, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3FC6)

    @scena.Lambda('lambda_3FE1')
    def lambda_3FE1():
        OP_99(0x00FE, 0x04, 0x06, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3FE1)

    Sleep(50)

    OP_22(0x0084, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 3)
    OP_8C(0x0008, 257, 0)

    @scena.Lambda('lambda_400C')
    def lambda_400C():
        OP_96(0x00FE, 0xFFFFFF38, 0x00000000, 0x00003584, 0x00000320, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_400C)

    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 4)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    @scena.Lambda('lambda_404C')
    def lambda_404C():
        OP_6D(-1000, 0, 13940, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_404C)

    @scena.Lambda('lambda_4064')
    def lambda_4064():
        OP_6C(118000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4064)

    SetChrChipByIndex(0x0009, 28)
    SetChrSubChip(0x0009, 4)

    @scena.Lambda('lambda_407E')
    def lambda_407E():
        OP_96(0x00FE, 0xFFFFF236, 0x00000000, 0x00004A4C, 0x000004B0, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_407E)

    CreateThread(0x0009, 0x03, 0x00, 0x000E)
    WaitForThreadExit(0x0009, 0x0003)
    OP_8C(0x0009, 147, 0)
    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 3)
    Sleep(50)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 4)
    CreateThread(0x0008, 0x03, 0x00, 0x000F)
    Sleep(200)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_40EC')
    def lambda_40EC():
        OP_6D(1360, 0, 15090, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_40EC)

    @scena.Lambda('lambda_4104')
    def lambda_4104():
        OP_6C(64000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4104)

    @scena.Lambda('lambda_4114')
    def lambda_4114():
        OP_6B(1780, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4114)

    @scena.Lambda('lambda_4124')
    def lambda_4124():
        OP_8F(0x00FE, -950, 400, 14700, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_4124)

    WaitForThreadExit(0x0009, 0x0000)

    @scena.Lambda('lambda_4144')
    def lambda_4144():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_4144)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 5)
    OP_22(0x0209, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 6)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x0009, 0x0000)

    @scena.Lambda('lambda_4185')
    def lambda_4185():
        OP_6D(-1170, 0, 17520, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4185)

    @scena.Lambda('lambda_419D')
    def lambda_419D():
        OP_67(0, 4340, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_419D)

    @scena.Lambda('lambda_41B5')
    def lambda_41B5():
        OP_6B(2240, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_41B5)

    @scena.Lambda('lambda_41C5')
    def lambda_41C5():
        OP_6C(45000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_41C5)

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 4)
    CreateThread(0x0008, 0x03, 0x00, 0x000F)
    ClearChrFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_41EB')
    def lambda_41EB():
        OP_96(0x00FE, 0xFFFFEC64, 0x00000000, 0x00004C86, 0x000004B0, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_41EB)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x0008, 0x0003)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 6)
    WaitForThreadExit(0x0009, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 4)

    @scena.Lambda('lambda_4242')
    def lambda_4242():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4242)

    Sleep(200)

    @scena.Lambda('lambda_4261')
    def lambda_4261():
        OP_6D(-1660, 0, 17640, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4261)

    @scena.Lambda('lambda_4279')
    def lambda_4279():
        OP_6C(80000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4279)

    Fade(250)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 8)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_42A3')
    def lambda_42A3():
        OP_6D(-4760, 0, 21530, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_42A3)

    @scena.Lambda('lambda_42BB')
    def lambda_42BB():
        OP_6B(1800, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_42BB)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 9)
    OP_7D(0x00, 0x0008, 0x000A, 0x01F4)

    @scena.Lambda('lambda_42E6')
    def lambda_42E6():
        OP_96(0x00FE, 0xFFFFE110, 0x00000000, 0x000059C4, 0x000000C8, 0x00001388)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_42E6)

    Sleep(100)

    OP_22(0x009B, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 7)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 3)
    WaitForThreadExit(0x0008, 0x0000)

    @scena.Lambda('lambda_435C')
    def lambda_435C():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00000190, 0x00001770)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_435C)

    OP_7D(0x01, 0x0008, 0x0000, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    @scena.Lambda('lambda_438C')
    def lambda_438C():
        OP_6D(-5050, 0, 21050, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_438C)

    @scena.Lambda('lambda_43A4')
    def lambda_43A4():
        OP_6B(2160, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_43A4)

    @scena.Lambda('lambda_43B4')
    def lambda_43B4():
        OP_6C(8000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_43B4)

    @scena.Lambda('lambda_43C4')
    def lambda_43C4():
        OP_8C(0x00FE, 35, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_43C4)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 3)
    OP_7D(0x00, 0x0008, 0x0032, 0x00C8)

    @scena.Lambda('lambda_43E4')
    def lambda_43E4():
        OP_96(0x00FE, 0xFFFFE304, 0x00000000, 0x00003F0C, 0x00000190, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_43E4)

    WaitForThreadExit(0x0009, 0x0003)

    @scena.Lambda('lambda_4407')
    def lambda_4407():
        OP_8C(0x00FE, 305, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_4407)

    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    OP_7D(0x01, 0x0008, 0x0000, 0x0000)

    @scena.Lambda('lambda_4427')
    def lambda_4427():
        OP_6D(-3930, 0, 22440, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4427)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 6)

    @scena.Lambda('lambda_4452')
    def lambda_4452():
        OP_8F(0x00FE, -5970, 0, 18180, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_4452)

    OP_8C(0x0008, 270, 1000)
    OP_8C(0x0008, 180, 1000)
    OP_8C(0x0008, 90, 1000)
    ChrTurnDirection(0x0008, 0x0009, 1000)
    WaitForThreadExit(0x0008, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00D6, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 26)
    SetChrSubChip(0x0008, 7)
    ChrTurnDirection(0x0009, 0x0008, 0)

    @scena.Lambda('lambda_44E2')
    def lambda_44E2():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00005EB0, 0x00000578, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_44E2)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x0009, 0x0000)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 4)
    Sleep(400)

    @scena.Lambda('lambda_452F')
    def lambda_452F():
        OP_6D(-2680, 0, 21130, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_452F)

    @scena.Lambda('lambda_4547')
    def lambda_4547():
        OP_6B(1820, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4547)

    @scena.Lambda('lambda_4557')
    def lambda_4557():
        OP_6C(296000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4557)

    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 9)

    @scena.Lambda('lambda_4571')
    def lambda_4571():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4571')

    DispatchAsync2(0x0008, 0x0003, lambda_4571)

    @scena.Lambda('lambda_4582')
    def lambda_4582():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00004466, 0x00000258, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_4582)

    @scena.Lambda('lambda_45A0')
    def lambda_45A0():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_45A0')

    DispatchAsync2(0x0009, 0x0003, lambda_45A0)

    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    TerminateThread(0x0008, 0x03)
    TerminateThread(0x0009, 0x03)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x000A,
        (
            '#0600240040V#163F#7P嗯，到此为止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_460F')
    def lambda_460F():
        OP_67(0, 4810, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_460F)

    @scena.Lambda('lambda_4627')
    def lambda_4627():
        OP_6B(2760, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4627)

    OP_22(0x00BF, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    ClearChrFlags(0x0008, 0x0020)
    ClearChrFlags(0x0008, 0x0040)
    ClearChrFlags(0x0009, 0x0020)
    ClearChrFlags(0x0009, 0x0040)

    ChrTalk(
        0x0009,
        (
            '#0100240041V#175F#2P呼、呼、呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 6)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160240042V#1125F#6P呵呵，真了不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240043V#1120F之前，我只是教了你一些\n',
            '基础的东西而已……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240044V没想到，你竟能靠自己的努力达到如此的水平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0100240045V#171F#2P哪……哪里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100240046V我还有很多的不足之处……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x000A, -4980, 0, 20880, 3500, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0600240047V#165F#5P这场比试很有水准。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100240048V#175F#2P将军，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600240049V#163F#5P说实话，我没想到你\n',
            '能达到这个地步。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600240050V就算是有相当水准的人，\n',
            '只要和卡西乌斯交手几个回合，\n',
            '剑也会脱手的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600240051V#165F你可以说是年轻一辈中最强的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100240052V#173F#2P惭、惭愧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100240053V#176F不过机会难得……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100240054V#172F真希望能够一直打到\n',
            '我被击溃为止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600240055V#164F#5P哈哈哈哈！\n',
            '真有志气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600240056V#165F怎么样，卡西乌斯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160240057V#1125F#6P呵呵，我也想\n',
            '奉陪到底啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000B, 12950, 0, 21590, 270)
    SetChrPos(0x000C, 13170, 0, 22870, 270)
    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    Sleep(500)

    ChrTurnDirection(0x0008, 0x000B, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160240058V#1120F#5P不过好像有客人来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)

    @scena.Lambda('lambda_4A8A')
    def lambda_4A8A():
        OP_6D(6670, 0, 21130, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_4A8A)

    @scena.Lambda('lambda_4AA2')
    def lambda_4AA2():
        ChrTurnDirection(0x0009, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4AA2)

    @scena.Lambda('lambda_4AB0')
    def lambda_4AB0():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_4AB0')

    DispatchAsync2(0x0008, 0x0001, lambda_4AB0)

    WaitForThreadExit(0x0009, 0x0002)
    Sleep(500)

    @scena.Lambda('lambda_4ACB')
    def lambda_4ACB():
        ChrTurnDirection(0x0009, 0x000B, 400)
        Yield()

        Jump('lambda_4ACB')

    DispatchAsync2(0x0009, 0x0001, lambda_4ACB)

    @scena.Lambda('lambda_4ADC')
    def lambda_4ADC():
        OP_8E(0x00FE, 550, 0, 19780, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4ADC)

    Sleep(500)

    @scena.Lambda('lambda_4AFC')
    def lambda_4AFC():
        OP_8E(0x00FE, 1510, 0, 21250, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4AFC)

    OP_69(0x0024, 0x00001388)
    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x000C, 0x0001)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)

    ChrTalk(
        0x000C,
        (
            '#0560240059V#692F哎呀～真是让我\n',
            '大饱眼福了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620240060V#703F两位辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0009, 400)
    Sleep(300)

    ChrTalk(
        0x000B,
        (
            '#0620240061V#701F#6P舒华兹上尉，\n',
            '你实在是非常出色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100240062V#171F希德中校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000C, 400)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0100240063V#173F请问这位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0009, 400)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0560240064V#691F#6P我是中央工房派来的，\n',
            '叫格斯塔夫。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560240065V#693F请多指教，队长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100240066V#173F失、失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100240067V#176F我是王室亲卫队中队长。\n',
            '尤莉亚·舒华兹上尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100240068V#170F也请你多多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600240069V#165F#5P嗯，看来该做的事\n',
            '都已经做完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4D45')
    def lambda_4D45():
        OP_6D(-6760, 0, 19100, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4D45)

    OP_8C(0x0008, 302, 400)
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0160240070V#1120F#6P各位，余兴节目结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240071V请返回各自的工作岗位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4DBC')
    def lambda_4DBC():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_4DBC)

    Sleep(50)

    @scena.Lambda('lambda_4DCF')
    def lambda_4DCF():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_4DCF)

    @scena.Lambda('lambda_4DDD')
    def lambda_4DDD():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4DDD)

    Sleep(50)

    @scena.Lambda('lambda_4DF0')
    def lambda_4DF0():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_4DF0)

    @scena.Lambda('lambda_4DFE')
    def lambda_4DFE():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4DFE)

    Sleep(50)

    @scena.Lambda('lambda_4E11')
    def lambda_4E11():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4E11)

    @scena.Lambda('lambda_4E1F')
    def lambda_4E1F():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_4E1F)

    Sleep(50)

    @scena.Lambda('lambda_4E32')
    def lambda_4E32():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_4E32)

    @scena.Lambda('lambda_4E40')
    def lambda_4E40():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_4E40)

    Sleep(50)

    @scena.Lambda('lambda_4E53')
    def lambda_4E53():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_4E53)

    @scena.Lambda('lambda_4E61')
    def lambda_4E61():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_4E61)

    Sleep(50)

    @scena.Lambda('lambda_4E74')
    def lambda_4E74():
        ChrTurnDirection(0x00FE, 0x0008, 500)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_4E74)

    Sleep(500)

    SetMessageWindowPos(140, 120, -1, -1)
    SetChrName('士兵们')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#2450240072V#5S是，长官！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    CreateThread(0x0008, 0x00, 0x00, 0x0015)
    CreateThread(0x0008, 0x01, 0x00, 0x0016)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_4EEB')
    def lambda_4EEB():
        OP_69(0x00FE, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_4EEB)

    ChrTurnDirection(0x0008, 0x0009, 400)
    WaitForThreadExit(0x0024, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#0560240073V#691F#6P那么，能不能\n',
            '马上让我看看机关部？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560240074V我想尽可能在今天之内\n',
            '找到头绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100240075V#171F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0100240076V#176F#2P那么我先告退了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100240077V#171F准将，感谢您\n',
            '今天给予我的指导！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160240078V#1121F#6P这不算什么。\n',
            '我也算是好好锻炼了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600240079V#165F#5P维修长，上尉。\n',
            '埃尔赛尤号就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100240080V#172F#2P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000A, 400)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0560240081V#691F请交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_50C8')
    def lambda_50C8():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_50C8')

    DispatchAsync2(0x0008, 0x0003, lambda_50C8)

    @scena.Lambda('lambda_50D9')
    def lambda_50D9():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_50D9')

    DispatchAsync2(0x000B, 0x0003, lambda_50D9)

    OP_8C(0x0009, 70, 400)

    @scena.Lambda('lambda_50F1')
    def lambda_50F1():
        OP_6D(-1480, 0, 22850, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_50F1)

    @scena.Lambda('lambda_5109')
    def lambda_5109():
        OP_8E(0x00FE, 15860, 0, 23490, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5109)

    OP_8C(0x000C, 70, 400)

    @scena.Lambda('lambda_512B')
    def lambda_512B():
        OP_8E(0x00FE, 15860, 0, 23490, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_512B)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x000C, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_5155')
    def lambda_5155():
        OP_6D(-3450, 0, 20710, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5155)

    @scena.Lambda('lambda_516D')
    def lambda_516D():
        OP_6C(308000, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_516D)

    @scena.Lambda('lambda_517D')
    def lambda_517D():
        OP_6E(325, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_517D)

    WaitForThreadExit(0x000B, 0x0001)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    TerminateThread(0x0008, 0x03)
    TerminateThread(0x000B, 0x03)

    ChrTalk(
        0x000B,
        (
            '#0620240082V#701F#5P呵呵……\n',
            '她真是不简单呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620240083V今后还会不断成长的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160240084V#1125F#5P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240085V#1120F跟你和理查德\n',
            '只差一两步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600240086V#164F#5P呼，看到这样的年轻人\n',
            '连我这把老骨头也热血沸腾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 148, 400)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0600240087V#165F#5P卡西乌斯，一会儿也和我切磋切磋吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_52E0')
    def lambda_52E0():
        OP_8C(0x00FE, 344, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_52E0)

    @scena.Lambda('lambda_52EE')
    def lambda_52EE():
        OP_8C(0x00FE, 267, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_52EE)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0160240088V#1123F#6P将军……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240089V还是应该考虑\n',
            '一下您的年龄吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600240090V#160F#5P唔唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160240091V#1120F#6P听说您在去年的武术大会上\n',
            '也大出了风头一番是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240092V是不是也该让年轻人\n',
            '有点进步的余地？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600240093V#163F#5P哼，所以我才\n',
            '把司令的位置交给你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600240094V#165F你既然都这么说了，\n',
            '那以后就不能再对工作有所抱怨了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160240095V#1123F#6P呀，早知道就不提了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620240096V#701F#6P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000B, 400)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0600240097V#161F#5P对了，希德中校。\n',
            '今天好像要出发了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620240098V#701F#6P是的，正午时分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620240099V预计率领2艘警备艇\n',
            '三个中队前去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600240100V#165F#5P我也会去参加签字仪式的，\n',
            '不过在此之前抽不开身来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600240101V守卫王都的任务就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620240102V#703F#6P请您放心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620240103V#701F我会和游击士协会\n',
            '一起妥善应对的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600240104V#161F#5P嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600240105V#163F虽然十分遗憾，\n',
            '不过这次实在没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160240106V#1120F#6P呵呵，将军你也开始变得\n',
            '不再那样讨厌游击士协会了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C3100._SN', 100, 0, 0)
    IdleLoop()
    SetMapFlags(0x00000010)

    Return()

# id: 0x000C offset: 0x56F8
@scena.Code('func_0C_56F8')
def func_0C_56F8():
    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    SetChrPos(0x0008, -2300, 0, 17510, 0)
    SetChrPos(0x0009, -2300, 0, 24240, 180)
    SetChrPos(0x000A, -4300, 0, 20880, 90)
    SetChrPos(0x000D, -12080, 0, 15010, 90)
    SetChrPos(0x000E, -12900, 0, 16840, 90)
    SetChrPos(0x000F, -13490, 0, 18730, 90)
    SetChrPos(0x0010, -14010, 0, 15710, 90)
    SetChrPos(0x0011, -14670, 0, 17570, 90)
    SetChrPos(0x0012, -15200, 0, 19820, 90)
    SetChrPos(0x001D, -13510, 0, 22660, 90)
    SetChrPos(0x001E, -12880, 0, 24340, 90)
    SetChrPos(0x001F, -11920, 0, 26130, 90)
    SetChrPos(0x0020, -15170, 0, 22090, 90)
    SetChrPos(0x0021, -14580, 0, 23690, 90)
    SetChrPos(0x0022, -13960, 0, 25780, 90)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)
    OP_6D(-16450, 0, 14000, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(247000, 0)
    OP_6E(316, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_589A')
    def lambda_589A():
        OP_6D(-16450, 0, 28000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_589A)

    @scena.Lambda('lambda_58B2')
    def lambda_58B2():
        OP_6C(310000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_58B2)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_58C7')
    def lambda_58C7():
        OP_6D(-2680, 0, 21130, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_58C7)

    @scena.Lambda('lambda_58DF')
    def lambda_58DF():
        OP_67(0, 4810, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_58DF)

    @scena.Lambda('lambda_58F7')
    def lambda_58F7():
        OP_6B(2760, 4500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_58F7)

    @scena.Lambda('lambda_5907')
    def lambda_5907():
        OP_6C(296000, 4500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5907)

    @scena.Lambda('lambda_5917')
    def lambda_5917():
        OP_6E(443, 4500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_5917)

    WaitForThreadExit(0x0009, 0x0001)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#160F#4P双方，预备！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3S开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0024,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0024,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0024,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0009,
        (
            '#170F#6P──呀啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_59B5')
    def lambda_59B5():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00004F9C, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_59B5)

    @scena.Lambda('lambda_59D3')
    def lambda_59D3():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00005384, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_59D3)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_59FB')
    def lambda_59FB():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00004466, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_59FB)

    @scena.Lambda('lambda_5A19')
    def lambda_5A19():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00005EB0, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5A19)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#170F#6P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120F#6P怎么回事！？\n',
            '行动太过直线化！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240029V你用的是细剑，就应该使出\n',
            '流畅的进攻套路！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240030V想想我教过你的东西！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F#6P是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5AF8')
    def lambda_5AF8():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00004F9C, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5AF8)

    @scena.Lambda('lambda_5B16')
    def lambda_5B16():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00005384, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5B16)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_5B3E')
    def lambda_5B3E():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00004466, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5B3E)

    @scena.Lambda('lambda_5B5C')
    def lambda_5B5C():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00005EB0, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5B5C)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1120F#6P这就对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，接招吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5BAF')
    def lambda_5BAF():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00004F9C, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5BAF)

    @scena.Lambda('lambda_5BCD')
    def lambda_5BCD():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00005384, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5BCD)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_5BF5')
    def lambda_5BF5():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00004466, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5BF5)

    @scena.Lambda('lambda_5C13')
    def lambda_5C13():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00005EB0, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5C13)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#170F#6P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120F#6P防守基本相同！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240037V注意对方动作的意图，\n',
            '同时想好攻守的步骤！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F#6P是！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哈啊啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5CC7')
    def lambda_5CC7():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00004F9C, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5CC7)

    @scena.Lambda('lambda_5CE5')
    def lambda_5CE5():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00005384, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5CE5)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_5D0D')
    def lambda_5D0D():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00004466, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5D0D)

    @scena.Lambda('lambda_5D2B')
    def lambda_5D2B():
        OP_96(0x00FE, 0xFFFFF704, 0x00000000, 0x00005EB0, 0x000002BC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5D2B)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(1000)

    OP_22(0x00BF, 0x00, 0x64)
    Sleep(6000)

    ChrTalk(
        0x0009,
        (
            '#170F#6P呼、呼、呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120F#6P呵呵，真了不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '以前我只是教给你一些\n',
            '基础的东西而已……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240044V没想到，你竟能靠自己的努力达到如此的水平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0009, 1)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#170F#6P不……不不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100240046V我还大有不足之处……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x000A, -3230, 0, 20880, 3000, 0x00)
    Sleep(1000)

    WaitForThreadExit(0x000A, 0x0000)

    ChrTalk(
        0x000A,
        (
            '#160F#4P嗯，到此为止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这场比试很有水准。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F#6P将军，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#160F#4P说实话，我没想到你\n',
            '能坚持到这一步。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600240050V就算是有相当水准的人，\n',
            '只要和卡西乌斯交手几个回合，\n',
            '剑也会脱手的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '能坚持到这一步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F#6P惭、惭愧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过机会难得……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真希望能够一直打到\n',
            '我被击溃为止',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#160F#4P哈哈哈哈！\n',
            '真有志气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '怎么样，卡西乌斯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120F#6P呵呵，我也想\n',
            '奉陪到底啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000B, 12950, 0, 21590, 270)
    SetChrPos(0x000C, 13170, 0, 22870, 270)
    ChrTurnDirection(0x0008, 0x000B, 400)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1120F#6P不过好像有客人来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0009, 0x000B, 400)
    Sleep(1000)

    @scena.Lambda('lambda_607F')
    def lambda_607F():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_607F')

    DispatchAsync2(0x0008, 0x0001, lambda_607F)

    OP_6D(6670, 0, 21130, 2000)

    @scena.Lambda('lambda_60A1')
    def lambda_60A1():
        OP_8E(0x00FE, 550, 0, 19780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_60A1)

    Sleep(300)

    @scena.Lambda('lambda_60C1')
    def lambda_60C1():
        OP_8E(0x00FE, 610, 0, 21940, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_60C1)

    OP_69(0x0024, 0x00001388)
    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x000C, 0x0001)
    Sleep(1000)

    TerminateThread(0x0008, 0x01)

    ChrTalk(
        0x000C,
        (
            '#690F哎呀～真是让我\n',
            '大饱眼福了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#700F两位辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '舒华兹上尉，\n',
            '你干得真不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F希德中校……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '请问这位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#690F他是中央工房派来的，\n',
            '叫格斯塔夫。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '请多指教，队长小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F失、失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我是王室亲卫队的中队长，\n',
            '尤莉亚·舒华兹上尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '也请你多多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#160F嗯，看来该做的事\n',
            '都已经做完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_623B')
    def lambda_623B():
        OP_6D(-6760, 0, 19100, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_623B)

    OP_8C(0x0008, 302, 400)
    Sleep(2000)

    ChrTalk(
        0x0008,
        (
            '#1120F#3P各位，余兴节目结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240071V请返回各自的工作岗位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 160, -1, -1)
    SetChrName('士兵们')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#4S YES！SIR！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    CreateThread(0x000D, 0x01, 0x00, 0x0011)
    CreateThread(0x0010, 0x01, 0x00, 0x0012)
    CreateThread(0x001F, 0x01, 0x00, 0x0013)
    CreateThread(0x0022, 0x01, 0x00, 0x0014)
    Sleep(300)

    CreateThread(0x000E, 0x01, 0x00, 0x0011)
    CreateThread(0x0011, 0x01, 0x00, 0x0012)
    CreateThread(0x001E, 0x01, 0x00, 0x0013)
    CreateThread(0x0021, 0x01, 0x00, 0x0014)
    Sleep(300)

    CreateThread(0x000F, 0x01, 0x00, 0x0011)
    CreateThread(0x0012, 0x01, 0x00, 0x0012)
    CreateThread(0x001D, 0x01, 0x00, 0x0013)
    CreateThread(0x0020, 0x01, 0x00, 0x0014)
    OP_69(0x0024, 0x000003E8)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x000B, 400)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#690F那么，能不能\n',
            '马上让我看看机关部？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560240074V我想尽可能在今天之内\n',
            '找到头绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#170F那么我先告退了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '准将，感谢您\n',
            '今天给予我的指导！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 343, 400)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1120F没什么的。\n',
            '我也正好做了不错的锻炼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#160F维修长，上尉。\n',
            '『埃尔赛尤』就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#690F请交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_64AE')
    def lambda_64AE():
        OP_8E(0x00FE, 15860, 0, 23490, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_64AE)

    Sleep(1000)

    @scena.Lambda('lambda_64CE')
    def lambda_64CE():
        OP_8E(0x00FE, 15860, 0, 23490, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_64CE)

    Sleep(2000)

    @scena.Lambda('lambda_64EE')
    def lambda_64EE():
        OP_6D(-2510, 0, 20260, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_64EE)

    @scena.Lambda('lambda_6506')
    def lambda_6506():
        OP_6C(308000, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_6506)

    @scena.Lambda('lambda_6516')
    def lambda_6516():
        OP_6E(325, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6516)

    WaitForThreadExit(0x000B, 0x0001)
    Sleep(1000)

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000C, 0x0080)

    ChrTalk(
        0x000B,
        (
            '#700F呵呵……\n',
            '她真是不简单呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620240083V今后还会不断成长的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '跟你和理查德\n',
            '只差一两步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 148, 400)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#160F呼，看到这样的年轻人\n',
            '连我这把老骨头也热血沸腾了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '卡西乌斯，一会儿也和我切磋切磋吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120F将军……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240089V您还是应该考虑一下\n',
            '您的年龄吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#160F唔唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120F听说您在去年的武术大会上\n',
            '大大地活跃了一番是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160240092V是不是也该让年轻人\n',
            '有点进步的余地？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#160F哼，所以我才\n',
            '把司令的位置交给你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你既然都这么说了，\n',
            '以后就不能再对工作有所抱怨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120F哎呀，早知道就不提了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#700F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#160F对了，希德中校。\n',
            '今天好像要出发了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#700F是的，正午时分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '预计率领２艘警备艇\n',
            '和３个中队前去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#160F我也会去参加签字仪式的，\n',
            '不过在此之前抽不开身来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600240101V守卫王都的任务就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#700F请您放心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我会和游击士协会\n',
            '一起行动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#160F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然十分遗憾，\n',
            '不过这次实在没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1120F呵呵，将军你也开始变得\n',
            '不再那样讨厌游击士协会了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C3100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x68F9
@scena.Code('func_0D_68F9')
def func_0D_68F9():
    OP_8C(0x00FE, 90, 1000)
    OP_8C(0x00FE, 0, 1000)
    OP_8C(0x00FE, 270, 1000)
    OP_8C(0x00FE, 180, 1000)
    OP_8C(0x00FE, 90, 1000)
    ChrTurnDirection(0x00FE, 0x0009, 1000)

    Return()

# id: 0x000E offset: 0x6924
@scena.Code('func_0E_6924')
def func_0E_6924():
    OP_8C(0x00FE, 270, 1000)
    OP_8C(0x00FE, 180, 1000)
    OP_8C(0x00FE, 90, 1000)
    OP_8C(0x00FE, 0, 1000)
    OP_8C(0x00FE, 270, 1000)
    ChrTurnDirection(0x00FE, 0x0008, 1000)

    Return()

# id: 0x000F offset: 0x694F
@scena.Code('func_0F_694F')
def func_0F_694F():
    OP_8C(0x00FE, 0, 1000)
    OP_8C(0x00FE, 90, 1000)
    OP_8C(0x00FE, 180, 1000)
    OP_8C(0x00FE, 270, 1000)
    ChrTurnDirection(0x00FE, 0x0009, 1000)

    Return()

# id: 0x0010 offset: 0x6973
@scena.Code('func_10_6973')
def func_10_6973():
    OP_8C(0x00FE, 90, 1400)
    OP_8C(0x00FE, 0, 1400)
    OP_8C(0x00FE, 270, 1400)
    OP_8C(0x00FE, 180, 1400)
    OP_8C(0x00FE, 90, 1400)
    ChrTurnDirection(0x00FE, 0x0008, 1400)

    Return()

# id: 0x0011 offset: 0x699E
@scena.Code('func_11_699E')
def func_11_699E():
    OP_8E(0x00FE, 450, 0, 6530, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0012 offset: 0x69B8
@scena.Code('func_12_69B8')
def func_12_69B8():
    OP_8E(0x00FE, -48260, 0, 17100, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0013 offset: 0x69D2
@scena.Code('func_13_69D2')
def func_13_69D2():
    OP_8E(0x00FE, -640, 0, 35200, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0014 offset: 0x69EC
@scena.Code('func_14_69EC')
def func_14_69EC():
    OP_8E(0x00FE, -32340, 0, 64709, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0015 offset: 0x6A06
@scena.Code('func_15_6A06')
def func_15_6A06():
    CreateThread(0x000F, 0x01, 0x00, 0x0017)
    Sleep(600)

    CreateThread(0x0010, 0x01, 0x00, 0x0018)
    Sleep(200)

    CreateThread(0x0012, 0x01, 0x00, 0x0018)
    Sleep(200)

    CreateThread(0x000E, 0x01, 0x00, 0x0017)
    Sleep(400)

    CreateThread(0x0011, 0x01, 0x00, 0x0018)
    Sleep(600)

    CreateThread(0x000D, 0x01, 0x00, 0x0017)

    Return()

# id: 0x0016 offset: 0x6A4A
@scena.Code('func_16_6A4A')
def func_16_6A4A():
    CreateThread(0x0021, 0x01, 0x00, 0x001A)
    Sleep(200)

    CreateThread(0x001D, 0x01, 0x00, 0x0019)
    Sleep(600)

    CreateThread(0x0020, 0x01, 0x00, 0x001A)
    Sleep(600)

    CreateThread(0x001F, 0x01, 0x00, 0x0019)
    Sleep(400)

    CreateThread(0x001E, 0x01, 0x00, 0x0019)
    Sleep(200)

    CreateThread(0x0022, 0x01, 0x00, 0x001A)

    Return()

# id: 0x0017 offset: 0x6A8E
@scena.Code('func_17_6A8E')
def func_17_6A8E():
    OP_8B(0x00FE, 0x000001C2, 0x00001982, 0x0190)
    OP_8E(0x00FE, 450, 0, 6530, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0018 offset: 0x6AB5
@scena.Code('func_18_6AB5')
def func_18_6AB5():
    OP_8B(0x00FE, 0xFFFF437C, 0x000042CC, 0x0190)
    OP_8E(0x00FE, -48260, 0, 17100, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0019 offset: 0x6ADC
@scena.Code('func_19_6ADC')
def func_19_6ADC():
    OP_8B(0x00FE, 0xFFFFFD80, 0x00008980, 0x0190)
    OP_8E(0x00FE, -640, 0, 35200, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001A offset: 0x6B03
@scena.Code('func_1A_6B03')
def func_1A_6B03():
    OP_8B(0x00FE, 0xFFFF81AC, 0x0000FCC5, 0x0190)
    OP_8E(0x00FE, -32340, 0, 64709, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

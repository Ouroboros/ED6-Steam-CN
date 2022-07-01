import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import A0021_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('A0021   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '00100艾丝蒂尔待机'),
    TXT(0x02, '00101艾丝蒂尔移动'),
    TXT(0x03, '00102艾丝蒂尔攻击'),
    TXT(0x04, '00103艾丝蒂尔被弹开'),
    TXT(0x05, '00104艾丝蒂尔倒下'),
    TXT(0x06, '00105艾丝蒂尔魔法咏唱'),
    TXT(0x07, '00106艾丝蒂尔魔法发射'),
    TXT(0x08, '00107艾丝蒂尔胜利'),
    TXT(0x09, '00110约修亚待机'),
    TXT(0x0A, '00111约修亚移动'),
    TXT(0x0B, '00112约修亚攻击'),
    TXT(0x0C, '00113约修亚被弹开'),
    TXT(0x0D, '00114约修亚倒下'),
    TXT(0x0E, '00115约修亚魔法咏唱'),
    TXT(0x0F, '00116约修亚魔法发射'),
    TXT(0x10, '00117约修亚胜利'),
    TXT(0x11, '00170金待机'),
    TXT(0x12, '00171金移动'),
    TXT(0x13, '00172金攻击'),
    TXT(0x14, '00173金被弹开'),
    TXT(0x15, '00174金倒下'),
    TXT(0x16, '00175金魔法咏唱'),
    TXT(0x17, '00176金魔法发射'),
    TXT(0x18, '00177金胜利'),
    TXT(0x19, '00150阿加特待机'),
    TXT(0x1A, '00151阿加特移动'),
    TXT(0x1B, '00152阿加特攻击'),
    TXT(0x1C, '00153阿加特被弹开'),
    TXT(0x1D, '00154阿加特倒下'),
    TXT(0x1E, '00155阿加特魔法咏唱'),
    TXT(0x1F, '00156阿加特魔法发射'),
    TXT(0x20, '00157阿加特胜利'),
    TXT(0x21, '00130奥利维尔待机'),
    TXT(0x22, '00131奥利维尔移动'),
    TXT(0x23, '00132奥利维尔攻击'),
    TXT(0x24, '00133奥利维尔被弹开'),
    TXT(0x25, '00134奥利维尔倒下'),
    TXT(0x26, '00135奥利维尔魔法咏唱'),
    TXT(0x27, '00136奥利维尔魔法发射'),
    TXT(0x28, '00137奥利维尔胜利'),
    TXT(0x29, ''),
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

# id: 0xFFFF offset: 0xBD5
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
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT27/CH04002._CH', 'ED6_DT27/CH04002P._CP'),
        ('ED6_DT27/CH04003._CH', 'ED6_DT27/CH04003P._CP'),
        ('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04004P._CP'),
        ('ED6_DT27/CH04005._CH', 'ED6_DT27/CH04005P._CP'),
        ('ED6_DT27/CH04006._CH', 'ED6_DT27/CH04006P._CP'),
        ('ED6_DT27/CH04007._CH', 'ED6_DT27/CH04007P._CP'),
        ('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP'),
        ('ED6_DT27/CH04012._CH', 'ED6_DT27/CH04012P._CP'),
        ('ED6_DT27/CH04013._CH', 'ED6_DT27/CH04013P._CP'),
        ('ED6_DT27/CH04014._CH', 'ED6_DT27/CH04014P._CP'),
        ('ED6_DT27/CH04015._CH', 'ED6_DT27/CH04015P._CP'),
        ('ED6_DT27/CH04016._CH', 'ED6_DT27/CH04016P._CP'),
        ('ED6_DT27/CH04017._CH', 'ED6_DT27/CH04017P._CP'),
        ('ED6_DT27/CH04014._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT27/CH04014._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT27/CH04014._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT27/CH04014._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH00172._CH', 'ED6_DT07/CH00172P._CP'),
        ('ED6_DT07/CH00173._CH', 'ED6_DT07/CH00173P._CP'),
        ('ED6_DT07/CH00174._CH', 'ED6_DT07/CH00174P._CP'),
        ('ED6_DT07/CH00175._CH', 'ED6_DT07/CH00175P._CP'),
        ('ED6_DT07/CH00176._CH', 'ED6_DT07/CH00176P._CP'),
        ('ED6_DT07/CH00177._CH', 'ED6_DT07/CH00177P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP'),
        ('ED6_DT07/CH00153._CH', 'ED6_DT07/CH00153P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00154P._CP'),
        ('ED6_DT07/CH00155._CH', 'ED6_DT07/CH00155P._CP'),
        ('ED6_DT07/CH00156._CH', 'ED6_DT07/CH00156P._CP'),
        ('ED6_DT07/CH00157._CH', 'ED6_DT07/CH00157P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH00132._CH', 'ED6_DT07/CH00132P._CP'),
        ('ED6_DT07/CH00133._CH', 'ED6_DT07/CH00133P._CP'),
        ('ED6_DT07/CH00134._CH', 'ED6_DT07/CH00134P._CP'),
        ('ED6_DT07/CH00135._CH', 'ED6_DT07/CH00135P._CP'),
        ('ED6_DT07/CH00136._CH', 'ED6_DT07/CH00136P._CP'),
        ('ED6_DT07/CH00137._CH', 'ED6_DT07/CH00137P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
    ]

# id: 0x10002 offset: 0x28A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000C,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000D,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000E,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000F,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0010,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0011,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0012,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0013,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 16000,
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
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0014,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0015,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0016,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0017,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 48,
            chipIndex           = 48,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 49,
            chipIndex           = 49,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 50,
            chipIndex           = 50,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0018,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 51,
            chipIndex           = 51,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 52,
            chipIndex           = 52,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 53,
            chipIndex           = 53,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0019,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 54,
            chipIndex           = 54,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001A,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 55,
            chipIndex           = 55,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
    )

# id: 0x10003 offset: 0x78A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x78A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x78A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x78A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x78B
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x78C
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7A1',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000708)

    Jump('ReInit')

    def _loc_7A1(): pass

    label('loc_7A1')

    Return()

# id: 0x0003 offset: 0x7A2
@scena.Code('func_03_7A2')
def func_03_7A2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7B7',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

    Jump('func_03_7A2')

    def _loc_7B7(): pass

    label('loc_7B7')

    Return()

# id: 0x0004 offset: 0x7B8
@scena.Code('func_04_7B8')
def func_04_7B8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7D2',
    )

    OP_99(0x00FE, 0x00, 0x00, 0x000005DC)
    Sleep(500)

    Jump('func_04_7B8')

    def _loc_7D2(): pass

    label('loc_7D2')

    Return()

# id: 0x0005 offset: 0x7D3
@scena.Code('func_05_7D3')
def func_05_7D3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7ED',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000007D0)
    Sleep(500)

    Jump('func_05_7D3')

    def _loc_7ED(): pass

    label('loc_7ED')

    Return()

# id: 0x0006 offset: 0x7EE
@scena.Code('func_06_7EE')
def func_06_7EE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_808',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
    Sleep(500)

    Jump('func_06_7EE')

    def _loc_808(): pass

    label('loc_808')

    Return()

# id: 0x0007 offset: 0x809
@scena.Code('func_07_809')
def func_07_809():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_82C',
    )

    OP_8D(0x00FE, 4000, 20000, 24000, 28000, 1500)

    Jump('func_07_809')

    def _loc_82C(): pass

    label('loc_82C')

    Return()

# id: 0x0008 offset: 0x82D
@scena.Code('func_08_82D')
def func_08_82D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_909',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(120)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(90)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(80)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(60)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(50)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(40)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(60)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x9),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(70)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(80)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(120)

    Jump('func_08_82D')

    def _loc_909(): pass

    label('loc_909')

    Return()

# id: 0x0009 offset: 0x90A
@scena.Code('func_09_90A')
def func_09_90A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_91F',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_09_90A')

    def _loc_91F(): pass

    label('loc_91F')

    Return()

# id: 0x000A offset: 0x920
@scena.Code('func_0A_920')
def func_0A_920():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_956',
    )

    SetChrChipByIndex(0x00FE, 5)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 6)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_0A_920')

    def _loc_956(): pass

    label('loc_956')

    Return()

# id: 0x000B offset: 0x957
@scena.Code('func_0B_957')
def func_0B_957():
    SetChrFlags(0x00FE, 0x0002)
    def _loc_95C(): pass

    label('loc_95C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_976',
    )

    OP_99(0x00FE, 0x00, 0x13, 0x000007D0)
    Sleep(500)

    Jump('loc_95C')

    def _loc_976(): pass

    label('loc_976')

    Return()

# id: 0x000C offset: 0x977
@scena.Code('func_0C_977')
def func_0C_977():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_991',
    )

    OP_99(0x00FE, 0x00, 0x0C, 0x000007D0)
    Sleep(500)

    Jump('func_0C_977')

    def _loc_991(): pass

    label('loc_991')

    Return()

# id: 0x000D offset: 0x992
@scena.Code('func_0D_992')
def func_0D_992():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9A7',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_0D_992')

    def _loc_9A7(): pass

    label('loc_9A7')

    Return()

# id: 0x000E offset: 0x9A8
@scena.Code('func_0E_9A8')
def func_0E_9A8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9DE',
    )

    SetChrChipByIndex(0x00FE, 17)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 18)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_0E_9A8')

    def _loc_9DE(): pass

    label('loc_9DE')

    Return()

# id: 0x000F offset: 0x9DF
@scena.Code('func_0F_9DF')
def func_0F_9DF():
    SetChrFlags(0x00FE, 0x0002)
    def _loc_9E4(): pass

    label('loc_9E4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9FE',
    )

    OP_99(0x00FE, 0x00, 0x21, 0x000007D0)
    Sleep(500)

    Jump('loc_9E4')

    def _loc_9FE(): pass

    label('loc_9FE')

    Return()

# id: 0x0010 offset: 0x9FF
@scena.Code('func_10_9FF')
def func_10_9FF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A19',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000009C4)
    Sleep(500)

    Jump('func_10_9FF')

    def _loc_A19(): pass

    label('loc_A19')

    Return()

# id: 0x0011 offset: 0xA1A
@scena.Code('func_11_A1A')
def func_11_A1A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A2F',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_11_A1A')

    def _loc_A2F(): pass

    label('loc_A2F')

    Return()

# id: 0x0012 offset: 0xA30
@scena.Code('func_12_A30')
def func_12_A30():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A66',
    )

    SetChrChipByIndex(0x00FE, 29)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 30)
    OP_99(0x00FE, 0x00, 0x00, 0x000003E8)
    Sleep(1000)

    Jump('func_12_A30')

    def _loc_A66(): pass

    label('loc_A66')

    Return()

# id: 0x0013 offset: 0xA67
@scena.Code('func_13_A67')
def func_13_A67():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A81',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
    Sleep(500)

    Jump('func_13_A67')

    def _loc_A81(): pass

    label('loc_A81')

    Return()

# id: 0x0014 offset: 0xA82
@scena.Code('func_14_A82')
def func_14_A82():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A9C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000009C4)
    Sleep(500)

    Jump('func_14_A82')

    def _loc_A9C(): pass

    label('loc_A9C')

    Return()

# id: 0x0015 offset: 0xA9D
@scena.Code('func_15_A9D')
def func_15_A9D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AB2',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_15_A9D')

    def _loc_AB2(): pass

    label('loc_AB2')

    Return()

# id: 0x0016 offset: 0xAB3
@scena.Code('func_16_AB3')
def func_16_AB3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AE9',
    )

    SetChrChipByIndex(0x00FE, 41)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 42)
    OP_99(0x00FE, 0x00, 0x00, 0x000003E8)
    Sleep(1000)

    Jump('func_16_AB3')

    def _loc_AE9(): pass

    label('loc_AE9')

    Return()

# id: 0x0017 offset: 0xAEA
@scena.Code('func_17_AEA')
def func_17_AEA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B04',
    )

    OP_99(0x00FE, 0x00, 0x0A, 0x000007D0)
    Sleep(500)

    Jump('func_17_AEA')

    def _loc_B04(): pass

    label('loc_B04')

    Return()

# id: 0x0018 offset: 0xB05
@scena.Code('func_18_B05')
def func_18_B05():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B1F',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
    Sleep(500)

    Jump('func_18_B05')

    def _loc_B1F(): pass

    label('loc_B1F')

    Return()

# id: 0x0019 offset: 0xB20
@scena.Code('func_19_B20')
def func_19_B20():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B35',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_19_B20')

    def _loc_B35(): pass

    label('loc_B35')

    Return()

# id: 0x001A offset: 0xB36
@scena.Code('func_1A_B36')
def func_1A_B36():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B6C',
    )

    SetChrChipByIndex(0x00FE, 53)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 54)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_1A_B36')

    def _loc_B6C(): pass

    label('loc_B6C')

    Return()

# id: 0x001B offset: 0xB6D
@scena.Code('func_1B_B6D')
def func_1B_B6D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B87',
    )

    OP_99(0x00FE, 0x00, 0x0E, 0x000007D0)
    Sleep(500)

    Jump('func_1B_B6D')

    def _loc_B87(): pass

    label('loc_B87')

    Return()

# id: 0x001C offset: 0xB88
@scena.Code('func_1C_B88')
def func_1C_B88():
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

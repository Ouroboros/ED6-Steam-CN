import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0033_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0033   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '00100艾丝蒂尔待机'),
    TXT(0x02, '00101艾丝蒂尔移动'),
    TXT(0x03, '00102艾丝蒂尔攻击'),
    TXT(0x04, '00103艾丝蒂尔挨打'),
    TXT(0x05, '00104艾丝蒂尔倒下'),
    TXT(0x06, '00105艾丝蒂尔魔法咏唱'),
    TXT(0x07, '00106艾丝蒂尔魔法发动'),
    TXT(0x08, '00107艾丝蒂尔胜利'),
    TXT(0x09, '00110约修亚待机'),
    TXT(0x0A, '00111约修亚移动'),
    TXT(0x0B, '00112约修亚攻击'),
    TXT(0x0C, '00113约修亚挨打'),
    TXT(0x0D, '00114约修亚倒下'),
    TXT(0x0E, '00115约修亚魔法咏唱'),
    TXT(0x0F, '00116约修亚魔法发动'),
    TXT(0x10, '00117约修亚胜利'),
    TXT(0x11, '00170金待机'),
    TXT(0x12, '00171金移动'),
    TXT(0x13, '00172金攻击'),
    TXT(0x14, '00173金挨打'),
    TXT(0x15, '00174金倒下'),
    TXT(0x16, '00175金魔法咏唱'),
    TXT(0x17, '00176金魔法发动'),
    TXT(0x18, '00177金胜利'),
    TXT(0x19, '00150阿加特待机'),
    TXT(0x1A, '00151阿加特移动'),
    TXT(0x1B, '00152阿加特攻击'),
    TXT(0x1C, '00153阿加特挨打'),
    TXT(0x1D, '00154阿加特倒下'),
    TXT(0x1E, '00155阿加特魔法咏唱'),
    TXT(0x1F, '00156阿加特魔法发动'),
    TXT(0x20, '00157阿加特胜利'),
    TXT(0x21, '00130奥利维尔待机'),
    TXT(0x22, '00131奥利维尔移动'),
    TXT(0x23, '00132奥利维尔攻击'),
    TXT(0x24, '00133奥利维尔挨打'),
    TXT(0x25, '00134奥利维尔倒下'),
    TXT(0x26, '00135奥利维尔魔法咏唱'),
    TXT(0x27, '00136奥利维尔魔法发动'),
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

# id: 0xFFFF offset: 0xB09
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
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00102._CH', 'ED6_DT07/CH00102P._CP'),
        ('ED6_DT07/CH00103._CH', 'ED6_DT07/CH00103P._CP'),
        ('ED6_DT07/CH00104._CH', 'ED6_DT07/CH00104P._CP'),
        ('ED6_DT07/CH00105._CH', 'ED6_DT07/CH00105P._CP'),
        ('ED6_DT07/CH00106._CH', 'ED6_DT07/CH00106P._CP'),
        ('ED6_DT07/CH00107._CH', 'ED6_DT07/CH00107P._CP'),
        ('ED6_DT07/CH00104._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00104._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00104._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00104._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00112._CH', 'ED6_DT07/CH00112P._CP'),
        ('ED6_DT07/CH00113._CH', 'ED6_DT07/CH00113P._CP'),
        ('ED6_DT07/CH00114._CH', 'ED6_DT07/CH00114P._CP'),
        ('ED6_DT07/CH00115._CH', 'ED6_DT07/CH00115P._CP'),
        ('ED6_DT07/CH00116._CH', 'ED6_DT07/CH00116P._CP'),
        ('ED6_DT07/CH00117._CH', 'ED6_DT07/CH00117P._CP'),
        ('ED6_DT07/CH00114._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00114._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00114._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00114._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH00172._CH', 'ED6_DT07/CH00172P._CP'),
        ('ED6_DT07/CH00173._CH', 'ED6_DT07/CH00173P._CP'),
        ('ED6_DT07/CH00174._CH', 'ED6_DT07/CH00174P._CP'),
        ('ED6_DT07/CH00175._CH', 'ED6_DT07/CH00175P._CP'),
        ('ED6_DT07/CH00176._CH', 'ED6_DT07/CH00176P._CP'),
        ('ED6_DT07/CH00177._CH', 'ED6_DT07/CH00177P._CP'),
        ('ED6_DT07/CH00174._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00174._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00174._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00174._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP'),
        ('ED6_DT07/CH00153._CH', 'ED6_DT07/CH00153P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00154P._CP'),
        ('ED6_DT07/CH00155._CH', 'ED6_DT07/CH00155P._CP'),
        ('ED6_DT07/CH00156._CH', 'ED6_DT07/CH00156P._CP'),
        ('ED6_DT07/CH00157._CH', 'ED6_DT07/CH00157P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH00132._CH', 'ED6_DT07/CH00132P._CP'),
        ('ED6_DT07/CH00133._CH', 'ED6_DT07/CH00133P._CP'),
        ('ED6_DT07/CH00134._CH', 'ED6_DT07/CH00134P._CP'),
        ('ED6_DT07/CH00135._CH', 'ED6_DT07/CH00135P._CP'),
        ('ED6_DT07/CH00136._CH', 'ED6_DT07/CH00136P._CP'),
        ('ED6_DT07/CH00137._CH', 'ED6_DT07/CH00137P._CP'),
        ('ED6_DT07/CH00134._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00134._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00134._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00134._CH', 'ED6_DT07/CH00130P._CP'),
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

    OP_99(0x00FE, 0x00, 0x07, 1800)

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

    OP_99(0x00FE, 0x00, 0x07, 2000)

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

    OP_99(0x00FE, 0x00, 0x00, 1500)
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

    OP_99(0x00FE, 0x00, 0x03, 2000)
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

    OP_99(0x00FE, 0x00, 0x07, 2000)
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
        'loc_847',
    )

    OP_99(0x00FE, 0x00, 0x0C, 2000)
    Sleep(500)

    Jump('func_08_82D')

    def _loc_847(): pass

    label('loc_847')

    Return()

# id: 0x0009 offset: 0x848
@scena.Code('func_09_848')
def func_09_848():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_85D',
    )

    OP_99(0x00FE, 0x00, 0x03, 1200)

    Jump('func_09_848')

    def _loc_85D(): pass

    label('loc_85D')

    Return()

# id: 0x000A offset: 0x85E
@scena.Code('func_0A_85E')
def func_0A_85E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_894',
    )

    SetChrChipByIndex(0x00FE, 5)
    OP_99(0x00FE, 0x00, 0x03, 1200)
    OP_99(0x00FE, 0x00, 0x03, 1200)
    SetChrChipByIndex(0x00FE, 6)
    OP_99(0x00FE, 0x00, 0x01, 1200)
    Sleep(1000)

    Jump('func_0A_85E')

    def _loc_894(): pass

    label('loc_894')

    Return()

# id: 0x000B offset: 0x895
@scena.Code('func_0B_895')
def func_0B_895():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8AF',
    )

    OP_99(0x00FE, 0x00, 0x13, 2000)
    Sleep(500)

    Jump('func_0B_895')

    def _loc_8AF(): pass

    label('loc_8AF')

    Return()

# id: 0x000C offset: 0x8B0
@scena.Code('func_0C_8B0')
def func_0C_8B0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8CA',
    )

    OP_99(0x00FE, 0x00, 0x0C, 2000)
    Sleep(500)

    Jump('func_0C_8B0')

    def _loc_8CA(): pass

    label('loc_8CA')

    Return()

# id: 0x000D offset: 0x8CB
@scena.Code('func_0D_8CB')
def func_0D_8CB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8E0',
    )

    OP_99(0x00FE, 0x00, 0x03, 1200)

    Jump('func_0D_8CB')

    def _loc_8E0(): pass

    label('loc_8E0')

    Return()

# id: 0x000E offset: 0x8E1
@scena.Code('func_0E_8E1')
def func_0E_8E1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_917',
    )

    SetChrChipByIndex(0x00FE, 17)
    OP_99(0x00FE, 0x00, 0x03, 1200)
    OP_99(0x00FE, 0x00, 0x03, 1200)
    SetChrChipByIndex(0x00FE, 18)
    OP_99(0x00FE, 0x00, 0x01, 1200)
    Sleep(1000)

    Jump('func_0E_8E1')

    def _loc_917(): pass

    label('loc_917')

    Return()

# id: 0x000F offset: 0x918
@scena.Code('func_0F_918')
def func_0F_918():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_932',
    )

    OP_99(0x00FE, 0x00, 0x21, 2000)
    Sleep(500)

    Jump('func_0F_918')

    def _loc_932(): pass

    label('loc_932')

    Return()

# id: 0x0010 offset: 0x933
@scena.Code('func_10_933')
def func_10_933():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_94D',
    )

    OP_99(0x00FE, 0x00, 0x07, 2500)
    Sleep(500)

    Jump('func_10_933')

    def _loc_94D(): pass

    label('loc_94D')

    Return()

# id: 0x0011 offset: 0x94E
@scena.Code('func_11_94E')
def func_11_94E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_963',
    )

    OP_99(0x00FE, 0x00, 0x03, 1000)

    Jump('func_11_94E')

    def _loc_963(): pass

    label('loc_963')

    Return()

# id: 0x0012 offset: 0x964
@scena.Code('func_12_964')
def func_12_964():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_99A',
    )

    SetChrChipByIndex(0x00FE, 29)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    SetChrChipByIndex(0x00FE, 30)
    OP_99(0x00FE, 0x00, 0x00, 1000)
    Sleep(1000)

    Jump('func_12_964')

    def _loc_99A(): pass

    label('loc_99A')

    Return()

# id: 0x0013 offset: 0x99B
@scena.Code('func_13_99B')
def func_13_99B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9B5',
    )

    OP_99(0x00FE, 0x00, 0x07, 2000)
    Sleep(500)

    Jump('func_13_99B')

    def _loc_9B5(): pass

    label('loc_9B5')

    Return()

# id: 0x0014 offset: 0x9B6
@scena.Code('func_14_9B6')
def func_14_9B6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9D0',
    )

    OP_99(0x00FE, 0x00, 0x07, 2500)
    Sleep(500)

    Jump('func_14_9B6')

    def _loc_9D0(): pass

    label('loc_9D0')

    Return()

# id: 0x0015 offset: 0x9D1
@scena.Code('func_15_9D1')
def func_15_9D1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9E6',
    )

    OP_99(0x00FE, 0x00, 0x03, 1000)

    Jump('func_15_9D1')

    def _loc_9E6(): pass

    label('loc_9E6')

    Return()

# id: 0x0016 offset: 0x9E7
@scena.Code('func_16_9E7')
def func_16_9E7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A1D',
    )

    SetChrChipByIndex(0x00FE, 41)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    SetChrChipByIndex(0x00FE, 42)
    OP_99(0x00FE, 0x00, 0x00, 1000)
    Sleep(1000)

    Jump('func_16_9E7')

    def _loc_A1D(): pass

    label('loc_A1D')

    Return()

# id: 0x0017 offset: 0xA1E
@scena.Code('func_17_A1E')
def func_17_A1E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A38',
    )

    OP_99(0x00FE, 0x00, 0x0A, 2000)
    Sleep(500)

    Jump('func_17_A1E')

    def _loc_A38(): pass

    label('loc_A38')

    Return()

# id: 0x0018 offset: 0xA39
@scena.Code('func_18_A39')
def func_18_A39():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A53',
    )

    OP_99(0x00FE, 0x00, 0x07, 2000)
    Sleep(500)

    Jump('func_18_A39')

    def _loc_A53(): pass

    label('loc_A53')

    Return()

# id: 0x0019 offset: 0xA54
@scena.Code('func_19_A54')
def func_19_A54():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A69',
    )

    OP_99(0x00FE, 0x00, 0x03, 1200)

    Jump('func_19_A54')

    def _loc_A69(): pass

    label('loc_A69')

    Return()

# id: 0x001A offset: 0xA6A
@scena.Code('func_1A_A6A')
def func_1A_A6A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AA0',
    )

    SetChrChipByIndex(0x00FE, 53)
    OP_99(0x00FE, 0x00, 0x03, 1200)
    OP_99(0x00FE, 0x00, 0x03, 1200)
    SetChrChipByIndex(0x00FE, 54)
    OP_99(0x00FE, 0x00, 0x01, 1200)
    Sleep(1000)

    Jump('func_1A_A6A')

    def _loc_AA0(): pass

    label('loc_AA0')

    Return()

# id: 0x001B offset: 0xAA1
@scena.Code('func_1B_AA1')
def func_1B_AA1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_ABB',
    )

    OP_99(0x00FE, 0x00, 0x0E, 2000)
    Sleep(500)

    Jump('func_1B_AA1')

    def _loc_ABB(): pass

    label('loc_ABB')

    Return()

# id: 0x001C offset: 0xABC
@scena.Code('func_1C_ABC')
def func_1C_ABC():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '你好。',
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

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import A0022_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('A0022   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '00130雪拉待机'),
    TXT(0x02, '00131雪拉移动'),
    TXT(0x03, '00132雪拉攻击'),
    TXT(0x04, '00133雪拉被弹开'),
    TXT(0x05, '00134雪拉倒下'),
    TXT(0x06, '00135雪拉魔法咏唱'),
    TXT(0x07, '00136雪拉魔法发射'),
    TXT(0x08, '00137雪拉胜利'),
    TXT(0x09, '00160提妲待机'),
    TXT(0x0A, '00161提妲移动'),
    TXT(0x0B, '00162提妲攻击'),
    TXT(0x0C, '00163提妲被弹开'),
    TXT(0x0D, '00164提妲倒下'),
    TXT(0x0E, '00165提妲魔法咏唱'),
    TXT(0x0F, '00166提妲魔法发射'),
    TXT(0x10, '00167提妲胜利'),
    TXT(0x11, '00140科洛丝待机'),
    TXT(0x12, '00141科洛丝移动'),
    TXT(0x13, '00142科洛丝攻击'),
    TXT(0x14, '00143科洛丝被弹开'),
    TXT(0x15, '00144科洛丝倒下'),
    TXT(0x16, '00145科洛丝魔法咏唱'),
    TXT(0x17, '00146科洛丝魔法发射'),
    TXT(0x18, '00147科洛丝胜利'),
    TXT(0x19, '04210科洛丝待机'),
    TXT(0x1A, '04211科洛丝移动'),
    TXT(0x1B, '04212科洛丝攻击'),
    TXT(0x1C, '04213科洛丝被弹开'),
    TXT(0x1D, '04214科洛丝倒下'),
    TXT(0x1E, '04215科洛丝魔法咏唱'),
    TXT(0x1F, '04216科洛丝魔法发射'),
    TXT(0x20, '04217科洛丝胜利'),
    TXT(0x21, '00110约修亚待机'),
    TXT(0x22, '00111约修亚移动'),
    TXT(0x23, '00112约修亚攻击'),
    TXT(0x24, '00113约修亚被弹开'),
    TXT(0x25, '00114约修亚倒下'),
    TXT(0x26, '00115约修亚魔法咏唱'),
    TXT(0x27, '00116约修亚魔法发射'),
    TXT(0x28, '00117约修亚胜利'),
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

# id: 0xFFFF offset: 0xB90
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
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00112._CH', 'ED6_DT07/CH00112P._CP'),
        ('ED6_DT07/CH00113._CH', 'ED6_DT07/CH00113P._CP'),
        ('ED6_DT07/CH00114._CH', 'ED6_DT07/CH00114P._CP'),
        ('ED6_DT07/CH00115._CH', 'ED6_DT07/CH00115P._CP'),
        ('ED6_DT07/CH00116._CH', 'ED6_DT07/CH00116P._CP'),
        ('ED6_DT07/CH00117._CH', 'ED6_DT07/CH00117P._CP'),
        ('ED6_DT07/CH00113._CH', 'ED6_DT07/CH00113P._CP'),
        ('ED6_DT07/CH00113._CH', 'ED6_DT07/CH00113P._CP'),
        ('ED6_DT07/CH00113._CH', 'ED6_DT07/CH00113P._CP'),
        ('ED6_DT07/CH00113._CH', 'ED6_DT07/CH00113P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT07/CH00123._CH', 'ED6_DT07/CH00123P._CP'),
        ('ED6_DT07/CH00124._CH', 'ED6_DT07/CH00124P._CP'),
        ('ED6_DT07/CH00125._CH', 'ED6_DT07/CH00125P._CP'),
        ('ED6_DT07/CH00126._CH', 'ED6_DT07/CH00126P._CP'),
        ('ED6_DT07/CH00127._CH', 'ED6_DT07/CH00127P._CP'),
        ('ED6_DT07/CH00123._CH', 'ED6_DT07/CH00123P._CP'),
        ('ED6_DT07/CH00123._CH', 'ED6_DT07/CH00123P._CP'),
        ('ED6_DT07/CH00123._CH', 'ED6_DT07/CH00123P._CP'),
        ('ED6_DT07/CH00123._CH', 'ED6_DT07/CH00123P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00162._CH', 'ED6_DT07/CH00162P._CP'),
        ('ED6_DT07/CH00163._CH', 'ED6_DT07/CH00163P._CP'),
        ('ED6_DT07/CH00164._CH', 'ED6_DT07/CH00164P._CP'),
        ('ED6_DT07/CH00165._CH', 'ED6_DT07/CH00165P._CP'),
        ('ED6_DT07/CH00166._CH', 'ED6_DT07/CH00166P._CP'),
        ('ED6_DT07/CH00167._CH', 'ED6_DT07/CH00167P._CP'),
        ('ED6_DT07/CH00163._CH', 'ED6_DT07/CH00163P._CP'),
        ('ED6_DT07/CH00163._CH', 'ED6_DT07/CH00163P._CP'),
        ('ED6_DT07/CH00163._CH', 'ED6_DT07/CH00163P._CP'),
        ('ED6_DT07/CH00163._CH', 'ED6_DT07/CH00163P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH00142._CH', 'ED6_DT07/CH00142P._CP'),
        ('ED6_DT07/CH00143._CH', 'ED6_DT07/CH00143P._CP'),
        ('ED6_DT07/CH00144._CH', 'ED6_DT07/CH00144P._CP'),
        ('ED6_DT07/CH00145._CH', 'ED6_DT07/CH00145P._CP'),
        ('ED6_DT07/CH00146._CH', 'ED6_DT07/CH00146P._CP'),
        ('ED6_DT07/CH00147._CH', 'ED6_DT07/CH00147P._CP'),
        ('ED6_DT07/CH00143._CH', 'ED6_DT07/CH00143P._CP'),
        ('ED6_DT07/CH00143._CH', 'ED6_DT07/CH00143P._CP'),
        ('ED6_DT07/CH00143._CH', 'ED6_DT07/CH00143P._CP'),
        ('ED6_DT07/CH00143._CH', 'ED6_DT07/CH00143P._CP'),
        ('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP'),
        ('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP'),
        ('ED6_DT27/CH04212._CH', 'ED6_DT27/CH04212P._CP'),
        ('ED6_DT27/CH04213._CH', 'ED6_DT27/CH04213P._CP'),
        ('ED6_DT27/CH04214._CH', 'ED6_DT27/CH04214P._CP'),
        ('ED6_DT27/CH04215._CH', 'ED6_DT27/CH04215P._CP'),
        ('ED6_DT27/CH04216._CH', 'ED6_DT27/CH04216P._CP'),
        ('ED6_DT27/CH04217._CH', 'ED6_DT27/CH04217P._CP'),
        ('ED6_DT27/CH04213._CH', 'ED6_DT27/CH04213P._CP'),
        ('ED6_DT27/CH04213._CH', 'ED6_DT27/CH04213P._CP'),
        ('ED6_DT27/CH04213._CH', 'ED6_DT27/CH04213P._CP'),
        ('ED6_DT27/CH04213._CH', 'ED6_DT27/CH04213P._CP'),
    ]

# id: 0x10002 offset: 0x28A
@scena.NpcData('NpcData')
def NpcData():
    return (
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
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x000C,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x000D,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x000E,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x000F,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x0010,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x0011,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x0012,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x0013,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x0014,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x0015,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x0016,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x0017,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x0018,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x0019,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x001A,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
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
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
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
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
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
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
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
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001C,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001D,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 32000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001E,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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

    OP_99(0x00FE, 0x00, 0x03, 0x000007D0)
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
        'loc_823',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
    Sleep(500)

    Jump('func_07_809')

    def _loc_823(): pass

    label('loc_823')

    Return()

# id: 0x0008 offset: 0x824
@scena.Code('func_08_824')
def func_08_824():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_839',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_08_824')

    def _loc_839(): pass

    label('loc_839')

    Return()

# id: 0x0009 offset: 0x83A
@scena.Code('func_09_83A')
def func_09_83A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_870',
    )

    SetChrChipByIndex(0x00FE, 5)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 6)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_09_83A')

    def _loc_870(): pass

    label('loc_870')

    Return()

# id: 0x000A offset: 0x871
@scena.Code('func_0A_871')
def func_0A_871():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_88B',
    )

    OP_99(0x00FE, 0x00, 0x0E, 0x000007D0)
    Sleep(500)

    Jump('func_0A_871')

    def _loc_88B(): pass

    label('loc_88B')

    Return()

# id: 0x000B offset: 0x88C
@scena.Code('func_0B_88C')
def func_0B_88C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8A6',
    )

    OP_99(0x00FE, 0x00, 0x09, 0x000007D0)
    Sleep(500)

    Jump('func_0B_88C')

    def _loc_8A6(): pass

    label('loc_8A6')

    Return()

# id: 0x000C offset: 0x8A7
@scena.Code('func_0C_8A7')
def func_0C_8A7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8BC',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_0C_8A7')

    def _loc_8BC(): pass

    label('loc_8BC')

    Return()

# id: 0x000D offset: 0x8BD
@scena.Code('func_0D_8BD')
def func_0D_8BD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8F3',
    )

    SetChrChipByIndex(0x00FE, 17)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 18)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_0D_8BD')

    def _loc_8F3(): pass

    label('loc_8F3')

    Return()

# id: 0x000E offset: 0x8F4
@scena.Code('func_0E_8F4')
def func_0E_8F4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_90E',
    )

    OP_99(0x00FE, 0x00, 0x0D, 0x000007D0)
    Sleep(500)

    Jump('func_0E_8F4')

    def _loc_90E(): pass

    label('loc_90E')

    Return()

# id: 0x000F offset: 0x90F
@scena.Code('func_0F_90F')
def func_0F_90F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_929',
    )

    OP_99(0x00FE, 0x00, 0x0D, 0x000007D0)
    Sleep(500)

    Jump('func_0F_90F')

    def _loc_929(): pass

    label('loc_929')

    Return()

# id: 0x0010 offset: 0x92A
@scena.Code('func_10_92A')
def func_10_92A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_93F',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_10_92A')

    def _loc_93F(): pass

    label('loc_93F')

    Return()

# id: 0x0011 offset: 0x940
@scena.Code('func_11_940')
def func_11_940():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_976',
    )

    SetChrChipByIndex(0x00FE, 29)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 30)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_11_940')

    def _loc_976(): pass

    label('loc_976')

    Return()

# id: 0x0012 offset: 0x977
@scena.Code('func_12_977')
def func_12_977():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_991',
    )

    OP_99(0x00FE, 0x00, 0x0E, 0x000003E8)
    Sleep(1000)

    Jump('func_12_977')

    def _loc_991(): pass

    label('loc_991')

    Return()

# id: 0x0013 offset: 0x992
@scena.Code('func_13_992')
def func_13_992():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9AC',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
    Sleep(500)

    Jump('func_13_992')

    def _loc_9AC(): pass

    label('loc_9AC')

    Return()

# id: 0x0014 offset: 0x9AD
@scena.Code('func_14_9AD')
def func_14_9AD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9C2',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_14_9AD')

    def _loc_9C2(): pass

    label('loc_9C2')

    Return()

# id: 0x0015 offset: 0x9C3
@scena.Code('func_15_9C3')
def func_15_9C3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9F9',
    )

    SetChrChipByIndex(0x00FE, 41)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 42)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_15_9C3')

    def _loc_9F9(): pass

    label('loc_9F9')

    Return()

# id: 0x0016 offset: 0x9FA
@scena.Code('func_16_9FA')
def func_16_9FA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A14',
    )

    OP_99(0x00FE, 0x00, 0x14, 0x000007D0)
    Sleep(500)

    Jump('func_16_9FA')

    def _loc_A14(): pass

    label('loc_A14')

    Return()

# id: 0x0017 offset: 0xA15
@scena.Code('func_17_A15')
def func_17_A15():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A2F',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
    Sleep(500)

    Jump('func_17_A15')

    def _loc_A2F(): pass

    label('loc_A2F')

    Return()

# id: 0x0018 offset: 0xA30
@scena.Code('func_18_A30')
def func_18_A30():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A45',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_18_A30')

    def _loc_A45(): pass

    label('loc_A45')

    Return()

# id: 0x0019 offset: 0xA46
@scena.Code('func_19_A46')
def func_19_A46():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A7C',
    )

    SetChrChipByIndex(0x00FE, 53)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 54)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_19_A46')

    def _loc_A7C(): pass

    label('loc_A7C')

    Return()

# id: 0x001A offset: 0xA7D
@scena.Code('func_1A_A7D')
def func_1A_A7D():
    SetChrFlags(0x00FE, 0x0002)
    def _loc_A82(): pass

    label('loc_A82')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A9C',
    )

    OP_99(0x00FE, 0x00, 0x14, 0x000007D0)
    Sleep(500)

    Jump('loc_A82')

    def _loc_A9C(): pass

    label('loc_A9C')

    Return()

# id: 0x001B offset: 0xA9D
@scena.Code('func_1B_A9D')
def func_1B_A9D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AB7',
    )

    OP_99(0x00FE, 0x00, 0x0C, 0x000007D0)
    Sleep(500)

    Jump('func_1B_A9D')

    def _loc_AB7(): pass

    label('loc_AB7')

    Return()

# id: 0x001C offset: 0xAB8
@scena.Code('func_1C_AB8')
def func_1C_AB8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_ACD',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)

    Jump('func_1C_AB8')

    def _loc_ACD(): pass

    label('loc_ACD')

    Return()

# id: 0x001D offset: 0xACE
@scena.Code('func_1D_ACE')
def func_1D_ACE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B04',
    )

    SetChrChipByIndex(0x00FE, 5)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    OP_99(0x00FE, 0x00, 0x03, 0x000004B0)
    SetChrChipByIndex(0x00FE, 6)
    OP_99(0x00FE, 0x00, 0x01, 0x000004B0)
    Sleep(1000)

    Jump('func_1D_ACE')

    def _loc_B04(): pass

    label('loc_B04')

    Return()

# id: 0x001E offset: 0xB05
@scena.Code('func_1E_B05')
def func_1E_B05():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B1F',
    )

    OP_99(0x00FE, 0x00, 0x21, 0x000007D0)
    Sleep(500)

    Jump('func_1E_B05')

    def _loc_B1F(): pass

    label('loc_B1F')

    Return()

# id: 0x001F offset: 0xB20
@scena.Code('func_1F_B20')
def func_1F_B20():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B3A',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)
    Sleep(500)

    Jump('func_1F_B20')

    def _loc_B3A(): pass

    label('loc_B3A')

    Return()

# id: 0x0020 offset: 0xB3B
@scena.Code('func_20_B3B')
def func_20_B3B():
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

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0036_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0036   ._SN')

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

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00450._CH', 'ED6_DT07/CH00450P._CP'),
        ('ED6_DT07/CH00451._CH', 'ED6_DT07/CH00451P._CP'),
        ('ED6_DT07/CH00452._CH', 'ED6_DT07/CH00452P._CP'),
        ('ED6_DT07/CH00453._CH', 'ED6_DT07/CH00453P._CP'),
        ('ED6_DT07/CH00454._CH', 'ED6_DT07/CH00454P._CP'),
        ('ED6_DT07/CH00460._CH', 'ED6_DT07/CH00460P._CP'),
        ('ED6_DT07/CH00461._CH', 'ED6_DT07/CH00461P._CP'),
        ('ED6_DT07/CH00462._CH', 'ED6_DT07/CH00462P._CP'),
        ('ED6_DT07/CH00463._CH', 'ED6_DT07/CH00463P._CP'),
        ('ED6_DT07/CH00464._CH', 'ED6_DT07/CH00464P._CP'),
        ('ED6_DT07/CH00470._CH', 'ED6_DT07/CH00470P._CP'),
        ('ED6_DT07/CH00471._CH', 'ED6_DT07/CH00471P._CP'),
        ('ED6_DT07/CH00472._CH', 'ED6_DT07/CH00472P._CP'),
        ('ED6_DT07/CH00473._CH', 'ED6_DT07/CH00473P._CP'),
        ('ED6_DT07/CH00474._CH', 'ED6_DT07/CH00474P._CP'),
        ('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP'),
        ('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP'),
        ('ED6_DT07/CH00412._CH', 'ED6_DT07/CH00412P._CP'),
        ('ED6_DT07/CH00413._CH', 'ED6_DT07/CH00413P._CP'),
        ('ED6_DT07/CH00414._CH', 'ED6_DT07/CH00414P._CP'),
        ('ED6_DT07/CH00415._CH', 'ED6_DT07/CH00415P._CP'),
        ('ED6_DT07/CH00416._CH', 'ED6_DT07/CH00416P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT07/CH00422._CH', 'ED6_DT07/CH00422P._CP'),
        ('ED6_DT07/CH00423._CH', 'ED6_DT07/CH00423P._CP'),
        ('ED6_DT07/CH00424._CH', 'ED6_DT07/CH00424P._CP'),
        ('ED6_DT07/CH00425._CH', 'ED6_DT07/CH00425P._CP'),
        ('ED6_DT07/CH00426._CH', 'ED6_DT07/CH00426P._CP'),
        ('ED6_DT07/CH00480._CH', 'ED6_DT07/CH00480P._CP'),
        ('ED6_DT07/CH00481._CH', 'ED6_DT07/CH00481P._CP'),
        ('ED6_DT07/CH00482._CH', 'ED6_DT07/CH00482P._CP'),
        ('ED6_DT07/CH00483._CH', 'ED6_DT07/CH00483P._CP'),
        ('ED6_DT07/CH00484._CH', 'ED6_DT07/CH00484P._CP'),
        ('ED6_DT07/CH00485._CH', 'ED6_DT07/CH00485P._CP'),
        ('ED6_DT07/CH00486._CH', 'ED6_DT07/CH00486P._CP'),
        ('ED6_DT07/CH00490._CH', 'ED6_DT07/CH00490P._CP'),
        ('ED6_DT07/CH00491._CH', 'ED6_DT07/CH00491P._CP'),
        ('ED6_DT07/CH00492._CH', 'ED6_DT07/CH00492P._CP'),
        ('ED6_DT07/CH00493._CH', 'ED6_DT07/CH00493P._CP'),
        ('ED6_DT07/CH00494._CH', 'ED6_DT07/CH00494P._CP'),
        ('ED6_DT07/CH00495._CH', 'ED6_DT07/CH00495P._CP'),
        ('ED6_DT07/CH00496._CH', 'ED6_DT07/CH00496P._CP'),
    ]

# id: 0x10001 offset: 0x202
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '00450迪恩待机',
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
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00451迪恩移动',
            x                   = 4000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00452迪恩攻击',
            x                   = 4000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00453迪恩挨打',
            x                   = 4000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00454迪恩倒下',
            x                   = 4000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00460雷斯待机',
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
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00461雷斯移动',
            x                   = 8000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00462雷斯攻击',
            x                   = 8000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00463雷斯挨打',
            x                   = 8000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00464雷斯倒下',
            x                   = 8000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00470洛克待机',
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
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00471洛克移动',
            x                   = 12000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00472洛克攻击',
            x                   = 12000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00473洛克挨打',
            x                   = 12000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00474洛克倒下',
            x                   = 12000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00410男游击士２待机',
            x                   = 16000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00411男游击士２移动',
            x                   = 16000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00412男游击士２攻击',
            x                   = 16000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00413男游击士２挨打',
            x                   = 16000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00414男游击士２倒下',
            x                   = 16000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00415男游击士２魔法咏唱',
            x                   = 16000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00418男游击士２魔法发动',
            x                   = 16000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00420女游击士２待机',
            x                   = 20000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00421女游击士２移动',
            x                   = 20000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00422女游击士２攻击',
            x                   = 20000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00423女游击士２挨打',
            x                   = 20000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00424女游击士２倒下',
            x                   = 20000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00425女游击士２魔法咏唱',
            x                   = 20000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00428女游击士２魔法发动',
            x                   = 20000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00480洛伦斯待机',
            x                   = 24000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00481洛伦斯移动',
            x                   = 24000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00482洛伦斯攻击',
            x                   = 24000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00483洛伦斯挨打',
            x                   = 24000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00484洛伦斯倒下',
            x                   = 24000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00485洛伦斯魔法咏唱',
            x                   = 24000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000C,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00488洛伦斯魔法发动',
            x                   = 24000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000D,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00490男游击士４待机',
            x                   = 28000,
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
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00491男游击士４移动',
            x                   = 28000,
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
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00492男游击士４攻击',
            x                   = 28000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00493男游击士４挨打',
            x                   = 28000,
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
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00494男游击士４倒下',
            x                   = 28000,
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
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00495男游击士４魔法咏唱',
            x                   = 28000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000E,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '00498男游击士４魔法发动',
            x                   = 28000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000F,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
    )

# id: 0x10002 offset: 0x762
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x762
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x762
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x762
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x763
@scena.Code('func_01_763')
def func_01_763():
    Return()

# id: 0x0002 offset: 0x764
@scena.Code('func_02_764')
def func_02_764():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_779',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_764')

    def _loc_779(): pass

    label('loc_779')

    Return()

# id: 0x0003 offset: 0x77A
@scena.Code('func_03_77A')
def func_03_77A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_78F',
    )

    OP_99(0x00FE, 0x00, 0x07, 3000)

    Jump('func_03_77A')

    def _loc_78F(): pass

    label('loc_78F')

    Return()

# id: 0x0004 offset: 0x790
@scena.Code('func_04_790')
def func_04_790():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7AA',
    )

    OP_99(0x00FE, 0x00, 0x00, 1500)
    Sleep(500)

    Jump('func_04_790')

    def _loc_7AA(): pass

    label('loc_7AA')

    Return()

# id: 0x0005 offset: 0x7AB
@scena.Code('func_05_7AB')
def func_05_7AB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7C5',
    )

    OP_99(0x00FE, 0x00, 0x03, 1000)
    Sleep(500)

    Jump('func_05_7AB')

    def _loc_7C5(): pass

    label('loc_7C5')

    Return()

# id: 0x0006 offset: 0x7C6
@scena.Code('func_06_7C6')
def func_06_7C6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7E0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1000)
    Sleep(500)

    Jump('func_06_7C6')

    def _loc_7E0(): pass

    label('loc_7E0')

    Return()

# id: 0x0007 offset: 0x7E1
@scena.Code('func_07_7E1')
def func_07_7E1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7FB',
    )

    OP_99(0x00FE, 0x00, 0x0B, 2400)
    Sleep(500)

    Jump('func_07_7E1')

    def _loc_7FB(): pass

    label('loc_7FB')

    Return()

# id: 0x0008 offset: 0x7FC
@scena.Code('func_08_7FC')
def func_08_7FC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_811',
    )

    OP_99(0x00FE, 0x00, 0x03, 1000)

    Jump('func_08_7FC')

    def _loc_811(): pass

    label('loc_811')

    Return()

# id: 0x0009 offset: 0x812
@scena.Code('func_09_812')
def func_09_812():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_848',
    )

    ChrSetChipByIndex(0x00FE, 20)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    ChrSetChipByIndex(0x00FE, 21)
    OP_99(0x00FE, 0x00, 0x01, 1000)
    Sleep(1000)

    Jump('func_09_812')

    def _loc_848(): pass

    label('loc_848')

    Return()

# id: 0x000A offset: 0x849
@scena.Code('func_0A_849')
def func_0A_849():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_85E',
    )

    OP_99(0x00FE, 0x00, 0x03, 1000)

    Jump('func_0A_849')

    def _loc_85E(): pass

    label('loc_85E')

    Return()

# id: 0x000B offset: 0x85F
@scena.Code('func_0B_85F')
def func_0B_85F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_895',
    )

    ChrSetChipByIndex(0x00FE, 27)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    ChrSetChipByIndex(0x00FE, 28)
    OP_99(0x00FE, 0x00, 0x01, 1000)
    Sleep(1000)

    Jump('func_0B_85F')

    def _loc_895(): pass

    label('loc_895')

    Return()

# id: 0x000C offset: 0x896
@scena.Code('func_0C_896')
def func_0C_896():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8AB',
    )

    OP_99(0x00FE, 0x00, 0x03, 1000)

    Jump('func_0C_896')

    def _loc_8AB(): pass

    label('loc_8AB')

    Return()

# id: 0x000D offset: 0x8AC
@scena.Code('func_0D_8AC')
def func_0D_8AC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8E2',
    )

    ChrSetChipByIndex(0x00FE, 34)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    ChrSetChipByIndex(0x00FE, 35)
    OP_99(0x00FE, 0x00, 0x01, 1000)
    Sleep(1000)

    Jump('func_0D_8AC')

    def _loc_8E2(): pass

    label('loc_8E2')

    Return()

# id: 0x000E offset: 0x8E3
@scena.Code('func_0E_8E3')
def func_0E_8E3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8F8',
    )

    OP_99(0x00FE, 0x00, 0x03, 1000)

    Jump('func_0E_8E3')

    def _loc_8F8(): pass

    label('loc_8F8')

    Return()

# id: 0x000F offset: 0x8F9
@scena.Code('func_0F_8F9')
def func_0F_8F9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_92F',
    )

    ChrSetChipByIndex(0x00FE, 41)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    ChrSetChipByIndex(0x00FE, 42)
    OP_99(0x00FE, 0x00, 0x01, 1000)
    Sleep(1000)

    Jump('func_0F_8F9')

    def _loc_92F(): pass

    label('loc_92F')

    Return()

# id: 0x0010 offset: 0x930
@scena.Code('func_10_930')
def func_10_930():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '喝～',
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

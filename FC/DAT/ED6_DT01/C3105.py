import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3105_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3105   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3105.x'
    header.mapIndex       = 1
    header.bgm            = 34
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02450._CH', 'ED6_DT07/CH02450P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT06/CH20043._CH', 'ED6_DT06/CH20043P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP'),
        ('ED6_DT09/CH10060._CH', 'ED6_DT09/CH10060P._CP'),
        ('ED6_DT09/CH10061._CH', 'ED6_DT09/CH10061P._CP'),
        ('ED6_DT09/CH11010._CH', 'ED6_DT09/CH11010P._CP'),
        ('ED6_DT09/CH11011._CH', 'ED6_DT09/CH11011P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '希德少校',
            x                   = 18530,
            z                   = 0,
            y                   = 20700,
            direction           = 270,
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
            name                = '士兵',
            x                   = 16000,
            z                   = 0,
            y                   = 26000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 16000,
            z                   = 0,
            y                   = 24500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 16000,
            z                   = 0,
            y                   = 23000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 16000,
            z                   = 0,
            y                   = 21500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 16000,
            z                   = 0,
            y                   = 20000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 16000,
            z                   = 0,
            y                   = 18500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 16000,
            z                   = 0,
            y                   = 17000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 16000,
            z                   = 0,
            y                   = 15500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 14500,
            z                   = 0,
            y                   = 26000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 14500,
            z                   = 0,
            y                   = 24500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 14500,
            z                   = 0,
            y                   = 23000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 14500,
            z                   = 0,
            y                   = 21500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 14500,
            z                   = 0,
            y                   = 20000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 14500,
            z                   = 0,
            y                   = 18500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 14500,
            z                   = 0,
            y                   = 17000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 14500,
            z                   = 0,
            y                   = 15500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 13000,
            z                   = 0,
            y                   = 26000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 13000,
            z                   = 0,
            y                   = 24500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 13000,
            z                   = 0,
            y                   = 23000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 13000,
            z                   = 0,
            y                   = 21500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 13000,
            z                   = 0,
            y                   = 20000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 13000,
            z                   = 0,
            y                   = 18500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 13000,
            z                   = 0,
            y                   = 17000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 13000,
            z                   = 0,
            y                   = 15500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 11500,
            z                   = 0,
            y                   = 26000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 11500,
            z                   = 0,
            y                   = 24500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 11500,
            z                   = 0,
            y                   = 23000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 11500,
            z                   = 0,
            y                   = 21500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 11500,
            z                   = 0,
            y                   = 20000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 11500,
            z                   = 0,
            y                   = 18500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 11500,
            z                   = 0,
            y                   = 17000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 11500,
            z                   = 0,
            y                   = 15500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 10000,
            z                   = 0,
            y                   = 26000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 10000,
            z                   = 0,
            y                   = 24500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 10000,
            z                   = 0,
            y                   = 23000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 10000,
            z                   = 0,
            y                   = 21500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 10000,
            z                   = 0,
            y                   = 20000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 10000,
            z                   = 0,
            y                   = 18500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 10000,
            z                   = 0,
            y                   = 17000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 10000,
            z                   = 0,
            y                   = 15500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 8500,
            z                   = 0,
            y                   = 26000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 8500,
            z                   = 0,
            y                   = 24500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 8500,
            z                   = 0,
            y                   = 23000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 8500,
            z                   = 0,
            y                   = 21500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 8500,
            z                   = 0,
            y                   = 20000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 8500,
            z                   = 0,
            y                   = 18500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 8500,
            z                   = 0,
            y                   = 17000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 8500,
            z                   = 0,
            y                   = 15500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 7000,
            z                   = 0,
            y                   = 26000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 7000,
            z                   = 0,
            y                   = 24500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 7000,
            z                   = 0,
            y                   = 23000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 7000,
            z                   = 0,
            y                   = 21500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 7000,
            z                   = 0,
            y                   = 20000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 7000,
            z                   = 0,
            y                   = 18500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 7000,
            z                   = 0,
            y                   = 17000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 7000,
            z                   = 0,
            y                   = 15500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 5500,
            z                   = 0,
            y                   = 26000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 5500,
            z                   = 0,
            y                   = 24500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 5500,
            z                   = 0,
            y                   = 23000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 5500,
            z                   = 0,
            y                   = 21500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 5500,
            z                   = 0,
            y                   = 20000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 5500,
            z                   = 0,
            y                   = 18500,
            direction           = 90,
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
            name                = '士兵',
            x                   = 5500,
            z                   = 0,
            y                   = 17000,
            direction           = 90,
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
            name                = '士兵',
            x                   = 5500,
            z                   = 0,
            y                   = 15500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x93A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -44530,
            z           = 0,
            y           = 58590,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0245,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -16570,
            z           = 0,
            y           = 59280,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0246,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -14450,
            z           = 0,
            y           = 31660,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0247,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 15470,
            z           = 0,
            y           = 29810,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0245,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 18860,
            z           = 0,
            y           = 12280,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0246,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 5110,
            z           = 0,
            y           = 17530,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0247,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -17400,
            z           = 0,
            y           = 12730,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0245,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -42340,
            z           = 0,
            y           = 9500,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0246,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -41490,
            z           = 0,
            y           = 41570,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0247,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -19000,
            z           = 0,
            y           = 44460,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0245,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -37970,
            z           = 0,
            y           = 29960,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0246,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0xA6E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA6E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 0,
            triggerY            = 2410,
            triggerRange        = 1500,
            actorX              = 0,
            actorZ              = 1500,
            actorY              = 2410,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1000,
            triggerZ            = 500,
            triggerY            = 36080,
            triggerRange        = 800,
            actorX              = -1000,
            actorZ              = 1500,
            actorY              = 36080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -52400,
            triggerZ            = 500,
            triggerY            = 17020,
            triggerRange        = 800,
            actorX              = -52400,
            actorZ              = 1500,
            actorY              = 17020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xADA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_AE8',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_06_DE6)

    def _loc_AE8(): pass

    label('loc_AE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 3, 0x56B)),
            Expr.Return,
        ),
        'loc_D1B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 5, 0x54D)),
            Expr.Return,
        ),
        'loc_AF9',
    )

    Jump('loc_AF9')

    def _loc_AF9(): pass

    label('loc_AF9')

    ChrSetPos(0x0013, 22160, 0, 11940, 180)
    ChrSetPos(0x0014, 7890, 0, 11990, 180)
    ChrSetPos(0x0015, -8220, 0, 11930, 270)
    ChrSetPos(0x0016, -25800, 0, 11830, 100)
    ChrSetPos(0x0017, -37890, 0, 11800, 272)
    ChrSetPos(0x0018, -38090, 0, 29890, 13)
    ChrSetPos(0x0019, -25930, 0, 29970, 69)
    ChrSetPos(0x001A, -8039, 0, 29860, 90)
    ChrSetPos(0x001B, 7940, 0, 29730, 71)
    ChrSetPos(0x001C, 21810, 0, 29930, 68)
    ChrSetPos(0x001D, -37900, 0, 45970, 195)
    ChrSetPos(0x001E, -26080, 0, 45970, 87)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    CreateThread(0x001D, 0x00, 0x00, func_02_D56)
    CreateThread(0x001E, 0x00, 0x00, func_02_D56)
    CreateThread(0x0016, 0x00, 0x00, func_03_D7A)
    CreateThread(0x0017, 0x00, 0x00, func_03_D7A)
    CreateThread(0x0018, 0x00, 0x00, func_03_D7A)
    CreateThread(0x0019, 0x00, 0x00, func_03_D7A)
    CreateThread(0x0014, 0x00, 0x00, func_04_D9E)
    CreateThread(0x0015, 0x00, 0x00, func_04_D9E)
    CreateThread(0x001A, 0x00, 0x00, func_04_D9E)
    CreateThread(0x001B, 0x00, 0x00, func_04_D9E)
    CreateThread(0x001C, 0x00, 0x00, func_05_DC2)
    CreateThread(0x0013, 0x00, 0x00, func_05_DC2)
    CreateThread(0x0013, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0014, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0015, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0016, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0017, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0018, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0019, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x001A, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x001B, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x001C, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x001D, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x001E, 0x01, 0x00, func_0F_21EE)

    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_CCF',
    )

    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x0017, 0xFF)

    def _loc_CCF(): pass

    label('loc_CCF')

    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_CF5',
    )

    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001B, 0xFF)

    def _loc_CF5(): pass

    label('loc_CF5')

    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_D1B',
    )

    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    TerminateThread(0x001A, 0xFF)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0014, 0xFF)

    def _loc_D1B(): pass

    label('loc_D1B')

    Return()

# id: 0x0001 offset: 0xD1C
@scena.Code('func_01_D1C')
def func_01_D1C():
    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 1, 0x569)),
            Expr.Return,
        ),
        'loc_D36',
    )

    OP_71(0x0001, 0x0010)
    OP_64(0x01, 0x0001)

    def _loc_D36(): pass

    label('loc_D36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 1, 0x569)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 1, 0x571)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D47',
    )

    OP_1B(0x01, 0x00, 0x0014)

    def _loc_D47(): pass

    label('loc_D47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 3, 0x56B)),
            Expr.Return,
        ),
        'loc_D55',
    )

    PlaySE(172, 0x01, 0x64)
    OP_B6(0x00)

    def _loc_D55(): pass

    label('loc_D55')

    Return()

# id: 0x0002 offset: 0xD56
@scena.Code('func_02_D56')
def func_02_D56():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D79',
    )

    OP_8D(0x00FE, -50290, 47710, -13220, 34370, 2200)

    Jump('func_02_D56')

    def _loc_D79(): pass

    label('loc_D79')

    Return()

# id: 0x0003 offset: 0xD7A
@scena.Code('func_03_D7A')
def func_03_D7A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D9D',
    )

    OP_8D(0x00FE, -48590, 32880, -16920, 5190, 2200)

    Jump('func_03_D7A')

    def _loc_D9D(): pass

    label('loc_D9D')

    Return()

# id: 0x0004 offset: 0xD9E
@scena.Code('func_04_D9E')
def func_04_D9E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DC1',
    )

    OP_8D(0x00FE, -14620, 32800, 13430, 4930, 2200)

    Jump('func_04_D9E')

    def _loc_DC1(): pass

    label('loc_DC1')

    Return()

# id: 0x0005 offset: 0xDC2
@scena.Code('func_05_DC2')
def func_05_DC2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DE5',
    )

    OP_8D(0x00FE, 10630, 32450, 23760, 5080, 2200)

    Jump('func_05_DC2')

    def _loc_DE5(): pass

    label('loc_DE5')

    Return()

# id: 0x0006 offset: 0xDE6
@scena.Code('func_06_DE6')
def func_06_DE6():
    EventBegin(0x00)
    PlaySE(172, 0x01, 0x64)
    OP_B6(0x00)
    CameraMove(-32990, 0, 64260, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -32119, 0, 62630, 135)
    ChrSetPos(0x0102, -33540, 0, 62350, 180)
    ChrSetPos(0x0106, -32290, 0, 63720, 135)
    ChrSetPos(0x010B, -33230, 0, 63910, 225)
    ChrSetPos(0x0107, -34440, 0, 63230, 270)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x010B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070091161V#065F啊……这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091162V#102F#5P被发现了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001B,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0020,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0021,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0022,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0023,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0024,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0028,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0029,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002A,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002B,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002C,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002D,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002E,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002F,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0030,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0031,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0032,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0033,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0034,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0035,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0036,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0037,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0038,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0039,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x003A,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x003B,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x003C,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x003D,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x003E,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x003F,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0040,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0041,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0042,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0043,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0044,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0045,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0046,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0047,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0048,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0028, 0x0080)
    ChrClearFlags(0x0029, 0x0080)
    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x002B, 0x0080)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrClearFlags(0x002E, 0x0080)
    ChrClearFlags(0x002F, 0x0080)
    ChrClearFlags(0x0030, 0x0080)
    ChrClearFlags(0x0031, 0x0080)
    ChrClearFlags(0x0032, 0x0080)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0035, 0x0080)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0037, 0x0080)
    ChrClearFlags(0x0038, 0x0080)
    ChrClearFlags(0x0039, 0x0080)
    ChrClearFlags(0x003A, 0x0080)
    ChrClearFlags(0x003B, 0x0080)
    ChrClearFlags(0x003C, 0x0080)
    ChrClearFlags(0x003D, 0x0080)
    ChrClearFlags(0x003E, 0x0080)
    ChrClearFlags(0x003F, 0x0080)
    ChrClearFlags(0x0040, 0x0080)
    ChrClearFlags(0x0041, 0x0080)
    ChrClearFlags(0x0042, 0x0080)
    ChrClearFlags(0x0043, 0x0080)
    ChrClearFlags(0x0044, 0x0080)
    ChrClearFlags(0x0045, 0x0080)
    ChrClearFlags(0x0046, 0x0080)
    ChrClearFlags(0x0047, 0x0080)
    ChrClearFlags(0x0048, 0x0080)
    ChrSetChipByIndex(0x0011, 8)
    ChrSetChipByIndex(0x0012, 8)
    ChrSetChipByIndex(0x0013, 8)
    ChrSetChipByIndex(0x0014, 8)
    ChrSetChipByIndex(0x0015, 8)
    ChrSetChipByIndex(0x0016, 8)
    ChrSetChipByIndex(0x0017, 8)
    ChrSetChipByIndex(0x0018, 8)
    ChrSetChipByIndex(0x0019, 8)
    ChrSetChipByIndex(0x001A, 8)
    ChrSetChipByIndex(0x001B, 8)
    ChrSetChipByIndex(0x001C, 8)
    ChrSetChipByIndex(0x001D, 8)
    ChrSetChipByIndex(0x001E, 8)
    ChrSetChipByIndex(0x001F, 8)
    ChrSetChipByIndex(0x0020, 8)
    ChrSetChipByIndex(0x0021, 8)
    ChrSetChipByIndex(0x0022, 8)
    ChrSetChipByIndex(0x0023, 8)
    ChrSetChipByIndex(0x0024, 8)
    ChrSetChipByIndex(0x0025, 8)
    ChrSetChipByIndex(0x0026, 8)
    ChrSetChipByIndex(0x0027, 8)
    ChrSetChipByIndex(0x0028, 8)
    ChrSetChipByIndex(0x0029, 8)
    ChrSetChipByIndex(0x002A, 8)
    ChrSetChipByIndex(0x002B, 8)
    ChrSetChipByIndex(0x002C, 8)
    ChrSetChipByIndex(0x002D, 8)
    ChrSetChipByIndex(0x002E, 8)
    ChrSetChipByIndex(0x002F, 8)
    ChrSetChipByIndex(0x0030, 8)
    ChrSetChipByIndex(0x0031, 8)
    ChrSetChipByIndex(0x0032, 8)
    ChrSetChipByIndex(0x0033, 8)
    ChrSetChipByIndex(0x0034, 8)
    ChrSetChipByIndex(0x0035, 8)
    ChrSetChipByIndex(0x0036, 8)
    ChrSetChipByIndex(0x0037, 8)
    ChrSetChipByIndex(0x0038, 8)
    ChrSetChipByIndex(0x0039, 8)
    ChrSetChipByIndex(0x003A, 8)
    ChrSetChipByIndex(0x003B, 8)
    ChrSetChipByIndex(0x003C, 8)
    ChrSetChipByIndex(0x003D, 8)
    ChrSetChipByIndex(0x003E, 8)
    ChrSetChipByIndex(0x003F, 8)
    ChrSetChipByIndex(0x0040, 8)
    ChrSetChipByIndex(0x0041, 8)
    ChrSetChipByIndex(0x0042, 8)
    ChrSetChipByIndex(0x0043, 8)
    ChrSetChipByIndex(0x0044, 8)
    ChrSetChipByIndex(0x0045, 8)
    ChrSetChipByIndex(0x0046, 8)
    ChrSetChipByIndex(0x0047, 8)
    ChrSetChipByIndex(0x0048, 8)
    Fade(1000)
    CameraMove(-11480, 0, 27470, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_14B6')
    def lambda_14B6():
        OP_6C(0, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_14B6)

    @scena.Lambda('lambda_14C6')
    def lambda_14C6():
        CameraMove(14990, 0, 20730, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14C6)

    @scena.Lambda('lambda_14DE')
    def lambda_14DE():
        OP_67(0, 8220, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_14DE)

    @scena.Lambda('lambda_14F6')
    def lambda_14F6():
        CameraSetDistance(2300, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_14F6)

    @scena.Lambda('lambda_1506')
    def lambda_1506():
        OP_6E(405, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1506)

    Sleep(5000)

    ChrTalk(
        0x0008,
        (
            '#0620091163V#700F要塞内出现了入侵者！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091164V大家立刻带战斗犬进行搜索！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091165V#703F第１、第２、第３、第４小队\n',
            '封锁飞艇停机坪以及码头！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091166V第５、第６、第７小队\n',
            '分别搜索兵营、监视塔、研究所！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091167V第８小队和我前往司令部！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620091168V#704F#3S完毕！立刻行动！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(40, 60, -1, -1)
    TalkSetChrName('士兵们')

    Talk(
        (
            '#2440091169V',
            (TxtCtl.SetColor, 0x0),
            '#5S是，长官！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)

    @scena.Lambda('lambda_1687')
    def lambda_1687():
        CameraMove(14990, 0, 20730, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1687)

    @scena.Lambda('lambda_169F')
    def lambda_169F():
        OP_67(0, 9500, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_169F)

    @scena.Lambda('lambda_16B7')
    def lambda_16B7():
        CameraSetDistance(3890, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_16B7)

    @scena.Lambda('lambda_16C7')
    def lambda_16C7():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16C7)

    @scena.Lambda('lambda_16D7')
    def lambda_16D7():
        OP_6E(262, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_16D7)

    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0018, 0x0040)
    ChrSetFlags(0x0020, 0x0040)
    ChrSetFlags(0x0028, 0x0040)
    ChrSetFlags(0x0030, 0x0040)
    ChrSetFlags(0x0038, 0x0040)
    ChrSetFlags(0x0040, 0x0040)
    ChrSetFlags(0x0048, 0x0040)
    CreateThread(0x0010, 0x01, 0x00, func_0E_2184)
    CreateThread(0x0018, 0x01, 0x00, func_0E_2184)
    CreateThread(0x0020, 0x01, 0x00, func_0E_2184)
    CreateThread(0x0028, 0x01, 0x00, func_0E_2184)
    CreateThread(0x0030, 0x01, 0x00, func_0E_2184)
    CreateThread(0x0038, 0x01, 0x00, func_0E_2184)
    CreateThread(0x0040, 0x01, 0x00, func_0E_2184)
    CreateThread(0x0048, 0x01, 0x00, func_0E_2184)
    Sleep(800)

    CreateThread(0x000F, 0x01, 0x00, func_0D_213B)
    CreateThread(0x0017, 0x01, 0x00, func_0D_213B)
    CreateThread(0x001F, 0x01, 0x00, func_0D_213B)
    CreateThread(0x0027, 0x01, 0x00, func_0D_213B)
    CreateThread(0x002F, 0x01, 0x00, func_0D_213B)
    CreateThread(0x0037, 0x01, 0x00, func_0D_213B)
    CreateThread(0x003F, 0x01, 0x00, func_0D_213B)
    CreateThread(0x0047, 0x01, 0x00, func_0D_213B)
    Sleep(100)

    @scena.Lambda('lambda_178E')
    def lambda_178E():
        ChrWalkTo(0x00FE, 18230, 0, 27420, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_178E)

    Sleep(700)

    CreateThread(0x000E, 0x01, 0x00, func_0C_20F2)
    CreateThread(0x0016, 0x01, 0x00, func_0C_20F2)
    CreateThread(0x001E, 0x01, 0x00, func_0C_20F2)
    CreateThread(0x0026, 0x01, 0x00, func_0C_20F2)
    CreateThread(0x002E, 0x01, 0x00, func_0C_20F2)
    CreateThread(0x0036, 0x01, 0x00, func_0C_20F2)
    CreateThread(0x003E, 0x01, 0x00, func_0C_20F2)
    CreateThread(0x0046, 0x01, 0x00, func_0C_20F2)
    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_17EB')
    def lambda_17EB():
        ChrWalkTo(0x00FE, -1040, 0, 32450, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_17EB)

    CreateThread(0x000D, 0x01, 0x00, func_0B_20BD)
    CreateThread(0x0015, 0x01, 0x00, func_0B_20BD)
    CreateThread(0x001D, 0x01, 0x00, func_0B_20BD)
    CreateThread(0x0025, 0x01, 0x00, func_0B_20BD)
    CreateThread(0x002D, 0x01, 0x00, func_0B_20BD)
    CreateThread(0x0035, 0x01, 0x00, func_0B_20BD)
    CreateThread(0x003D, 0x01, 0x00, func_0B_20BD)
    CreateThread(0x0045, 0x01, 0x00, func_0B_20BD)
    Sleep(1000)

    CreateThread(0x000C, 0x01, 0x00, func_0A_207B)
    CreateThread(0x0014, 0x01, 0x00, func_0A_207B)
    CreateThread(0x001C, 0x01, 0x00, func_0A_207B)
    CreateThread(0x0024, 0x01, 0x00, func_0A_207B)
    CreateThread(0x002C, 0x01, 0x00, func_0A_207B)
    CreateThread(0x0034, 0x01, 0x00, func_0A_207B)
    CreateThread(0x003C, 0x01, 0x00, func_0A_207B)
    CreateThread(0x0044, 0x01, 0x00, func_0A_207B)
    CreateThread(0x000B, 0x01, 0x00, func_09_2039)
    CreateThread(0x0013, 0x01, 0x00, func_09_2039)
    CreateThread(0x001B, 0x01, 0x00, func_09_2039)
    CreateThread(0x0023, 0x01, 0x00, func_09_2039)
    CreateThread(0x002B, 0x01, 0x00, func_09_2039)
    CreateThread(0x0033, 0x01, 0x00, func_09_2039)
    CreateThread(0x003B, 0x01, 0x00, func_09_2039)
    CreateThread(0x0043, 0x01, 0x00, func_09_2039)
    CreateThread(0x0042, 0x01, 0x00, func_08_1FE3)
    CreateThread(0x0041, 0x01, 0x00, func_07_1F8D)
    Sleep(530)

    CreateThread(0x0039, 0x01, 0x00, func_07_1F8D)
    CreateThread(0x003A, 0x01, 0x00, func_08_1FE3)
    Sleep(530)

    CreateThread(0x0032, 0x01, 0x00, func_08_1FE3)
    CreateThread(0x0031, 0x01, 0x00, func_07_1F8D)
    Sleep(530)

    CreateThread(0x002A, 0x01, 0x00, func_08_1FE3)
    CreateThread(0x0029, 0x01, 0x00, func_07_1F8D)
    Sleep(530)

    CreateThread(0x0022, 0x01, 0x00, func_08_1FE3)
    CreateThread(0x0021, 0x01, 0x00, func_07_1F8D)
    Sleep(530)

    CreateThread(0x001A, 0x01, 0x00, func_08_1FE3)
    CreateThread(0x0019, 0x01, 0x00, func_07_1F8D)
    Sleep(530)

    CreateThread(0x0012, 0x01, 0x00, func_08_1FE3)
    CreateThread(0x0011, 0x01, 0x00, func_07_1F8D)
    Sleep(530)

    CreateThread(0x000A, 0x01, 0x00, func_08_1FE3)
    CreateThread(0x0009, 0x01, 0x00, func_07_1F8D)
    ChrTurnDirection(0x0101, 0x0008, 0)
    ChrTurnDirection(0x0102, 0x0008, 0)
    ChrTurnDirection(0x0106, 0x0008, 0)
    ChrTurnDirection(0x0107, 0x0008, 0)
    ChrTurnDirection(0x010B, 0x0008, 0)
    Sleep(4000)

    Fade(1000)
    CameraMove(-33270, 0, 63630, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0030, 0x0080)
    ChrSetFlags(0x0038, 0x0080)
    ChrSetFlags(0x0040, 0x0080)
    ChrSetFlags(0x0048, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0029, 0x0080)
    ChrSetFlags(0x002A, 0x0080)
    ChrSetFlags(0x002B, 0x0080)
    ChrSetFlags(0x002C, 0x0080)
    ChrSetFlags(0x002D, 0x0080)
    ChrSetFlags(0x002E, 0x0080)
    ChrSetFlags(0x002F, 0x0080)
    ChrSetFlags(0x0031, 0x0080)
    ChrSetFlags(0x0032, 0x0080)
    ChrSetFlags(0x0033, 0x0080)
    ChrSetFlags(0x0034, 0x0080)
    ChrSetFlags(0x0035, 0x0080)
    ChrSetFlags(0x0036, 0x0080)
    ChrSetFlags(0x0037, 0x0080)
    ChrSetFlags(0x0039, 0x0080)
    ChrSetFlags(0x003A, 0x0080)
    ChrSetFlags(0x003B, 0x0080)
    ChrSetFlags(0x003C, 0x0080)
    ChrSetFlags(0x003D, 0x0080)
    ChrSetFlags(0x003E, 0x0080)
    ChrSetFlags(0x003F, 0x0080)
    ChrSetFlags(0x0041, 0x0080)
    ChrSetFlags(0x0042, 0x0080)
    ChrSetFlags(0x0043, 0x0080)
    ChrSetFlags(0x0044, 0x0080)
    ChrSetFlags(0x0045, 0x0080)
    ChrSetFlags(0x0046, 0x0080)
    ChrSetFlags(0x0047, 0x0080)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001A, 0xFF)
    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    ChrSetPos(0x0013, 22160, 0, 11940, 180)
    ChrSetPos(0x0014, 7890, 0, 11990, 180)
    ChrSetPos(0x0015, -8220, 0, 11930, 270)
    ChrSetPos(0x0016, -25800, 0, 11830, 100)
    ChrSetPos(0x0017, -37890, 0, 11800, 272)
    ChrSetPos(0x0018, -38090, 0, 29890, 13)
    ChrSetPos(0x0019, -25930, 0, 29970, 69)
    ChrSetPos(0x001A, -8039, 0, 29860, 90)
    ChrSetPos(0x001B, 7940, 0, 29730, 71)
    ChrSetPos(0x001C, 21810, 0, 29930, 68)
    ChrSetPos(0x001D, -37900, 0, 45970, 195)
    ChrSetPos(0x001E, -26080, 0, 45970, 87)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    CreateThread(0x001D, 0x00, 0x00, func_02_D56)
    CreateThread(0x001E, 0x00, 0x00, func_02_D56)
    CreateThread(0x0016, 0x00, 0x00, func_03_D7A)
    CreateThread(0x0017, 0x00, 0x00, func_03_D7A)
    CreateThread(0x0018, 0x00, 0x00, func_03_D7A)
    CreateThread(0x0019, 0x00, 0x00, func_03_D7A)
    CreateThread(0x0014, 0x00, 0x00, func_04_D9E)
    CreateThread(0x0015, 0x00, 0x00, func_04_D9E)
    CreateThread(0x001A, 0x00, 0x00, func_04_D9E)
    CreateThread(0x001B, 0x00, 0x00, func_04_D9E)
    CreateThread(0x001C, 0x00, 0x00, func_05_DC2)
    CreateThread(0x0013, 0x00, 0x00, func_05_DC2)
    CreateThread(0x0013, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0014, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0015, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0016, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0017, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0018, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x0019, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x001A, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x001B, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x001C, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x001D, 0x01, 0x00, func_0F_21EE)
    CreateThread(0x001E, 0x01, 0x00, func_0F_21EE)
    ChrSetChipByIndex(0x0011, 1)
    ChrSetChipByIndex(0x0012, 1)
    ChrSetChipByIndex(0x0013, 1)
    ChrSetChipByIndex(0x0014, 1)
    ChrSetChipByIndex(0x0015, 1)
    ChrSetChipByIndex(0x0016, 1)
    ChrSetChipByIndex(0x0017, 1)
    ChrSetChipByIndex(0x0018, 1)
    ChrSetChipByIndex(0x0019, 1)
    ChrSetChipByIndex(0x001A, 1)
    ChrSetChipByIndex(0x001B, 1)
    ChrSetChipByIndex(0x001C, 1)
    ChrSetChipByIndex(0x001D, 1)
    ChrSetChipByIndex(0x001E, 1)
    ChrSetChipByIndex(0x001F, 1)
    ChrSetChipByIndex(0x0020, 1)
    ChrSetChipByIndex(0x0021, 1)
    ChrSetChipByIndex(0x0022, 1)
    ChrSetChipByIndex(0x0023, 1)
    ChrSetChipByIndex(0x0024, 1)
    ChrSetChipByIndex(0x0025, 1)
    ChrSetChipByIndex(0x0026, 1)
    ChrSetChipByIndex(0x0027, 1)
    ChrSetChipByIndex(0x0028, 1)
    ChrSetChipByIndex(0x0029, 1)
    ChrSetChipByIndex(0x002A, 1)
    ChrSetChipByIndex(0x002B, 1)
    ChrSetChipByIndex(0x002C, 1)
    ChrSetChipByIndex(0x002D, 1)
    ChrSetChipByIndex(0x002E, 1)
    ChrSetChipByIndex(0x002F, 1)
    ChrSetChipByIndex(0x0030, 1)
    ChrSetChipByIndex(0x0031, 1)
    ChrSetChipByIndex(0x0032, 1)
    ChrSetChipByIndex(0x0033, 1)
    ChrSetChipByIndex(0x0034, 1)
    ChrSetChipByIndex(0x0035, 1)
    ChrSetChipByIndex(0x0036, 1)
    ChrSetChipByIndex(0x0037, 1)
    ChrSetChipByIndex(0x0038, 1)
    ChrSetChipByIndex(0x0039, 1)
    ChrSetChipByIndex(0x003A, 1)
    ChrSetChipByIndex(0x003B, 1)
    ChrSetChipByIndex(0x003C, 1)
    ChrSetChipByIndex(0x003D, 1)
    ChrSetChipByIndex(0x003E, 1)
    ChrSetChipByIndex(0x003F, 1)
    ChrSetChipByIndex(0x0040, 1)
    ChrSetChipByIndex(0x0041, 1)
    ChrSetChipByIndex(0x0042, 1)
    ChrSetChipByIndex(0x0043, 1)
    ChrSetChipByIndex(0x0044, 1)
    ChrSetChipByIndex(0x0045, 1)
    ChrSetChipByIndex(0x0046, 1)
    ChrSetChipByIndex(0x0047, 1)
    ChrSetChipByIndex(0x0048, 1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010091170V#005F不好……\n',
            '要塞的士兵都出动了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091171V#012F停机坪和码头好像都被封锁了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091172V那个少校的判断很敏锐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091173V#104F呼……\n',
            '不愧是守卫根据地的守备队长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091174V#065F怎、怎么办……\n',
            '要从哪儿逃出去才好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091175V#057F总之从码头逃走是行不通了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091176V#054F先避开士兵，\n',
            '然后再寻找逃脱路线吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, 26890, 0, 25790, 270)
    ChrSetPos(0x000A, 26950, 0, 19870, 270)
    SetScenaFlags(ScenaFlag(0x00AD, 3, 0x56B))
    OP_28(0x0044, 0x01, 0x0100)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1F8D
@scena.Code('func_07_1F8D')
def func_07_1F8D():
    ChrMoveToRelative(0x00FE, 1500, 0, -3000, 6000, 0x00)
    ChrWalkTo(0x00FE, 17910, 0, 23020, 6000, 0x00)
    ChrWalkTo(0x00FE, 26900, 0, 22130, 6000, 0x00)
    ChrWalkTo(0x00FE, 36900, 0, 22130, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0008 offset: 0x1FE3
@scena.Code('func_08_1FE3')
def func_08_1FE3():
    ChrMoveToRelative(0x00FE, 1500, 0, -3000, 6000, 0x00)
    ChrWalkTo(0x00FE, 17910, 0, 21550, 6000, 0x00)
    ChrWalkTo(0x00FE, 26900, 0, 20810, 6000, 0x00)
    ChrWalkTo(0x00FE, 36900, 0, 20810, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0009 offset: 0x2039
@scena.Code('func_09_2039')
def func_09_2039():
    ChrWalkTo(0x00FE, 17910, 0, 23020, 6000, 0x00)
    ChrWalkTo(0x00FE, 26900, 0, 22130, 6000, 0x00)
    ChrWalkTo(0x00FE, 36900, 0, 22130, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000A offset: 0x207B
@scena.Code('func_0A_207B')
def func_0A_207B():
    ChrWalkTo(0x00FE, 17910, 0, 21550, 6000, 0x00)
    ChrWalkTo(0x00FE, 26900, 0, 20810, 6000, 0x00)
    ChrWalkTo(0x00FE, 36900, 0, 20810, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000B offset: 0x20BD
@scena.Code('func_0B_20BD')
def func_0B_20BD():
    ChrSetDirection(0x00FE, 270, 400)
    ChrWalkTo(0x00FE, 3730, 0, 19920, 6000, 0x00)
    ChrWalkTo(0x00FE, -51420, 500, 16930, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000C offset: 0x20F2
@scena.Code('func_0C_20F2')
def func_0C_20F2():
    ChrSetDirection(0x00FE, 270, 400)
    ChrWalkTo(0x00FE, 3560, 0, 18490, 6000, 0x00)
    ChrWalkTo(0x00FE, -14290, 0, 24580, 6000, 0x00)
    ChrWalkTo(0x00FE, -32780, 0, 65230, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000D offset: 0x213B
@scena.Code('func_0D_213B')
def func_0D_213B():
    ChrSetDirection(0x00FE, 270, 400)
    ChrWalkTo(0x00FE, 3790, 0, 17030, 6000, 0x00)
    ChrWalkTo(0x00FE, -14290, 0, 24580, 6000, 0x00)
    ChrWalkTo(0x00FE, -32780, 0, 65230, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000E offset: 0x2184
@scena.Code('func_0E_2184')
def func_0E_2184():
    ChrWalkTo(0x00FE, 17880, 0, 15620, 6000, 0x00)
    ChrWalkTo(0x00FE, 18530, 0, 20700, 6000, 0x00)
    ChrWalkTo(0x00FE, 18230, 0, 27420, 6000, 0x00)
    ChrWalkTo(0x00FE, -1040, 0, 32450, 6000, 0x00)
    ChrWalkTo(0x00FE, -970, 500, 36330, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000F offset: 0x21EE
@scena.Code('func_0F_21EE')
def func_0F_21EE():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_274B',
    )

    Yield()

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x151),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2221',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_233E')

    def _loc_2221(): pass

    label('loc_2221')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x125),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2247',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_233E')

    def _loc_2247(): pass

    label('loc_2247')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xF8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_226D',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_233E')

    def _loc_226D(): pass

    label('loc_226D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xCA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2294',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_233E')

    def _loc_2294(): pass

    label('loc_2294')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x9E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_22BA',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_233E')

    def _loc_22BA(): pass

    label('loc_22BA')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x70),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_22E0',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_233E')

    def _loc_22E0(): pass

    label('loc_22E0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x44),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2305',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_233E')

    def _loc_2305(): pass

    label('loc_2305')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x16),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_232A',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_233E')

    def _loc_232A(): pass

    label('loc_232A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x5DC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_233E(): pass

    label('loc_233E')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x7D0),
            Expr.Add,
            (Expr.PushReg, 0x0),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x7D0),
            Expr.Sub,
            (Expr.PushReg, 0x0),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x7D0),
            Expr.Add,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x7D0),
            Expr.Sub,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x7D0),
            Expr.Add,
            (Expr.PushReg, 0x0),
            Expr.Add,
            (Expr.GetChrWork, 0x3, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x7D0),
            Expr.Sub,
            (Expr.PushReg, 0x0),
            Expr.Add,
            (Expr.GetChrWork, 0x3, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x7D0),
            Expr.Add,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x3, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x7D0),
            Expr.Sub,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x3, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Or,
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2748',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x00FE, 0x00)
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    ChrTurnDirection(0x0002, 0x00FE, 0)
    ChrTurnDirection(0x0003, 0x00FE, 0)
    ChrTurnDirection(0x0004, 0x00FE, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0000, 400)
    OP_69(0x00FE, 1000)
    OP_23(0x00AC)
    Battle(0x0000024F, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_245F'),
        (-1, 'loc_2462'),
    )

    def _loc_245F(): pass

    label('loc_245F')

    OP_B4(0x00)

    Return()

    def _loc_2462(): pass

    label('loc_2462')

    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0106,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0107,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0106, 5)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetChipByIndex(0x0107, 6)
    CameraMove(-26010, 0, 31860, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -26500, 0, 33350, 183)
    ChrSetPos(0x0106, -27660, 0, 32600, 140)
    ChrSetPos(0x0102, -25580, 0, 33330, 188)
    ChrSetPos(0x0107, -27660, 0, 33860, 155)
    ChrSetPos(0x010B, -26280, 0, 34780, 168)

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
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
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
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 7)
    ChrSetChipByIndex(0x000A, 7)
    ChrSetChipByIndex(0x000B, 7)
    ChrSetChipByIndex(0x000C, 7)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0009, -27380, 0, 30460, 198)
    ChrSetPos(0x000A, -25280, 0, 31010, 89)
    ChrSetPos(0x000B, -26360, 0, 28750, 278)
    ChrSetPos(0x000C, -25160, 0, 29280, 2)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x000A, 0x0001)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 6, 0x54E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26BC',
    )

    ChrTalk(
        0x0101,
        (
            '#0010091177V#004F糟了……\n',
            '虽然把他们打倒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091178V#012F别的士兵好像\n',
            '已经注意到这里了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091179V#054F赶快回研究所去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_272E')

    def _loc_26BC(): pass

    label('loc_26BC')

    ChrTalk(
        0x0101,
        (
            '#0010091180V#007F糟了……\n',
            '又不得不把他们打晕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091181V#057F有别的家伙来了……\n',
            '赶快回研究所去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_272E(): pass

    label('loc_272E')

    FadeOut(500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C3107._SN', 100, 0, 0)
    IdleLoop()
    EventEnd(0x01)

    Return()

    def _loc_2748(): pass

    label('loc_2748')

    Jump('func_0F_21EE')

    def _loc_274B(): pass

    label('loc_274B')

    Return()

# id: 0x0010 offset: 0x274C
@scena.Code('func_10_274C')
def func_10_274C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 1, 0x569)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 5, 0x54D)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2759',
    )

    Return()

    def _loc_2759(): pass

    label('loc_2759')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    EventBegin(0x00)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_27D5')
    def lambda_27D5():
        ChrTurnDirection(0x00FE, 0x0000, 800)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_27D5)

    @scena.Lambda('lambda_27E3')
    def lambda_27E3():
        ChrTurnDirection(0x00FE, 0x0000, 800)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_27E3)

    CameraMove(24450, 0, 23030, 1000)

    ChrTalk(
        0x0011,
        (
            '#2510091182V你们是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_2839')
    def lambda_2839():
        ChrTurnDirection(0x00FE, 0x0011, 800)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2839)

    @scena.Lambda('lambda_2847')
    def lambda_2847():
        ChrTurnDirection(0x00FE, 0x0011, 800)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2847)

    @scena.Lambda('lambda_2855')
    def lambda_2855():
        ChrTurnDirection(0x00FE, 0x0011, 800)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2855)

    @scena.Lambda('lambda_2863')
    def lambda_2863():
        ChrTurnDirection(0x00FE, 0x0011, 800)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2863)

    @scena.Lambda('lambda_2871')
    def lambda_2871():
        ChrTurnDirection(0x00FE, 0x0011, 800)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_2871)

    ChrTalk(
        0x0012,
        (
            '找到了！入侵者在这里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28C5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010091184V#005F糟了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2946')

    def _loc_28C5(): pass

    label('loc_28C5')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28E9',
    )

    ChrTalk(
        0x0102,
        (
            '#012F不好……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2946')

    def _loc_28E9(): pass

    label('loc_28E9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_291B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070091186V#065F哇呀呀……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2946')

    def _loc_291B(): pass

    label('loc_291B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2946',
    )

    ChrTalk(
        0x0106,
        (
            '#0050091187V#057F嘁……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2946(): pass

    label('loc_2946')

    OP_23(0x00AC)
    Battle(0x0000024E, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_2962'),
        (-1, 'loc_2965'),
    )

    def _loc_2962(): pass

    label('loc_2962')

    OP_B4(0x00)

    Return()

    def _loc_2965(): pass

    label('loc_2965')

    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0106,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0107,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0106, 5)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetChipByIndex(0x0107, 6)
    CameraMove(27210, 0, 23250, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(66000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 24110, 0, 23210, 88)
    ChrSetPos(0x0106, 23600, 0, 24470, 127)
    ChrSetPos(0x0102, 23740, 0, 21940, 72)
    ChrSetPos(0x0107, 22580, 0, 23620, 91)
    ChrSetPos(0x010B, 22110, 0, 22320, 94)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)

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
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 7)
    ChrSetChipByIndex(0x000A, 7)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x000A, 0x0001)
    ChrSetPos(0x0009, 26660, 0, 24400, 270)
    ChrSetPos(0x000A, 26530, 0, 22820, 225)
    ChrSetPos(0x000C, 36620, 400, 22980, 45)
    ChrSetPos(0x000B, 36620, 400, 22980, 45)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '怎么了，刚才的声音是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '有入侵者！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091190V#580F又、又来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091191V#054F赶快回研究所去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/C3107._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x2B95
@scena.Code('func_11_2B95')
def func_11_2B95():
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)
    OP_4A(0x0018, 255)
    OP_4A(0x0019, 255)
    OP_4A(0x001A, 255)
    OP_4A(0x001B, 255)
    OP_4A(0x001C, 255)
    OP_4A(0x001D, 255)
    OP_4A(0x001E, 255)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)
    OP_4B(0x0013, 255)
    OP_4B(0x0014, 255)
    OP_4B(0x0015, 255)
    OP_4B(0x0016, 255)
    OP_4B(0x0017, 255)
    OP_4B(0x0018, 255)
    OP_4B(0x0019, 255)
    OP_4B(0x001A, 255)
    OP_4B(0x001B, 255)
    OP_4B(0x001C, 255)
    OP_4B(0x001D, 255)
    OP_4B(0x001E, 255)

    Return()

# id: 0x0012 offset: 0x2C35
@scena.Code('func_12_2C35')
def func_12_2C35():
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)
    OP_4A(0x0018, 255)
    OP_4A(0x0019, 255)
    OP_4A(0x001A, 255)
    OP_4A(0x001B, 255)
    OP_4A(0x001C, 255)
    OP_4A(0x001D, 255)
    OP_4A(0x001E, 255)
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)
    OP_4B(0x0013, 255)
    OP_4B(0x0014, 255)
    OP_4B(0x0015, 255)
    OP_4B(0x0016, 255)
    OP_4B(0x0017, 255)
    OP_4B(0x0018, 255)
    OP_4B(0x0019, 255)
    OP_4B(0x001A, 255)
    OP_4B(0x001B, 255)
    OP_4B(0x001C, 255)
    OP_4B(0x001D, 255)
    OP_4B(0x001E, 255)

    Return()

# id: 0x0013 offset: 0x2CE5
@scena.Code('func_13_2CE5')
def func_13_2CE5():
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)
    OP_4A(0x0018, 255)
    OP_4A(0x0019, 255)
    OP_4A(0x001A, 255)
    OP_4A(0x001B, 255)
    OP_4A(0x001C, 255)
    OP_4A(0x001D, 255)
    OP_4A(0x001E, 255)
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)
    OP_4B(0x0013, 255)
    OP_4B(0x0014, 255)
    OP_4B(0x0015, 255)
    OP_4B(0x0016, 255)
    OP_4B(0x0017, 255)
    OP_4B(0x0018, 255)
    OP_4B(0x0019, 255)
    OP_4B(0x001A, 255)
    OP_4B(0x001B, 255)
    OP_4B(0x001C, 255)
    OP_4B(0x001D, 255)
    OP_4B(0x001E, 255)

    Return()

# id: 0x0014 offset: 0x2D95
@scena.Code('func_14_2D95')
def func_14_2D95():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 5, 0x54D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3285',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    EventBegin(0x00)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0011, 38740, 400, 22480, 270)
    ChrSetPos(0x0012, 38480, 400, 23440, 270)

    ChrTalk(
        0x0011,
        (
            '#2510091182V你们是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_2E12')
    def lambda_2E12():
        ChrTurnDirection(0x00FE, 0x0011, 800)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2E12)

    @scena.Lambda('lambda_2E20')
    def lambda_2E20():
        ChrTurnDirection(0x00FE, 0x0011, 800)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2E20)

    @scena.Lambda('lambda_2E2E')
    def lambda_2E2E():
        ChrTurnDirection(0x00FE, 0x0011, 800)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2E2E)

    @scena.Lambda('lambda_2E3C')
    def lambda_2E3C():
        ChrTurnDirection(0x00FE, 0x0011, 800)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2E3C)

    @scena.Lambda('lambda_2E4A')
    def lambda_2E4A():
        ChrTurnDirection(0x00FE, 0x0011, 800)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_2E4A)

    Sleep(500)

    Fade(2000)

    @scena.Lambda('lambda_2E62')
    def lambda_2E62():
        CameraMove(36080, 400, 23100, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2E62)

    @scena.Lambda('lambda_2E7A')
    def lambda_2E7A():
        OP_6C(80000, 2000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2E7A)

    WaitForThreadExit(0x0012, 0x0001)
    OP_0D()

    ChrTalk(
        0x0012,
        (
            '#4180091183V#6P找到了！入侵者在这里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EE5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010091184V#005F糟了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F72')

    def _loc_2EE5(): pass

    label('loc_2EE5')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F15',
    )

    ChrTalk(
        0x0102,
        (
            '#0020091185V#016F不好……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F72')

    def _loc_2F15(): pass

    label('loc_2F15')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F47',
    )

    ChrTalk(
        0x0107,
        (
            '#0070091186V#065F哇呀呀……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F72')

    def _loc_2F47(): pass

    label('loc_2F47')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F72',
    )

    ChrTalk(
        0x0106,
        (
            '#0050091187V#057F嘁……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F72(): pass

    label('loc_2F72')

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0106,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0107,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0106, 5)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetChipByIndex(0x0107, 6)

    @scena.Lambda('lambda_2FB8')
    def lambda_2FB8():
        CameraMove(29430, 0, 23120, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2FB8)

    ChrSetChipByIndex(0x0011, 9)

    @scena.Lambda('lambda_2FD5')
    def lambda_2FD5():
        ChrWalkTo(0x00FE, 28960, 400, 22470, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2FD5)

    Sleep(200)

    ChrSetChipByIndex(0x0012, 9)

    @scena.Lambda('lambda_2FFA')
    def lambda_2FFA():
        ChrWalkTo(0x00FE, 29030, 400, 23540, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2FFA)

    Sleep(1000)

    OP_23(0x00AC)
    Battle(0x0000024E, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_3030'),
        (-1, 'loc_3033'),
    )

    def _loc_3030(): pass

    label('loc_3030')

    OP_B4(0x00)

    Return()

    def _loc_3033(): pass

    label('loc_3033')

    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0106,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0107,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0106, 5)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetChipByIndex(0x0107, 6)
    CameraMove(26830, 0, 24070, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(66000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 24110, 0, 23210, 88)
    ChrSetPos(0x0106, 23600, 0, 24470, 127)
    ChrSetPos(0x0102, 23740, 0, 21940, 72)
    ChrSetPos(0x0107, 22580, 0, 23620, 91)
    ChrSetPos(0x010B, 22110, 0, 22320, 94)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)

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
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 7)
    ChrSetChipByIndex(0x000A, 7)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x000A, 0x0001)
    ChrSetPos(0x0009, 26660, 0, 24400, 270)
    ChrSetPos(0x000A, 26530, 0, 22820, 225)
    ChrSetPos(0x000C, 36620, 400, 22980, 45)
    ChrSetPos(0x000B, 36620, 400, 22980, 45)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#2500091188V#3P怎么了，刚才的声音是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2440091189V#3P是入侵者吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091190V#580F又、又来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091191V#054F赶快回研究所去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/C3107._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_33ED')

    def _loc_3285(): pass

    label('loc_3285')

    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)
    OP_4A(0x0018, 255)
    OP_4A(0x0019, 255)
    OP_4A(0x001A, 255)
    OP_4A(0x001B, 255)
    OP_4A(0x001C, 255)
    OP_4A(0x001D, 255)
    OP_4A(0x001E, 255)
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_332B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050091192V#057F飞艇坪已经不能去了……\n',
            '会被抓住的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091193V总之先找一找\n',
            '别的逃跑路线吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33A2')

    def _loc_332B(): pass

    label('loc_332B')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050091194V#057F喂，不能去飞艇坪。\n',
            '守备队肯定已经在那边布下重兵了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091195V赶快找找别的逃跑路线吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33A2(): pass

    label('loc_33A2')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    OP_4B(0x0013, 255)
    OP_4B(0x0014, 255)
    OP_4B(0x0015, 255)
    OP_4B(0x0016, 255)
    OP_4B(0x0017, 255)
    OP_4B(0x0018, 255)
    OP_4B(0x0019, 255)
    OP_4B(0x001A, 255)
    OP_4B(0x001B, 255)
    OP_4B(0x001C, 255)
    OP_4B(0x001D, 255)
    OP_4B(0x001E, 255)
    def _loc_33ED(): pass

    label('loc_33ED')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

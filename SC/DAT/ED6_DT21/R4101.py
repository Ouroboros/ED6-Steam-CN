import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R4101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R4101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'R4101.x'
    header.mapIndex       = 1
    header.bgm            = 29
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
        ('ED6_DT09/CH10780._CH', 'ED6_DT09/CH10780P._CP'),
        ('ED6_DT09/CH10781._CH', 'ED6_DT09/CH10781P._CP'),
        ('ED6_DT09/CH10790._CH', 'ED6_DT09/CH10790P._CP'),
        ('ED6_DT09/CH10791._CH', 'ED6_DT09/CH10791P._CP'),
        ('ED6_DT09/CH10050._CH', 'ED6_DT09/CH10050P._CP'),
        ('ED6_DT09/CH10051._CH', 'ED6_DT09/CH10051P._CP'),
        ('ED6_DT09/CH10800._CH', 'ED6_DT09/CH10800P._CP'),
        ('ED6_DT09/CH10801._CH', 'ED6_DT09/CH10801P._CP'),
        ('ED6_DT09/CH10810._CH', 'ED6_DT09/CH10810P._CP'),
        ('ED6_DT09/CH10811._CH', 'ED6_DT09/CH10811P._CP'),
        ('ED6_DT09/CH10820._CH', 'ED6_DT09/CH10820P._CP'),
        ('ED6_DT09/CH10821._CH', 'ED6_DT09/CH10821P._CP'),
        ('ED6_DT09/CH11220._CH', 'ED6_DT09/CH11220P._CP'),
        ('ED6_DT09/CH11221._CH', 'ED6_DT09/CH11221P._CP'),
        ('ED6_DT09/CH11230._CH', 'ED6_DT09/CH11230P._CP'),
        ('ED6_DT09/CH11231._CH', 'ED6_DT09/CH11231P._CP'),
        ('ED6_DT27/CH03590._CH', 'ED6_DT27/CH03590P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT06/CH20043._CH', 'ED6_DT06/CH20043P._CP'),
        ('ED6_DT26/CH20335._CH', 'ED6_DT26/CH20335P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT26/CH20419._CH', 'ED6_DT26/CH20419P._CP'),
    ]

# id: 0x10001 offset: 0x162
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '希德中校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '贝尔克副队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '王国军士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亡命守护者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亡命守护者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亡命守护者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亡命守护者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '装甲猎豹',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '装甲猎豹',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '装甲猎豹',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '装甲猎豹',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '装甲猎豹',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士官',
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
            name                = '王国军士官',
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
            name                = '王国军士官',
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
            name                = '怪盗布卢布兰',
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
            name                = '瘦狼瓦鲁特',
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
            name                = '歼灭天使玲',
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
            name                = '幻惑之铃露茜奥拉',
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
            name                = '结社艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '结社艇影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '结社艇影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '结社艇影',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '圣海姆门方向',
            x                   = -5160,
            z                   = -50,
            y                   = -7520,
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
            name                = '王都格兰赛尔方向',
            x                   = -39160,
            z                   = 0,
            y                   = 152720,
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
            name                = '格鲁纳门方向',
            x                   = 61180,
            z                   = 0,
            y                   = 83020,
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

# id: 0x10002 offset: 0xA42
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '沼泽剑齿吸血魔',
            x           = -6830,
            z           = 90,
            y           = 29510,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0297,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '丘陵毒蜂',
            x           = 16290,
            z           = 70,
            y           = 76970,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0295,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '迅猛小鹫',
            x           = 31220,
            z           = 40,
            y           = 83060,
            word_0C     = 0x0000,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x029C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '好战蝙蝠',
            x           = -33000,
            z           = 20,
            y           = 72240,
            word_0C     = 0x0000,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x029A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '沼泽剑齿吸血魔',
            x           = -17830,
            z           = 10,
            y           = 103860,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0297,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '迅猛小鹫',
            x           = -61630,
            z           = 70,
            y           = 108700,
            word_0C     = 0x0000,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x029C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0xAEA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -44700,
            y           = -2000,
            z           = 142100,
            range       = -33800,
            dword_10    = 0x000007D0,
            dword_14    = 0x000231B8,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = -48550,
            y           = -2000,
            z           = 98420,
            range       = -29640,
            dword_10    = 0x000007D0,
            dword_14    = 0x0001762E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000073,
        ),
        ScenaEventData(
            x           = -44700,
            y           = -2000,
            z           = 142700,
            range       = -33800,
            dword_10    = 0x000007D0,
            dword_14    = 0x00023A50,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0xB4A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -13540,
            triggerZ            = 0,
            triggerY            = 63650,
            triggerRange        = 1500,
            actorX              = -13540,
            actorZ              = 1700,
            actorY              = 63650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0075,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 130,
            triggerZ            = 0,
            triggerY            = 56450,
            triggerRange        = 1500,
            actorX              = 130,
            actorZ              = 1700,
            actorY              = 56450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0076,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1460,
            triggerZ            = 0,
            triggerY            = 53030,
            triggerRange        = 1500,
            actorX              = -1460,
            actorZ              = 1700,
            actorY              = 53030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0077,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xBB6
@scena.Code('Init')
def Init():
    Call(0, 0x0005)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_BD9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x5B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_06_1150)

    Jump('loc_C15')

    def _loc_BD9(): pass

    label('loc_BD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_BFA',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x74),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    OP_B5(0x00)
    MapSetFlags(0x10000000)
    Event(0, func_08_1335)

    Jump('loc_C15')

    def _loc_BFA(): pass

    label('loc_BFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 1, 0x2039)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C15',
    )

    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_11_1AD4)

    def _loc_C15(): pass

    label('loc_C15')

    Return()

# id: 0x0001 offset: 0xC16
@scena.Code('func_01_C16')
def func_01_C16():
    OP_16(0x02, 4000, -135000, -60000, 2293820)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C52',
    )

    ChrSetFlags(0x004F, 0x0080)
    ChrSetFlags(0x0050, 0x0080)
    ChrSetFlags(0x0051, 0x0080)
    ChrSetFlags(0x0052, 0x0080)
    ChrSetFlags(0x0053, 0x0080)
    ChrSetFlags(0x0054, 0x0080)

    def _loc_C52(): pass

    label('loc_C52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            Expr.Return,
        ),
        'loc_C67',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C67(): pass

    label('loc_C67')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x2710),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C7C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C7C(): pass

    label('loc_C7C')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x2711),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C91',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C91(): pass

    label('loc_C91')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x2712),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CA6',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CA6(): pass

    label('loc_CA6')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x2713),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CBB',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CBB(): pass

    label('loc_CBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CD3',
    )

    OP_B1('R4101_y')

    Jump('loc_CDC')

    def _loc_CD3(): pass

    label('loc_CD3')

    OP_B1('R4101_n')

    def _loc_CDC(): pass

    label('loc_CDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Return,
        ),
        'loc_CE7',
    )

    Call(0, 0x0005)

    def _loc_CE7(): pass

    label('loc_CE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 7, 0x1637)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CF8',
    )

    OP_1B(0x00, 0x00, 0x0074)

    def _loc_CF8(): pass

    label('loc_CF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 1, 0x2039)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D38',
    )

    OP_B5(0x00)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_D1A'),
        (0x00000065, 'loc_D29'),
        (-1, 'loc_D38'),
    )

    def _loc_D1A(): pass

    label('loc_D1A')

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    MapSetFlags(0x10000000)
    Event(0, func_14_32C9)

    Jump('loc_D38')

    def _loc_D29(): pass

    label('loc_D29')

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    MapSetFlags(0x10000000)
    Event(0, func_15_3376)

    Jump('loc_D38')

    def _loc_D38(): pass

    label('loc_D38')

    Return()

# id: 0x0002 offset: 0xD39
@scena.Code('func_02_D39')
def func_02_D39():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D4E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_D39')

    def _loc_D4E(): pass

    label('loc_D4E')

    Return()

# id: 0x0003 offset: 0xD4F
@scena.Code('func_03_D4F')
def func_03_D4F():
    EventBegin(0x01)
    ChrSetSubChip(0x0001, 3)
    ChrSetSubChip(0x0002, 3)
    ChrSetSubChip(0x0003, 3)
    FadeOut(500, 0, -1)
    ChrSetDirection(0x0000, 0, 0)

    @scena.Lambda('lambda_0D77')
    def lambda_0D77():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 2000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0D77)

    MapClearFlags(0x02000000)
    OP_0D()
    NewScene('ED6_DT21/T4100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0xD9C
@scena.Code('func_04_D9C')
def func_04_D9C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DA5',
    )

    Return()

    def _loc_DA5(): pass

    label('loc_DA5')

    MapClearFlags(0x02000000)

    Return()

# id: 0x0005 offset: 0xDAB
@scena.Code('func_05_DAB')
def func_05_DAB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 1, 0x2039)),
            Expr.Return,
        ),
        'loc_114F',
    )

    ChrClearFlags(0x0041, 0x0080)
    ChrSetFlags(0x0041, 0x0020)
    ChrClearFlags(0x0041, 0x0001)
    ChrSetChipByIndex(0x0041, 20)
    ChrSetPos(0x0041, -38950, 0, 125450, 180)
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
    ChrSetFlags(0x000A, 0x0020)
    ChrSetFlags(0x000B, 0x0020)
    ChrSetFlags(0x000C, 0x0020)
    ChrSetFlags(0x000D, 0x0020)
    ChrSetFlags(0x000E, 0x0020)
    ChrSetFlags(0x000F, 0x0020)
    ChrSetFlags(0x0010, 0x0020)
    ChrSetFlags(0x0011, 0x0020)
    ChrSetFlags(0x0012, 0x0020)
    ChrSetFlags(0x0013, 0x0020)
    ChrSetFlags(0x0014, 0x0020)
    ChrSetFlags(0x0015, 0x0020)
    ChrSetFlags(0x0016, 0x0020)
    ChrSetFlags(0x0017, 0x0020)
    ChrSetFlags(0x0018, 0x0020)
    ChrSetFlags(0x0019, 0x0020)
    ChrSetFlags(0x001A, 0x0020)
    ChrSetFlags(0x001B, 0x0020)
    ChrSetFlags(0x001C, 0x0020)
    ChrSetFlags(0x001D, 0x0020)
    ChrSetFlags(0x001E, 0x0020)
    ChrSetFlags(0x001F, 0x0020)
    ChrSetFlags(0x0020, 0x0020)
    ChrSetFlags(0x0021, 0x0020)
    ChrClearFlags(0x000A, 0x0001)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    ChrClearFlags(0x000D, 0x0001)
    ChrClearFlags(0x000E, 0x0001)
    ChrClearFlags(0x000F, 0x0001)
    ChrClearFlags(0x0010, 0x0001)
    ChrClearFlags(0x0011, 0x0001)
    ChrClearFlags(0x0012, 0x0001)
    ChrClearFlags(0x0013, 0x0001)
    ChrClearFlags(0x0014, 0x0001)
    ChrClearFlags(0x0015, 0x0001)
    ChrClearFlags(0x0016, 0x0001)
    ChrClearFlags(0x0017, 0x0001)
    ChrClearFlags(0x0018, 0x0001)
    ChrClearFlags(0x0019, 0x0001)
    ChrClearFlags(0x001A, 0x0001)
    ChrClearFlags(0x001B, 0x0001)
    ChrClearFlags(0x001C, 0x0001)
    ChrClearFlags(0x001D, 0x0001)
    ChrClearFlags(0x001E, 0x0001)
    ChrClearFlags(0x001F, 0x0001)
    ChrClearFlags(0x0020, 0x0001)
    ChrClearFlags(0x0021, 0x0001)
    ChrSetChipByIndex(0x000A, 22)
    ChrSetChipByIndex(0x000B, 19)
    ChrSetChipByIndex(0x000C, 19)
    ChrSetChipByIndex(0x000D, 22)
    ChrSetChipByIndex(0x000E, 22)
    ChrSetChipByIndex(0x000F, 19)
    ChrSetChipByIndex(0x0010, 19)
    ChrSetChipByIndex(0x0011, 22)
    ChrSetChipByIndex(0x0012, 19)
    ChrSetChipByIndex(0x0013, 19)
    ChrSetChipByIndex(0x0014, 22)
    ChrSetChipByIndex(0x0015, 19)
    ChrSetChipByIndex(0x0016, 22)
    ChrSetChipByIndex(0x0017, 19)
    ChrSetChipByIndex(0x0018, 22)
    ChrSetChipByIndex(0x0019, 19)
    ChrSetChipByIndex(0x001A, 19)
    ChrSetChipByIndex(0x001B, 22)
    ChrSetChipByIndex(0x001C, 19)
    ChrSetChipByIndex(0x001D, 19)
    ChrSetChipByIndex(0x001E, 19)
    ChrSetChipByIndex(0x001F, 22)
    ChrSetChipByIndex(0x0020, 22)
    ChrSetChipByIndex(0x0021, 19)
    ChrSetPos(0x000A, -32360, 0, 119050, 45)
    ChrSetPos(0x000B, -30880, 0, 120220, 315)
    ChrSetPos(0x000C, -32770, 0, 122700, 180)
    ChrSetPos(0x000D, -30610, 250, 124400, 270)
    ChrSetPos(0x000E, -30670, 250, 127190, 135)
    ChrSetPos(0x000F, -34040, 0, 126930, 45)
    ChrSetPos(0x0010, -29470, 250, 125310, 315)
    ChrSetPos(0x0011, -32520, 0, 127180, 0)
    ChrSetPos(0x0012, -44210, 0, 117600, 180)
    ChrSetPos(0x0013, -46830, 0, 119130, 0)
    ChrSetPos(0x0014, -44450, 0, 119820, 45)
    ChrSetPos(0x0015, -47450, 0, 121690, 180)
    ChrSetPos(0x0016, -43440, 0, 122980, 0)
    ChrSetPos(0x0017, -46070, 250, 125390, 135)
    ChrSetPos(0x0018, -49300, 0, 122100, 270)
    ChrSetPos(0x0019, -48780, 250, 125590, 180)
    ChrSetPos(0x001A, -33410, 0, 124960, 1350)
    ChrSetPos(0x001B, -30660, 250, 129020, 0)
    ChrSetPos(0x001C, -28390, 0, 121800, 315)
    ChrSetPos(0x001D, -33200, 0, 129930, 270)
    ChrSetPos(0x001E, -45060, 0, 122340, 135)
    ChrSetPos(0x001F, -44090, 0, 125830, 225)
    ChrSetPos(0x0020, -46660, 250, 127320, 270)
    ChrSetPos(0x0021, -54520, 0, 121790, 180)

    def _loc_114F(): pass

    label('loc_114F')

    Return()

# id: 0x0006 offset: 0x1150
@scena.Code('func_06_1150')
def func_06_1150():
    EventBegin(0x00)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x07, 0xFF)
    ChrSetPos(0x0101, -38810, 0, 147550, 180)
    CameraMove(-38810, 0, 139930, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_11B5')
    def lambda_11B5():
        ChrWalkTo(0x00FE, -38810, 0, 139930, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11B5)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010260962V#1003F哈哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260963V格鲁纳门的\n',
            '长城『亚宁堡』上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260964V#1002F必须要赶快过去……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C6, 6, 0x1636))
    OP_28(0x008C, 0x01, 0x0200)
    OP_28(0x008C, 0x04, 0x10)
    OP_28(0x008D, 0x04, 0x02)
    OP_28(0x008D, 0x04, 0x08)
    OP_28(0x008D, 0x01, 0x0001)
    OP_28(0x008D, 0x01, 0x0002)
    OP_1B(0x00, 0x00, 0x0074)
    OP_20(0x000003E8)
    OP_21()
    PlayBGM(29)
    Sleep(500)

    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x128D
@scena.Code('func_07_128D')
def func_07_128D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_129A',
    )

    Return()

    def _loc_129A(): pass

    label('loc_129A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1334',
    )

    EventBegin(0x02)

    ChrTalk(
        0x0101,
        (
            '#0010260965V#1003F（离傍晚\n',
            '　没多少时间了……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260966V#1002F（得快点……得快点\n',
            '　赶到格鲁纳门才行！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_1334(): pass

    label('loc_1334')

    Return()

# id: 0x0008 offset: 0x1335
@scena.Code('func_08_1335')
def func_08_1335():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    ChrSetPos(0x0044, -35200, 0, 128000, 0)
    ChrSetPos(0x0045, -35200, 0, 135000, 0)
    ChrSetPos(0x0046, -41700, 0, 128000, 0)
    ChrSetPos(0x0047, -41700, 0, 135000, 0)
    OP_A1(0x0044, 0x0002)
    OP_A1(0x0045, 0x0003)
    OP_A1(0x0046, 0x0004)
    OP_A1(0x0047, 0x0005)
    CameraMove(-39360, 250, 110440, 0)
    OP_67(0, 12030, -10000, 0)
    CameraSetDistance(4620, 0)
    OP_6C(33000, 0)
    OP_6E(381, 0)
    ChrSetPos(0x0008, -31690, 250, 129009, 270)
    ChrSetPos(0x0009, -30900, 250, 128050, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    CreateThread(0x0101, 0x02, 0x00, func_09_15DD)

    @scena.Lambda('lambda_1437')
    def lambda_1437():
        CameraMove(-40190, 0, 126470, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1437)

    @scena.Lambda('lambda_144F')
    def lambda_144F():
        OP_6C(69000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_144F)

    OP_C8(0x0200, 0x0046, 'C_PLAC04._CH', 0x00, 0x03E8)
    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    Fade(1000)
    CameraMove(-32450, 250, 129930, 0)
    OP_67(0, 8780, -10000, 0)
    CameraSetDistance(2290, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#3170341411V呼，总算是在傍晚前\n',
            '将那些机器人解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3170341412V终于可以喘口气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0620341413V#703F#5P是啊……\n',
            '士兵们也累了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620341414V#701F接下来的警戒就交给预备队，\n',
            '今天让他们先好好休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3170341415V明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/C3100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x15DD
@scena.Code('func_09_15DD')
def func_09_15DD():
    ChrSetPos(0x000A, -37500, 0, 114000, 0)
    ChrSetPos(0x000B, -39300, 0, 114000, 0)
    ChrSetPos(0x000C, -37500, 0, 112000, 0)
    ChrSetPos(0x000D, -39300, 0, 112000, 0)
    ChrSetPos(0x000E, -37500, 0, 110000, 0)
    ChrSetPos(0x000F, -39300, 0, 110000, 0)
    ChrSetPos(0x0010, -37500, 0, 108000, 0)
    ChrSetPos(0x0011, -39300, 0, 108000, 0)
    ChrSetPos(0x0012, -37500, 0, 106000, 0)
    ChrSetPos(0x0013, -39300, 0, 106000, 0)
    ChrSetPos(0x0014, -37500, 0, 104000, 0)
    ChrSetPos(0x0015, -39300, 0, 104000, 0)
    ChrSetPos(0x0016, -37500, 0, 102000, 0)
    ChrSetPos(0x0017, -39300, 0, 102000, 0)
    ChrSetPos(0x0018, -37500, 0, 100000, 0)
    ChrSetPos(0x0019, -39300, 0, 100000, 0)
    ChrSetPos(0x001A, -37500, 0, 98000, 0)
    ChrSetPos(0x001B, -39300, 0, 98000, 0)
    ChrSetPos(0x001C, -37500, 0, 96000, 0)
    ChrSetPos(0x001D, -39300, 0, 96000, 0)
    ChrSetPos(0x001E, -37500, 0, 94000, 0)
    ChrSetPos(0x001F, -39300, 0, 94000, 0)
    ChrSetPos(0x0020, -37500, 0, 92000, 0)
    ChrSetPos(0x0021, -39300, 0, 92000, 0)
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
    ChrClearFlags(0x000A, 0x0040)
    ChrClearFlags(0x000B, 0x0040)
    ChrClearFlags(0x000C, 0x0040)
    ChrClearFlags(0x000D, 0x0040)
    ChrClearFlags(0x000E, 0x0040)
    ChrClearFlags(0x000F, 0x0040)
    ChrClearFlags(0x0010, 0x0040)
    ChrClearFlags(0x0011, 0x0040)
    ChrClearFlags(0x0012, 0x0040)
    ChrClearFlags(0x0013, 0x0040)
    ChrClearFlags(0x0014, 0x0040)
    ChrClearFlags(0x0015, 0x0040)
    ChrClearFlags(0x0016, 0x0040)
    ChrClearFlags(0x0017, 0x0040)
    ChrClearFlags(0x0018, 0x0040)
    ChrClearFlags(0x0019, 0x0040)
    ChrClearFlags(0x001A, 0x0040)
    ChrClearFlags(0x001B, 0x0040)
    ChrClearFlags(0x001C, 0x0040)
    ChrClearFlags(0x001D, 0x0040)
    ChrClearFlags(0x001E, 0x0040)
    ChrClearFlags(0x001F, 0x0040)
    ChrClearFlags(0x0020, 0x0040)
    ChrClearFlags(0x0021, 0x0040)
    CreateThread(0x0101, 0x03, 0x00, func_0A_1879)
    WaitForThreadExit(0x0101, 0x0003)
    CreateThread(0x0101, 0x03, 0x00, func_0D_1965)

    Return()

# id: 0x000A offset: 0x1879
@scena.Code('func_0A_1879')
def func_0A_1879():
    CreateThread(0x000A, 0x01, 0x00, func_0B_1927)
    CreateThread(0x000B, 0x01, 0x00, func_0C_1946)
    CreateThread(0x000C, 0x01, 0x00, func_0B_1927)
    CreateThread(0x000D, 0x01, 0x00, func_0C_1946)
    CreateThread(0x000E, 0x01, 0x00, func_0B_1927)
    CreateThread(0x000F, 0x01, 0x00, func_0C_1946)
    CreateThread(0x0010, 0x01, 0x00, func_0B_1927)
    CreateThread(0x0011, 0x01, 0x00, func_0C_1946)
    CreateThread(0x0012, 0x01, 0x00, func_0B_1927)
    CreateThread(0x0013, 0x01, 0x00, func_0C_1946)
    CreateThread(0x0014, 0x01, 0x00, func_0B_1927)
    CreateThread(0x0015, 0x01, 0x00, func_0C_1946)
    CreateThread(0x0016, 0x01, 0x00, func_0B_1927)
    CreateThread(0x0017, 0x01, 0x00, func_0C_1946)
    CreateThread(0x0018, 0x01, 0x00, func_0B_1927)
    CreateThread(0x0019, 0x01, 0x00, func_0C_1946)
    CreateThread(0x001A, 0x01, 0x00, func_0B_1927)
    CreateThread(0x001B, 0x01, 0x00, func_0C_1946)
    CreateThread(0x001C, 0x01, 0x00, func_0B_1927)
    CreateThread(0x001D, 0x01, 0x00, func_0C_1946)
    CreateThread(0x001E, 0x01, 0x00, func_0B_1927)
    CreateThread(0x001F, 0x01, 0x00, func_0C_1946)
    CreateThread(0x0020, 0x01, 0x00, func_0B_1927)
    CreateThread(0x0021, 0x01, 0x00, func_0C_1946)
    WaitForThreadExit(0x000F, 0x0001)

    Return()

# id: 0x000B offset: 0x1927
@scena.Code('func_0B_1927')
def func_0B_1927():
    ChrSetChipByIndex(0x00FE, 21)
    ChrWalkTo(0x00FE, -37500, 0, 139500, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000C offset: 0x1946
@scena.Code('func_0C_1946')
def func_0C_1946():
    ChrSetChipByIndex(0x00FE, 21)
    ChrWalkTo(0x00FE, -39300, 0, 139500, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000D offset: 0x1965
@scena.Code('func_0D_1965')
def func_0D_1965():
    CreateThread(0x000A, 0x01, 0x00, func_0E_1A1F)
    CreateThread(0x000B, 0x01, 0x00, func_0F_1A60)
    Sleep(800)

    CreateThread(0x000C, 0x01, 0x00, func_0E_1A1F)
    CreateThread(0x000D, 0x01, 0x00, func_0F_1A60)
    Sleep(800)

    CreateThread(0x000E, 0x01, 0x00, func_0E_1A1F)
    CreateThread(0x000F, 0x01, 0x00, func_0F_1A60)
    Sleep(800)

    CreateThread(0x0010, 0x01, 0x00, func_0E_1A1F)
    CreateThread(0x0011, 0x01, 0x00, func_0F_1A60)
    Sleep(800)

    CreateThread(0x0012, 0x01, 0x00, func_0E_1A1F)
    CreateThread(0x0013, 0x01, 0x00, func_0F_1A60)
    Sleep(800)

    CreateThread(0x0014, 0x01, 0x00, func_0E_1A1F)
    CreateThread(0x0015, 0x01, 0x00, func_0F_1A60)
    Sleep(800)

    CreateThread(0x0016, 0x01, 0x00, func_0E_1A1F)
    CreateThread(0x0017, 0x01, 0x00, func_0F_1A60)
    Sleep(800)

    CreateThread(0x0018, 0x01, 0x00, func_0E_1A1F)
    CreateThread(0x0019, 0x01, 0x00, func_0F_1A60)
    Sleep(800)

    CreateThread(0x001A, 0x01, 0x00, func_0E_1A1F)
    CreateThread(0x001B, 0x01, 0x00, func_0F_1A60)
    Sleep(800)

    CreateThread(0x001C, 0x01, 0x00, func_0E_1A1F)
    CreateThread(0x001D, 0x01, 0x00, func_0F_1A60)

    Return()

# id: 0x000E offset: 0x1A1F
@scena.Code('func_0E_1A1F')
def func_0E_1A1F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1A5F',
    )

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -37500, 0, 120000, 0)
    ChrSetChipByIndex(0x00FE, 21)
    ChrWalkTo(0x00FE, -37500, 0, 136700, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('func_0E_1A1F')

    def _loc_1A5F(): pass

    label('loc_1A5F')

    Return()

# id: 0x000F offset: 0x1A60
@scena.Code('func_0F_1A60')
def func_0F_1A60():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1AA0',
    )

    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -39300, 0, 120000, 0)
    ChrSetChipByIndex(0x00FE, 21)
    ChrWalkTo(0x00FE, -39300, 0, 136700, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('func_0F_1A60')

    def _loc_1AA0(): pass

    label('loc_1AA0')

    Return()

# id: 0x0010 offset: 0x1AA1
@scena.Code('func_10_1AA1')
def func_10_1AA1():
    LoadChip('ED6_DT07/CH00330._CH', 'ED6_DT07/CH00330P._CP', 0)
    LoadChip('ED6_DT07/CH00331._CH', 'ED6_DT07/CH00331P._CP', 1)
    LoadChip('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP', 2)
    LoadChip('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP', 3)
    LoadChip('ED6_DT07/CH00336._CH', 'ED6_DT07/CH00336P._CP', 4)

    Return()

# id: 0x0011 offset: 0x1AD4
@scena.Code('func_11_1AD4')
def func_11_1AD4():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    LoadChip('ED6_DT27/CH03530._CH', 'ED6_DT27/CH03530P._CP', 23)
    LoadChip('ED6_DT27/CH03500._CH', 'ED6_DT27/CH03500P._CP', 24)
    LoadChip('ED6_DT26/CH20203._CH', 'ED6_DT26/CH20203P._CP', 25)
    LoadChip('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP', 26)
    LoadChip('ED6_DT26/CH20242._CH', 'ED6_DT26/CH20242P._CP', 5)
    LoadChip('ED6_DT27/CH04511._CH', 'ED6_DT27/CH04511P._CP', 6)
    LoadChip('ED6_DT27/CH04521._CH', 'ED6_DT27/CH04521P._CP', 7)
    LoadChip('ED6_DT26/CH20273._CH', 'ED6_DT26/CH20273P._CP', 8)
    LoadChip('ED6_DT27/CH04535._CH', 'ED6_DT27/CH04535P._CP', 9)
    LoadChip('ED6_DT26/CH20280._CH', 'ED6_DT26/CH20280P._CP', 11)
    CameraMove(-38970, 0, 100000, 0)
    OP_67(0, 12930, -10000, 0)
    CameraSetDistance(3880, 0)
    OP_6C(0, 0)
    OP_6E(516, 0)
    OP_A1(0x0048, 0x0000)
    OP_A1(0x0049, 0x0001)
    OP_A1(0x004A, 0x0007)
    OP_A1(0x004B, 0x0009)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_72(0x0009, 0x0004)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 800)
    OP_70(0x0000, 900)
    PlaySE(121, 0x01, 0x64)
    LoadEffect(0x00, 'map\\mp021_00.eff')
    ChrSetPos(0x0048, -39000, 10000, 60000, 0)
    ChrSetPos(0x0049, -39000, 0, 60000, 0)
    ChrSetPos(0x004A, -28000, 2000, 70000, 0)
    ChrSetPos(0x004B, -50000, 2000, 70000, 0)
    ChrSetChipByIndex(0x0044, 8)
    ChrSetChipByIndex(0x0046, 6)
    ChrSetChipByIndex(0x0045, 5)
    ChrSetChipByIndex(0x0047, 7)
    ChrSetSubChip(0x0045, 2)
    ChrSetFlags(0x0044, 0x0004)
    ChrSetFlags(0x0046, 0x0004)
    ChrSetFlags(0x0045, 0x0004)
    ChrSetFlags(0x0047, 0x0004)
    ChrSetPos(0x0044, -39150, 6000, 105360, 0)
    ChrSetPos(0x0046, -37150, 6000, 105360, 0)
    ChrSetPos(0x0045, -41150, 6000, 105360, 0)
    ChrSetPos(0x0047, -42150, 6000, 105360, 0)
    ChrSetChipByIndex(0x0041, 0)
    ChrSetChipByIndex(0x000A, 2)
    ChrSetChipByIndex(0x000B, 2)
    ChrSetChipByIndex(0x000C, 2)
    ChrSetChipByIndex(0x000D, 2)
    ChrSetChipByIndex(0x000E, 2)
    ChrSetChipByIndex(0x000F, 2)
    ChrSetChipByIndex(0x0010, 2)
    ChrSetChipByIndex(0x0011, 2)
    ChrSetChipByIndex(0x0012, 2)
    ChrSetChipByIndex(0x0013, 2)
    ChrSetChipByIndex(0x0014, 2)
    ChrSetChipByIndex(0x0015, 2)
    ChrSetChipByIndex(0x0016, 2)
    ChrSetChipByIndex(0x0017, 2)
    ChrSetChipByIndex(0x0018, 2)
    ChrSetChipByIndex(0x0019, 2)
    ChrSetChipByIndex(0x001A, 2)
    ChrSetChipByIndex(0x001B, 2)
    ChrSetChipByIndex(0x001C, 2)
    ChrSetChipByIndex(0x001D, 2)
    ChrSetChipByIndex(0x001E, 2)
    ChrSetChipByIndex(0x001F, 2)
    ChrSetChipByIndex(0x0020, 2)
    ChrSetChipByIndex(0x0021, 2)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_1D16')
    def lambda_1D16():
        CameraMove(-38970, 0, 108000, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D16)

    @scena.Lambda('lambda_1D2E')
    def lambda_1D2E():
        OP_67(0, 10000, -10000, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1D2E)

    @scena.Lambda('lambda_1D46')
    def lambda_1D46():
        OP_6E(385, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1D46)

    CreateThread(0x004A, 0x01, 0x00, func_1F_3C76)
    Sleep(2000)

    CreateThread(0x004B, 0x01, 0x00, func_20_3C90)
    Sleep(4000)

    CreateThread(0x0049, 0x01, 0x00, func_19_3813)
    WaitForThreadExit(0x0049, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    OP_DC()
    CreateThread(0x000A, 0x03, 0x00, func_10_1AA1)

    ChrTalk(
        0x0044,
        (
            '#0170380079V#230F#6P那么……\n',
            '差不多可以开始了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0045,
        (
            '#0200380080V#252F#2P真是的，如果『剑圣』在的话，\n',
            '多少会更有意思些……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200380081V不能开枪的士兵，\n',
            '拿来热身都不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0046,
        (
            '#0220380082V#261F#5P呵呵，这不也挺好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220380083V#265F一边解决这些小木偶，\n',
            '一边前进也挺开心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0047,
        (
            '#0210380084V#240F#4P帕蒂尔·玛蒂尔\n',
            '就不要叫出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210380085V不然他们一转眼\n',
            '就会跑个精光了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0046,
        (
            '#0220380086V#268F#5P唉，真没劲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220380087V#1306F我本来还想砸碎\n',
            '那座美丽的城堡呢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0044,
        (
            '#0170380088V#231F#6P被蹂躏毁灭的美吗……\n',
            '听起来似乎也不坏嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    WaitForThreadExit(0x000A, 0x0003)
    Fade(500)
    CameraMove(-39180, 0, 114670, 0)
    OP_67(0, 6100, -10000, 0)
    CameraSetDistance(1870, 0)
    OP_6C(36000, 0)
    OP_6E(478, 0)
    CreateThread(0x000A, 0x01, 0x00, func_21_3CAA)
    CreateThread(0x000B, 0x01, 0x00, func_22_3CEB)
    CreateThread(0x000C, 0x01, 0x00, func_23_3D31)
    CreateThread(0x000D, 0x01, 0x00, func_24_3D77)
    CreateThread(0x000E, 0x01, 0x00, func_25_3DBD)
    CreateThread(0x000F, 0x01, 0x00, func_26_3E03)
    CreateThread(0x0010, 0x01, 0x00, func_27_3E49)
    CreateThread(0x0011, 0x01, 0x00, func_28_3E8F)
    CreateThread(0x0012, 0x01, 0x00, func_29_3ED5)
    CreateThread(0x0013, 0x01, 0x00, func_2A_3F1B)
    CreateThread(0x0014, 0x01, 0x00, func_2B_3F61)
    CreateThread(0x0015, 0x01, 0x00, func_2C_3FA7)
    CreateThread(0x0016, 0x01, 0x00, func_2D_3FED)
    CreateThread(0x0017, 0x01, 0x00, func_2E_4033)
    CreateThread(0x0018, 0x01, 0x00, func_2F_4079)
    CreateThread(0x0019, 0x01, 0x00, func_30_40BF)
    CreateThread(0x001A, 0x01, 0x00, func_31_4105)
    CreateThread(0x001B, 0x01, 0x00, func_32_414B)
    CreateThread(0x001C, 0x01, 0x00, func_33_4191)
    CreateThread(0x001D, 0x01, 0x00, func_34_41D7)
    CreateThread(0x001E, 0x01, 0x00, func_35_421D)
    CreateThread(0x001F, 0x01, 0x00, func_36_4263)
    CreateThread(0x0020, 0x01, 0x00, func_37_42A9)
    CreateThread(0x0021, 0x01, 0x00, func_38_42EF)
    CreateThread(0x0041, 0x01, 0x00, func_39_4335)
    OP_0D()

    @scena.Lambda('lambda_20A4')
    def lambda_20A4():
        CameraMove(-38780, 0, 125730, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_20A4)

    @scena.Lambda('lambda_20BC')
    def lambda_20BC():
        OP_6E(491, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_20BC)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0041, 0x0001)

    ChrTalk(
        0x0041,
        (
            '#2420380089V#5P你们是『噬身之蛇』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0041,
        (
            '#2420380090V#5P可恶……\n',
            '现在竟然还能使用飞艇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-38410, 0, 114210, 0)
    OP_67(0, 6520, -10000, 0)
    CameraSetDistance(2080, 0)
    OP_6C(147000, 0)
    OP_6E(477, 0)

    @scena.Lambda('lambda_217C')
    def lambda_217C():
        ChrTurnDirection(0x00FE, 0x0047, 400)
        Yield()

        Jump('lambda_217C')

    DispatchAsync2(0x000A, 0x0001, lambda_217C)

    @scena.Lambda('lambda_218D')
    def lambda_218D():
        ChrTurnDirection(0x00FE, 0x0047, 400)
        Yield()

        Jump('lambda_218D')

    DispatchAsync2(0x000B, 0x0001, lambda_218D)

    @scena.Lambda('lambda_219E')
    def lambda_219E():
        ChrTurnDirection(0x00FE, 0x0046, 400)
        Yield()

        Jump('lambda_219E')

    DispatchAsync2(0x0012, 0x0001, lambda_219E)

    @scena.Lambda('lambda_21AF')
    def lambda_21AF():
        ChrTurnDirection(0x00FE, 0x0046, 400)
        Yield()

        Jump('lambda_21AF')

    DispatchAsync2(0x0013, 0x0001, lambda_21AF)

    @scena.Lambda('lambda_21C0')
    def lambda_21C0():
        ChrTurnDirection(0x00FE, 0x0046, 400)
        Yield()

        Jump('lambda_21C0')

    DispatchAsync2(0x0014, 0x0001, lambda_21C0)

    @scena.Lambda('lambda_21D1')
    def lambda_21D1():
        ChrTurnDirection(0x00FE, 0x0046, 400)
        Yield()

        Jump('lambda_21D1')

    DispatchAsync2(0x0015, 0x0001, lambda_21D1)

    @scena.Lambda('lambda_21E2')
    def lambda_21E2():
        CameraMove(-38290, 0, 118490, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_21E2)

    @scena.Lambda('lambda_21FA')
    def lambda_21FA():
        OP_67(0, 5290, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21FA)

    @scena.Lambda('lambda_2212')
    def lambda_2212():
        OP_6E(488, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2212)

    ChrSetChipByIndex(0x0044, 23)
    ChrSetSubChip(0x0044, 0)

    @scena.Lambda('lambda_222C')
    def lambda_222C():
        ChrWalkTo(0x00FE, -38320, 0, 117870, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0044, 0x0001, lambda_222C)

    Sleep(200)

    @scena.Lambda('lambda_224C')
    def lambda_224C():
        ChrWalkTo(0x00FE, -36850, 0, 116710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0046, 0x0001, lambda_224C)

    Sleep(50)

    @scena.Lambda('lambda_226C')
    def lambda_226C():
        ChrWalkTo(0x00FE, -40280, 0, 116770, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0047, 0x0001, lambda_226C)

    Sleep(200)

    ChrSetFlags(0x0045, 0x0040)
    ChrSetChipByIndex(0x0045, 24)

    @scena.Lambda('lambda_2296')
    def lambda_2296():
        ChrWalkTo(0x00FE, -38400, 0, 115880, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0045, 0x0001, lambda_2296)

    WaitForThreadExit(0x0044, 0x0001)
    ChrSetChipByIndex(0x0044, 9)
    ChrSetSubChip(0x0044, 0)
    WaitForThreadExit(0x0045, 0x0001)
    ChrSetChipByIndex(0x0045, 11)
    ChrSetSubChip(0x0045, 0)
    Sleep(200)

    OP_D3(0x01)
    OP_D3(0x03)
    OP_D3(0x05)
    OP_D3(0x06)
    OP_D3(0x07)
    OP_D3(0x08)

    ChrTalk(
        0x0044,
        (
            '#0170380091V#231F#5P呵呵，初次见面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380092V鄙人的名字是\n',
            '『怪盗绅士』布卢布兰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0045,
        (
            '#0200380093V#252F#2P嘿嘿……\n',
            '我是『瘦狼』瓦鲁特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200380094V你们就尽情享受恐惧的滋味吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0047,
        (
            '#0210380095V#244F#2P我是『幻惑之铃』露茜奥拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210380096V#240F虽然只能相聚片刻，\n',
            '但希望能给各位留下个好印象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0046,
        (
            '#0220380097V#261F#5P嘻嘻……\n',
            '我是『歼灭天使』玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220380098V#1306F你们会发出\n',
            '怎样的惨叫声呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0041,
        (
            '#2420380099V#5P还、还有闲情来自报家门……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0041, 0)
    ChrSetChipByIndex(0x0041, 4)
    OP_0D()

    ChrTalk(
        0x0041,
        (
            '#2420380100V#5P#3S全体准备！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrSetSubChip(0x0041, 1)

    ChrTalk(
        0x0041,
        (
            '#2420380101V#5P#3S突击！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Battle(0x00002710, 0x0030000F, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0044, 0x0080)
    ChrSetFlags(0x0045, 0x0080)
    ChrSetFlags(0x0047, 0x0080)
    ChrSetFlags(0x0046, 0x0080)
    ChrSetFlags(0x0041, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
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
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00002711, 0x00300010, 0x00, 0x0000, 0xFF)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00002712, 0x00300011, 0x00, 0x0000, 0xFF)
    Call(0, 0x0012)

    Return()

# id: 0x0012 offset: 0x25E9
@scena.Code('func_12_25E9')
def func_12_25E9():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0045, 0x01)
    TerminateThread(0x0046, 0x01)
    TerminateThread(0x0047, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0014, 0x01)
    TerminateThread(0x0015, 0x01)
    TerminateThread(0x0016, 0x01)
    TerminateThread(0x0017, 0x01)
    TerminateThread(0x0018, 0x01)
    TerminateThread(0x0019, 0x01)
    LoadChip('ED6_DT07/CH00330._CH', 'ED6_DT07/CH00330P._CP', 0)
    LoadChip('ED6_DT27/CH03530._CH', 'ED6_DT27/CH03530P._CP', 23)
    LoadChip('ED6_DT26/CH20203._CH', 'ED6_DT26/CH20203P._CP', 25)
    LoadChip('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP', 26)
    LoadChip('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP', 2)
    LoadChip('ED6_DT07/CH00323._CH', 'ED6_DT07/CH00323P._CP', 5)
    LoadChip('ED6_DT06/CH20043._CH', 'ED6_DT06/CH20043P._CP', 6)
    LoadChip('ED6_DT07/CH00334._CH', 'ED6_DT07/CH00334P._CP', 7)
    LoadChip('ED6_DT26/CH20280._CH', 'ED6_DT26/CH20280P._CP', 8)
    LoadChip('ED6_DT27/CH04535._CH', 'ED6_DT27/CH04535P._CP', 9)
    LoadChip('ED6_DT26/CH20419._CH', 'ED6_DT26/CH20419P._CP', 27)
    ChrClearFlags(0x0044, 0x0080)
    ChrClearFlags(0x0045, 0x0080)
    ChrClearFlags(0x0047, 0x0080)
    ChrClearFlags(0x0046, 0x0080)
    ChrClearFlags(0x0041, 0x0080)
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
    CameraMove(-38500, 0, 119490, 0)
    OP_67(0, 5160, -10000, 0)
    CameraSetDistance(1730, 0)
    OP_6C(180000, 0)
    OP_6E(498, 0)
    ChrSetFlags(0x0044, 0x0080)
    ChrClearFlags(0x0041, 0x0080)
    ChrSetSubChip(0x0041, 0)
    ChrSetChipByIndex(0x0041, 0)
    ChrSetSubChip(0x0041, 0)
    ChrSetPos(0x0041, -38950, 0, 126850, 180)
    ChrClearFlags(0x0045, 0x0080)
    ChrClearFlags(0x0046, 0x0080)
    ChrClearFlags(0x0047, 0x0080)
    ChrSetPos(0x0045, -38310, 0, 120840, 0)
    ChrSetPos(0x0046, -35960, 0, 120330, 45)
    ChrSetPos(0x0047, -40360, 0, 119490, 315)
    ChrSetChipByIndex(0x0045, 8)
    ChrSetChipByIndex(0x0046, 25)
    ChrSetChipByIndex(0x0047, 26)
    ChrSetChipByIndex(0x0044, 9)
    ChrSetSubChip(0x0045, 0)
    ChrSetSubChip(0x0046, 0)
    ChrSetSubChip(0x0047, 0)
    OP_A1(0x0048, 0x0000)
    OP_A1(0x0049, 0x0001)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    ChrSetPos(0x0048, -39020, 0, 97470, 0)
    ChrSetPos(0x0049, -39020, 100, 98470, 0)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 1100)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0014, 0x0040)
    ChrSetFlags(0x0015, 0x0040)
    ChrSetFlags(0x0016, 0x0040)
    ChrSetFlags(0x0017, 0x0040)
    ChrSetFlags(0x0018, 0x0040)
    ChrSetFlags(0x0019, 0x0040)
    MapClearFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(1000, 0)

    @scena.Lambda('lambda_28BB')
    def lambda_28BB():
        CameraMove(-38500, 0, 121000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_28BB)

    @scena.Lambda('lambda_28D3')
    def lambda_28D3():
        CameraSetDistance(2000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_28D3)

    CreateThread(0x0101, 0x03, 0x00, func_6F_519D)
    CreateThread(0x000A, 0x01, 0x00, func_57_47AD)
    CreateThread(0x000B, 0x01, 0x00, func_58_4817)
    CreateThread(0x000C, 0x01, 0x00, func_59_4881)
    CreateThread(0x000D, 0x01, 0x00, func_5A_48EB)
    CreateThread(0x000E, 0x01, 0x00, func_5B_4955)
    CreateThread(0x000F, 0x01, 0x00, func_5C_49BF)
    CreateThread(0x0010, 0x01, 0x00, func_5D_4A29)
    CreateThread(0x0011, 0x01, 0x00, func_5E_4A93)
    CreateThread(0x0012, 0x01, 0x00, func_5F_4AFD)
    CreateThread(0x0013, 0x01, 0x00, func_60_4B67)
    CreateThread(0x0014, 0x01, 0x00, func_61_4BD1)
    CreateThread(0x0015, 0x01, 0x00, func_62_4C3B)
    CreateThread(0x0016, 0x01, 0x00, func_63_4CA5)
    CreateThread(0x0017, 0x01, 0x00, func_64_4D0F)
    CreateThread(0x0018, 0x01, 0x00, func_65_4D79)
    CreateThread(0x0019, 0x01, 0x00, func_66_4DE3)
    CreateThread(0x001A, 0x01, 0x00, func_67_4E4D)
    CreateThread(0x001B, 0x01, 0x00, func_68_4EB7)
    CreateThread(0x001C, 0x01, 0x00, func_69_4F21)
    CreateThread(0x001D, 0x01, 0x00, func_6A_4F8B)
    CreateThread(0x001E, 0x01, 0x00, func_6B_4FF5)
    CreateThread(0x001F, 0x01, 0x00, func_6C_505F)
    CreateThread(0x0020, 0x01, 0x00, func_6D_50C9)
    CreateThread(0x0021, 0x01, 0x00, func_6E_5133)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0021, 0x0001)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    MapSetFlags(0x00000010)
    TerminateThread(0x0101, 0x03)
    OP_62(0x0041, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0041)
    Sleep(500)

    ChrTalk(
        0x0041,
        (
            '#2420380102V#5P……啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_29EF')
    def lambda_29EF():
        CameraMove(-39000, 0, 125640, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_29EF)

    @scena.Lambda('lambda_2A07')
    def lambda_2A07():
        OP_67(0, 5520, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A07)

    ChrSetFlags(0x0044, 0x0020)
    ChrSetFlags(0x0044, 0x0004)
    ChrSetPos(0x0044, -39060, 1500, 130190, 180)
    ChrSetRGBAMask(0x0044, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0044, 0x0080)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x0044, 0x0020)

    @scena.Lambda('lambda_2A54')
    def lambda_2A54():
        ChrMoveTo(0x00FE, -39060, 0, 130190, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0044, 0x0001, lambda_2A54)

    ChrSetRGBAMask(0x0044, 255, 255, 255, 255, 1000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0044, 0x0001)
    ChrClearFlags(0x0044, 0x0020)

    ChrTalk(
        0x0044,
        (
            '#0170380103V#230F──这就是所谓的“世事如梦幻”。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0041, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0041, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_2AEE')
    def lambda_2AEE():
        ChrSetDirection(0x00FE, 0, 600)

        ExitThread()

    DispatchAsync(0x0041, 0x0001, lambda_2AEE)

    WaitForThreadExit(0x0041, 0x0001)

    ChrTalk(
        0x0041,
        (
            '#2420380104V#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
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
    TerminateThread(0x001F, 0xFF)
    TerminateThread(0x0020, 0xFF)
    TerminateThread(0x0021, 0xFF)
    FadeOut(1000, 0, -1)
    OP_0D()

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x00002713, 0x00300012, 0x00, 0x0000, 0xFF)

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(0, 0x0013)

    Return()

# id: 0x0013 offset: 0x2BA5
@scena.Code('func_13_2BA5')
def func_13_2BA5():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0044, 0x01)
    LoadChip('ED6_DT27/CH03530._CH', 'ED6_DT27/CH03530P._CP', 23)
    LoadChip('ED6_DT27/CH03500._CH', 'ED6_DT27/CH03500P._CP', 24)
    LoadChip('ED6_DT26/CH20203._CH', 'ED6_DT26/CH20203P._CP', 25)
    LoadChip('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP', 26)
    LoadChip('ED6_DT06/CH20043._CH', 'ED6_DT06/CH20043P._CP', 6)
    LoadChip('ED6_DT07/CH00334._CH', 'ED6_DT07/CH00334P._CP', 7)
    LoadChip('ED6_DT26/CH20208._CH', 'ED6_DT26/CH20208P._CP', 8)
    LoadChip('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP', 9)
    LoadChip('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP', 10)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 13)
    LoadChip('ED6_DT26/CH20280._CH', 'ED6_DT26/CH20280P._CP', 14)
    LoadChip('ED6_DT26/CH20419._CH', 'ED6_DT26/CH20419P._CP', 27)
    ChrClearFlags(0x0045, 0x0080)
    ChrClearFlags(0x0046, 0x0080)
    ChrClearFlags(0x0047, 0x0080)
    ChrSetPos(0x0045, -38410, 0, 118740, 0)
    ChrSetPos(0x0046, -36890, 0, 117820, 0)
    ChrSetPos(0x0047, -39620, 0, 117750, 0)
    ChrSetChipByIndex(0x0046, 25)
    ChrSetChipByIndex(0x0047, 26)
    ChrSetChipByIndex(0x0045, 14)
    ChrSetSubChip(0x0045, 0)
    ChrClearFlags(0x0044, 0x0080)
    ChrSetPos(0x0044, -38760, 0, 123350, 180)
    ChrSetChipByIndex(0x0044, 23)
    LoadEffect(0x00, 'map\\\\mp021_00.eff')
    OP_A1(0x0048, 0x0000)
    OP_A1(0x0049, 0x0001)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    ChrSetPos(0x0048, -39020, 0, 97470, 0)
    ChrSetPos(0x0049, -39020, 100, 98470, 0)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 1100)
    Call(0, 0x0018)
    ChrClearFlags(0x0041, 0x0080)
    ChrSetPos(0x0041, -38950, 0, 125450, 0)
    ChrSetSubChip(0x0041, 0)
    ChrSetChipByIndex(0x0041, 7)
    CameraMove(-38720, 0, 124180, 0)
    OP_67(0, 6440, -10000, 0)
    CameraSetDistance(1910, 0)
    OP_6C(134000, 0)
    OP_6E(428, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_99(0x0041, 0x00, 0x03, 1500)
    Fade(250)
    PlaySE(524, 0x00, 0x64)
    ChrClearFlags(0x0041, 0x0001)
    ChrSetPos(0x0041, -39500, 0, 126600, 0)
    ChrSetSubChip(0x0041, 0)
    ChrSetChipByIndex(0x0041, 20)
    Sleep(1500)

    @scena.Lambda('lambda_2D9D')
    def lambda_2D9D():
        CameraMove(-37580, 0, 118220, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2D9D)

    @scena.Lambda('lambda_2DB5')
    def lambda_2DB5():
        CameraSetDistance(2000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DB5)

    @scena.Lambda('lambda_2DC5')
    def lambda_2DC5():
        ChrWalkTo(0x00FE, -38070, 0, 120620, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0044, 0x0000, lambda_2DC5)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0044, 0x0000)

    ChrTalk(
        0x0045,
        (
            '#0200380105V#254F#2P哼哼，一群小杂鱼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0046,
        (
            '#0220380106V#266F真是的……\n',
            '也太不禁打了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0047,
        (
            '#0210380107V#241F#2P呵呵……别要求太高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210380108V算了，不知女王陛下的亲卫队\n',
            '能不能给我们一点惊喜呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0044,
        (
            '#0170380109V#230F#6P嗯，但愿如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380110V#231F……那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_2F05')
    def lambda_2F05():
        CameraMove(-37380, 0, 116150, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2F05)

    @scena.Lambda('lambda_2F1D')
    def lambda_2F1D():
        ChrWalkTo(0x00FE, -37890, 0, 116570, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0044, 0x0000, lambda_2F1D)

    @scena.Lambda('lambda_2F38')
    def lambda_2F38():
        ChrTurnDirection(0x00FE, 0x0044, 400)
        Yield()

        Jump('lambda_2F38')

    DispatchAsync2(0x0046, 0x0002, lambda_2F38)

    @scena.Lambda('lambda_2F49')
    def lambda_2F49():
        ChrTurnDirection(0x00FE, 0x0044, 400)
        Yield()

        Jump('lambda_2F49')

    DispatchAsync2(0x0047, 0x0002, lambda_2F49)

    Sleep(100)

    CreateThread(0x0045, 0x00, 0x00, func_16_3423)
    WaitForThreadExit(0x0044, 0x0000)
    TerminateThread(0x0046, 0x02)
    TerminateThread(0x0047, 0x02)
    TerminateThread(0x0045, 0x02)

    @scena.Lambda('lambda_2F77')
    def lambda_2F77():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0046, 0x0001, lambda_2F77)

    @scena.Lambda('lambda_2F85')
    def lambda_2F85():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0047, 0x0001, lambda_2F85)

    ChrSetDirection(0x0045, 180, 400)
    WaitForThreadExit(0x0101, 0x0000)
    PlayEffect(0x00, 0x00, 0x0048, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(121, 0x01, 0x64)
    PlaySE(204, 0x00, 0x64)

    @scena.Lambda('lambda_2FDE')
    def lambda_2FDE():
        CameraMove(-38930, 0, 112070, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2FDE)

    @scena.Lambda('lambda_2FF6')
    def lambda_2FF6():
        OP_67(0, 10930, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FF6)

    @scena.Lambda('lambda_300E')
    def lambda_300E():
        CameraSetDistance(1370, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_300E)

    @scena.Lambda('lambda_301E')
    def lambda_301E():
        OP_6E(578, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_301E)

    @scena.Lambda('lambda_302E')
    def lambda_302E():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0045, 0x0001, lambda_302E)

    Sleep(100)

    @scena.Lambda('lambda_3041')
    def lambda_3041():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0046, 0x0001, lambda_3041)

    Sleep(100)

    @scena.Lambda('lambda_3054')
    def lambda_3054():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0047, 0x0001, lambda_3054)

    Sleep(1800)

    CreateThread(0x0048, 0x03, 0x00, func_17_3464)

    @scena.Lambda('lambda_306E')
    def lambda_306E():
        ChrWalkTo(0x00FE, -39020, 10000, 106470, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0001, lambda_306E)

    @scena.Lambda('lambda_3089')
    def lambda_3089():
        ChrWalkTo(0x00FE, -39020, 0, 106470, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0001, lambda_3089)

    Sleep(1000)

    @scena.Lambda('lambda_30A9')
    def lambda_30A9():
        ChrWalkTo(0x00FE, -39020, 10000, 106470, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0001, lambda_30A9)

    @scena.Lambda('lambda_30C4')
    def lambda_30C4():
        ChrWalkTo(0x00FE, -39020, 0, 106470, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0001, lambda_30C4)

    Sleep(2000)

    @scena.Lambda('lambda_30E4')
    def lambda_30E4():
        ChrWalkTo(0x00FE, -39020, 10000, 116470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0001, lambda_30E4)

    @scena.Lambda('lambda_30FF')
    def lambda_30FF():
        ChrWalkTo(0x00FE, -39020, 0, 116470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0001, lambda_30FF)

    Sleep(2000)

    @scena.Lambda('lambda_311F')
    def lambda_311F():
        ChrWalkTo(0x00FE, -39020, 10000, 146470, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0001, lambda_311F)

    @scena.Lambda('lambda_313A')
    def lambda_313A():
        ChrWalkTo(0x00FE, -39020, 0, 146470, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0001, lambda_313A)

    StopEffect(0x00, 0x02)
    OP_23(0x00CC)
    CreateThread(0x0028, 0x02, 0x00, func_70_51C9)
    CreateThread(0x0028, 0x03, 0x00, func_72_5689)
    WaitForThreadExit(0x0028, 0x0002)
    TerminateThread(0x0028, 0x03)
    OP_23(0x013A)
    WaitForThreadExit(0x0101, 0x0000)
    Fade(500)
    CameraMove(-37770, 0, 112810, 0)
    OP_67(0, 6180, -10000, 0)
    CameraSetDistance(1900, 0)
    OP_6C(134000, 0)
    OP_6E(470, 0)
    OP_23(0x0079)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0044,
        (
            '#0170380111V#234F#6P我们执行者现在\n',
            '开始前往格兰赛尔城！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380112V你们就照原定计划，\n',
            '格兰赛尔的市区！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetMessageWindowPos(350, 100, -1, -1)
    TalkSetChrName('强化猎兵们')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#4210380113V#5S明白了！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(1000, 0, -1)
    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32BC',
    )

    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/R4101._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_32C8')

    def _loc_32BC(): pass

    label('loc_32BC')

    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/R4101._SN', 101, 0, 0)
    IdleLoop()

    def _loc_32C8(): pass

    label('loc_32C8')

    Return()

# id: 0x0014 offset: 0x32C9
@scena.Code('func_14_32C9')
def func_14_32C9():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    CameraMove(-5000, 0, 7380, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -5000, 0, 7380, 0)
    ChrSetPos(0x0001, -5000, 0, 7380, 0)
    ChrSetPos(0x0002, -5000, 0, 7380, 0)
    ChrSetPos(0x0003, -5000, 0, 7380, 0)
    OP_69(0x0000, 0)
    SetScenaFlags(ScenaFlag(0x0407, 1, 0x2039))
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0015 offset: 0x3376
@scena.Code('func_15_3376')
def func_15_3376():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    CameraMove(46870, 0, 83250, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 46870, 0, 83250, 270)
    ChrSetPos(0x0001, 46870, 0, 83250, 270)
    ChrSetPos(0x0002, 46870, 0, 83250, 270)
    ChrSetPos(0x0003, 46870, 0, 83250, 270)
    OP_69(0x0000, 0)
    SetScenaFlags(ScenaFlag(0x0407, 1, 0x2039))
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0016 offset: 0x3423
@scena.Code('func_16_3423')
def func_16_3423():
    ChrSetChipByIndex(0x00FE, 24)
    ChrSetDirection(0x00FE, 90, 400)
    ChrMoveTo(0x00FE, -38910, 0, 118970, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 14)
    Sleep(100)

    @scena.Lambda('lambda_3458')
    def lambda_3458():
        ChrTurnDirection(0x00FE, 0x0044, 400)
        Yield()

        Jump('lambda_3458')

    DispatchAsync2(0x00FE, 0x0002, lambda_3458)

    Return()

# id: 0x0017 offset: 0x3464
@scena.Code('func_17_3464')
def func_17_3464():
    OP_6F(0x0000, 561)
    OP_70(0x0000, 650)
    OP_73(0x0000)
    OP_6F(0x0000, 651)
    OP_70(0x0000, 680)
    OP_73(0x0000)
    OP_71(0x0000, 0x0008)
    OP_6F(0x0000, 680)
    OP_70(0x0000, 780)

    Return()

# id: 0x0018 offset: 0x349A
@scena.Code('func_18_349A')
def func_18_349A():
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
    ChrSetFlags(0x000A, 0x0020)
    ChrSetFlags(0x000B, 0x0020)
    ChrSetFlags(0x000C, 0x0020)
    ChrSetFlags(0x000D, 0x0020)
    ChrSetFlags(0x000E, 0x0020)
    ChrSetFlags(0x000F, 0x0020)
    ChrSetFlags(0x0010, 0x0020)
    ChrSetFlags(0x0011, 0x0020)
    ChrSetFlags(0x0012, 0x0020)
    ChrSetFlags(0x0013, 0x0020)
    ChrSetFlags(0x0014, 0x0020)
    ChrSetFlags(0x0015, 0x0020)
    ChrSetFlags(0x0016, 0x0020)
    ChrSetFlags(0x0017, 0x0020)
    ChrSetFlags(0x0018, 0x0020)
    ChrSetFlags(0x0019, 0x0020)
    ChrSetFlags(0x001A, 0x0020)
    ChrSetFlags(0x001B, 0x0020)
    ChrSetFlags(0x001C, 0x0020)
    ChrSetFlags(0x001D, 0x0020)
    ChrSetFlags(0x001E, 0x0020)
    ChrSetFlags(0x001F, 0x0020)
    ChrSetFlags(0x0020, 0x0020)
    ChrSetFlags(0x0021, 0x0020)
    ChrClearFlags(0x000A, 0x0001)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    ChrClearFlags(0x000D, 0x0001)
    ChrClearFlags(0x000E, 0x0001)
    ChrClearFlags(0x000F, 0x0001)
    ChrClearFlags(0x0010, 0x0001)
    ChrClearFlags(0x0011, 0x0001)
    ChrClearFlags(0x0012, 0x0001)
    ChrClearFlags(0x0013, 0x0001)
    ChrClearFlags(0x0014, 0x0001)
    ChrClearFlags(0x0015, 0x0001)
    ChrClearFlags(0x0016, 0x0001)
    ChrClearFlags(0x0017, 0x0001)
    ChrClearFlags(0x0018, 0x0001)
    ChrClearFlags(0x0019, 0x0001)
    ChrClearFlags(0x001A, 0x0001)
    ChrClearFlags(0x001B, 0x0001)
    ChrClearFlags(0x001C, 0x0001)
    ChrClearFlags(0x001D, 0x0001)
    ChrClearFlags(0x001E, 0x0001)
    ChrClearFlags(0x001F, 0x0001)
    ChrClearFlags(0x0020, 0x0001)
    ChrClearFlags(0x0021, 0x0001)
    ChrSetChipByIndex(0x000A, 19)
    ChrSetChipByIndex(0x000B, 27)
    ChrSetChipByIndex(0x000C, 19)
    ChrSetChipByIndex(0x000D, 19)
    ChrSetChipByIndex(0x000E, 27)
    ChrSetChipByIndex(0x000F, 19)
    ChrSetChipByIndex(0x0010, 27)
    ChrSetChipByIndex(0x0011, 19)
    ChrSetChipByIndex(0x0012, 19)
    ChrSetChipByIndex(0x0013, 27)
    ChrSetChipByIndex(0x0014, 27)
    ChrSetChipByIndex(0x0015, 19)
    ChrSetChipByIndex(0x0016, 19)
    ChrSetChipByIndex(0x0017, 27)
    ChrSetChipByIndex(0x0018, 27)
    ChrSetChipByIndex(0x0019, 19)
    ChrSetChipByIndex(0x001A, 19)
    ChrSetChipByIndex(0x001B, 27)
    ChrSetChipByIndex(0x001C, 19)
    ChrSetChipByIndex(0x001D, 27)
    ChrSetChipByIndex(0x001E, 27)
    ChrSetChipByIndex(0x001F, 19)
    ChrSetChipByIndex(0x0020, 27)
    ChrSetChipByIndex(0x0021, 19)
    ChrSetPos(0x000A, -32360, 0, 119050, 315)
    ChrSetPos(0x000B, -30880, 0, 120220, 90)
    ChrSetPos(0x000C, -32770, 0, 122700, 225)
    ChrSetPos(0x000D, -30610, 250, 124400, 270)
    ChrSetPos(0x000E, -30670, 250, 127190, 135)
    ChrSetPos(0x000F, -34040, 0, 126930, 45)
    ChrSetPos(0x0010, -29470, 250, 125310, 45)
    ChrSetPos(0x0011, -30310, 250, 127840, 0)
    ChrSetPos(0x0012, -44210, 0, 117600, 180)
    ChrSetPos(0x0013, -46380, 0, 119590, 225)
    ChrSetPos(0x0014, -44450, 0, 119820, 225)
    ChrSetPos(0x0015, -47450, 0, 121690, 45)
    ChrSetPos(0x0016, -43440, 0, 122980, 270)
    ChrSetPos(0x0017, -46070, 250, 125390, 135)
    ChrSetPos(0x0018, -49300, 0, 122100, 315)
    ChrSetPos(0x0019, -48780, 250, 125590, 180)
    ChrSetPos(0x001A, -35240, 0, 125600, 135)
    ChrSetPos(0x001B, -33350, 0, 124670, 45)
    ChrSetPos(0x001C, -36960, 0, 125620, 180)
    ChrSetPos(0x001D, -36270, 0, 128990, 0)
    ChrSetPos(0x001E, -42380, 0, 125390, 315)
    ChrSetPos(0x001F, -41140, 0, 127160, 0)
    ChrSetPos(0x0020, -42200, 0, 123740, 270)
    ChrSetPos(0x0021, -43690, 0, 127730, 180)

    Return()

# id: 0x0019 offset: 0x3813
@scena.Code('func_19_3813')
def func_19_3813():
    @scena.Lambda('lambda_3819')
    def lambda_3819():
        ChrWalkTo(0x00FE, -39020, 10000, 86470, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0002, lambda_3819)

    @scena.Lambda('lambda_3834')
    def lambda_3834():
        ChrWalkTo(0x00FE, -39020, 100, 86470, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0002, lambda_3834)

    Sleep(1000)

    @scena.Lambda('lambda_3854')
    def lambda_3854():
        ChrWalkTo(0x00FE, -39020, 10000, 86470, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0002, lambda_3854)

    @scena.Lambda('lambda_386F')
    def lambda_386F():
        ChrWalkTo(0x00FE, -39020, 100, 86470, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0002, lambda_386F)

    Sleep(500)

    @scena.Lambda('lambda_388F')
    def lambda_388F():
        ChrWalkTo(0x00FE, -39020, 10000, 86470, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0002, lambda_388F)

    @scena.Lambda('lambda_38AA')
    def lambda_38AA():
        ChrWalkTo(0x00FE, -39020, 100, 86470, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0002, lambda_38AA)

    Sleep(500)

    @scena.Lambda('lambda_38CA')
    def lambda_38CA():
        ChrWalkTo(0x00FE, -39020, 10000, 86470, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0002, lambda_38CA)

    @scena.Lambda('lambda_38E5')
    def lambda_38E5():
        ChrWalkTo(0x00FE, -39020, 100, 86470, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0002, lambda_38E5)

    WaitForThreadExit(0x0048, 0x0002)

    @scena.Lambda('lambda_3905')
    def lambda_3905():
        ChrWalkTo(0x00FE, -39020, 0, 97470, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0002, lambda_3905)

    @scena.Lambda('lambda_3920')
    def lambda_3920():
        ChrWalkTo(0x00FE, -39020, 100, 97470, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0002, lambda_3920)

    Sleep(1000)

    @scena.Lambda('lambda_3940')
    def lambda_3940():
        ChrWalkTo(0x00FE, -39020, 0, 97470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0002, lambda_3940)

    @scena.Lambda('lambda_395B')
    def lambda_395B():
        ChrWalkTo(0x00FE, -39020, 100, 97470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0002, lambda_395B)

    Sleep(1000)

    @scena.Lambda('lambda_397B')
    def lambda_397B():
        ChrWalkTo(0x00FE, -39020, 0, 97470, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0002, lambda_397B)

    @scena.Lambda('lambda_3996')
    def lambda_3996():
        ChrWalkTo(0x00FE, -39020, 100, 98470, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0002, lambda_3996)

    PlayEffect(0x00, 0x00, 0x0048, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(204, 0x00, 0x64)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0101, 0x03)
    Fade(500)
    CameraMove(-38120, 6130, 109760, 0)
    OP_67(0, 4550, -10000, 0)
    CameraSetDistance(2300, 0)
    OP_6C(134000, 0)
    OP_6E(473, 0)
    CreateThread(0x0048, 0x03, 0x00, func_1A_3AAD)
    OP_0D()

    @scena.Lambda('lambda_3A41')
    def lambda_3A41():
        CameraMove(-38120, 0, 109760, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3A41)

    Sleep(1500)

    CreateThread(0x0044, 0x01, 0x00, func_1B_3AC7)
    Sleep(100)

    CreateThread(0x0045, 0x01, 0x00, func_1D_3B9C)
    Sleep(100)

    CreateThread(0x0046, 0x01, 0x00, func_1C_3B2F)
    Sleep(100)

    CreateThread(0x0047, 0x01, 0x00, func_1E_3C09)
    WaitForThreadExit(0x0048, 0x0002)
    WaitForThreadExit(0x0048, 0x0003)
    StopEffect(0x00, 0x02)
    OP_23(0x00CC)
    OP_23(0x0079)
    PlaySE(200, 0x00, 0x64)
    OP_7C(100, 0, 5000, 1000)

    Return()

# id: 0x001A offset: 0x3AAD
@scena.Code('func_1A_3AAD')
def func_1A_3AAD():
    OP_72(0x0000, 0x0020)
    OP_73(0x0000)
    OP_6F(0x0000, 1021)
    OP_70(0x0000, 1100)
    OP_73(0x0000)

    Return()

# id: 0x001B offset: 0x3AC7
@scena.Code('func_1B_3AC7')
def func_1B_3AC7():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0044, 0x0080)
    ChrClearFlags(0x0044, 0x0001)
    ChrSetAfterImage(0x00, 0x0044, 0x0032, 0x01F4)

    @scena.Lambda('lambda_3AEA')
    def lambda_3AEA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 800)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3AEA)

    PlaySE(153, 0x00, 0x64)
    ChrJumpTo(0x0044, -39490, 0, 112610, 3000, 5000)
    ChrSetChipByIndex(0x0044, 9)
    ChrSetSubChip(0x0044, 0)
    PlaySE(164, 0x00, 0x64)
    ChrSetAfterImage(0x01, 0x0044, 0x0000, 0x0000)
    ChrSetFlags(0x0044, 0x0001)

    Return()

# id: 0x001C offset: 0x3B2F
@scena.Code('func_1C_3B2F')
def func_1C_3B2F():
    Sleep(100)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0046, 0x0080)
    ChrClearFlags(0x0046, 0x0001)
    ChrSetAfterImage(0x00, 0x0046, 0x0032, 0x01F4)

    @scena.Lambda('lambda_3B57')
    def lambda_3B57():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 800)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3B57)

    PlaySE(153, 0x00, 0x64)
    ChrJumpTo(0x0046, -37550, 0, 111980, 3000, 5000)
    ChrSetChipByIndex(0x0046, 25)
    ChrSetSubChip(0x0046, 0)
    PlaySE(164, 0x00, 0x64)
    ChrSetAfterImage(0x01, 0x0046, 0x0000, 0x0000)
    ChrSetFlags(0x0046, 0x0001)

    Return()

# id: 0x001D offset: 0x3B9C
@scena.Code('func_1D_3B9C')
def func_1D_3B9C():
    Sleep(200)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0045, 0x0080)
    ChrClearFlags(0x0045, 0x0001)
    ChrSetAfterImage(0x00, 0x0045, 0x0032, 0x01F4)

    @scena.Lambda('lambda_3BC4')
    def lambda_3BC4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 800)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3BC4)

    PlaySE(153, 0x00, 0x64)
    ChrJumpTo(0x0045, -39000, 0, 110350, 3000, 5000)
    ChrSetChipByIndex(0x0045, 11)
    ChrSetSubChip(0x0045, 0)
    PlaySE(164, 0x00, 0x64)
    ChrSetAfterImage(0x01, 0x0045, 0x0000, 0x0000)
    ChrSetFlags(0x0045, 0x0001)

    Return()

# id: 0x001E offset: 0x3C09
@scena.Code('func_1E_3C09')
def func_1E_3C09():
    Sleep(300)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0047, 0x0080)
    ChrClearFlags(0x0047, 0x0001)
    ChrSetAfterImage(0x00, 0x0047, 0x0032, 0x01F4)

    @scena.Lambda('lambda_3C31')
    def lambda_3C31():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 800)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3C31)

    PlaySE(153, 0x00, 0x64)
    ChrJumpTo(0x0047, -40880, 0, 110720, 3000, 5000)
    ChrSetChipByIndex(0x0047, 26)
    ChrSetSubChip(0x0047, 0)
    PlaySE(164, 0x00, 0x64)
    ChrSetAfterImage(0x01, 0x0047, 0x0000, 0x0000)
    ChrSetFlags(0x0047, 0x0001)

    Return()

# id: 0x001F offset: 0x3C76
@scena.Code('func_1F_3C76')
def func_1F_3C76():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, 100000, 30000, 0x00)
    OP_71(0x0007, 0x0004)

    Return()

# id: 0x0020 offset: 0x3C90
@scena.Code('func_20_3C90')
def func_20_3C90():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, 100000, 30000, 0x00)
    OP_71(0x0009, 0x0004)

    Return()

# id: 0x0021 offset: 0x3CAA
@scena.Code('func_21_3CAA')
def func_21_3CAA():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    ChrSetPos(0x00FE, -37450, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -32189, 0, 118940, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0022 offset: 0x3CEB
@scena.Code('func_22_3CEB')
def func_22_3CEB():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(400)

    ChrSetPos(0x00FE, -37450, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -31010, 0, 120100, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0023 offset: 0x3D31
@scena.Code('func_23_3D31')
def func_23_3D31():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(800)

    ChrSetPos(0x00FE, -37450, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -32980, 0, 120530, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0024 offset: 0x3D77
@scena.Code('func_24_3D77')
def func_24_3D77():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(1200)

    ChrSetPos(0x00FE, -37450, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -31930, 0, 121530, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0025 offset: 0x3DBD
@scena.Code('func_25_3DBD')
def func_25_3DBD():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(1600)

    ChrSetPos(0x00FE, -37450, 0, 133600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -33700, 0, 121820, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0026 offset: 0x3E03
@scena.Code('func_26_3E03')
def func_26_3E03():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(2000)

    ChrSetPos(0x00FE, -37450, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -32770, 0, 123000, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0027 offset: 0x3E49
@scena.Code('func_27_3E49')
def func_27_3E49():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(2400)

    ChrSetPos(0x00FE, -37450, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -34310, 0, 123060, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0028 offset: 0x3E8F
@scena.Code('func_28_3E8F')
def func_28_3E8F():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(2800)

    ChrSetPos(0x00FE, -37450, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -33360, 0, 124290, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0029 offset: 0x3ED5
@scena.Code('func_29_3ED5')
def func_29_3ED5():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(50)

    ChrSetPos(0x00FE, -40590, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -45120, 0, 118750, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x002A offset: 0x3F1B
@scena.Code('func_2A_3F1B')
def func_2A_3F1B():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(450)

    ChrSetPos(0x00FE, -40590, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -46280, 0, 119950, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x002B offset: 0x3F61
@scena.Code('func_2B_3F61')
def func_2B_3F61():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(850)

    ChrSetPos(0x00FE, -40590, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -44490, 0, 120420, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x002C offset: 0x3FA7
@scena.Code('func_2C_3FA7')
def func_2C_3FA7():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(1250)

    ChrSetPos(0x00FE, -40590, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -45680, 0, 121410, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x002D offset: 0x3FED
@scena.Code('func_2D_3FED')
def func_2D_3FED():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(1650)

    ChrSetPos(0x00FE, -40590, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -43780, 0, 122020, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x002E offset: 0x4033
@scena.Code('func_2E_4033')
def func_2E_4033():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(2050)

    ChrSetPos(0x00FE, -40590, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -45100, 0, 122980, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x002F offset: 0x4079
@scena.Code('func_2F_4079')
def func_2F_4079():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(2450)

    ChrSetPos(0x00FE, -40590, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -43060, 100, 123370, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x0030 offset: 0x40BF
@scena.Code('func_30_40BF')
def func_30_40BF():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(2850)

    ChrSetPos(0x00FE, -40590, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -44180, 0, 124520, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x0031 offset: 0x4105
@scena.Code('func_31_4105')
def func_31_4105():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(100)

    ChrSetPos(0x00FE, -38990, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -36220, 0, 123360, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0032 offset: 0x414B
@scena.Code('func_32_414B')
def func_32_414B():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(500)

    ChrSetPos(0x00FE, -38990, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -37760, 0, 123670, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0033 offset: 0x4191
@scena.Code('func_33_4191')
def func_33_4191():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(900)

    ChrSetPos(0x00FE, -38990, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -39650, 0, 123650, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0034 offset: 0x41D7
@scena.Code('func_34_41D7')
def func_34_41D7():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(1300)

    ChrSetPos(0x00FE, -38990, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -41390, 0, 123470, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0035 offset: 0x421D
@scena.Code('func_35_421D')
def func_35_421D():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(1700)

    ChrSetPos(0x00FE, -38990, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -35900, 0, 124730, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0036 offset: 0x4263
@scena.Code('func_36_4263')
def func_36_4263():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(2100)

    ChrSetPos(0x00FE, -38990, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -37400, 0, 125010, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0037 offset: 0x42A9
@scena.Code('func_37_42A9')
def func_37_42A9():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(2500)

    ChrSetPos(0x00FE, -38990, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -39880, 0, 125020, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0038 offset: 0x42EF
@scena.Code('func_38_42EF')
def func_38_42EF():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 3)
    Sleep(2900)

    ChrSetPos(0x00FE, -38990, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -41810, 0, 124870, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0039 offset: 0x4335
@scena.Code('func_39_4335')
def func_39_4335():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 1)
    Sleep(3200)

    ChrSetPos(0x00FE, -38450, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -38500, 0, 125940, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 0)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x003A offset: 0x437B
@scena.Code('func_3A_437B')
def func_3A_437B():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 1)
    Sleep(3550)

    ChrSetPos(0x00FE, -38590, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -38020, 0, 128039, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 0)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x003B offset: 0x43C1
@scena.Code('func_3B_43C1')
def func_3B_43C1():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x00FE, 1)
    Sleep(3600)

    ChrSetPos(0x00FE, -39990, 0, 134600, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -39900, 0, 128009, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 0)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x003C offset: 0x4407
@scena.Code('func_3C_4407')
def func_3C_4407():
    ChrSetChipByIndex(0x00FE, 24)
    ChrWalkTo(0x00FE, -38050, 0, 119870, 5000, 0x00)

    Return()

# id: 0x003D offset: 0x4421
@scena.Code('func_3D_4421')
def func_3D_4421():
    Sleep(30)

    ChrWalkTo(0x00FE, -35350, 0, 118580, 5000, 0x00)

    Return()

# id: 0x003E offset: 0x443B
@scena.Code('func_3E_443B')
def func_3E_443B():
    Sleep(20)

    ChrWalkTo(0x00FE, -41460, 0, 118040, 5000, 0x00)

    Return()

# id: 0x003F offset: 0x4455
@scena.Code('func_3F_4455')
def func_3F_4455():
    Sleep(20)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 270, 0)
    ChrWalkTo(0x00FE, -33960, 0, 117320, 5000, 0x00)

    Return()

# id: 0x0040 offset: 0x447B
@scena.Code('func_40_447B')
def func_40_447B():
    Sleep(40)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 270, 0)
    ChrWalkTo(0x00FE, -33960, 0, 117320, 5000, 0x00)

    Return()

# id: 0x0041 offset: 0x44A1
@scena.Code('func_41_44A1')
def func_41_44A1():
    Sleep(50)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 270, 0)
    ChrWalkTo(0x00FE, -34440, 0, 118340, 5000, 0x00)

    Return()

# id: 0x0042 offset: 0x44C7
@scena.Code('func_42_44C7')
def func_42_44C7():
    Sleep(40)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 270, 0)
    ChrWalkTo(0x00FE, -34440, 0, 118340, 5000, 0x00)

    Return()

# id: 0x0043 offset: 0x44ED
@scena.Code('func_43_44ED')
def func_43_44ED():
    Sleep(30)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 270, 0)
    ChrWalkTo(0x00FE, -34920, 0, 119410, 5000, 0x00)

    Return()

# id: 0x0044 offset: 0x4513
@scena.Code('func_44_4513')
def func_44_4513():
    Sleep(80)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 270, 0)
    ChrWalkTo(0x00FE, -34920, 0, 119410, 5000, 0x00)

    Return()

# id: 0x0045 offset: 0x4539
@scena.Code('func_45_4539')
def func_45_4539():
    Sleep(20)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 270, 0)
    ChrWalkTo(0x00FE, -35670, 0, 119930, 5000, 0x00)

    Return()

# id: 0x0046 offset: 0x455F
@scena.Code('func_46_455F')
def func_46_455F():
    Sleep(40)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 270, 0)
    ChrWalkTo(0x00FE, -35670, 0, 119930, 5000, 0x00)

    Return()

# id: 0x0047 offset: 0x4585
@scena.Code('func_47_4585')
def func_47_4585():
    Sleep(10)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 90, 0)
    ChrWalkTo(0x00FE, -42680, 0, 117030, 5000, 0x00)

    Return()

# id: 0x0048 offset: 0x45AB
@scena.Code('func_48_45AB')
def func_48_45AB():
    Sleep(50)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 90, 0)
    ChrWalkTo(0x00FE, -42680, 0, 117030, 5000, 0x00)

    Return()

# id: 0x0049 offset: 0x45D1
@scena.Code('func_49_45D1')
def func_49_45D1():
    Sleep(80)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 90, 0)
    ChrWalkTo(0x00FE, -42130, 0, 117940, 5000, 0x00)

    Return()

# id: 0x004A offset: 0x45F7
@scena.Code('func_4A_45F7')
def func_4A_45F7():
    Sleep(20)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 90, 0)
    ChrWalkTo(0x00FE, -42130, 0, 117940, 5000, 0x00)

    Return()

# id: 0x004B offset: 0x461D
@scena.Code('func_4B_461D')
def func_4B_461D():
    Sleep(40)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 90, 0)
    ChrWalkTo(0x00FE, -41800, 0, 118640, 5000, 0x00)

    Return()

# id: 0x004C offset: 0x4643
@scena.Code('func_4C_4643')
def func_4C_4643():
    Sleep(90)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 90, 0)
    ChrWalkTo(0x00FE, -41800, 0, 118640, 5000, 0x00)

    Return()

# id: 0x004D offset: 0x4669
@scena.Code('func_4D_4669')
def func_4D_4669():
    Sleep(80)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 90, 0)
    ChrWalkTo(0x00FE, -41230, 0, 119600, 5000, 0x00)

    Return()

# id: 0x004E offset: 0x468F
@scena.Code('func_4E_468F')
def func_4E_468F():
    Sleep(60)

    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 90, 0)
    ChrWalkTo(0x00FE, -41230, 0, 119600, 5000, 0x00)

    Return()

# id: 0x004F offset: 0x46B5
@scena.Code('func_4F_46B5')
def func_4F_46B5():
    Sleep(20)

    ChrSetChipByIndex(0x00FE, 3)
    ChrWalkTo(0x00FE, -36860, 0, 120240, 5000, 0x00)

    Return()

# id: 0x0050 offset: 0x46D4
@scena.Code('func_50_46D4')
def func_50_46D4():
    Sleep(40)

    ChrSetChipByIndex(0x00FE, 3)
    ChrWalkTo(0x00FE, -37840, 0, 120580, 5000, 0x00)

    Return()

# id: 0x0051 offset: 0x46F3
@scena.Code('func_51_46F3')
def func_51_46F3():
    Sleep(50)

    ChrSetChipByIndex(0x00FE, 3)
    ChrWalkTo(0x00FE, -38860, 0, 120530, 5000, 0x00)

    Return()

# id: 0x0052 offset: 0x4712
@scena.Code('func_52_4712')
def func_52_4712():
    Sleep(60)

    ChrSetChipByIndex(0x00FE, 3)
    ChrWalkTo(0x00FE, -39850, 0, 120350, 5000, 0x00)

    Return()

# id: 0x0053 offset: 0x4731
@scena.Code('func_53_4731')
def func_53_4731():
    Sleep(50)

    ChrSetChipByIndex(0x00FE, 3)
    ChrWalkTo(0x00FE, -36860, 0, 120240, 5000, 0x00)

    Return()

# id: 0x0054 offset: 0x4750
@scena.Code('func_54_4750')
def func_54_4750():
    Sleep(80)

    ChrSetChipByIndex(0x00FE, 3)
    ChrWalkTo(0x00FE, -37840, 0, 120580, 5000, 0x00)

    Return()

# id: 0x0055 offset: 0x476F
@scena.Code('func_55_476F')
def func_55_476F():
    Sleep(10)

    ChrSetChipByIndex(0x00FE, 3)
    ChrWalkTo(0x00FE, -38860, 0, 120530, 5000, 0x00)

    Return()

# id: 0x0056 offset: 0x478E
@scena.Code('func_56_478E')
def func_56_478E():
    Sleep(90)

    ChrSetChipByIndex(0x00FE, 3)
    ChrWalkTo(0x00FE, -39850, 0, 120350, 5000, 0x00)

    Return()

# id: 0x0057 offset: 0x47AD
@scena.Code('func_57_47AD')
def func_57_47AD():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -34880, 0, 119870, 270)
    Sleep(200)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -32360, 0, 119050, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 315, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0058 offset: 0x4817
@scena.Code('func_58_4817')
def func_58_4817():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -33980, 0, 120510, 270)
    Sleep(400)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -30880, 0, 120220, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 90, 0)
    ChrSetChipByIndex(0x00FE, 27)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0059 offset: 0x4881
@scena.Code('func_59_4881')
def func_59_4881():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -34870, 0, 121180, 225)
    Sleep(500)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -32770, 0, 122700, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 225, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x005A offset: 0x48EB
@scena.Code('func_5A_48EB')
def func_5A_48EB():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -34390, 0, 121970, 225)
    Sleep(400)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -30610, 250, 124400, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 270, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x005B offset: 0x4955
@scena.Code('func_5B_4955')
def func_5B_4955():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -35560, 0, 121900, 225)
    Sleep(300)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -30670, 250, 127190, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 135, 0)
    ChrSetChipByIndex(0x00FE, 27)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x005C offset: 0x49BF
@scena.Code('func_5C_49BF')
def func_5C_49BF():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -35070, 0, 123090, 225)
    Sleep(800)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -34040, 0, 126930, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 45, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x005D offset: 0x4A29
@scena.Code('func_5D_4A29')
def func_5D_4A29():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -33590, 0, 121760, 225)
    Sleep(200)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -29470, 250, 125310, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 45, 0)
    ChrSetChipByIndex(0x00FE, 27)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x005E offset: 0x4A93
@scena.Code('func_5E_4A93')
def func_5E_4A93():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -34560, 0, 123170, 225)
    Sleep(400)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -30310, 250, 127840, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 0, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x005F offset: 0x4AFD
@scena.Code('func_5F_4AFD')
def func_5F_4AFD():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -41410, 0, 119170, 90)
    Sleep(100)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -44210, 0, 117600, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 225, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0060 offset: 0x4B67
@scena.Code('func_60_4B67')
def func_60_4B67():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -42020, 0, 120000, 90)
    Sleep(500)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -46380, 0, 119590, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 225, 0)
    ChrSetChipByIndex(0x00FE, 27)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0061 offset: 0x4BD1
@scena.Code('func_61_4BD1')
def func_61_4BD1():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -41330, 0, 120560, 135)
    Sleep(800)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -44450, 0, 119820, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 45, 0)
    ChrSetChipByIndex(0x00FE, 27)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0062 offset: 0x4C3B
@scena.Code('func_62_4C3B')
def func_62_4C3B():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -42310, 0, 121240, 135)
    Sleep(200)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -47450, 0, 121690, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 270, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0063 offset: 0x4CA5
@scena.Code('func_63_4CA5')
def func_63_4CA5():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -40800, 0, 121420, 135)
    Sleep(400)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -43440, 0, 122980, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 135, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0064 offset: 0x4D0F
@scena.Code('func_64_4D0F')
def func_64_4D0F():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -41440, 0, 122490, 135)
    Sleep(900)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -46070, 250, 125390, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 315, 0)
    ChrSetChipByIndex(0x00FE, 27)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0065 offset: 0x4D79
@scena.Code('func_65_4D79')
def func_65_4D79():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -42570, 0, 119320, 90)
    Sleep(800)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -49300, 0, 122100, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 270, 0)
    ChrSetChipByIndex(0x00FE, 27)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0066 offset: 0x4DE3
@scena.Code('func_66_4DE3')
def func_66_4DE3():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -42820, 0, 120840, 135)
    Sleep(600)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -48780, 250, 125590, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 180, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0067 offset: 0x4E4D
@scena.Code('func_67_4E4D')
def func_67_4E4D():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -37210, 0, 121610, 225)
    Sleep(200)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -35240, 0, 125600, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 135, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0068 offset: 0x4EB7
@scena.Code('func_68_4EB7')
def func_68_4EB7():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -37130, 0, 122850, 225)
    Sleep(400)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -33350, 0, 124670, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 45, 0)
    ChrSetChipByIndex(0x00FE, 27)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0069 offset: 0x4F21
@scena.Code('func_69_4F21')
def func_69_4F21():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -38020, 0, 122240, 180)
    Sleep(500)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -36960, 0, 125620, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 180, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x006A offset: 0x4F8B
@scena.Code('func_6A_4F8B')
def func_6A_4F8B():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -37880, 0, 123820, 180)
    Sleep(600)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -36270, 0, 128990, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 0, 0)
    ChrSetChipByIndex(0x00FE, 27)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x006B offset: 0x4FF5
@scena.Code('func_6B_4FF5')
def func_6B_4FF5():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -38840, 0, 122190, 180)
    Sleep(500)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -42380, 0, 125390, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 315, 0)
    ChrSetChipByIndex(0x00FE, 27)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x006C offset: 0x505F
@scena.Code('func_6C_505F')
def func_6C_505F():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -39210, 0, 123540, 180)
    Sleep(800)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -41140, 0, 127160, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 0, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x006D offset: 0x50C9
@scena.Code('func_6D_50C9')
def func_6D_50C9():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -39510, 0, 121560, 135)
    Sleep(100)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -42200, 0, 123740, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 270, 0)
    ChrSetChipByIndex(0x00FE, 27)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x006E offset: 0x5133
@scena.Code('func_6E_5133')
def func_6E_5133():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -40050, 0, 122630, 135)
    Sleep(900)

    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_7C(0, 200, 3000, 100)
    ChrJumpTo(0x00FE, -43690, 0, 127730, 4000, 4000)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetDirection(0x00FE, 135, 0)
    ChrSetChipByIndex(0x00FE, 19)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x006F offset: 0x519D
@scena.Code('func_6F_519D')
def func_6F_519D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_51C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_51B5',
    )

    PlaySE(521, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_51B5(): pass

    label('loc_51B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_51C4',
    )

    PlaySE(524, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_51C4(): pass

    label('loc_51C4')

    Yield()

    Jump('func_6F_519D')

    def _loc_51C8(): pass

    label('loc_51C8')

    Return()

# id: 0x0070 offset: 0x51C9
@scena.Code('func_70_51C9')
def func_70_51C9():
    ChrSetChipByIndex(0x0028, 8)
    ChrSetChipByIndex(0x0029, 8)
    ChrSetChipByIndex(0x002A, 8)
    ChrSetChipByIndex(0x002B, 8)
    ChrSetChipByIndex(0x002C, 8)
    ChrSetChipByIndex(0x002D, 8)
    ChrSetChipByIndex(0x002E, 8)
    ChrSetChipByIndex(0x002F, 8)
    ChrSetChipByIndex(0x0030, 13)
    ChrSetChipByIndex(0x0031, 13)
    ChrSetChipByIndex(0x0032, 13)
    ChrSetChipByIndex(0x0033, 13)
    ChrSetChipByIndex(0x0034, 13)
    ChrSetChipByIndex(0x0035, 13)
    ChrSetChipByIndex(0x0036, 13)
    ChrSetChipByIndex(0x0037, 13)
    ChrSetChipByIndex(0x0038, 10)
    ChrSetChipByIndex(0x0039, 10)
    ChrSetChipByIndex(0x003A, 10)
    ChrSetChipByIndex(0x003B, 10)
    ChrSetPos(0x0028, -35530, 0, 97120, 0)
    ChrSetPos(0x0029, -36530, 0, 97120, 0)
    ChrSetPos(0x002A, -37530, 0, 97120, 0)
    ChrSetPos(0x002B, -38530, 0, 97120, 0)
    ChrSetPos(0x002C, -39530, 0, 97120, 0)
    ChrSetPos(0x002D, -40530, 0, 97120, 0)
    ChrSetPos(0x002E, -41530, 0, 97120, 0)
    ChrSetPos(0x002F, -42530, 0, 97120, 0)
    ChrSetPos(0x0030, -35530, 0, 95750, 0)
    ChrSetPos(0x0031, -36530, 0, 95750, 0)
    ChrSetPos(0x0032, -37530, 0, 95750, 0)
    ChrSetPos(0x0033, -38530, 0, 95750, 0)
    ChrSetPos(0x0034, -39530, 0, 95750, 0)
    ChrSetPos(0x0035, -40530, 0, 95750, 0)
    ChrSetPos(0x0036, -41530, 0, 95750, 0)
    ChrSetPos(0x0037, -42530, 0, 95750, 0)
    ChrSetPos(0x0038, -35000, 500, 92930, 0)
    ChrSetPos(0x0039, -37800, 500, 92930, 0)
    ChrSetPos(0x003A, -40200, 500, 92930, 0)
    ChrSetPos(0x003B, -42600, 500, 92930, 0)
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
    ChrSetFlags(0x0038, 0x0004)
    ChrSetFlags(0x0039, 0x0004)
    ChrSetFlags(0x003A, 0x0004)
    ChrSetFlags(0x003B, 0x0004)
    ChrSetFlags(0x003C, 0x0004)
    ChrSetFlags(0x003D, 0x0004)
    ChrSetFlags(0x003E, 0x0004)
    ChrSetFlags(0x003F, 0x0004)
    ChrSetFlags(0x0040, 0x0004)
    ChrSetFlags(0x0038, 0x0800)
    ChrSetFlags(0x0039, 0x0800)
    ChrSetFlags(0x003A, 0x0800)
    ChrSetFlags(0x003B, 0x0800)

    @scena.Lambda('lambda_542C')
    def lambda_542C():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_542C)

    Sleep(10)

    @scena.Lambda('lambda_5447')
    def lambda_5447():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5447)

    Sleep(10)

    @scena.Lambda('lambda_5462')
    def lambda_5462():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_5462)

    Sleep(10)

    @scena.Lambda('lambda_547D')
    def lambda_547D():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_547D)

    Sleep(10)

    @scena.Lambda('lambda_5498')
    def lambda_5498():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_5498)

    Sleep(10)

    @scena.Lambda('lambda_54B3')
    def lambda_54B3():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_54B3)

    Sleep(10)

    @scena.Lambda('lambda_54CE')
    def lambda_54CE():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x002E, 0x0001, lambda_54CE)

    Sleep(10)

    @scena.Lambda('lambda_54E9')
    def lambda_54E9():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x002F, 0x0001, lambda_54E9)

    Sleep(100)

    @scena.Lambda('lambda_5504')
    def lambda_5504():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0030, 0x0001, lambda_5504)

    Sleep(10)

    @scena.Lambda('lambda_551F')
    def lambda_551F():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_551F)

    Sleep(10)

    @scena.Lambda('lambda_553A')
    def lambda_553A():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_553A)

    Sleep(10)

    @scena.Lambda('lambda_5555')
    def lambda_5555():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_5555)

    Sleep(10)

    @scena.Lambda('lambda_5570')
    def lambda_5570():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0034, 0x0001, lambda_5570)

    Sleep(10)

    @scena.Lambda('lambda_558B')
    def lambda_558B():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0035, 0x0001, lambda_558B)

    Sleep(10)

    @scena.Lambda('lambda_55A6')
    def lambda_55A6():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0036, 0x0001, lambda_55A6)

    Sleep(10)

    @scena.Lambda('lambda_55C1')
    def lambda_55C1():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0037, 0x0001, lambda_55C1)

    Sleep(500)

    @scena.Lambda('lambda_55DC')
    def lambda_55DC():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0038, 0x0001, lambda_55DC)

    Sleep(50)

    @scena.Lambda('lambda_55F7')
    def lambda_55F7():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_55F7)

    Sleep(50)

    @scena.Lambda('lambda_5612')
    def lambda_5612():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_5612)

    Sleep(50)

    @scena.Lambda('lambda_562D')
    def lambda_562D():
        OP_94(0x00, 0x00FE, 0x0000, 0x00003E80, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x003B, 0x0001, lambda_562D)

    WaitForThreadExit(0x003B, 0x0001)
    ChrSetChipByIndex(0x0038, 9)
    ChrSetChipByIndex(0x0039, 9)
    ChrSetChipByIndex(0x003A, 9)
    ChrSetChipByIndex(0x003B, 9)
    CreateThread(0x0038, 0x02, 0x00, func_71_5673)
    CreateThread(0x0039, 0x02, 0x00, func_71_5673)
    CreateThread(0x003A, 0x02, 0x00, func_71_5673)
    CreateThread(0x003B, 0x02, 0x00, func_71_5673)

    Return()

# id: 0x0071 offset: 0x5673
@scena.Code('func_71_5673')
def func_71_5673():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5688',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_71_5673')

    def _loc_5688(): pass

    label('loc_5688')

    Return()

# id: 0x0072 offset: 0x5689
@scena.Code('func_72_5689')
def func_72_5689():
    PlaySE(314, 0x01, 0x28)
    Sleep(400)

    OP_24(0x013A, 0x2D)
    Sleep(400)

    OP_24(0x013A, 0x32)
    Sleep(400)

    OP_24(0x013A, 0x37)
    Sleep(400)

    OP_24(0x013A, 0x3C)
    Sleep(400)

    OP_24(0x013A, 0x41)
    Sleep(400)

    OP_24(0x013A, 0x46)
    Sleep(400)

    OP_24(0x013A, 0x4B)
    Sleep(400)

    OP_24(0x013A, 0x50)
    Sleep(400)

    OP_24(0x013A, 0x55)
    Sleep(400)

    OP_24(0x013A, 0x5A)
    Sleep(400)

    OP_24(0x013A, 0x5F)
    Sleep(400)

    OP_24(0x013A, 0x64)

    Return()

# id: 0x0073 offset: 0x56FB
@scena.Code('func_73_56FB')
def func_73_56FB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 1, 0x2039)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_5708',
    )

    Return()

    def _loc_5708(): pass

    label('loc_5708')

    EventBegin(0x00)
    Fade(1000)
    CameraMove(-38400, 0, 96420, 0)
    OP_67(0, 7590, -10000, 0)
    CameraSetDistance(2390, 0)
    OP_6C(45000, 0)
    OP_6E(329, 0)
    ChrSetPos(0x0101, -39570, 0, 96480, 0)
    ChrSetPos(0x0102, -38490, 0, 96410, 0)
    ChrSetPos(0x00F8, -39910, 0, 95110, 0)
    ChrSetPos(0x00F9, -38480, 0, 95200, 0)
    Call(0, 0x0005)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010380114V#1020F#6P那、那是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380115V#1046F#2P……赶快！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_57EE')
    def lambda_57EE():
        ChrWalkTo(0x00FE, -38930, 0, 122520, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_57EE)

    Sleep(100)

    @scena.Lambda('lambda_580E')
    def lambda_580E():
        ChrWalkTo(0x00FE, -37650, 0, 122480, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_580E)

    Sleep(100)

    @scena.Lambda('lambda_582E')
    def lambda_582E():
        ChrWalkTo(0x00FE, -38840, 0, 121330, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_582E)

    Sleep(100)

    @scena.Lambda('lambda_584E')
    def lambda_584E():
        ChrWalkTo(0x00FE, -37430, 0, 121300, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_584E)

    Sleep(500)

    Fade(500)
    CameraMove(-38910, 0, 122270, 0)
    OP_67(0, 7900, -10000, 0)
    CameraSetDistance(2460, 0)
    OP_6C(134000, 0)
    OP_6E(383, 0)

    @scena.Lambda('lambda_58B0')
    def lambda_58B0():
        CameraMove(-37600, 0, 121220, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_58B0)

    @scena.Lambda('lambda_58C8')
    def lambda_58C8():
        OP_67(0, 6850, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_58C8)

    @scena.Lambda('lambda_58E0')
    def lambda_58E0():
        CameraSetDistance(2040, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_58E0)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 315, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrSetDirection(0x0102, 45, 400)
    WaitForThreadExit(0x00F8, 0x0001)
    ChrSetDirection(0x00F8, 270, 400)
    WaitForThreadExit(0x00F9, 0x0001)
    ChrSetDirection(0x00F9, 90, 400)
    WaitForThreadExit(0x0101, 0x0003)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5956',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380116V#057F#5P这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_59C1')

    def _loc_5956(): pass

    label('loc_5956')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_598D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380117V#023F#5P这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_59C1')

    def _loc_598D(): pass

    label('loc_598D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_59C1',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380118V#072F#5P……这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_59C1(): pass

    label('loc_59C1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5A05',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380119V#065F#5P啊啊……\n',
            '得、得包扎一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A82')

    def _loc_5A05(): pass

    label('loc_5A05')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5A45',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380120V#072F#5P看来……\n',
            '得包扎一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A82')

    def _loc_5A45(): pass

    label('loc_5A45')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5A82',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380121V#022F#5P看来……\n',
            '得包扎一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5A82(): pass

    label('loc_5A82')

    ChrTalk(
        0x0041,
        (
            '#2420380122V#6P没、没这个必要……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B08',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5B46')

    def _loc_5B08(): pass

    label('loc_5B08')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B2F',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5B46')

    def _loc_5B2F(): pass

    label('loc_5B2F')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_5B46(): pass

    label('loc_5B46')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B72',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5BB0')

    def _loc_5B72(): pass

    label('loc_5B72')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B99',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5BB0')

    def _loc_5B99(): pass

    label('loc_5B99')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_5BB0(): pass

    label('loc_5BB0')

    Sleep(1000)

    @scena.Lambda('lambda_5BBB')
    def lambda_5BBB():
        CameraMove(-37860, 0, 122950, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5BBB)

    @scena.Lambda('lambda_5BD3')
    def lambda_5BD3():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5BD3)

    Sleep(50)

    @scena.Lambda('lambda_5BE6')
    def lambda_5BE6():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5BE6)

    Sleep(50)

    @scena.Lambda('lambda_5BF9')
    def lambda_5BF9():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_5BF9)

    Sleep(50)

    ChrSetDirection(0x00F9, 0, 400)
    WaitForThreadExit(0x0101, 0x0003)
    OP_9E(0x0041, 15, 0, 300, 3000)
    Fade(500)
    LoadChip('ED6_DT07/CH00334._CH', 'ED6_DT07/CH00334P._CP', 0)
    ChrSetChipByIndex(0x0041, 0)
    ChrSetSubChip(0x0041, 3)
    ChrSetFlags(0x0041, 0x0001)
    ChrSetPos(0x0041, -38200, 0, 125200, 180)
    OP_0D()
    OP_9E(0x0041, 15, 0, 300, 3000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010380123V#1020F#2P没、没问题吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0041,
        (
            '#2420380124V#6P你们是游击士吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0041,
        (
            '#2420380125V#6P刚才……\n',
            '『结社』的执行者们\n',
            '已经通过这里了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0041,
        (
            '#2420380126V#6P他们的目标……\n',
            '……似乎是格兰赛尔城……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380127V#1042F#5P果然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0041,
        (
            '#2420380128V#6P其余的敌方部队\n',
            '好象控制着市区……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0041,
        (
            '#2420380129V#6P……拜托……请救救市区和王城……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0041, 15, 0, 300, 3000)
    Fade(500)
    PlaySE(524, 0x00, 0x64)
    ChrClearFlags(0x0041, 0x0001)
    ChrSetPos(0x0041, -38950, 0, 125450, 180)
    ChrSetSubChip(0x0041, 0)
    ChrSetChipByIndex(0x0041, 20)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_5E15')
    def lambda_5E15():
        CameraMove(-37540, 0, 121320, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5E15)

    ChrTurnDirection(0x0102, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020380130V#1042F#5P艾丝蒂尔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 600)

    ChrTalk(
        0x0101,
        (
            '#0010380131V#1002F嗯……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380132V#1005F虽然有点对不起士兵们，\n',
            '不过我们还是先追上去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-39120, 0, 123180, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -39120, 0, 123180, 0)
    ChrSetPos(0x0001, -39120, 0, 123180, 0)
    ChrSetPos(0x0002, -39120, 0, 123180, 0)
    ChrSetPos(0x0003, -39120, 0, 123180, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0407, 2, 0x203A))
    OP_28(0x009C, 0x01, 0x0002)
    OP_28(0x009C, 0x01, 0x0004)
    OP_28(0x009C, 0x01, 0x0008)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0074 offset: 0x5F6F
@scena.Code('func_74_5F6F')
def func_74_5F6F():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010260967V#1003F（这边不是近道！\n',
            '……必须一直向东才行！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0075 offset: 0x5FCE
@scena.Code('func_75_5FCE')
def func_75_5FCE():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　王都格兰赛尔',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0076 offset: 0x6011
@scena.Code('func_76_6011')
def func_76_6011():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　格鲁纳门　　　１６５塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0077 offset: 0x6062
@scena.Code('func_77_6062')
def func_77_6062():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　圣海姆门　　　２２８塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

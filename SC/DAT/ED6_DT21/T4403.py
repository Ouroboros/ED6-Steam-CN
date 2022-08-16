import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4403_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4403   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4403.x'
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
        ('ED6_DT27/CH04512._CH', 'ED6_DT27/CH04512P._CP'),
        ('ED6_DT27/CH03120._CH', 'ED6_DT27/CH03120P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03090._CH', 'ED6_DT27/CH03090P._CP'),
        ('ED6_DT26/CH20287._CH', 'ED6_DT26/CH20287P._CP'),
        ('ED6_DT27/CH03590._CH', 'ED6_DT27/CH03590P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT26/CH20303._CH', 'ED6_DT26/CH20303P._CP'),
        ('ED6_DT26/CH20308._CH', 'ED6_DT26/CH20308P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT27/CH04586._CH', 'ED6_DT27/CH04586P._CP'),
        ('ED6_DT27/CH04584._CH', 'ED6_DT27/CH04584P._CP'),
        ('ED6_DT26/CH20309._CH', 'ED6_DT26/CH20309P._CP'),
        ('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP'),
        ('ED6_DT27/CH04120._CH', 'ED6_DT27/CH04120P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT27/CH04124._CH', 'ED6_DT27/CH04124P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT26/CH20447._CH', 'ED6_DT26/CH20447P._CP'),
        ('ED6_DT09/CH10060._CH', 'ED6_DT09/CH10060P._CP'),
        ('ED6_DT09/CH10061._CH', 'ED6_DT09/CH10061P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
        ('ED6_DT26/CH20293._CH', 'ED6_DT26/CH20293P._CP'),
        ('ED6_DT26/CH20294._CH', 'ED6_DT26/CH20294P._CP'),
        ('ED6_DT26/CH20302._CH', 'ED6_DT26/CH20302P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP'),
        ('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP'),
        ('ED6_DT27/CH04121._CH', 'ED6_DT27/CH04121P._CP'),
        ('ED6_DT26/CH20286._CH', 'ED6_DT26/CH20286P._CP'),
        ('ED6_DT27/CH04511._CH', 'ED6_DT27/CH04511P._CP'),
        ('ED6_DT27/CH04516._CH', 'ED6_DT27/CH04516P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
    ]

# id: 0x10001 offset: 0x232
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '军犬',
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
            name                = '军犬',
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
            name                = '军犬',
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
            name                = '凯诺娜',
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
            name                = '杜南公爵',
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
            name                = '雪拉扎德',
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
            name                = '阿加特',
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
            name                = '奥利维尔',
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
            name                = '科洛丝',
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
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '金',
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
            name                = '亚妮拉丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '歼灭天使玲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 45,
            chipIndex           = 45,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '希德中校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '管家菲利普',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '奈尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '玲的爸爸',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '玲的妈妈',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '亲卫队队员',
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
            name                = '亲卫队队员',
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
            name                = '亲卫队队员',
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
            name                = '亲卫队队员',
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
            name                = '亲卫队队员',
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
            name                = '亲卫队队员',
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
            name                = '亲卫队队员',
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
            name                = '亲卫队队员',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '士兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
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
            name                = '导力战车『奥尔杰尤』',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0189,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '榴弹炮',
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
            name                = '榴弹炮',
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
            name                = '榴弹炮',
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
            name                = '帕蒂尔·玛蒂尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0189,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·西街区',
            x                   = 60310,
            z                   = 0,
            y                   = -1230,
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
            name                = '王都格兰赛尔·码头北',
            x                   = -9950,
            z                   = 0,
            y                   = 71270,
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

# id: 0x10002 offset: 0x7F2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '侵蚀狼犬',
            x           = 9400,
            z           = 0,
            y           = -1180,
            word_0C     = 0x00B4,
            word_0E     = 0x001E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03DE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '侵蚀狼犬',
            x           = -15030,
            z           = 0,
            y           = -9320,
            word_0C     = 0x00B4,
            word_0E     = 0x001E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03DE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '侵蚀狼犬',
            x           = -11830,
            z           = 0,
            y           = 6760,
            word_0C     = 0x00B4,
            word_0E     = 0x001E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03DE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '侵蚀狼犬',
            x           = -24660,
            z           = 0,
            y           = -820,
            word_0C     = 0x00B4,
            word_0E     = 0x001E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03DE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x862
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 27000,
            y           = -2000,
            z           = -11000,
            range       = 29500,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000251C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -18200,
            y           = -2000,
            z           = 32700,
            range       = -6000,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000878C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000F,
        ),
    )

# id: 0x10004 offset: 0x8A2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x8A2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_8C2',
    )

    ChrSetFlags(0x0036, 0x0080)
    ChrSetFlags(0x0037, 0x0080)
    ChrSetFlags(0x0038, 0x0080)
    ChrSetFlags(0x0039, 0x0080)

    def _loc_8C2(): pass

    label('loc_8C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_8DE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x71),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_10_135C)

    def _loc_8DE(): pass

    label('loc_8DE')

    Return()

# id: 0x0001 offset: 0x8DF
@scena.Code('func_01_8DF')
def func_01_8DF():
    OP_16(0x02, 4000, -116000, -104000, 2293869)
    PlaySE(453, 0x00, 0x64)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_1C(0x02, 0x00, 0x003C)

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x45E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_98E',
    )

    LoadChip('ED6_DT27/CH04590._CH', 'ED6_DT27/CH04590P._CP', 49)
    LoadChip('ED6_DT27/CH04591._CH', 'ED6_DT27/CH04591P._CP', 50)
    LoadChip('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP', 51)
    LoadChip('ED6_DT07/CH00021._CH', 'ED6_DT07/CH00021P._CP', 53)
    LoadChip('ED6_DT07/CH00051._CH', 'ED6_DT07/CH00051P._CP', 54)
    LoadChip('ED6_DT07/CH00031._CH', 'ED6_DT07/CH00031P._CP', 55)
    LoadChip('ED6_DT07/CH00041._CH', 'ED6_DT07/CH00041P._CP', 56)
    LoadChip('ED6_DT07/CH00061._CH', 'ED6_DT07/CH00061P._CP', 57)
    LoadChip('ED6_DT07/CH00071._CH', 'ED6_DT07/CH00071P._CP', 58)
    LoadChip('ED6_DT27/CH03091._CH', 'ED6_DT27/CH03091P._CP', 59)

    def _loc_98E(): pass

    label('loc_98E')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x44E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9A3',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_9A3(): pass

    label('loc_9A3')

    Return()

# id: 0x0002 offset: 0x9A4
@scena.Code('func_02_9A4')
def func_02_9A4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9B9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_9A4')

    def _loc_9B9(): pass

    label('loc_9B9')

    Return()

# id: 0x0003 offset: 0x9BA
@scena.Code('func_03_9BA')
def func_03_9BA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            Expr.Return,
        ),
        'loc_9C2',
    )

    Return()

    def _loc_9C2(): pass

    label('loc_9C2')

    Call(0, 0x0004)
    Call(0, 0x0005)

    Return()

# id: 0x0004 offset: 0x9CB
@scena.Code('func_04_9CB')
def func_04_9CB():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9E7',
    )

    Call(0, 0x003B)
    FadeIn(0, 0)

    def _loc_9E7(): pass

    label('loc_9E7')

    Fade(1000)
    ChrSetPos(0x0101, 28170, 0, -970, 270)
    ChrSetPos(0x00F7, 28170, 0, 530, 270)
    ChrSetPos(0x0109, 29480, 0, -250, 270)
    CameraMove(28120, 0, -40, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(1850, 0)
    OP_6C(315000, 0)
    OP_6E(357, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A8D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270361V#052F唔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AAC')

    def _loc_A8D(): pass

    label('loc_A8D')

    ChrTalk(
        0x0103,
        (
            '#0030270362V#023F哈……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AAC(): pass

    label('loc_AAC')

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0008, 8490, 0, -970, 90)
    ChrSetPos(0x0009, 8380, 0, 530, 90)
    ChrSetPos(0x000A, 6950, 0, -250, 90)
    CreateThread(0x0008, 0x00, 0x00, func_02_9A4)
    CreateThread(0x0009, 0x00, 0x00, func_02_9A4)
    CreateThread(0x000A, 0x00, 0x00, func_02_9A4)
    OP_20(0x000007D0)
    CameraMove(20000, 0, -550, 2000)
    CreateThread(0x0008, 0x01, 0x00, func_06_F12)
    Sleep(100)

    CreateThread(0x0009, 0x01, 0x00, func_07_F3B)
    Sleep(100)

    CreateThread(0x000A, 0x01, 0x00, func_08_F64)

    @scena.Lambda('lambda_0B3E')
    def lambda_0B3E():
        CameraMove(25120, 0, 240, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B3E)

    @scena.Lambda('lambda_0B56')
    def lambda_0B56():
        OP_67(0, 9180, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B56)

    @scena.Lambda('lambda_0B6E')
    def lambda_0B6E():
        CameraSetDistance(1990, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B6E)

    @scena.Lambda('lambda_0B7E')
    def lambda_0B7E():
        OP_6E(385, 1500)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_0B7E)

    PlayBGM(53)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 32)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0109, 35)
    ChrSetSubChip(0x0109, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BD7',
    )

    ChrSetChipByIndex(0x0106, 33)
    ChrSetSubChip(0x0106, 0)

    Jump('loc_BE1')

    def _loc_BD7(): pass

    label('loc_BD7')

    ChrSetChipByIndex(0x0103, 34)
    ChrSetSubChip(0x0103, 0)

    def _loc_BE1(): pass

    label('loc_BE1')

    OP_0D()
    Sleep(500)

    OP_62(0x0109, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0109,
        (
            '#0180270363V#1061F#4P好、好凶的\n',
            '狗狗啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270364V#1005F#5P特务兵的军用犬……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C97',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211674V#054F#2P……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CBB')

    def _loc_C97(): pass

    label('loc_C97')

    ChrTalk(
        0x0103,
        (
            '#0030211675V#024F#2P……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CBB(): pass

    label('loc_CBB')

    CreateThread(0x0008, 0x01, 0x00, func_09_F8D)
    Sleep(50)

    CreateThread(0x0009, 0x01, 0x00, func_0A_FC3)
    Sleep(50)

    CreateThread(0x000A, 0x01, 0x00, func_0B_FF9)

    @scena.Lambda('lambda_0CE0')
    def lambda_0CE0():
        CameraMove(26990, 0, 1000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0CE0)

    @scena.Lambda('lambda_0CF8')
    def lambda_0CF8():
        CameraSetDistance(1600, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0CF8)

    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0101, 0xFF)
    Battle(0x0000045B, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_D30'),
        (-1, 'loc_D35'),
    )

    def _loc_D30(): pass

    label('loc_D30')

    OP_B4(0x00)

    Jump('loc_D35')

    def _loc_D35(): pass

    label('loc_D35')

    Return()

# id: 0x0005 offset: 0xD36
@scena.Code('func_05_D36')
def func_05_D36():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Sleep(1000)

    CameraMove(28240, 0, -280, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 28170, 0, -970, 270)
    ChrSetPos(0x00F7, 28170, 0, 530, 270)
    ChrSetPos(0x0109, 29480, 0, -250, 270)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetChipByIndex(0x0109, 65535)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    FadeIn(2000, 0)
    CreateThread(0x0101, 0x01, 0x00, func_0C_102F)
    Sleep(100)

    CreateThread(0x00F7, 0x01, 0x00, func_0D_1067)
    Sleep(100)

    CreateThread(0x0109, 0x01, 0x00, func_0E_109F)
    WaitForThreadExit(0x0109, 0x0001)
    OP_0D()

    ChrTalk(
        0x0109,
        (
            '#0180270367V#1068F呼～吓一大跳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270368V#1060F不过『茶会』的会场\n',
            '看来是这儿没错了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270369V#1002F#1P嗯……是啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EC6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270370V#050F#5P好，慎重前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF2')

    def _loc_EC6(): pass

    label('loc_EC6')

    ChrTalk(
        0x0103,
        (
            '#0030270371V#022F#5P好，要慎重前进哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EF2(): pass

    label('loc_EF2')

    SetScenaFlags(ScenaFlag(0x02C7, 3, 0x163B))
    OP_28(0x008E, 0x01, 0x0002)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0037, 0x0080)
    ChrClearFlags(0x0038, 0x0080)
    ChrClearFlags(0x0039, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xF12
@scena.Code('func_06_F12')
def func_06_F12():
    ChrSetChipByIndex(0x00FE, 31)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x00FE, 22020, 0, -910, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0007 offset: 0xF3B
@scena.Code('func_07_F3B')
def func_07_F3B():
    ChrSetChipByIndex(0x00FE, 31)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x00FE, 22110, 0, 920, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0008 offset: 0xF64
@scena.Code('func_08_F64')
def func_08_F64():
    ChrSetChipByIndex(0x00FE, 31)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x00FE, 20660, 0, 470, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 30)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0009 offset: 0xF8D
@scena.Code('func_09_F8D')
def func_09_F8D():
    ChrSetChipByIndex(0x00FE, 31)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x00FE, 23900, 0, -1030, 6000, 0x00)
    ChrJumpTo(0x00FE, 27420, 0, -990, 1500, 8000)

    Return()

# id: 0x000A offset: 0xFC3
@scena.Code('func_0A_FC3')
def func_0A_FC3():
    ChrSetChipByIndex(0x00FE, 31)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x00FE, 23890, 0, 570, 6000, 0x00)
    ChrJumpTo(0x00FE, 27250, 0, 440, 1500, 8000)

    Return()

# id: 0x000B offset: 0xFF9
@scena.Code('func_0B_FF9')
def func_0B_FF9():
    ChrSetChipByIndex(0x00FE, 31)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x00FE, 22640, 0, 0, 6000, 0x00)
    ChrJumpTo(0x00FE, 25960, 0, -50, 1500, 8000)

    Return()

# id: 0x000C offset: 0x102F
@scena.Code('func_0C_102F')
def func_0C_102F():
    ChrSetDirection(0x00FE, 315, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x000D offset: 0x1067
@scena.Code('func_0D_1067')
def func_0D_1067():
    ChrSetDirection(0x00FE, 360, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 360, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x000E offset: 0x109F
@scena.Code('func_0E_109F')
def func_0E_109F():
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1000)

    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x000F offset: 0x10CB
@scena.Code('func_0F_10CB')
def func_0F_10CB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 4, 0x163C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_135B',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_121B',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1184',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270372V#052F等等、艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0106, 270, 400)

    ChrTalk(
        0x0106,
        (
            '#0050270373V#552F这栋建筑\n',
            '有人的气息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270374V#1002F真的……\n',
            '总之调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1218')

    def _loc_1184(): pass

    label('loc_1184')

    ChrTalk(
        0x0103,
        (
            '#0030270375V#023F等一下、艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030270376V#022F这栋建筑\n',
            '有人的气息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270374V#1002F真的……\n',
            '总之调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1218(): pass

    label('loc_1218')

    Jump('loc_1340')

    def _loc_121B(): pass

    label('loc_121B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12B5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270378V#1004F等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270379V#1002F这栋建筑\n',
            '有人的气息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0106, 270, 400)

    ChrTalk(
        0x0106,
        (
            '#0050270380V#552F哼……\n',
            '总之调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1340')

    def _loc_12B5(): pass

    label('loc_12B5')

    ChrTalk(
        0x0101,
        (
            '#0010270378V#1004F等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270379V#1002F这栋建筑\n',
            '有人的气息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030270383V#022F确实……\n',
            '总之调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1340(): pass

    label('loc_1340')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_135B(): pass

    label('loc_135B')

    Return()

# id: 0x0010 offset: 0x135C
@scena.Code('func_10_135C')
def func_10_135C():
    Call(0, 0x0011)
    Call(0, 0x0016)
    Call(0, 0x0017)

    Return()

# id: 0x0011 offset: 0x1369
@scena.Code('func_11_1369')
def func_11_1369():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1387',
    )

    Call(0, 0x003B)

    def _loc_1387(): pass

    label('loc_1387')

    FormationAddMember(ChrTable['尤莉亚上尉'], 0xF9, 0xFF)
    LoadEffect(0x00, 'monster\\ms30600d.eff')
    LoadEffect(0x01, 'monster\\ms30600b.eff')
    LoadEffect(0x02, 'monster\\ms30600a.eff')
    LoadEffect(0x03, 'battle\\\\btbomb00.eff')
    PlayEffect(0x00, 0x01, 0x002F, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x002F, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x03, 0x002F, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x04, 0x002F, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x05, 0x002F, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x06, 0x002F, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrClearFlags(0x002F, 0x0080)
    OP_72(0x0005, 0x0004)
    OP_A1(0x002F, 0x0005)
    ChrSetPos(0x002F, -11220, 0, 51980, 180)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000B, 0x0020)
    ChrClearFlags(0x000B, 0x0001)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -12500, 2000, 51890, 180)
    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_A1(0x0030, 0x0000)
    OP_A1(0x0031, 0x0001)
    OP_A1(0x0032, 0x0003)
    ChrSetPos(0x0030, 1540, 0, 3700, 90)
    ChrSetPos(0x0031, 1190, 0, -2000, 90)
    ChrSetPos(0x0032, -1450, 0, 8080, 45)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetFlags(0x001A, 0x0004)
    ChrSetFlags(0x001B, 0x0004)
    ChrSetBattleFlags(0x001A, 0x0020)
    ChrSetBattleFlags(0x001B, 0x0020)
    OP_89(0x001A, 1540, 750, 3700, 270)
    OP_89(0x001B, 1190, 750, -2000, 270)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrSetPos(0x010F, 4290, 0, 380, 270)
    ChrSetPos(0x001C, 5510, 0, -1750, 270)
    ChrSetPos(0x001D, 5700, 0, 520, 270)
    ChrSetPos(0x001E, 5710, 0, -3450, 270)
    ChrSetPos(0x001F, 5630, 0, 1960, 270)
    ChrSetPos(0x0020, 7090, 0, -1780, 270)
    ChrSetPos(0x0021, 7090, 0, -120, 270)

    @scena.Lambda('lambda_16C6')
    def lambda_16C6():
        OP_7C(50, 50, 3000, 100)
        Yield()

        Jump('lambda_16C6')

    DispatchAsync2(0x002F, 0x0003, lambda_16C6)

    PlaySE(271, 0x00, 0x64)
    PlaySE(272, 0x00, 0x64)
    ChrSetFlags(0x0036, 0x0080)
    ChrSetFlags(0x0037, 0x0080)
    ChrSetFlags(0x0038, 0x0080)
    ChrSetFlags(0x0039, 0x0080)
    CameraMove(-11130, 0, 7550, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(332000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_173C')
    def lambda_173C():
        OP_69(0x002F, 0)
        Yield()

        Jump('lambda_173C')

    DispatchAsync2(0x002F, 0x0002, lambda_173C)

    FadeIn(2000, 0)

    @scena.Lambda('lambda_1756')
    def lambda_1756():
        ChrMoveTo(0x00FE, -11220, 0, 3220, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002F, 0x0001, lambda_1756)

    @scena.Lambda('lambda_1771')
    def lambda_1771():
        ChrMoveTo(0x00FE, -12500, 2000, 40220, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1771)

    Sleep(1000)

    PlaySE(106, 0x00, 0x64)
    OP_B0(0x0005, 0x0F)
    OP_6F(0x0005, 371)
    OP_70(0x0005, 390)
    OP_73(0x0005)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrClearFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_17BB')
    def lambda_17BB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_17BB)

    @scena.Lambda('lambda_17CD')
    def lambda_17CD():
        ChrMoveTo(0x00FE, -12500, 2300, 3220, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_17CD)

    Sleep(2000)

    @scena.Lambda('lambda_17ED')
    def lambda_17ED():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_17ED)

    WaitForThreadExit(0x000B, 0x0002)

    ChrTalk(
        0x000B,
        (
            '#0610270502V#1181F#6P#30A呼呼……\n',
            '似乎完全分开了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270503V#1181F#6P#30A就这样将统治城的\n',
            '女王陛下抓走的话……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(7000)

    PlayEffect(0x03, 0xFF, 0x00FF, -11910, 0, -720, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(1045220557, 200, 2000, 100)
    Sleep(300)

    PlayEffect(0x03, 0xFF, 0x00FF, -9980, 0, -1310, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(1045220557, 200, 2000, 100)
    Sleep(500)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x002F, 0x0001)
    OP_23(0x0110)
    TerminateThread(0x002F, 0x03)
    TerminateThread(0x000B, 0x01)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    OP_20(0x00000000)
    Sleep(1000)

    @scena.Lambda('lambda_194A')
    def lambda_194A():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_194A)

    WaitForThreadExit(0x000B, 0x0002)
    OP_DC()

    ChrTalk(
        0x000B,
        (
            '#0610270504V#1185F#6P什……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 10)
    OP_73(0x0003)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 10)
    OP_73(0x0004)

    NpcTalk(
        0x010F,
        '女性的声音',
        (
            '#0100270505V嗯……\n',
            '看来赶上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x002F, 0x02)
    PlayBGM(116)
    Sleep(500)

    @scena.Lambda('lambda_19E0')
    def lambda_19E0():
        CameraMove(-6040, 0, 4270, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_19E0)

    @scena.Lambda('lambda_19F8')
    def lambda_19F8():
        OP_67(0, 4190, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_19F8)

    @scena.Lambda('lambda_1A10')
    def lambda_1A10():
        CameraSetDistance(9600, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1A10)

    @scena.Lambda('lambda_1A20')
    def lambda_1A20():
        OP_6C(315000, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_1A20)

    @scena.Lambda('lambda_1A30')
    def lambda_1A30():
        OP_6E(156, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_1A30)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0109, 0x0001)
    WaitForThreadExit(0x0109, 0x0002)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0610270506V#1185F王、王室亲卫队……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270507V而且……\n',
            '尤莉亚·舒华兹！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270508V#176F#2P好久不见了，凯诺娜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270509V#178F没想到会和你\n',
            '在这种地方相见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270510V#1185F你们……\n',
            '你怎么在这里！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270511V不是在雷斯顿要塞\n',
            '进行飞行训练吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270512V#170F#2P希德中校\n',
            '有紧急的支援请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270513V好像格兰赛尔市街\n',
            '发生了意外的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270514V所以我们就飞过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270515V#1187F哼……\n',
            '还以为就是个废物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270516V#170F#2P中校和理查德上校一样\n',
            '原本是卡西乌斯准将的部下嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270517V轻视他是你的错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270518V#1183F看来是了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270519V#1180F对了，你们。\n',
            '打算做什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270520V#173F#2P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270521V#1181F埃尔赛尤搭载的\n',
            '移动式的导力榴弹炮……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270522V想用那种东西\n',
            '对抗这个\n',
            '奥尔杰尤？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270523V#178F#2P就算不能对抗\n',
            '至少能拖拖后腿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270524V很快希德中校的部队\n',
            '应该也能到达这里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270525V投降对你自己比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270526V#1181F哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0610270527V#1188F#3S啊──哈哈哈！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270528V#178F#2P……有什么好笑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270529V#1320F你一点也没变呢，尤莉亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270530V直率凛然的性情\n',
            '和士官学校时一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270531V以前每次碰头\n',
            '就会相互挖苦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270532V不过对你这种性格\n',
            '我可是一点也不讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270533V#175F#2P凯诺娜……\n',
            '我也是一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270534V#1183F不过呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270535V#1182F要是阻挠解放理查德阁下的\n',
            '计划，我可绝不宽恕！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270536V#173F#2P！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(230, 0x00, 0x64)
    ChrMoveTo(0x000B, -12500, 2000, 3220, 4000, 0x00)
    OP_B0(0x0005, 0x0F)
    OP_6F(0x0005, 391)
    OP_70(0x0005, 410)
    OP_73(0x0005)
    ChrSetFlags(0x000B, 0x0080)
    OP_B0(0x0005, 0x05)
    OP_6F(0x0005, 251)
    OP_70(0x0005, 260)
    PlaySE(273, 0x00, 0x64)

    ChrTalk(
        0x010F,
        (
            '#0100270537V#176F#2P没办法了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270538V#172F１号、２号同时发射准备！\n',
            '阻止坦克前进！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetMessageWindowPos(-1, 160, -1, -1)
    TalkSetChrName('队员们')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#2690270539V#3S是·长官！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    LoadEffect(0x03, 'map\\\\mp063_00.eff')
    LoadEffect(0x04, 'map\\\\mp015_00.eff')
    LoadEffect(0x05, 'map\\\\mp007_00.eff')
    LoadEffect(0x07, 'map\\\\mp007_01.eff')
    PlayEffect(0x03, 0x02, 0x00FF, -2070, 1500, 3480, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(853, 0x00, 0x64)
    Sleep(200)

    PlayEffect(0x03, 0x07, 0x00FF, -2420, 1500, -2230, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(853, 0x00, 0x64)
    OP_B0(0x0005, 0x05)
    OP_6F(0x0005, 261)
    OP_70(0x0005, 264)
    OP_73(0x0005)
    OP_B0(0x0005, 0x0A)
    OP_6F(0x0005, 264)
    OP_70(0x0005, 268)
    OP_73(0x0005)
    OP_B0(0x0005, 0x0F)
    OP_6F(0x0005, 268)
    OP_70(0x0005, 270)
    OP_73(0x0005)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 411)
    OP_70(0x0005, 430)
    Sleep(1000)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x010F, 19)
    ChrSetSubChip(0x010F, 0)
    Sleep(500)

    OP_99(0x010F, 0x00, 0x01, 1500)

    ChrTalk(
        0x010F,
        (
            '#0100270540V#177F#2P#3S发射──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000000)
    Play3DEffect(0x05, 0x00, 0x05, 'Frame68__gospel__1_', 0x00000000, 0x00000000, 0x00000000, 0x0000, 0x0000, 0x0000, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    PlaySE(144, 0x00, 0x64)
    Play3DEffect(0x07, 0x01, 0x05, 'Frame68__gospel__1_', 0x00000000, 0x00000000, 0x00000000, 0x0000, 0x0000, 0x0000, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    Sleep(500)

    PlaySE(145, 0x00, 0x64)

    @scena.Lambda('lambda_22E4')
    def lambda_22E4():
        OP_67(0, 6190, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_22E4)

    @scena.Lambda('lambda_22FC')
    def lambda_22FC():
        CameraSetDistance(12600, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_22FC)

    PlayEffect(0x04, 0xFF, 0x00FF, -11100, 2650, 2870, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    StopEffect(0x01, 0x02)
    OP_23(0x010F)
    PlayBGM(92)
    StopEffect(0x03, 0x02)
    StopEffect(0x04, 0x02)
    StopEffect(0x05, 0x02)
    StopEffect(0x06, 0x02)
    StopEffect(0x02, 0x02)
    StopEffect(0x07, 0x02)
    OP_7B()
    Sleep(150)

    OP_79(0x02, 0x0002)
    OP_7B()
    Sleep(150)

    OP_79(0x03, 0x0002)
    OP_7B()
    Sleep(100)

    OP_6F(0x0003, 0)
    OP_7B()
    Sleep(150)

    OP_6F(0x0004, 0)
    OP_7B()
    Sleep(150)

    OP_79(0x04, 0x0002)
    OP_7B()
    Sleep(100)

    OP_79(0x05, 0x0002)
    OP_7B()
    Sleep(250)

    OP_6F(0x0000, 1)
    OP_7B()
    Sleep(150)

    OP_6F(0x0001, 1)
    OP_7B()
    Sleep(200)

    OP_79(0x0C, 0x0002)
    OP_7B()
    Sleep(100)

    OP_79(0x0D, 0x0002)
    OP_7B()
    Sleep(150)

    OP_79(0x01, 0x0002)
    OP_79(0x00, 0x0002)
    OP_79(0x06, 0x0002)
    OP_79(0x07, 0x0002)
    OP_79(0x08, 0x0002)
    OP_79(0x09, 0x0002)
    OP_79(0x0A, 0x0002)
    OP_79(0x0B, 0x0002)
    Fade(500)
    OP_7B()
    OP_0D()
    ChrSetChipByIndex(0x010F, 22)
    ChrSetSubChip(0x010F, 0)
    Sleep(500)

    ChrTalk(
        0x010F,
        (
            '#0100270541V#173F#2P什…什么…！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#2690270542V#2P不、不行！\n',
            '机能停止了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270543V#177F#2P……导力停止现象吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270544V但是，那样做\n',
            '重要的坦克也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(271, 0x00, 0x64)
    PlayEffect(0x01, 0x03, 0x002F, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    PlayEffect(0x01, 0x04, 0x002F, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x02, 0x05, 0x002F, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x02, 0x06, 0x002F, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_62(0x010F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_25C4')
    def lambda_25C4():
        OP_7C(50, 50, 3000, 100)
        Yield()

        Jump('lambda_25C4')

    DispatchAsync2(0x002F, 0x0003, lambda_25C4)

    PlayEffect(0x00, 0x01, 0x002F, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x002F, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_B0(0x0005, 0x0F)
    Sleep(300)

    PlaySE(272, 0x00, 0x64)
    ChrSetDirection(0x002F, 90, 50)
    OP_23(0x0110)
    TerminateThread(0x002F, 0x03)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)

    ChrTalk(
        0x010F,
        (
            '#0100270545V#173F#2P不、不可能！\n',
            '为什么能动！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    LoadEffect(0x03, 'scraft\\sc003_12.eff')
    LoadEffect(0x04, 'battle\\btbomb00.eff')
    OP_0D()

    @scena.Lambda('lambda_26D2')
    def lambda_26D2():
        OP_67(0, 4190, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_26D2)

    @scena.Lambda('lambda_26EA')
    def lambda_26EA():
        CameraSetDistance(9600, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_26EA)

    OP_12(0x000186A0, 0x0002BF20, 0x00001770)
    CreateThread(0x002F, 0x01, 0x00, func_12_3F30)
    WaitForThreadExit(0x002F, 0x0001)
    LoadEffect(0x03, 'monster\\ms30602a.eff')
    LoadEffect(0x04, 'monster\\ms30602b.eff')
    OP_72(0x0005, 0x0020)
    OP_B0(0x0005, 0x0A)
    OP_6F(0x0005, 121)
    OP_70(0x0005, 145)
    PlaySE(118, 0x00, 0x64)
    OP_73(0x0005)
    PlaySE(992, 0x00, 0x64)
    OP_73(0x0001)
    Sleep(200)

    Sleep(300)

    Sleep(500)

    PlayEffect(0x03, 0xFF, 0x002F, 0, 2200, 3500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_27AC')
    def lambda_27AC():
        ChrMoveTo(0x00FE, -12220, 0, 3220, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002F, 0x0001, lambda_27AC)

    OP_6F(0x0005, 161)
    OP_70(0x0005, 190)
    PlaySE(993, 0x00, 0x64)
    PlaySE(510, 0x00, 0x64)
    OP_7C(3000, 3000, 5000, 200)
    PlayEffect(0x04, 0xFF, 0x00FF, 290, 0, 3540, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    OP_6F(0x0000, 2)
    OP_70(0x0000, 60)
    Sleep(50)

    @scena.Lambda('lambda_283D')
    def lambda_283D():
        ChrJumpTo(0x001A, 2130, 0, 6400, 2000, 2000)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_283D)

    ChrSetChipByIndex(0x001A, 21)
    ChrSetSubChip(0x001A, 3)
    WaitForThreadExit(0x001A, 0x0001)
    ChrSetFlags(0x001A, 0x0002)
    ChrSetChipByIndex(0x001A, 29)
    ChrSetSubChip(0x001A, 0)
    OP_73(0x0000)
    Sleep(200)

    OP_73(0x0001)
    Sleep(200)

    ChrTalk(
        0x010F,
        (
            '#0100270546V#177F#2P什…什么…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x03, 'monster\\msc0311.eff')
    LoadEffect(0x04, 'map\\\\mp003_00.eff')
    OP_B0(0x0005, 0x0F)
    OP_6F(0x0005, 191)
    OP_70(0x0005, 210)
    PlaySE(118, 0x00, 0x64)
    OP_73(0x0005)
    OP_6F(0x0005, 101)
    OP_70(0x0005, 120)
    OP_73(0x0005)
    OP_62(0x010F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayEffect(0x03, 0x07, 0x002F, 500, 3000, 2300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FF, 4019, 0, -1270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FF, 6310, 0, 580, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FF, 6820, 0, 1440, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    ChrTalk(
        0x001F,
        (
            '#2690270547V#10A#2P呜哦……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FF, 7720, 0, -1790, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FF, 4030, 0, 1650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FF, 7690, 0, 210, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FF, 5160, 0, -4490, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x04, 0xFF, 0x00FF, 6820, 0, -3850, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    StopEffect(0x07, 0x00)
    ChrSetChipByIndex(0x010F, 20)
    ChrSetChipByIndex(0x001C, 21)
    ChrSetChipByIndex(0x001D, 21)
    ChrSetChipByIndex(0x001E, 21)
    ChrSetChipByIndex(0x001F, 21)
    ChrSetChipByIndex(0x0020, 21)
    ChrSetChipByIndex(0x0021, 21)
    ChrSetSubChip(0x010F, 0)
    ChrSetSubChip(0x001C, 0)
    ChrSetSubChip(0x001D, 0)
    ChrSetSubChip(0x001E, 0)
    ChrSetSubChip(0x001F, 0)
    ChrSetSubChip(0x0020, 0)
    ChrSetSubChip(0x0021, 0)

    @scena.Lambda('lambda_2BBA')
    def lambda_2BBA():
        OP_99(0x001E, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_2BBA)

    PlaySE(524, 0x00, 0x64)
    Sleep(50)

    @scena.Lambda('lambda_2BD4')
    def lambda_2BD4():
        OP_99(0x001F, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_2BD4)

    PlaySE(524, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_2BEE')
    def lambda_2BEE():
        OP_99(0x001C, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_2BEE)

    PlaySE(524, 0x00, 0x64)
    Sleep(50)

    @scena.Lambda('lambda_2C08')
    def lambda_2C08():
        OP_99(0x0020, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_2C08)

    PlaySE(524, 0x00, 0x64)
    Sleep(50)

    @scena.Lambda('lambda_2C22')
    def lambda_2C22():
        OP_99(0x001D, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_2C22)

    PlaySE(524, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_2C3C')
    def lambda_2C3C():
        OP_99(0x0021, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_2C3C)

    PlaySE(524, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_2C56')
    def lambda_2C56():
        OP_99(0x010F, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_2C56)

    PlaySE(524, 0x00, 0x64)
    Sleep(1000)

    PlaySE(106, 0x00, 0x64)
    OP_B0(0x0005, 0x0F)
    OP_6F(0x0005, 271)
    OP_70(0x0005, 290)
    OP_73(0x0005)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrSetPos(0x000B, -12290, 2000, 1850, 90)
    ChrClearFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_2CAB')
    def lambda_2CAB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2CAB)

    ChrMoveTo(0x000B, -12290, 2500, 1850, 2000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0610270548V#1181F#6P使周围的导力器停止，\n',
            '同时连接的机体还能动的元件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270549V哈哈哈……超过预想的力量呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270550V#175F#2P凯诺娜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270551V那个『福音』到底是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270552V#1181F#6P呵呵、从某条道得到的秘密武器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270553V作为帮忙『实验』的交换。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-11440, 0, 35260, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2770, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    MapClearFlags(0x00000010)
    ChrSetPos(0x0101, -11270, 0, 40480, 180)
    ChrSetPos(0x00F7, -10400, 0, 41140, 180)
    ChrSetPos(0x0109, -12300, 0, 41220, 180)

    @scena.Lambda('lambda_2E74')
    def lambda_2E74():
        ChrWalkTo(0x00FE, -11220, 0, 34200, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E74)

    Sleep(100)

    @scena.Lambda('lambda_2E94')
    def lambda_2E94():
        ChrWalkTo(0x00FE, -10400, 0, 35140, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2E94)

    Sleep(100)

    @scena.Lambda('lambda_2EB4')
    def lambda_2EB4():
        ChrWalkTo(0x00FE, -12300, 0, 35220, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_2EB4)

    WaitForThreadExit(0x0109, 0x0001)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F0E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270554V#055F#2P那、那是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F3A')

    def _loc_2F0E(): pass

    label('loc_2F0E')

    ChrTalk(
        0x0103,
        (
            '#0030270555V#023F#2P那、那是什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F3A(): pass

    label('loc_2F3A')

    ChrTalk(
        0x0101,
        (
            '#0010270556V#1020F#6P使用新型福音\n',
            '『噬身之蛇』的实验……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270557V竟、竟然以这样的形式来做！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270558V#1067F#5P啊……这下不妙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270559V那个工作的时候\n',
            '魔法之类的也不能使用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270560V#1065F既然如此……\n',
            '看来只有使用杀手锏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0109, 400)
    Sleep(100)

    ChrTurnDirection(0x00F7, 0x0109, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270561V#1004F#6P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31BB',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270562V#1063F#5P艾丝蒂尔、阿加特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270563V接下来的行动如果能成功，\n',
            '说不定可以暂时\n',
            '令『福音』停止。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270564V我们就趁机拖住坦克吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260333V#052F你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270566V#1002F#6P这、这能做到吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270567V#1066F#5P几率是一半对一半……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270568V大家一起\n',
            '向女神祈祷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32F4')

    def _loc_31BB(): pass

    label('loc_31BB')

    ChrTalk(
        0x0109,
        (
            '#0180270569V#1063F#5P艾丝蒂尔、雪拉小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270563V接下来的行动如果能成功，\n',
            '说不定可以暂时\n',
            '令『福音』停止。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270564V我们就趁机拖住坦克吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030270572V#023F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270566V#1002F#6P这、这能做到吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270567V#1066F#5P几率是一半对一半……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270568V大家一起\n',
            '向女神祈祷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32F4(): pass

    label('loc_32F4')

    Sleep(250)

    ChrSetFlags(0x0109, 0x0002)
    ChrSetChipByIndex(0x0109, 36)
    ChrSetSubChip(0x0109, 8)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_3314')
    def lambda_3314():
        CameraMove(-12300, 0, 35220, 1000)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_3314)

    @scena.Lambda('lambda_332C')
    def lambda_332C():
        OP_6E(246, 1000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_332C)

    OP_99(0x0109, 0x08, 0x0B, 1500)
    PlaySE(213, 0x00, 0x64)
    ChrSetFlags(0x0109, 0x2000)
    OP_D7(0x01, 15000, 265)
    OP_99(0x0109, 0x0B, 0x0F, 1500)
    CreateThread(0x0109, 0x00, 0x00, func_23_8564)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010270576V#1004F啊……那不是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270577V#1065F『封印宝杖』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270578V#1063F戴尔蒙市长持有的\n',
            '禁制之古代遗物！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_340D')
    def lambda_340D():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_340D')

    DispatchAsync2(0x0101, 0x0003, lambda_340D)

    @scena.Lambda('lambda_341E')
    def lambda_341E():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_341E')

    DispatchAsync2(0x00F7, 0x0001, lambda_341E)

    @scena.Lambda('lambda_342F')
    def lambda_342F():
        CameraMove(-13800, 0, 3000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_342F)

    @scena.Lambda('lambda_3447')
    def lambda_3447():
        OP_67(0, 4000, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3447)

    @scena.Lambda('lambda_345F')
    def lambda_345F():
        CameraSetDistance(2800, 5000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0003, lambda_345F)

    @scena.Lambda('lambda_346F')
    def lambda_346F():
        OP_6C(200000, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_346F)

    @scena.Lambda('lambda_347F')
    def lambda_347F():
        OP_6E(402, 5000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_347F)

    TerminateThread(0x0109, 0x00)
    ChrClearFlags(0x0109, 0x0002)
    ChrSetFlags(0x0109, 0x1000)
    ChrSetChipByIndex(0x0109, 37)
    ChrSetSubChip(0x0109, 0)
    ChrWalkTo(0x0109, -11270, 0, 11390, 6000, 0x00)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_34C4')
    def lambda_34C4():
        CameraMove(-14370, 0, -1260, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_34C4)

    @scena.Lambda('lambda_34DC')
    def lambda_34DC():
        CameraSetDistance(2500, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_34DC)

    ChrTalk(
        0x0109,
        (
            '#0180270579V#1069F#5P#3S#8A接招！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrWalkTo(0x0109, -12000, 0, 9000, 6000, 0x00)
    ChrSetFlags(0x0109, 0x0002)
    ChrSetFlags(0x0109, 0x0004)
    ChrSetFlags(0x0109, 0x0040)
    ChrClearFlags(0x0109, 0x1000)
    ChrSetChipByIndex(0x0109, 36)
    ChrSetSubChip(0x0109, 24)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_354A')
    def lambda_354A():
        ChrJumpTo(0x0109, -12800, 3500, 6000, 4000, 6000)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_354A)

    OP_56(0x00)
    OP_99(0x0109, 0x19, 0x1C, 1500)
    PlaySE(238, 0x00, 0x64)
    LoadEffect(0x03, 'Scraft\\\\sc008_02.eff')
    OP_20(0x00000000)
    OP_23(0x010F)
    OP_23(0x0090)
    PlayEffect(0x03, 0xFF, 0x00FF, -12000, 4600, 5930, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    StopEffect(0x00, 0x02)
    FadeOut(2000, 16777215, -1)

    ChrTalk(
        0x000B,
        (
            '#0610270580V#1189F#6P#10A呀啊啊啊！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_360C')
    def lambda_360C():
        ChrJumpTo(0x0109, -12800, 0, 7760, 200, 5000)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_360C)

    OP_99(0x0109, 0x1D, 0x20, 750)
    OP_0D()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    StopEffect(0x03, 0x00)
    StopEffect(0x04, 0x00)
    StopEffect(0x05, 0x00)
    StopEffect(0x06, 0x00)
    TerminateThread(0x010F, 0x00)
    TerminateThread(0x010F, 0x03)
    ChrSetPos(0x010F, -3000, 0, 1690, 270)
    ChrClearFlags(0x0109, 0x0004)
    ChrSetPos(0x0109, -11320, 0, 9220, 180)
    ChrClearFlags(0x0109, 0x0002)
    ChrSetSubChip(0x0109, 0)
    ChrSetChipByIndex(0x0109, 65535)
    CameraMove(-11790, 0, 4700, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2390, 0)
    OP_6C(224000, 0)
    OP_6E(402, 0)
    ChrSetDirection(0x0109, 180, 0)
    ChrSetDirection(0x010F, 270, 0)
    CloseMessageWindow()
    OP_7A(0xFF, 0x0002)
    OP_7B()
    ChrClearFlags(0x0109, 0x2000)
    OP_6F(0x0003, 10)
    OP_6F(0x0004, 10)
    MapSetFlags(0x00000010)
    Sleep(2000)

    FadeIn(3000, 16777215)
    OP_D7(0x00, 0, 0)
    LoadEffect(0x03, 'Scraft\\\\sc000_31.eff')
    PlayEffect(0x03, 0x07, 0x00FF, -11960, 4500, 5930, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x010F, 0x00, 0x00, func_14_40BB)
    Sleep(3000)

    StopEffect(0x07, 0x00)
    WaitForThreadExit(0x010F, 0x0000)

    ChrTalk(
        0x010F,
        (
            '#0100270581V#173F#7P照、照明恢复了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270582V导力停止现象失效了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 0, 400)
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0610270583V#1185F#6P怎、怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270584V你到底，做了什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0109,
        (
            '#0180270585V#1066F嘿嘿，没什么大不了的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270586V只是将古代遗物破坏时\n',
            '释放的庞大导力\n',
            '打了过去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270587V就连福音也\n',
            '短路了呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270588V#1187F#6P不、不可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, -12110, 0, 16900, 180)
    ChrSetPos(0x00F7, -9990, 0, 16900, 180)

    @scena.Lambda('lambda_38FC')
    def lambda_38FC():
        ChrWalkTo(0x00FE, -12110, 0, 10560, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38FC)

    Sleep(100)

    @scena.Lambda('lambda_391C')
    def lambda_391C():
        ChrWalkTo(0x00FE, -9990, 0, 10560, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_391C)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010270589V#1018F#2P凯文先生，太棒了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39A5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270590V#051F#5P干得好，不良神父！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39D3')

    def _loc_39A5(): pass

    label('loc_39A5')

    ChrTalk(
        0x0103,
        (
            '#0030270591V#021F#5P成功了呢，神父先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39D3(): pass

    label('loc_39D3')

    ChrTalk(
        0x0109,
        (
            '#0180270592V#1071F#5P呀～过奖过奖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270593V#1187F#6P呜……\n',
            '那又怎么样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270594V就算不用什么福音\n',
            '你们也不是我的对手！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270595V#1186F奥尔杰尤的力量，就让你们见识见识！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    PlayBGM(41)
    Sleep(500)

    ChrMoveTo(0x000B, -12290, 2000, 1850, 2000, 0x00)

    @scena.Lambda('lambda_3AB5')
    def lambda_3AB5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_3AB5)

    PlaySE(230, 0x00, 0x64)
    OP_B0(0x0005, 0x0A)
    OP_6F(0x0005, 331)
    OP_70(0x0005, 350)
    OP_73(0x0005)
    ChrSetFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_3AE6')
    def lambda_3AE6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 0)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_3AE6)

    Sleep(500)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 32)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0109, 35)
    ChrSetSubChip(0x0109, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B30',
    )

    ChrSetChipByIndex(0x0106, 33)
    ChrSetSubChip(0x0106, 0)

    Jump('loc_3B3A')

    def _loc_3B30(): pass

    label('loc_3B30')

    ChrSetChipByIndex(0x0103, 34)
    ChrSetSubChip(0x0103, 0)

    def _loc_3B3A(): pass

    label('loc_3B3A')

    OP_0D()
    PlaySE(271, 0x00, 0x64)
    CreateThread(0x002F, 0x00, 0x00, func_15_40FB)
    ChrSetDirection(0x0109, 90, 400)
    CameraMove(-9950, 0, 4770, 1500)

    ChrTalk(
        0x0109,
        (
            '#0180270596V#1069F#2P尤莉亚上尉！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270597V受到福音短路影响\n',
            '坦克的机能应该也下降了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270598V要阻止它只有趁现在！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270599V#178F是吗……明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0109, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270600V#1006F#2P尤莉亚小姐，拜托了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C8C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270601V#051F#2P大叔真传的剑技、\n',
            '就让我们见识见识吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CCB')

    def _loc_3C8C(): pass

    label('loc_3C8C')

    ChrTalk(
        0x0103,
        (
            '#0030270602V#526F#2P先生真传的剑技、\n',
            '就让我们见识见识吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CCB(): pass

    label('loc_3CCB')

    ChrTalk(
        0x010F,
        (
            '#0100270603V#171F呼……明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x002F, 0x0000)
    Fade(250)
    PlayEffect(0x01, 0x03, 0x002F, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x04, 0x002F, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x05, 0x002F, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x06, 0x002F, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_0D()
    Sleep(250)

    @scena.Lambda('lambda_3DDA')
    def lambda_3DDA():
        CameraMove(-11160, 0, 3600, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3DDA)

    @scena.Lambda('lambda_3DF2')
    def lambda_3DF2():
        CameraSetDistance(2000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3DF2)

    ChrSetFlags(0x010F, 0x1000)
    ChrSetFlags(0x0109, 0x1000)
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x00F7, 0x1000)
    ChrSetChipByIndex(0x010F, 43)

    @scena.Lambda('lambda_3E1B')
    def lambda_3E1B():
        ChrMoveTo(0x00FE, -9310, 0, 1370, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x010F, 0x0000, lambda_3E1B)

    Sleep(50)

    ChrSetChipByIndex(0x0109, 42)

    @scena.Lambda('lambda_3E40')
    def lambda_3E40():
        ChrMoveTo(0x00FE, -12640, 0, 4740, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_3E40)

    Sleep(50)

    ChrSetChipByIndex(0x0101, 39)

    @scena.Lambda('lambda_3E65')
    def lambda_3E65():
        ChrMoveTo(0x00FE, -13350, 0, 5630, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3E65)

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E95',
    )

    ChrSetChipByIndex(0x0106, 40)

    Jump('loc_3E9A')

    def _loc_3E95(): pass

    label('loc_3E95')

    ChrSetChipByIndex(0x0103, 41)

    def _loc_3E9A(): pass

    label('loc_3E9A')

    @scena.Lambda('lambda_3EA0')
    def lambda_3EA0():
        ChrMoveTo(0x00FE, -11370, 0, 5710, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_3EA0)

    Sleep(400)

    ChrSetStatus(ChrTable['尤莉亚上尉'], 0x00, 59)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0x03, 250)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0x05, 110)
    ChrSetStatus(ChrTable['尤莉亚上尉'], 0xFE, 0)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['长刺剑'], 0xFF)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['纤维大衣'], 0xFF)
    EquipCmd(ChrTable['尤莉亚上尉'], ItemTable['斯托雷加Ｆ'], 0xFF)
    AddCraft(ChrTable['尤莉亚上尉'], 0x0000)
    OP_37(0x0E, 0x00)
    OP_37(0x0E, 0x01)
    OP_37(0x0E, 0x02)
    OP_37(0x0E, 0x03)
    OP_37(0x0E, 0x04)
    OP_37(0x0E, 0x05)
    OP_34(0x0E, 0x006F)
    OP_34(0x0E, 0x0073)
    OP_34(0x0E, 0x0039)
    OP_34(0x0E, 0x0046)
    OP_34(0x0E, 0x0047)
    OP_34(0x0E, 0x0011)
    OP_BB(0x0E, 0x06, 0x0000011A)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0109, 0xFF)
    TerminateThread(0x010F, 0xFF)
    TerminateThread(0x00F7, 0xFF)
    Battle(0x0000044E, 0x00000000, 0x00, 0x0000, 0xFF)

    Return()

# id: 0x0012 offset: 0x3F30
@scena.Code('func_12_3F30')
def func_12_3F30():
    PlayEffect(0x03, 0x01, 0x00FF, -9700, 1500, 1670, 90, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x03, 0x02, 0x00FF, -9700, 1500, 1000, 90, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(400)

    PlayEffect(0x04, 0xFF, 0x00FF, -800, 250, -1940, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    StopEffect(0x01, 0x00)
    OP_6F(0x0001, 2)
    OP_70(0x0001, 10)
    Sleep(100)

    PlayEffect(0x04, 0xFF, 0x00FF, -800, 250, -1940, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    StopEffect(0x02, 0x00)
    Sleep(100)

    OP_6F(0x0001, 11)
    OP_70(0x0001, 60)

    @scena.Lambda('lambda_4040')
    def lambda_4040():
        ChrJumpTo(0x001B, 1460, 0, -6180, 2000, 2000)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_4040)

    ChrSetChipByIndex(0x001B, 21)
    ChrSetSubChip(0x001B, 3)
    Sleep(100)

    WaitForThreadExit(0x001B, 0x0001)
    ChrSetFlags(0x001B, 0x0002)
    ChrSetChipByIndex(0x001B, 29)
    ChrSetSubChip(0x001B, 1)

    Return()

# id: 0x0013 offset: 0x407C
@scena.Code('func_13_407C')
def func_13_407C():
    @scena.Lambda('lambda_4082')
    def lambda_4082():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_4082')

    DispatchAsync2(0x00FE, 0x0003, lambda_4082)

    Sleep(500)

    OP_99(0x00FE, 0x03, 0x00, 1000)
    TerminateThread(0x00FE, 0x03)
    ChrSetChipByIndex(0x00FE, 22)
    ChrSetSubChip(0x00FE, 0)
    Sleep(500)

    Return()

# id: 0x0014 offset: 0x40BB
@scena.Code('func_14_40BB')
def func_14_40BB():
    ChrSetChipByIndex(0x00FE, 43)
    ChrWalkTo(0x00FE, -5000, 0, 1690, 1000, 0x00)
    TerminateThread(0x00FE, 0x03)
    ChrSetChipByIndex(0x010F, 22)
    ChrSetSubChip(0x010F, 0)
    ChrSetDirection(0x010F, 0, 400)
    Sleep(500)

    ChrSetDirection(0x010F, 270, 400)
    Sleep(500)

    Return()

# id: 0x0015 offset: 0x40FB
@scena.Code('func_15_40FB')
def func_15_40FB():
    @scena.Lambda('lambda_4101')
    def lambda_4101():
        OP_7C(50, 50, 3000, 100)
        Yield()

        Jump('lambda_4101')

    DispatchAsync2(0x002F, 0x0003, lambda_4101)

    PlaySE(272, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x002F, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x002F, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetDirection(0x002F, 45, 20)
    Sleep(500)

    ChrMoveTo(0x002F, -12890, 0, 2600, 1000, 0x00)
    Sleep(500)

    ChrMoveTo(0x002F, -14850, 0, 1200, 1000, 0x00)
    OP_23(0x0110)
    TerminateThread(0x002F, 0x03)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)

    Return()

# id: 0x0016 offset: 0x41CC
@scena.Code('func_16_41CC')
def func_16_41CC():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_23(0x010F)
    FormationAddMember(ChrTable['尤莉亚上尉'], 0xF9, 0xFF)
    StopEffect(0x03, 0x00)
    StopEffect(0x04, 0x00)
    StopEffect(0x05, 0x00)
    StopEffect(0x06, 0x00)
    ChrClearFlags(0x002F, 0x0080)
    OP_72(0x0005, 0x0004)
    ChrSetPos(0x002F, -14380, 0, -8330, 0)
    OP_A1(0x002F, 0x0005)
    OP_6F(0x0005, 311)
    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -13200, 3500, -5000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x01, 0x00FF, 2000, 600, 3460, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x00FF, 1220, 600, -2270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetPos(0x0101, -14540, 0, -1200, 180)
    ChrSetPos(0x010F, -12870, 0, -1230, 180)
    ChrSetPos(0x00F7, -14350, 0, 570, 180)
    ChrSetPos(0x0109, -12660, 0, 750, 180)
    ChrSetChipByIndex(0x0101, 32)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0109, 35)
    ChrSetSubChip(0x0109, 0)
    ChrSetChipByIndex(0x010F, 22)
    ChrSetSubChip(0x010F, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4340',
    )

    ChrSetChipByIndex(0x0106, 33)
    ChrSetSubChip(0x0106, 0)

    Jump('loc_434A')

    def _loc_4340(): pass

    label('loc_4340')

    ChrSetChipByIndex(0x0103, 34)
    ChrSetSubChip(0x0103, 0)

    def _loc_434A(): pass

    label('loc_434A')

    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_A1(0x0030, 0x0000)
    OP_A1(0x0031, 0x0001)
    ChrSetPos(0x0030, 1540, 0, 3700, 90)
    ChrSetPos(0x0031, 1190, 0, -2000, 90)
    OP_6F(0x0000, 60)
    OP_6F(0x0001, 60)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_6F(0x0003, 10)
    OP_6F(0x0004, 10)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetBattleFlags(0x001A, 0x0020)
    ChrSetBattleFlags(0x001B, 0x0020)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrSetPos(0x001A, 2130, 0, 6400, 270)
    ChrSetPos(0x001B, 1460, 0, -6180, 270)
    ChrSetPos(0x001C, 5510, 0, -1750, 270)
    ChrSetPos(0x001D, 5700, 0, 520, 270)
    ChrSetPos(0x001E, 5710, 0, -3450, 270)
    ChrSetPos(0x001F, 5630, 0, 1960, 270)
    ChrSetPos(0x0020, 7090, 0, -1780, 270)
    ChrSetPos(0x0021, 7090, 0, -120, 270)
    ChrSetChipByIndex(0x001A, 21)
    ChrSetChipByIndex(0x001B, 21)
    ChrSetChipByIndex(0x001C, 21)
    ChrSetChipByIndex(0x001D, 21)
    ChrSetChipByIndex(0x001E, 21)
    ChrSetChipByIndex(0x001F, 21)
    ChrSetChipByIndex(0x0020, 21)
    ChrSetChipByIndex(0x0021, 21)
    ChrSetSubChip(0x001A, 3)
    ChrSetSubChip(0x001B, 3)
    ChrSetSubChip(0x001C, 3)
    ChrSetSubChip(0x001D, 3)
    ChrSetSubChip(0x001E, 3)
    ChrSetSubChip(0x001F, 3)
    ChrSetSubChip(0x0020, 3)
    ChrSetSubChip(0x0021, 3)
    ChrSetFlags(0x0036, 0x0080)
    ChrSetFlags(0x0037, 0x0080)
    ChrSetFlags(0x0038, 0x0080)
    ChrSetFlags(0x0039, 0x0080)
    CameraMove(-15120, 0, -4350, 0)
    OP_67(0, 6960, -10000, 0)
    CameraSetDistance(2400, 0)
    OP_6C(224000, 0)
    OP_6E(422, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010270604V#1018F#2P成、成功了……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270605V#171F#5P啊啊……\n',
            '看来完全停住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_457B')
    def lambda_457B():
        CameraMove(-15080, 0, -6490, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_457B)

    @scena.Lambda('lambda_4593')
    def lambda_4593():
        OP_67(0, 8370, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4593)

    @scena.Lambda('lambda_45AB')
    def lambda_45AB():
        CameraSetDistance(2250, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_45AB)

    PlaySE(106, 0x00, 0x64)
    OP_B0(0x0005, 0x0A)
    OP_6F(0x0005, 311)
    OP_70(0x0005, 330)
    OP_73(0x0005)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrSetPos(0x000B, -13000, 2000, -8200, 0)
    ChrSetFlags(0x000B, 0x0001)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0040)

    @scena.Lambda('lambda_4605')
    def lambda_4605():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_4605)

    ChrMoveTo(0x000B, -13000, 2500, -8200, 2000, 0x00)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0610270606V#1187F#6P呜……\n',
            '干得不错嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270607V#178F#5P凯诺娜，你输了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270608V老老实实投降吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270609V#1185F#6P开什么玩笑！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270610V怎能因为这种事\n',
            '就放弃解放阁下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_46FC')
    def lambda_46FC():
        OP_67(0, 7100, -10000, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_46FC)

    @scena.Lambda('lambda_4714')
    def lambda_4714():
        CameraSetDistance(2590, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_4714)

    ChrSetChipByIndex(0x000B, 44)
    ChrSetSubChip(0x000B, 4)
    PlaySE(571, 0x00, 0x64)
    ChrJumpTo(0x000B, -13520, 2750, -7560, 1000, 5000)
    ChrSetChipByIndex(0x000B, 23)
    ChrSetSubChip(0x000B, 0)
    Sleep(300)

    PlaySE(106, 0x00, 0x64)
    Sleep(500)

    CreateThread(0x002C, 0x01, 0x00, func_19_830C)
    Sleep(300)

    CreateThread(0x002D, 0x01, 0x00, func_1A_8361)
    Sleep(300)

    CreateThread(0x002E, 0x01, 0x00, func_1B_83C0)
    WaitForThreadExit(0x002E, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    PlayBGM(51)

    ChrTalk(
        0x000B,
        (
            '#0610270611V#1186F#6P尤莉亚！　游击士！\n',
            '这是最后一战了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270612V来堂堂正正地决个胜负吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270613V#1007F#2P用完坦克\n',
            '之后才说这种话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270614V#1006F好啊！\n',
            '要来就来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270615V#176F#5P看来和你\n',
            '一决胜负的时刻来经到来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270616V#177F……来吧，凯诺娜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x1000)
    ChrSetChipByIndex(0x0101, 39)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_48D7',
    )

    ChrSetFlags(0x0106, 0x1000)
    ChrSetChipByIndex(0x0106, 40)

    Jump('loc_48E1')

    def _loc_48D7(): pass

    label('loc_48D7')

    ChrSetFlags(0x0103, 0x1000)
    ChrSetChipByIndex(0x0103, 41)

    def _loc_48E1(): pass

    label('loc_48E1')

    ChrSetFlags(0x0109, 0x1000)
    ChrSetChipByIndex(0x0109, 42)
    ChrSetFlags(0x010F, 0x1000)
    ChrSetChipByIndex(0x010F, 43)
    ChrSetChipByIndex(0x000B, 44)
    ChrSetChipByIndex(0x002C, 25)
    ChrSetChipByIndex(0x002D, 26)
    ChrSetChipByIndex(0x002E, 25)

    @scena.Lambda('lambda_490F')
    def lambda_490F():
        ChrMoveToRelative(0x00FE, 0, 0, -2000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_490F)

    @scena.Lambda('lambda_492A')
    def lambda_492A():
        ChrMoveToRelative(0x00FE, 0, 0, -2000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_492A)

    @scena.Lambda('lambda_4945')
    def lambda_4945():
        ChrMoveToRelative(0x00FE, 0, 0, -2000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_4945)

    @scena.Lambda('lambda_4960')
    def lambda_4960():
        ChrMoveToRelative(0x00FE, 0, 0, -2000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_4960)

    @scena.Lambda('lambda_497B')
    def lambda_497B():
        ChrMoveToRelative(0x00FE, -500, 0, 2000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_497B)

    @scena.Lambda('lambda_4996')
    def lambda_4996():
        ChrMoveToRelative(0x00FE, -500, 0, 2000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_4996)

    @scena.Lambda('lambda_49B1')
    def lambda_49B1():
        ChrMoveToRelative(0x00FE, 500, 0, 2000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x002E, 0x0001, lambda_49B1)

    @scena.Lambda('lambda_49CC')
    def lambda_49CC():
        CameraSetDistance(2000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_49CC)

    Sleep(300)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x010F, 0xFF)
    TerminateThread(0x0109, 0xFF)
    TerminateThread(0x00F7, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x002C, 0xFF)
    TerminateThread(0x002D, 0xFF)
    TerminateThread(0x002E, 0xFF)
    Battle(0x0000045E, 0x00000000, 0x00, 0x0000, 0xFF)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    OP_20(0x00000000)

    Return()

# id: 0x0017 offset: 0x4A30
@scena.Code('func_17_4A30')
def func_17_4A30():
    OP_7E(1000, -2000, -500, 80, 0)
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_20(0x000007D0)
    Sleep(2000)

    PlayBGM(84)
    FormationAddMember(ChrTable['尤莉亚上尉'], 0xF9, 0xFF)
    ChrSetPos(0x0101, -18580, 0, -1200, 270)
    ChrSetPos(0x00F7, -17350, 0, 170, 270)
    ChrSetPos(0x0109, -17070, 0, -1450, 270)
    ChrSetPos(0x010F, -18780, 0, 320, 270)
    ChrSetChipByIndex(0x0101, 32)
    ChrSetSubChip(0x0101, 0)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4AC1',
    )

    ChrSetChipByIndex(0x0106, 33)
    ChrSetSubChip(0x0106, 0)

    Jump('loc_4ACB')

    def _loc_4AC1(): pass

    label('loc_4AC1')

    ChrSetChipByIndex(0x0103, 34)
    ChrSetSubChip(0x0103, 0)

    def _loc_4ACB(): pass

    label('loc_4ACB')

    ChrSetChipByIndex(0x0109, 35)
    ChrSetSubChip(0x0109, 0)
    ChrSetChipByIndex(0x010F, 22)
    ChrSetSubChip(0x010F, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrClearFlags(0x002E, 0x0080)
    ChrSetPos(0x000B, -23470, 0, -40, 90)
    ChrSetPos(0x002C, -23800, 0, 2380, 90)
    ChrSetPos(0x002D, -25000, 0, 1040, 90)
    ChrSetPos(0x002E, -24000, 0, -1130, 90)
    ChrSetFlags(0x002C, 0x0002)
    ChrSetFlags(0x002D, 0x0002)
    ChrSetFlags(0x002E, 0x0002)
    ChrSetFlags(0x002C, 0x0800)
    ChrSetFlags(0x002D, 0x0800)
    ChrSetFlags(0x002E, 0x0800)
    ChrSetChipByIndex(0x000B, 27)
    ChrSetChipByIndex(0x002C, 28)
    ChrSetChipByIndex(0x002D, 28)
    ChrSetChipByIndex(0x002E, 28)
    ChrSetSubChip(0x000B, 3)
    ChrSetSubChip(0x002C, 1)
    ChrSetSubChip(0x002D, 4)
    ChrSetSubChip(0x002E, 7)
    ChrClearFlags(0x002F, 0x0080)
    OP_72(0x0005, 0x0004)
    ChrSetPos(0x002F, -14380, 0, -8330, 0)
    OP_A1(0x002F, 0x0005)
    OP_6F(0x0005, 330)
    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -14380, 2500, -6590, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x01, 0x00FF, 2000, 600, 3460, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x00FF, 1220, 600, -2270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    LoadEffect(0x01, 'map\\\\mp064_01.eff')
    LoadEffect(0x02, 'map\\\\mp065_01.eff')
    LoadEffect(0x03, 'map\\\\mp064_00.eff')
    LoadEffect(0x04, 'map\\\\mp065_00.eff')
    LoadEffect(0x05, 'map\\\\mp021_00.eff')
    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_A1(0x0030, 0x0000)
    OP_A1(0x0031, 0x0001)
    ChrSetPos(0x0030, 1540, 0, 3700, 90)
    ChrSetPos(0x0031, 1190, 0, -2000, 90)
    OP_6F(0x0000, 60)
    OP_6F(0x0001, 60)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_6F(0x0003, 10)
    OP_6F(0x0004, 10)
    ChrSetFlags(0x0036, 0x0080)
    ChrSetFlags(0x0037, 0x0080)
    ChrSetFlags(0x0038, 0x0080)
    ChrSetFlags(0x0039, 0x0080)
    CameraMove(-21000, 0, -490, 0)
    OP_67(0, 10150, -10000, 0)
    CameraSetDistance(1700, 0)
    OP_6C(224000, 0)
    OP_6E(422, 0)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetBattleFlags(0x001A, 0x0020)
    ChrSetBattleFlags(0x001B, 0x0020)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrSetPos(0x001A, 2130, 0, 6400, 270)
    ChrSetPos(0x001B, 1460, 0, -6180, 270)
    ChrSetPos(0x001C, 5510, 0, -1750, 270)
    ChrSetPos(0x001D, 5700, 0, 520, 270)
    ChrSetPos(0x001E, 5710, 0, -3450, 270)
    ChrSetPos(0x001F, 5630, 0, 1960, 270)
    ChrSetPos(0x0020, 7090, 0, -1780, 270)
    ChrSetPos(0x0021, 7090, 0, -120, 270)
    ChrSetChipByIndex(0x001A, 21)
    ChrSetChipByIndex(0x001B, 21)
    ChrSetChipByIndex(0x001C, 21)
    ChrSetChipByIndex(0x001D, 21)
    ChrSetChipByIndex(0x001E, 21)
    ChrSetChipByIndex(0x001F, 21)
    ChrSetChipByIndex(0x0020, 21)
    ChrSetChipByIndex(0x0021, 21)
    ChrSetSubChip(0x001A, 3)
    ChrSetSubChip(0x001B, 3)
    ChrSetSubChip(0x001C, 3)
    ChrSetSubChip(0x001D, 3)
    ChrSetSubChip(0x001E, 3)
    ChrSetSubChip(0x001F, 3)
    ChrSetSubChip(0x0020, 3)
    ChrSetSubChip(0x0021, 3)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0610270617V#1321F#2P呜……唔唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270618V理查德阁下……\n',
            '实在……抱歉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270619V#175F#6P呼呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100270620V终、终于结束了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270621V#1007F#5P真、真是累死人了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270622V#1068F#5P呼呼……\n',
            '因、因为是连续作战啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FCC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270623V#556F#6P哦……\n',
            '总算成功了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5001')

    def _loc_4FCC(): pass

    label('loc_4FCC')

    ChrTalk(
        0x0103,
        (
            '#0030270624V#524F#6P呼……\n',
            '看来总算成功了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5001(): pass

    label('loc_5001')

    ChrSetFlags(0x000C, 0x0040)
    ChrSetPos(0x000C, -17890, 0, -11940, 0)

    NpcTalk(
        0x000C,
        '男人的声音',
        (
            '#0640270625V#4P结、结束了吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    Sleep(100)

    ChrClearFlags(0x00F7, 0x0002)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetSubChip(0x00F7, 0)
    Sleep(100)

    ChrClearFlags(0x0109, 0x0002)
    ChrSetChipByIndex(0x0109, 65535)
    ChrSetSubChip(0x0109, 0)
    Sleep(100)

    ChrClearFlags(0x010F, 0x0002)
    ChrSetChipByIndex(0x010F, 65535)
    ChrSetSubChip(0x010F, 0)
    OP_0D()
    Sleep(100)

    @scena.Lambda('lambda_50A5')
    def lambda_50A5():
        CameraMove(-19790, 0, -4520, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_50A5)

    @scena.Lambda('lambda_50BD')
    def lambda_50BD():
        CameraSetDistance(2009, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_50BD)

    ChrClearFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_50D2')
    def lambda_50D2():
        ChrWalkTo(0x000C, -18000, 0, -9040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_50D2)

    @scena.Lambda('lambda_50ED')
    def lambda_50ED():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_50ED')

    DispatchAsync2(0x0101, 0x0002, lambda_50ED)

    Sleep(100)

    @scena.Lambda('lambda_5103')
    def lambda_5103():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_5103')

    DispatchAsync2(0x00F7, 0x0002, lambda_5103)

    Sleep(50)

    @scena.Lambda('lambda_5119')
    def lambda_5119():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_5119')

    DispatchAsync2(0x0109, 0x0002, lambda_5119)

    Sleep(50)

    @scena.Lambda('lambda_512F')
    def lambda_512F():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_512F')

    DispatchAsync2(0x010F, 0x0002, lambda_512F)

    WaitForThreadExit(0x000C, 0x0001)
    ChrSetDirection(0x000C, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010270626V#1004F#2P啊、公爵先生……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270627V#1060F#5P怎么……\n',
            '原来被关在坦克里了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0640270628V#220F#6P唔，算是吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x00F7, 0x02)
    TerminateThread(0x0109, 0x02)
    TerminateThread(0x010F, 0x02)

    @scena.Lambda('lambda_51EE')
    def lambda_51EE():
        CameraMove(-18080, 0, -2070, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_51EE)

    @scena.Lambda('lambda_5206')
    def lambda_5206():
        CameraSetDistance(1670, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5206)

    ChrWalkTo(0x000C, -17840, 0, -3190, 2000, 0x00)
    ChrSetDirection(0x000C, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#0640270629V#220F#5P看来这次\n',
            '不得不向你们道谢了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640270630V#221F作为答谢，就把我秘藏多年的\n',
            '连环画佳作让给你们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0109, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x010F, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010270631V#1016F心、心领了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270632V#1006F不过，真没想到会被公爵先生\n',
            '感谢呢──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_538F')
    def lambda_538F():
        CameraMove(-17930, 0, -2800, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_538F)

    ChrMoveTo(0x0101, -18140, 0, -2560, 5000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010270633V#1020F#4P#3S玲呢！？#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270634V#3S玲没事吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#0640270635V#226F#5P怎、怎么突然说什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640270636V谁啊，那个叫玲的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270637V#1005F#4P是个女孩子啦！\n',
            '穿白裙子的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270638V不在坦克里吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0640270639V#222F#5P除、除了那些家伙之外\n',
            '就只有我在了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 600)
    Sleep(500)

    @scena.Lambda('lambda_550C')
    def lambda_550C():
        CameraMove(-22590, 0, -220, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_550C)

    @scena.Lambda('lambda_5524')
    def lambda_5524():
        ChrMoveTo(0x00FE, -21500, 0, -170, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5524)

    @scena.Lambda('lambda_553F')
    def lambda_553F():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_553F')

    DispatchAsync2(0x000C, 0x0002, lambda_553F)

    @scena.Lambda('lambda_5550')
    def lambda_5550():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_5550')

    DispatchAsync2(0x00F7, 0x0002, lambda_5550)

    @scena.Lambda('lambda_5561')
    def lambda_5561():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_5561')

    DispatchAsync2(0x0109, 0x0002, lambda_5561)

    @scena.Lambda('lambda_5572')
    def lambda_5572():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_5572')

    DispatchAsync2(0x010F, 0x0002, lambda_5572)

    WaitForThreadExit(0x0101, 0x0000)
    ChrSetDirection(0x0101, 270, 400)
    TerminateThread(0x000C, 0x02)
    TerminateThread(0x00F7, 0x02)
    TerminateThread(0x0109, 0x02)
    TerminateThread(0x010F, 0x02)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010270640V#1005F#6P喂！\n',
            '玲怎么样了！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270641V被关在哪里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270642V#1182F……？\n',
            '你说什么呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270643V#1009F#6P到、到了这个地步\n',
            '别再装傻了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270644V当然就是你们\n',
            '从协会掳走的女孩啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270645V#1184F从协会掳走……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270646V#1183F……是吗……\n',
            '是这么回事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270647V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270526V#1181F哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_20(0x000007D0)

    ChrTalk(
        0x000B,
        (
            '#0610270649V#1188F#3S啊哈哈哈哈哈哈哈哈哈哈哈！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270650V#1020F#6P等、等等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270651V#173F#5P凯诺娜……\n',
            '到底怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610270652V#1181F这能\n',
            '不让人发笑吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270653V#1189F我！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270654V为阁下完成众多\n',
            '谋略的我！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610270655V#1187F……竟然被那种小丫头\n',
            '完全利用了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0014, 0x0001)
    ChrSetFlags(0x0014, 0x0004)
    ChrSetPos(0x0014, -27100, 7300, -880, 90)
    Sleep(500)

    NpcTalk(
        0x0014,
        '少女的声音',
        (
            '#0220270656V#3P嘻嘻。\n',
            '叫人家小丫头多没礼貌呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayBGM(90)
    Sleep(500)

    @scena.Lambda('lambda_5974')
    def lambda_5974():
        CameraMove(-29980, 870, -950, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5974)

    @scena.Lambda('lambda_598C')
    def lambda_598C():
        OP_67(0, 5490, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_598C)

    @scena.Lambda('lambda_59A4')
    def lambda_59A4():
        CameraSetDistance(2810, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_59A4)

    @scena.Lambda('lambda_59B4')
    def lambda_59B4():
        OP_6E(599, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_59B4)

    OP_6C(270000, 4000)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010270657V#1004F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270658V……………咦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-34440, 890, 2870, 0)
    OP_67(0, 7990, -10000, 0)
    CameraSetDistance(3420, 0)
    OP_6C(297000, 0)
    OP_6E(272, 0)
    OP_0D()

    @scena.Lambda('lambda_5A6E')
    def lambda_5A6E():
        ChrWalkTo(0x00FE, -20720, 0, -1130, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_5A6E)

    Sleep(200)

    @scena.Lambda('lambda_5A8E')
    def lambda_5A8E():
        ChrWalkTo(0x00FE, -20720, 0, 890, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010F, 0x0000, lambda_5A8E)

    Sleep(100)

    @scena.Lambda('lambda_5AAE')
    def lambda_5AAE():
        ChrWalkTo(0x00FE, -19430, 0, -60, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_5AAE)

    NpcTalk(
        0x0014,
        '玲',
        (
            '#0220270659V#261F哈哈哈，晚上好。\n',
            '今晚月色真美。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270660V今宵的茶会…\n',
            '大家尽情享受到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x010F, 0x0000)
    WaitForThreadExit(0x0109, 0x0000)

    ChrTalk(
        0x0109,
        (
            '#0180270661V#1064F#5P什、什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5B9C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270662V#055F#5P小孩……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BC4')

    def _loc_5B9C(): pass

    label('loc_5B9C')

    ChrTalk(
        0x0103,
        (
            '#0030270663V#023F#5P女孩子……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5BC4(): pass

    label('loc_5BC4')

    ChrTalk(
        0x0101,
        (
            '#0010270664V#1026F#2P……玲………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270665V你、你在干什么。\n',
            '爬到那种地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270666V#1020F很、很危险的呀！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0014,
        '玲',
        (
            '#0220270667V#263F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270668V#1025F#2P真是的……\n',
            '真像只猫一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270669V现在就去救你\n',
            '在那里等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0014,
        '玲',
        (
            '#0220270670V#1305F哈哈哈，没那个必要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270671V因为这里\n',
            '可是最上等的席位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270672V作为举办茶会的主人，\n',
            '当然有权利站在这里呀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270673V#1026F#2P……咦…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0014, 0)
    ChrSetSubChip(0x0014, 8)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_5DB1')
    def lambda_5DB1():
        OP_99(0x0014, 0x08, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_5DB1)

    Sleep(200)

    Fade(500)

    @scena.Lambda('lambda_5DCB')
    def lambda_5DCB():
        CameraSetDistance(3300, 0)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_5DCB)

    PlaySE(505, 0x00, 0x64)
    WaitForThreadExit(0x0014, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_5DEA')
    def lambda_5DEA():
        OP_99(0x0014, 0x02, 0x01, 1500)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_5DEA)

    WaitForThreadExit(0x0014, 0x0001)
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0014, 10)
    ChrSetSubChip(0x0014, 0)
    OP_0D()
    Sleep(500)

    OP_C5(0x00, 0, 0, 640, 512, 75, 0, 768, 512, 0, 0, 640, 512, 0x00FFFFFF, 0x00, 'C_VIS116._CH')
    OP_C6(0x00, 0x00, 100000, 0, 500)
    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('玲')

    Talk(
        (
            '#0220270674V#1306F执行者ＮＯ．ⅩⅤ。\n',
            '『歼灭天使』玲──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270675V大家都是这样称呼我的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270676V有点没品位的名字，\n',
            '我并不是很喜欢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x03, 16777215, 250, 0)
    Sleep(1000)

    OP_C6(0x00, 0x06, 0, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#0010270677V#1020F#2P…………骗人……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270678V#173F#5P这，这样的孩子…\n',
            '竟是『噬身之蛇』的一员！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0220270679V#263F哈哈哈。\n',
            '『结社』不分孩子和大人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270680V只分有用和没用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270681V#1305F玲很有用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270682V就像从前的『漆黑之牙』一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270683V#1020F#2P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270684V#1069F#5P这、这么说……那个是？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270685V发信给我的\n',
            '是小妹妹你！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0220270686V#1306F嗯嗯，是玲哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270687V#263F恐吓信一共发了９封。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270688V教会的哥哥１封。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270689V情报部的姐姐１封。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270690V还有，艾丝蒂尔１封。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270691V#1305F总共１２封──哈哈哈、\n',
            '好像一直在写信呢，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270692V莱维会夸奖我吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_620D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270693V#057F#5P这、这一切阴谋难道\n',
            '全部是你设计的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_624A')

    def _loc_620D(): pass

    label('loc_620D')

    ChrTalk(
        0x0103,
        (
            '#0030270694V#022F#5P难、难道这一切\n',
            '全部是你设计的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_624A(): pass

    label('loc_624A')

    ChrTalk(
        0x0014,
        (
            '#0220270695V#263F因为玲是招待大家\n',
            '来参加茶会的主人嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270696V让出席的客人\n',
            '感到无聊可不行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270697V我很努力的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270698V#1003F#2P……那………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270699V#1005F那么，爸爸和妈妈呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270700V玲的爸爸妈妈\n',
            '到底怎样了啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0220270701V#264F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270702V#269F啊啊，怎么。\n',
            '还没发现啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270703V#263F哈哈哈，是玲\n',
            '太厉害了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270704V还是艾丝蒂尔你们\n',
            '太迟钝了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270705V#1019F#2P你、你说什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0220270706V#1306F哈哈哈，生气可不好哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270707V……是说这个吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlaySE(189, 0x00, 0x64)
    ChrSetPos(0x0018, -27000, 8500, -2300, 90)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetFlags(0x0018, 0x0020)
    ChrSetFlags(0x0018, 0x0004)
    ChrSetRGBAMask(0x0018, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_649F')
    def lambda_649F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0002, lambda_649F)

    @scena.Lambda('lambda_64B1')
    def lambda_64B1():
        ChrMoveTo(0x00FE, -27000, 8000, -2300, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0003, lambda_64B1)

    Sleep(300)

    PlaySE(189, 0x00, 0x64)
    ChrSetPos(0x0019, -27000, 8500, -3200, 90)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetFlags(0x0019, 0x0020)
    ChrSetFlags(0x0019, 0x0004)
    ChrSetRGBAMask(0x0019, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_6501')
    def lambda_6501():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_6501)

    @scena.Lambda('lambda_6513')
    def lambda_6513():
        ChrMoveTo(0x00FE, -27000, 8000, -3200, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0003, lambda_6513)

    WaitForThreadExit(0x0019, 0x0003)
    Sleep(500)

    ChrTalk(
        0x0018,
        (
            '#0720270708V#1364F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0730270709V#1373F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010270710V#1020F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0220270711V#263F这不是玲的\n',
            '爸爸妈妈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270712V#1306F已经用完了\n',
            '……就要这样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0014, 0x0020)
    ChrSetDirection(0x0014, 180, 400)
    ChrClearFlags(0x0014, 0x0020)
    Fade(250)
    ChrSetChipByIndex(0x0014, 0)
    ChrSetSubChip(0x0014, 1)
    PlaySE(213, 0x00, 0x64)
    OP_0D()
    Sleep(500)

    ChrSetFlags(0x0018, 0x0020)
    ChrSetFlags(0x0019, 0x0020)
    ChrSetFlags(0x0018, 0x0800)
    ChrSetFlags(0x0019, 0x0800)
    ChrClearFlags(0x0018, 0x0001)
    ChrClearFlags(0x0019, 0x0001)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_6667')
    def lambda_6667():
        CameraMove(-34440, 1890, 1870, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6667)

    @scena.Lambda('lambda_667F')
    def lambda_667F():
        OP_67(0, 7000, -10000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_667F)

    @scena.Lambda('lambda_6697')
    def lambda_6697():
        CameraSetDistance(3200, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6697)

    @scena.Lambda('lambda_66A7')
    def lambda_66A7():
        ChrJumpTo(0x00FE, -27290, 8800, -1500, 2000, 10000)

        ExitThread()

    DispatchAsync(0x0014, 0x0000, lambda_66A7)

    Sleep(200)

    PlaySE(505, 0x00, 0x64)

    @scena.Lambda('lambda_66CF')
    def lambda_66CF():
        OP_99(0x0014, 0x01, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_66CF)

    CreateThread(0x0014, 0x01, 0x00, func_26_85BE)
    WaitForThreadExit(0x0014, 0x0000)
    ChrJumpTo(0x0014, -27290, 7300, -1500, 0, 3000)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    Fade(500)
    CameraMove(-22230, 0, -20, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2009, 0)
    OP_6C(315000, 0)
    OP_6E(336, 0)
    OP_0D()

    @scena.Lambda('lambda_6759')
    def lambda_6759():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6759)

    @scena.Lambda('lambda_6767')
    def lambda_6767():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_6767)

    Sleep(100)

    @scena.Lambda('lambda_677A')
    def lambda_677A():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_677A)

    @scena.Lambda('lambda_6788')
    def lambda_6788():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_6788)

    WaitForThreadExit(0x0014, 0x0001)

    ChrTalk(
        0x010F,
        (
            '#0100270713V#173F#2P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270714V#1020F#5P啊啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270715V#1022F你、你、你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010270716V#1005F#6P#3S在干什么啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetDirection(0x00F7, 270, 400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_68A1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270717V#054F#6P镇定、艾丝蒂尔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270718V并没有出血！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68E5')

    def _loc_68A1(): pass

    label('loc_68A1')

    ChrTalk(
        0x0103,
        (
            '#0030270719V#024F#6P艾丝蒂尔、冷静点！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270720V没出血吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_68E5(): pass

    label('loc_68E5')

    ChrTalk(
        0x0101,
        (
            '#0010270721V#1004F#6P咦……啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010270722V#1026F#5P……真……真的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270723V#1067F#2P『结社』制造的自动人偶……\n',
            '而且和人一模一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270724V#1065F真是不得了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0014, 10)
    ChrSetSubChip(0x0014, 0)
    ChrSetPos(0x0014, -27290, 7300, -880, 90)
    Sleep(100)

    Fade(500)
    CameraMove(-34440, 890, 2870, 0)
    OP_67(0, 7990, -10000, 0)
    CameraSetDistance(3420, 0)
    OP_6C(297000, 0)
    OP_6E(272, 0)
    ChrSetDirection(0x0101, 180, 0)
    ChrSetDirection(0x00F7, 180, 0)
    ChrSetDirection(0x0109, 180, 0)
    ChrSetDirection(0x010F, 180, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0014,
        (
            '#0220270725V#263F哈哈哈，玲不在旁边\n',
            '就不能操纵得像人一样了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270726V但也有不输给\n',
            '『人偶骑士』佩德罗的自信哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270727V#1306F啊，不过这次又找了乐子\n',
            '又成为茶会的主人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270728V扮演蒂娅公主的角色也真多啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270729V#1068F#5P开、开啥玩笑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0220270730V#1305F好了，得叫\n',
            '真正的爸爸妈妈来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0014, 47)
    ChrSetSubChip(0x0014, 0)
    OP_0D()
    PlaySE(213, 0x00, 0x64)
    OP_99(0x0014, 0x00, 0x01, 1000)
    Sleep(500)

    ChrTalk(
        0x0014,
        (
            '#0220270731V#263F来吧——帕蒂尔·玛蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    Sleep(500)

    PlaySE(275, 0x01, 0x46)
    OP_24(0x0113, 0x46)
    Sleep(500)

    @scena.Lambda('lambda_6BE5')
    def lambda_6BE5():
        OP_7C(20, 20, 2000, 100)
        Yield()

        Jump('lambda_6BE5')

    DispatchAsync2(0x002F, 0x0003, lambda_6BE5)

    Sleep(1000)

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    CreateThread(0x0101, 0x01, 0x00, func_1E_844D)
    Sleep(50)

    CreateThread(0x00F7, 0x01, 0x00, func_1F_8484)
    Sleep(50)

    CreateThread(0x0109, 0x01, 0x00, func_20_84BB)
    Sleep(50)

    CreateThread(0x010F, 0x01, 0x00, func_21_84FE)
    Sleep(50)

    CreateThread(0x000C, 0x01, 0x00, func_1E_844D)

    @scena.Lambda('lambda_6C3F')
    def lambda_6C3F():
        CameraMove(-24790, 0, -7120, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6C3F)

    @scena.Lambda('lambda_6C57')
    def lambda_6C57():
        OP_6C(225000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6C57)

    @scena.Lambda('lambda_6C67')
    def lambda_6C67():
        CameraSetDistance(4300, 10000)

        ExitThread()

    DispatchAsync(0x010F, 0x0003, lambda_6C67)

    OP_24(0x0113, 0x50)
    Sleep(1000)

    OP_24(0x0113, 0x55)
    Sleep(1000)

    OP_24(0x0113, 0x5A)
    Sleep(1000)

    OP_24(0x0113, 0x5F)
    Sleep(1000)

    OP_24(0x0113, 0x64)

    @scena.Lambda('lambda_6C9F')
    def lambda_6C9F():
        OP_7C(50, 50, 3000, 100)
        Yield()

        Jump('lambda_6C9F')

    DispatchAsync2(0x002F, 0x0003, lambda_6C9F)

    WaitForThreadExit(0x0101, 0x0003)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010270732V#1026F#5P这、这声音是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x010F,
        (
            '#0100270733V#177F#2P上面！　当心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A1(0x0033, 0x0006)
    ChrSetFlags(0x0033, 0x0004)
    ChrClearFlags(0x0033, 0x0080)
    ChrSetFlags(0x0033, 0x0008)
    OP_72(0x0006, 0x0004)
    ChrSetPos(0x0033, -21490, 15000, -8050, 0)
    ChrSetFlags(0x0033, 0x0001)

    ExecExpressionWithValue(
        0x0033,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0033,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000040)
    OP_71(0x0006, 0x0020)
    OP_B0(0x0006, 0x0F)
    OP_6F(0x0006, 241)
    OP_70(0x0006, 260)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_B0(0x0006, 0x0F)
    OP_6F(0x0006, 260)
    OP_70(0x0006, 241)

    @scena.Lambda('lambda_6E43')
    def lambda_6E43():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6E43)

    @scena.Lambda('lambda_6E51')
    def lambda_6E51():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_6E51)

    Sleep(100)

    @scena.Lambda('lambda_6E64')
    def lambda_6E64():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_6E64)

    @scena.Lambda('lambda_6E72')
    def lambda_6E72():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_6E72)

    @scena.Lambda('lambda_6E80')
    def lambda_6E80():
        ChrMoveTo(0x0033, -21490, 0, -8050, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_6E80)

    Sleep(500)

    OP_72(0x0006, 0x0020)
    OP_6F(0x0006, 221)
    OP_70(0x0006, 240)
    WaitForThreadExit(0x0033, 0x0001)
    ChrSetChipByIndex(0x0014, 10)
    ChrSetSubChip(0x0014, 0)
    CameraMove(-22260, 0, -9450, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(212000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0019, 0x0800)
    MapClearFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x002F, 0x03)
    OP_23(0x0113)
    PlaySE(136, 0x00, 0x64)
    PlaySE(245, 0x00, 0x64)
    OP_7C(0, 400, 5000, 1500)
    OP_73(0x0006)
    OP_71(0x0006, 0x0020)
    OP_D8(0x06, 0x01F4)
    OP_6F(0x0006, 1)
    OP_70(0x0006, 40)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    MapSetFlags(0x00000010)

    ChrTalk(
        0x0101,
        (
            '#0010270734V#1020F#3S什！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0640270735V#226F#3S#5P呀呀！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000C, 0x01, 0x00, func_25_859A)
    CreateThread(0x000C, 0x00, 0x00, func_24_857A)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6FEA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270736V#055F好、好大……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7011')

    def _loc_6FEA(): pass

    label('loc_6FEA')

    ChrTalk(
        0x0103,
        (
            '#0030270737V#523F怎么这么大……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7011(): pass

    label('loc_7011')

    ChrTalk(
        0x0109,
        (
            '#0180270738V#1069F#5P什、什么呀！这东西！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7048')
    def lambda_7048():
        OP_6C(237000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7048)

    OP_72(0x0006, 0x0020)

    @scena.Lambda('lambda_705D')
    def lambda_705D():
        ChrSetDirection(0x00FE, 45, 60)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_705D)

    OP_6F(0x0006, 201)
    OP_70(0x0006, 210)
    PlaySE(236, 0x00, 0x64)
    Sleep(300)

    PlaySE(236, 0x00, 0x64)
    Sleep(300)

    PlaySE(236, 0x00, 0x64)
    WaitForThreadExit(0x0033, 0x0001)
    OP_73(0x0006)
    Sleep(500)

    PlaySE(277, 0x00, 0x64)
    OP_B0(0x0006, 0x0A)
    OP_6F(0x0006, 301)
    OP_70(0x0006, 315)
    OP_73(0x0006)
    OP_6F(0x0005, 231)
    OP_70(0x0005, 250)
    OP_7C(300, 300, 3000, 100)
    OP_6F(0x0006, 316)
    OP_70(0x0006, 340)
    PlaySE(966, 0x00, 0x64)
    OP_73(0x0006)
    OP_71(0x0006, 0x0020)
    OP_6F(0x0006, 341)
    OP_70(0x0006, 380)

    ChrTalk(
        0x0101,
        (
            '#0010270739V#1026F#1P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100270740V#173F#1P把『福音』！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_714F')
    def lambda_714F():
        CameraMove(-31920, 0, -6080, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_714F)

    OP_B0(0x0006, 0x19)
    OP_72(0x0006, 0x0020)
    OP_6F(0x0006, 381)
    OP_70(0x0006, 420)
    PlaySE(277, 0x00, 0x64)
    Sleep(800)

    ChrSetAfterImage(0x00, 0x0014, 0x0032, 0x01F4)

    @scena.Lambda('lambda_7190')
    def lambda_7190():
        CameraMove(-25540, 0, -10760, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7190)

    @scena.Lambda('lambda_71A8')
    def lambda_71A8():
        OP_67(0, 5750, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_71A8)

    @scena.Lambda('lambda_71C0')
    def lambda_71C0():
        CameraSetDistance(3750, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_71C0)

    @scena.Lambda('lambda_71D0')
    def lambda_71D0():
        OP_6C(225000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_71D0)

    @scena.Lambda('lambda_71E0')
    def lambda_71E0():
        OP_6E(250, 2000)

        ExitThread()

    DispatchAsync(0x010F, 0x0003, lambda_71E0)

    ChrSetChipByIndex(0x0014, 46)
    ChrSetSubChip(0x0014, 4)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_71FF')
    def lambda_71FF():
        ChrJumpTo(0x0014, -22000, 3000, -5000, 300, 3000)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_71FF)

    Sleep(700)

    OP_CF(0x0014, 0x06, 'Frame85__ren')
    ChrClearFlags(0x0014, 0x0004)
    ChrClearFlags(0x0014, 0x0001)
    ChrSetFlags(0x0014, 0x0020)
    ChrSetChipByIndex(0x0014, 0)
    ChrSetSubChip(0x0014, 0)
    PlaySE(164, 0x00, 0x64)
    ChrSetAfterImage(0x01, 0x0014, 0x0000, 0x0000)
    ChrClearFlags(0x0014, 0x0001)
    ChrSetDirection(0x0014, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0014,
        (
            '#0220270741V#1306F#5P这就是玲的爸爸妈妈『帕蒂尔·玛蒂尔』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270742V像爸爸一样强大，\n',
            '像妈妈一样温柔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270743V除此以外\n',
            '不需要别的爸爸妈妈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Sleep(500)

    ChrSetPos(0x0022, -10900, 0, 230, 270)
    ChrSetPos(0x0023, -10370, 0, -1430, 270)

    NpcTalk(
        0x0022,
        '男人的声音',
        (
            '#2450270744V#2P发、发现目标！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0023,
        '女孩的声音',
        (
            '#0120270745V#5P哇哇，那是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0014, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_73B4')
    def lambda_73B4():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_73B4)

    @scena.Lambda('lambda_73C2')
    def lambda_73C2():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_73C2)

    @scena.Lambda('lambda_73D0')
    def lambda_73D0():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_73D0)

    @scena.Lambda('lambda_73DE')
    def lambda_73DE():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x010F, 0x0000, lambda_73DE)

    @scena.Lambda('lambda_73EC')
    def lambda_73EC():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_73EC)

    Fade(1000)
    CameraMove(-21560, 0, -7400, 0)
    OP_67(0, 4560, -10000, 0)
    CameraSetDistance(8250, 0)
    OP_6C(223000, 0)
    OP_6E(165, 0)
    LoadChip('ED6_DT27/CH04590._CH', 'ED6_DT27/CH04590P._CP', 29)
    LoadChip('ED6_DT27/CH04591._CH', 'ED6_DT27/CH04591P._CP', 30)
    LoadChip('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP', 31)
    LoadChip('ED6_DT07/CH00021._CH', 'ED6_DT07/CH00021P._CP', 32)
    LoadChip('ED6_DT07/CH00051._CH', 'ED6_DT07/CH00051P._CP', 33)
    LoadChip('ED6_DT07/CH00031._CH', 'ED6_DT07/CH00031P._CP', 34)
    LoadChip('ED6_DT07/CH00041._CH', 'ED6_DT07/CH00041P._CP', 35)
    LoadChip('ED6_DT07/CH00061._CH', 'ED6_DT07/CH00061P._CP', 36)
    LoadChip('ED6_DT07/CH00071._CH', 'ED6_DT07/CH00071P._CP', 37)
    LoadChip('ED6_DT27/CH03091._CH', 'ED6_DT27/CH03091P._CP', 39)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0016, 0x0040)
    ChrSetFlags(0x0015, 0x0040)
    ChrSetFlags(0x0022, 0x0040)
    ChrSetFlags(0x0023, 0x0040)
    ChrSetFlags(0x0024, 0x0040)
    ChrSetFlags(0x0025, 0x0040)
    ChrSetFlags(0x0026, 0x0040)
    ChrSetFlags(0x0027, 0x0040)
    ChrSetFlags(0x0028, 0x0040)
    ChrSetFlags(0x0029, 0x0040)
    ChrSetFlags(0x002A, 0x0040)
    ChrSetFlags(0x002B, 0x0040)
    ChrSetPos(0x0013, 6000, 0, -1790, 270)
    ChrSetPos(0x0011, 6000, 0, -1370, 270)
    ChrSetPos(0x0012, 6000, 0, -3420, 270)
    ChrSetPos(0x0010, 6000, 0, -2160, 270)
    ChrSetPos(0x000F, 6000, 0, -2300, 270)
    ChrSetPos(0x0016, 6000, 0, -3260, 270)
    ChrSetPos(0x0015, 8000, 0, 510, 270)
    ChrSetPos(0x0022, 8000, 0, 2500, 270)
    ChrSetPos(0x0023, 8000, 0, 2400, 270)
    ChrSetPos(0x0024, 8000, 0, 800, 270)
    ChrSetPos(0x0025, 8000, 0, -90, 270)
    ChrSetPos(0x0026, 8000, 0, 2110, 270)
    ChrSetPos(0x0027, 8000, 0, 270, 270)
    ChrSetPos(0x0028, 8000, 0, 1610, 270)
    ChrSetPos(0x0029, 8000, 0, 2750, 270)
    ChrSetPos(0x002A, 8000, 0, 2170, 270)
    ChrSetPos(0x002B, 8000, 0, 1040, 270)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
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

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7691',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetPos(0x000E, 6000, 0, -3010, 270)
    CreateThread(0x000E, 0x00, 0x00, func_28_8684)

    Jump('loc_76B3')

    def _loc_7691(): pass

    label('loc_7691')

    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetPos(0x000D, 6000, 0, -3010, 270)
    CreateThread(0x000D, 0x00, 0x00, func_27_865E)

    def _loc_76B3(): pass

    label('loc_76B3')

    CreateThread(0x0013, 0x00, 0x00, func_29_86AA)
    CreateThread(0x0011, 0x00, 0x00, func_2B_8700)
    CreateThread(0x0010, 0x00, 0x00, func_2C_872B)
    CreateThread(0x0012, 0x00, 0x00, func_2A_86D5)
    CreateThread(0x000F, 0x00, 0x00, func_2D_8756)
    CreateThread(0x0016, 0x00, 0x00, func_2E_8781)
    CreateThread(0x0015, 0x00, 0x00, func_2F_87A2)
    CreateThread(0x0022, 0x00, 0x00, func_30_87CD)
    CreateThread(0x0023, 0x00, 0x00, func_31_87F8)
    CreateThread(0x0024, 0x00, 0x00, func_32_8823)
    CreateThread(0x0025, 0x00, 0x00, func_33_884E)
    CreateThread(0x0026, 0x00, 0x00, func_34_8879)
    CreateThread(0x0027, 0x00, 0x00, func_35_88A4)
    CreateThread(0x0028, 0x00, 0x00, func_36_88CF)
    CreateThread(0x0029, 0x00, 0x00, func_37_88FA)
    CreateThread(0x002A, 0x00, 0x00, func_38_8925)
    CreateThread(0x002B, 0x00, 0x00, func_39_8950)
    WaitForThreadExit(0x0013, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0013,
        (
            '#0120270746V#1317F#6P巨、巨人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0015, 0x0000)

    ChrTalk(
        0x0015,
        (
            '#0620270747V#702F#4P怎可能……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_77BC',
    )

    ChrTalk(
        0x000E,
        (
            '#0050270748V#054F#3P怎、怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77E8')

    def _loc_77BC(): pass

    label('loc_77BC')

    ChrTalk(
        0x000D,
        (
            '#0030270749V#024F#3P怎、怎么回事啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_77E8(): pass

    label('loc_77E8')

    ChrTalk(
        0x0011,
        (
            '#0070270750V#065F#6P玲、玲……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010270751V#1026F#5P大家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    CameraMove(-30740, 0, -15630, 0)
    OP_67(0, 2870, -10000, 0)
    CameraSetDistance(5020, 0)
    OP_6C(225000, 0)
    OP_6E(245, 0)
    ChrSetDirection(0x0014, 180, 0)
    ChrSetDirection(0x0013, 270, 0)
    ChrSetDirection(0x0012, 270, 0)
    ChrSetDirection(0x000F, 270, 0)
    ChrSetDirection(0x0017, 270, 0)
    ChrSetDirection(0x0016, 270, 0)
    ChrSetDirection(0x0011, 270, 0)
    ChrSetDirection(0x0010, 270, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0014,
        (
            '#0220270752V#263F#5P哈哈哈，安眠药的效果\n',
            '看来发挥得正是时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270753V就像以前约修亚教的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270754V#1002F#2P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_794D')
    def lambda_794D():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_794D)

    @scena.Lambda('lambda_795B')
    def lambda_795B():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_795B)

    Sleep(100)

    @scena.Lambda('lambda_796E')
    def lambda_796E():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_796E)

    @scena.Lambda('lambda_797C')
    def lambda_797C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x010F, 0x0000, lambda_797C)

    Sleep(100)

    @scena.Lambda('lambda_798F')
    def lambda_798F():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_798F)

    ChrTalk(
        0x0014,
        (
            '#0220270755V#1305F#5P其实啊，本来想\n',
            '杀了艾丝蒂尔的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270756V因为教授，\n',
            '说约修亚不回来\n',
            '是因为艾丝蒂尔嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230705V#1020F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0220270758V#261F#5P不过，因为很开心\n',
            '这次就特别饶了你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270759V哈哈哈，是特别优待哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270760V#1020F#2P等、等等，玲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0070270761V#065F#5P玲、玲！\n',
            '这是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0220270762V#263F#5P哈哈哈，提妲也再见啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270763V和你在一起很开心\n',
            '以后再一起吃冰淇淋吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270764V#1306F那么各位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220270765V今宵大家能出席茶会，\n',
            '实在是感激不尽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_DB()

    @scena.Lambda('lambda_7BAB')
    def lambda_7BAB():
        CameraMove(-21660, 3000, -6840, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7BAB)

    @scena.Lambda('lambda_7BC3')
    def lambda_7BC3():
        CameraSetDistance(2400, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7BC3)

    PlaySE(275, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_7BDD')
    def lambda_7BDD():
        OP_7C(50, 50, 3000, 100)
        Yield()

        Jump('lambda_7BDD')

    DispatchAsync2(0x002F, 0x0003, lambda_7BDD)

    PlaySE(133, 0x01, 0x50)

    @scena.Lambda('lambda_7BFD')
    def lambda_7BFD():
        OP_67(0, 32810, -10000, 25000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7BFD)

    @scena.Lambda('lambda_7C15')
    def lambda_7C15():
        OP_6C(0, 25000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7C15)

    ChrClearFlags(0x002C, 0x0800)
    ChrClearFlags(0x002D, 0x0800)
    ChrClearFlags(0x002E, 0x0800)
    ChrSetFlags(0x0014, 0x0020)
    ChrSetFlags(0x0014, 0x0002)
    ChrSetSubChip(0x0014, 6)
    PlayEffect(0x05, 0x05, 0x0033, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(204, 0x00, 0x64)
    PlayEffect(0x03, 0x03, 0x0033, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x04, 0x0033, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(276, 0x00, 0x64)

    @scena.Lambda('lambda_7CEC')
    def lambda_7CEC():
        ChrMoveTo(0x0033, -21490, 5000, -8050, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_7CEC)

    OP_B0(0x0006, 0x0A)
    OP_71(0x0006, 0x0020)
    OP_D8(0x06, 0x07D0)
    OP_6F(0x0006, 461)
    OP_70(0x0006, 480)
    PlayEffect(0x01, 0x03, 0x0033, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x04, 0x0033, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_7D8C')
    def lambda_7D8C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0000, lambda_7D8C)

    @scena.Lambda('lambda_7D9A')
    def lambda_7D9A():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_7D9A)

    @scena.Lambda('lambda_7DA8')
    def lambda_7DA8():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_7DA8)

    @scena.Lambda('lambda_7DB6')
    def lambda_7DB6():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_7DB6)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7DD6',
    )

    @scena.Lambda('lambda_7DCB')
    def lambda_7DCB():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_7DCB)

    Jump('loc_7DE4')

    def _loc_7DD6(): pass

    label('loc_7DD6')

    @scena.Lambda('lambda_7DDC')
    def lambda_7DDC():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_7DDC)

    def _loc_7DE4(): pass

    label('loc_7DE4')

    @scena.Lambda('lambda_7DEA')
    def lambda_7DEA():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0000, lambda_7DEA)

    @scena.Lambda('lambda_7DF8')
    def lambda_7DF8():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_7DF8)

    @scena.Lambda('lambda_7E06')
    def lambda_7E06():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_7E06)

    @scena.Lambda('lambda_7E14')
    def lambda_7E14():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0022, 0x0000, lambda_7E14)

    @scena.Lambda('lambda_7E22')
    def lambda_7E22():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0023, 0x0000, lambda_7E22)

    @scena.Lambda('lambda_7E30')
    def lambda_7E30():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0024, 0x0000, lambda_7E30)

    @scena.Lambda('lambda_7E3E')
    def lambda_7E3E():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0025, 0x0000, lambda_7E3E)

    @scena.Lambda('lambda_7E4C')
    def lambda_7E4C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0026, 0x0000, lambda_7E4C)

    @scena.Lambda('lambda_7E5A')
    def lambda_7E5A():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0000, lambda_7E5A)

    @scena.Lambda('lambda_7E68')
    def lambda_7E68():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0027, 0x0000, lambda_7E68)

    Sleep(1000)

    @scena.Lambda('lambda_7E7B')
    def lambda_7E7B():
        ChrMoveTo(0x0033, -21490, 5000, -8050, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_7E7B)

    Sleep(1000)

    @scena.Lambda('lambda_7E9B')
    def lambda_7E9B():
        ChrMoveTo(0x0033, -21490, 5000, -8050, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_7E9B)

    OP_71(0x0006, 0x0020)
    OP_B0(0x0006, 0x0A)
    StopEffect(0x05, 0x02)
    Sleep(800)

    @scena.Lambda('lambda_7EC7')
    def lambda_7EC7():
        ChrMoveTo(0x0033, -21490, 5000, -8050, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_7EC7)

    Sleep(800)

    WaitForThreadExit(0x0033, 0x0001)

    @scena.Lambda('lambda_7EEC')
    def lambda_7EEC():
        ChrSetDirection(0x0033, 180, 50)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_7EEC)

    Sleep(500)

    ChrSetSubChip(0x0014, 7)
    Sleep(1000)

    ChrSetSubChip(0x0014, 0)
    WaitForThreadExit(0x0033, 0x0001)

    @scena.Lambda('lambda_7F13')
    def lambda_7F13():
        CameraMove(-21660, 3000, -15000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7F13)

    @scena.Lambda('lambda_7F2B')
    def lambda_7F2B():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_7F2B)

    @scena.Lambda('lambda_7F39')
    def lambda_7F39():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_7F39)

    @scena.Lambda('lambda_7F47')
    def lambda_7F47():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_7F47)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7F67',
    )

    @scena.Lambda('lambda_7F5C')
    def lambda_7F5C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_7F5C)

    Jump('loc_7F75')

    def _loc_7F67(): pass

    label('loc_7F67')

    @scena.Lambda('lambda_7F6D')
    def lambda_7F6D():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_7F6D)

    def _loc_7F75(): pass

    label('loc_7F75')

    @scena.Lambda('lambda_7F7B')
    def lambda_7F7B():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0000, lambda_7F7B)

    @scena.Lambda('lambda_7F89')
    def lambda_7F89():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_7F89)

    @scena.Lambda('lambda_7F97')
    def lambda_7F97():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_7F97)

    OP_72(0x0006, 0x0020)
    OP_6F(0x0006, 481)
    OP_70(0x0006, 500)
    PlaySE(278, 0x00, 0x64)
    OP_73(0x0006)
    OP_71(0x0006, 0x0020)
    OP_6F(0x0006, 501)
    OP_70(0x0006, 520)
    PlaySE(276, 0x00, 0x64)
    PlayEffect(0x01, 0x03, 0x0033, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x04, 0x0033, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x0033, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x0033, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x0033, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x0033, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_8116')
    def lambda_8116():
        ChrMoveToRelative(0x0033, 0, 10000, -55000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_8116)

    Sleep(1500)

    ChrClearFlags(0x0033, 0x0001)

    @scena.Lambda('lambda_813B')
    def lambda_813B():
        ChrMoveToRelative(0x0033, 0, 30000, -55000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_813B)

    Sleep(1500)

    CreateThread(0x0014, 0x03, 0x00, func_3A_897B)

    @scena.Lambda('lambda_8162')
    def lambda_8162():
        OP_7C(500, 500, 3000, 100)
        Yield()

        Jump('lambda_8162')

    DispatchAsync2(0x002F, 0x0003, lambda_8162)

    @scena.Lambda('lambda_817D')
    def lambda_817D():
        ChrMoveToRelative(0x0033, 0, 40000, -55000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_817D)

    Sleep(1500)

    @scena.Lambda('lambda_819D')
    def lambda_819D():
        ChrMoveToRelative(0x0033, 5000, 60000, -55000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_819D)

    Sleep(1000)

    @scena.Lambda('lambda_81BD')
    def lambda_81BD():
        ChrMoveToRelative(0x0033, 5000, 100000, -55000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_81BD)

    Sleep(1000)

    ChrSetSubChip(0x0014, 7)

    @scena.Lambda('lambda_81E2')
    def lambda_81E2():
        ChrMoveToRelative(0x0033, 5000, 150000, -55000, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_81E2)

    Sleep(1000)

    ChrSetSubChip(0x0014, 6)

    @scena.Lambda('lambda_8207')
    def lambda_8207():
        ChrMoveToRelative(0x0033, 5000, 250000, -57000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_8207)

    OP_24(0x0113, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010270766V#5S#30A#5P玲～～！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    FadeOut(4000, 0, -1)
    OP_24(0x0113, 0x50)
    OP_24(0x0085, 0x50)
    Sleep(1000)

    OP_24(0x0113, 0x3C)
    OP_24(0x0085, 0x3C)
    Sleep(1000)

    OP_24(0x0113, 0x28)
    OP_24(0x0085, 0x28)
    Sleep(1000)

    OP_24(0x0113, 0x14)
    OP_24(0x0085, 0x14)
    Sleep(1000)

    OP_23(0x0113)
    OP_20(0x00000BB8)
    TerminateThread(0x002F, 0x03)
    OP_23(0x0085)
    TerminateThread(0x0033, 0x01)
    ChrSetFlags(0x0014, 0x0080)
    OP_71(0x0006, 0x0004)
    WaitForThreadExit(0x0101, 0x0001)
    OP_21()
    OP_0D()
    ChrClearFlags(0x0101, 0x0040)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    Sleep(1000)

    OP_DC()

    OP_CE(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T4313._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x82D6
@scena.Code('func_18_82D6')
def func_18_82D6():
    ChrJumpTo(0x00FE, -17150, 0, -4480, 1500, 5000)
    ChrJumpTo(0x00FE, -19470, 0, -40, 1000, 5000)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0019 offset: 0x830C
@scena.Code('func_19_830C')
def func_19_830C():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetPos(0x00FE, -14240, 0, -12370, 0)
    ChrWalkTo(0x00FE, -10740, 0, -12080, 5000, 0x00)
    ChrWalkTo(0x00FE, -10720, 0, -7190, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x00FE, 48)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x001A offset: 0x8361
@scena.Code('func_1A_8361')
def func_1A_8361():
    ChrSetChipByIndex(0x00FE, 26)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetPos(0x00FE, -14240, 0, -12370, 0)
    ChrWalkTo(0x00FE, -10740, 0, -12080, 5000, 0x00)
    ChrWalkTo(0x00FE, -10100, 0, -8540, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x00FE, 24)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x001B offset: 0x83C0
@scena.Code('func_1B_83C0')
def func_1B_83C0():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetPos(0x00FE, -14240, 0, -12370, 0)
    ChrWalkTo(0x00FE, -17700, 0, -12660, 5000, 0x00)
    ChrWalkTo(0x00FE, -17680, 0, -7270, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x00FE, 48)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x001C offset: 0x8415
@scena.Code('func_1C_8415')
def func_1C_8415():
    ChrWalkTo(0x00FE, -13390, 0, 160, 4000, 0x00)
    ChrTurnDirection(0x00FE, 0x0014, 400)

    Return()

# id: 0x001D offset: 0x8431
@scena.Code('func_1D_8431')
def func_1D_8431():
    ChrWalkTo(0x00FE, -11850, 0, 830, 4000, 0x00)
    ChrTurnDirection(0x00FE, 0x0014, 400)

    Return()

# id: 0x001E offset: 0x844D
@scena.Code('func_1E_844D')
def func_1E_844D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8483',
    )

    Sleep(200)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 270, 400)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 270, 400)

    Jump('func_1E_844D')

    def _loc_8483(): pass

    label('loc_8483')

    Return()

# id: 0x001F offset: 0x8484
@scena.Code('func_1F_8484')
def func_1F_8484():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_84BA',
    )

    Sleep(50)

    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 270, 400)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 270, 400)

    Jump('func_1F_8484')

    def _loc_84BA(): pass

    label('loc_84BA')

    Return()

# id: 0x0020 offset: 0x84BB
@scena.Code('func_20_84BB')
def func_20_84BB():
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(500)

    def _loc_84C7(): pass

    label('loc_84C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_84FD',
    )

    Sleep(150)

    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)

    Jump('loc_84C7')

    def _loc_84FD(): pass

    label('loc_84FD')

    Return()

# id: 0x0021 offset: 0x84FE
@scena.Code('func_21_84FE')
def func_21_84FE():
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(500)

    def _loc_850A(): pass

    label('loc_850A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8540',
    )

    Sleep(100)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)

    Jump('loc_850A')

    def _loc_8540(): pass

    label('loc_8540')

    Return()

# id: 0x0022 offset: 0x8541
@scena.Code('func_22_8541')
def func_22_8541():
    @scena.Lambda('lambda_8547')
    def lambda_8547():
        ChrMoveTo(0x00FE, -15410, 7000, -3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_8547)

    ChrSetDirection(0x00FE, 180, 100)

    Return()

# id: 0x0023 offset: 0x8564
@scena.Code('func_23_8564')
def func_23_8564():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8579',
    )

    OP_99(0x0109, 0x0C, 0x0F, 1500)

    Jump('func_23_8564')

    def _loc_8579(): pass

    label('loc_8579')

    Return()

# id: 0x0024 offset: 0x857A
@scena.Code('func_24_857A')
def func_24_857A():
    ChrWalkTo(0x00FE, -18620, 0, 1570, 4000, 0x00)
    TerminateThread(0x000C, 0x01)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0025 offset: 0x859A
@scena.Code('func_25_859A')
def func_25_859A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_85BD',
    )

    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    Jump('func_25_859A')

    def _loc_85BD(): pass

    label('loc_85BD')

    Return()

# id: 0x0026 offset: 0x85BE
@scena.Code('func_26_85BE')
def func_26_85BE():
    Sleep(200)

    PlaySE(911, 0x00, 0x64)

    @scena.Lambda('lambda_85CE')
    def lambda_85CE():
        OP_99(0x00FE, 0x00, 0x04, 1500)

        ExitThread()

    DispatchAsync(0x0018, 0x0002, lambda_85CE)

    @scena.Lambda('lambda_85DE')
    def lambda_85DE():
        ChrJumpTo(0x0018, -23950, 0, -3220, 50, 7000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_85DE)

    Sleep(50)

    PlaySE(911, 0x00, 0x64)

    @scena.Lambda('lambda_8606')
    def lambda_8606():
        OP_99(0x00FE, 0x00, 0x04, 1500)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_8606)

    @scena.Lambda('lambda_8616')
    def lambda_8616():
        ChrJumpTo(0x0019, -22540, 0, -4300, 50, 7000)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_8616)

    WaitForThreadExit(0x0018, 0x0001)
    PlaySE(209, 0x00, 0x64)

    @scena.Lambda('lambda_863E')
    def lambda_863E():
        OP_99(0x00FE, 0x05, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0018, 0x0002, lambda_863E)

    WaitForThreadExit(0x0019, 0x0001)

    @scena.Lambda('lambda_8653')
    def lambda_8653():
        OP_99(0x00FE, 0x05, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_8653)

    Return()

# id: 0x0027 offset: 0x865E
@scena.Code('func_27_865E')
def func_27_865E():
    ChrSetChipByIndex(0x00FE, 32)
    ChrWalkTo(0x00FE, -16390, 0, -3010, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 3)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0028 offset: 0x8684
@scena.Code('func_28_8684')
def func_28_8684():
    ChrSetChipByIndex(0x00FE, 33)
    ChrWalkTo(0x00FE, -16390, 0, -3010, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 4)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0029 offset: 0x86AA
@scena.Code('func_29_86AA')
def func_29_86AA():
    Sleep(200)

    ChrSetChipByIndex(0x00FE, 39)
    ChrWalkTo(0x00FE, -17210, 0, -1790, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 9)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x002A offset: 0x86D5
@scena.Code('func_2A_86D5')
def func_2A_86D5():
    Sleep(400)

    ChrSetChipByIndex(0x00FE, 37)
    ChrWalkTo(0x00FE, -14770, 0, -3420, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 8)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x002B offset: 0x8700
@scena.Code('func_2B_8700')
def func_2B_8700():
    Sleep(600)

    ChrSetChipByIndex(0x00FE, 36)
    ChrWalkTo(0x00FE, -15860, 0, -1370, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 7)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x002C offset: 0x872B
@scena.Code('func_2C_872B')
def func_2C_872B():
    Sleep(800)

    ChrSetChipByIndex(0x00FE, 35)
    ChrWalkTo(0x00FE, -14900, 0, -2160, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 6)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x002D offset: 0x8756
@scena.Code('func_2D_8756')
def func_2D_8756():
    Sleep(1000)

    ChrSetChipByIndex(0x00FE, 34)
    ChrWalkTo(0x00FE, -13450, 0, -2300, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x002E offset: 0x8781
@scena.Code('func_2E_8781')
def func_2E_8781():
    Sleep(1200)

    ChrWalkTo(0x00FE, -12870, 0, -3260, 5000, 0x00)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x002F offset: 0x87A2
@scena.Code('func_2F_87A2')
def func_2F_87A2():
    Sleep(1500)

    ChrSetChipByIndex(0x00FE, 30)
    ChrWalkTo(0x00FE, -16760, 0, 510, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0030 offset: 0x87CD
@scena.Code('func_30_87CD')
def func_30_87CD():
    Sleep(1700)

    ChrSetChipByIndex(0x00FE, 31)
    ChrWalkTo(0x00FE, -15360, 0, 470, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0031 offset: 0x87F8
@scena.Code('func_31_87F8')
def func_31_87F8():
    Sleep(1900)

    ChrSetChipByIndex(0x00FE, 31)
    ChrWalkTo(0x00FE, -15960, 0, 2400, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0032 offset: 0x8823
@scena.Code('func_32_8823')
def func_32_8823():
    Sleep(2100)

    ChrSetChipByIndex(0x00FE, 31)
    ChrWalkTo(0x00FE, -13830, 0, 800, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0033 offset: 0x884E
@scena.Code('func_33_884E')
def func_33_884E():
    Sleep(2300)

    ChrSetChipByIndex(0x00FE, 31)
    ChrWalkTo(0x00FE, -13250, 0, -90, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0034 offset: 0x8879
@scena.Code('func_34_8879')
def func_34_8879():
    Sleep(2500)

    ChrSetChipByIndex(0x00FE, 31)
    ChrWalkTo(0x00FE, -14350, 0, 2110, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0035 offset: 0x88A4
@scena.Code('func_35_88A4')
def func_35_88A4():
    Sleep(2600)

    ChrSetChipByIndex(0x00FE, 31)
    ChrWalkTo(0x00FE, -11690, 0, 270, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0036 offset: 0x88CF
@scena.Code('func_36_88CF')
def func_36_88CF():
    Sleep(2700)

    ChrSetChipByIndex(0x00FE, 31)
    ChrWalkTo(0x00FE, -12030, 0, 1610, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0037 offset: 0x88FA
@scena.Code('func_37_88FA')
def func_37_88FA():
    Sleep(2900)

    ChrSetChipByIndex(0x00FE, 31)
    ChrWalkTo(0x00FE, -12690, 0, 2750, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0038 offset: 0x8925
@scena.Code('func_38_8925')
def func_38_8925():
    Sleep(3100)

    ChrSetChipByIndex(0x00FE, 31)
    ChrWalkTo(0x00FE, -10530, 0, 2170, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x0039 offset: 0x8950
@scena.Code('func_39_8950')
def func_39_8950():
    Sleep(3300)

    ChrSetChipByIndex(0x00FE, 31)
    ChrWalkTo(0x00FE, -9710, 0, 1040, 6000, 0x00)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetDirection(0x00FE, 215, 400)

    Return()

# id: 0x003A offset: 0x897B
@scena.Code('func_3A_897B')
def func_3A_897B():
    ChrSetFlags(0x0101, 0x0040)

    @scena.Lambda('lambda_8986')
    def lambda_8986():
        ChrWalkTo(0x0101, -21140, 0, -15130, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8986)

    Sleep(800)

    @scena.Lambda('lambda_89A6')
    def lambda_89A6():
        ChrWalkTo(0x00FE, -23040, 0, -15060, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_89A6)

    Sleep(200)

    @scena.Lambda('lambda_89C6')
    def lambda_89C6():
        ChrWalkTo(0x00FE, -19830, 0, -14760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_89C6)

    Sleep(200)

    @scena.Lambda('lambda_89E6')
    def lambda_89E6():
        ChrWalkTo(0x00FE, -21220, 0, -13760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x010F, 0x0000, lambda_89E6)

    Sleep(300)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8A25',
    )

    @scena.Lambda('lambda_8A0D')
    def lambda_8A0D():
        ChrWalkTo(0x00FE, -20060, 0, -13710, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_8A0D)

    Jump('loc_8A40')

    def _loc_8A25(): pass

    label('loc_8A25')

    @scena.Lambda('lambda_8A2B')
    def lambda_8A2B():
        ChrWalkTo(0x00FE, -20060, 0, -13710, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_8A2B)

    def _loc_8A40(): pass

    label('loc_8A40')

    Sleep(200)

    @scena.Lambda('lambda_8A4B')
    def lambda_8A4B():
        ChrWalkTo(0x00FE, -19340, 0, -12600, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_8A4B)

    Sleep(300)

    @scena.Lambda('lambda_8A6B')
    def lambda_8A6B():
        ChrWalkTo(0x00FE, -22320, 0, -13820, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0000, lambda_8A6B)

    Sleep(300)

    @scena.Lambda('lambda_8A8B')
    def lambda_8A8B():
        ChrWalkTo(0x00FE, -21610, 0, -12120, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_8A8B)

    Sleep(200)

    @scena.Lambda('lambda_8AAB')
    def lambda_8AAB():
        ChrWalkTo(0x00FE, -20660, 0, -11090, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_8AAB)

    Sleep(200)

    @scena.Lambda('lambda_8ACB')
    def lambda_8ACB():
        ChrWalkTo(0x00FE, -19490, 0, -10140, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_8ACB)

    Sleep(300)

    @scena.Lambda('lambda_8AEB')
    def lambda_8AEB():
        ChrWalkTo(0x00FE, -21780, 0, -7430, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_8AEB)

    Sleep(200)

    @scena.Lambda('lambda_8B0B')
    def lambda_8B0B():
        ChrWalkTo(0x00FE, -20870, 0, -7000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0000, lambda_8B0B)

    Sleep(300)

    ChrSetChipByIndex(0x0015, 11)

    @scena.Lambda('lambda_8B30')
    def lambda_8B30():
        ChrWalkTo(0x00FE, -20870, 0, -9190, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0000, lambda_8B30)

    Sleep(300)

    @scena.Lambda('lambda_8B50')
    def lambda_8B50():
        ChrWalkTo(0x00FE, -21450, 0, -5360, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0000, lambda_8B50)

    Sleep(200)

    @scena.Lambda('lambda_8B70')
    def lambda_8B70():
        ChrWalkTo(0x00FE, -19910, 0, -5310, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0000, lambda_8B70)

    Sleep(300)

    @scena.Lambda('lambda_8B90')
    def lambda_8B90():
        ChrWalkTo(0x00FE, -18300, 0, -5740, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0000, lambda_8B90)

    @scena.Lambda('lambda_8BAB')
    def lambda_8BAB():
        ChrWalkTo(0x00FE, -20600, 0, -3990, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0000, lambda_8BAB)

    Sleep(300)

    @scena.Lambda('lambda_8BCB')
    def lambda_8BCB():
        ChrWalkTo(0x00FE, -19130, 0, -4170, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0000, lambda_8BCB)

    Sleep(200)

    @scena.Lambda('lambda_8BEB')
    def lambda_8BEB():
        ChrWalkTo(0x00FE, -17440, 0, -4510, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0000, lambda_8BEB)

    Sleep(200)

    @scena.Lambda('lambda_8C0B')
    def lambda_8C0B():
        ChrWalkTo(0x00FE, -18990, 0, -2680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0000, lambda_8C0B)

    Sleep(200)

    @scena.Lambda('lambda_8C2B')
    def lambda_8C2B():
        ChrWalkTo(0x00FE, -17240, 0, -3090, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0000, lambda_8C2B)

    Sleep(200)

    @scena.Lambda('lambda_8C4B')
    def lambda_8C4B():
        ChrWalkTo(0x00FE, -17130, 0, -1470, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0000, lambda_8C4B)

    Sleep(200)

    @scena.Lambda('lambda_8C6B')
    def lambda_8C6B():
        ChrWalkTo(0x00FE, -15680, 0, -2960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002B, 0x0000, lambda_8C6B)

    Return()

# id: 0x003B offset: 0x8C81
@scena.Code('func_3B_8C81')
def func_3B_8C81():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_8CFB'),
        (0x00000001, 'loc_8D01'),
        (-1, 'loc_8D07'),
    )

    def _loc_8CFB(): pass

    label('loc_8CFB')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_8D07')

    def _loc_8D01(): pass

    label('loc_8D01')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_8D07')

    def _loc_8D07(): pass

    label('loc_8D07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_8D15',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    Jump('loc_8D19')

    def _loc_8D15(): pass

    label('loc_8D15')

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    def _loc_8D19(): pass

    label('loc_8D19')

    Return()

# id: 0x003C offset: 0x8D1A
@scena.Code('func_3C_8D1A')
def func_3C_8D1A():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

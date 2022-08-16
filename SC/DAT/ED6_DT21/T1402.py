import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1402_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1402   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1402.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T1402._SN', 'ED6_DT21/T1402_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雪拉扎德',
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
            name                = '阿加特',
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
            name                = '提妲',
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
            name                = '金',
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
            name                = '科洛蒂娅公主',
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
            name                = '奥利维特皇子',
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
            name                = '赛克斯中将',
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
            name                = '摩尔根将军',
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
            name                = '穆拉少校',
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
            name                = '卡西乌斯',
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
            name                = '拉赛尔博士',
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
            name                = '尤莉亚上尉',
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
            name                = '凯文神父',
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
            name                = '王国军将校',
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
            name                = '王国军将校',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '蒸气坦克',
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
            name                = '飞船',
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
            name                = '飞船的影子',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
            name                = '帝国兵',
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
    )

# id: 0x10002 offset: 0xF88
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xF88
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xF88
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xF88
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_FA2',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x74),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_02_FBB)

    Jump('loc_FB9')

    def _loc_FA2(): pass

    label('loc_FA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_FB9',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(1, 0x0002)

    def _loc_FB9(): pass

    label('loc_FB9')

    Return()

# id: 0x0001 offset: 0xFBA
@scena.Code('func_01_FBA')
def func_01_FBA():
    Return()

# id: 0x0002 offset: 0xFBB
@scena.Code('func_02_FBB')
def func_02_FBB():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_A1(0x0017, 0x0003)
    OP_A1(0x0018, 0x0004)
    OP_A1(0x0019, 0x0005)
    OP_A1(0x001A, 0x0006)
    OP_A1(0x001B, 0x0007)
    OP_A1(0x001C, 0x0008)
    OP_A1(0x001D, 0x0009)
    OP_A1(0x001E, 0x000A)
    OP_A1(0x001F, 0x000B)
    OP_A1(0x0020, 0x000C)
    OP_A1(0x0021, 0x000D)
    OP_A1(0x0022, 0x000E)
    OP_A1(0x0023, 0x000F)
    OP_A1(0x0024, 0x0010)
    OP_71(0x0003, 0x0020)
    OP_71(0x0004, 0x0020)
    OP_71(0x0005, 0x0020)
    OP_71(0x0006, 0x0020)
    OP_71(0x0007, 0x0020)
    OP_71(0x0008, 0x0020)
    OP_71(0x0009, 0x0020)
    OP_71(0x000A, 0x0020)
    OP_71(0x000B, 0x0020)
    OP_71(0x000C, 0x0020)
    OP_71(0x000D, 0x0020)
    OP_71(0x000E, 0x0020)
    OP_71(0x000F, 0x0020)
    OP_71(0x0010, 0x0020)
    OP_6F(0x0003, 91)
    OP_6F(0x0004, 91)
    OP_6F(0x0005, 91)
    OP_6F(0x0006, 91)
    OP_6F(0x0007, 91)
    OP_6F(0x0008, 91)
    OP_6F(0x0009, 91)
    OP_6F(0x000A, 91)
    OP_6F(0x000B, 91)
    OP_6F(0x000C, 91)
    OP_6F(0x000D, 91)
    OP_6F(0x000E, 91)
    OP_6F(0x000F, 91)
    OP_6F(0x0010, 91)
    OP_70(0x0003, 150)
    OP_70(0x0004, 150)
    OP_70(0x0005, 150)
    OP_70(0x0006, 150)
    OP_70(0x0007, 150)
    OP_70(0x0008, 150)
    OP_70(0x0009, 150)
    OP_70(0x000A, 150)
    OP_70(0x000B, 150)
    OP_70(0x000C, 150)
    OP_70(0x000D, 150)
    OP_70(0x000E, 150)
    OP_70(0x000F, 150)
    OP_70(0x0010, 150)
    LoadChip('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP', 0)
    LoadChip('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP', 1)
    LoadChip('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP', 2)
    LoadChip('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP', 3)
    LoadChip('ED6_DT27/CH03210._CH', 'ED6_DT27/CH03210P._CP', 4)
    LoadChip('ED6_DT27/CH03680._CH', 'ED6_DT27/CH03680P._CP', 5)
    LoadChip('ED6_DT27/CH03700._CH', 'ED6_DT27/CH03700P._CP', 6)
    LoadChip('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP', 7)
    LoadChip('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP', 8)
    LoadChip('ED6_DT27/CH03800._CH', 'ED6_DT27/CH03800P._CP', 9)
    LoadChip('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP', 10)
    OP_71(0x0002, 0x0004)
    OP_71(0x0011, 0x0004)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 560)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetChipByIndex(0x000A, 2)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetChipByIndex(0x000C, 4)
    ChrSetChipByIndex(0x000D, 5)
    ChrSetChipByIndex(0x000E, 6)
    ChrSetChipByIndex(0x000F, 7)
    ChrSetChipByIndex(0x0010, 8)
    ChrSetChipByIndex(0x0027, 9)
    ChrSetChipByIndex(0x0028, 9)
    ChrSetChipByIndex(0x0029, 9)
    ChrSetChipByIndex(0x002A, 9)
    ChrSetChipByIndex(0x002B, 9)
    ChrSetChipByIndex(0x002C, 9)
    ChrSetChipByIndex(0x002D, 9)
    ChrSetChipByIndex(0x002E, 9)
    ChrSetChipByIndex(0x002F, 9)
    ChrSetChipByIndex(0x0030, 9)
    ChrSetChipByIndex(0x0031, 9)
    ChrSetChipByIndex(0x0032, 9)
    ChrSetChipByIndex(0x0033, 9)
    ChrSetChipByIndex(0x0034, 9)
    ChrSetChipByIndex(0x0035, 9)
    ChrSetChipByIndex(0x0036, 9)
    ChrSetChipByIndex(0x0037, 9)
    ChrSetChipByIndex(0x0038, 9)
    ChrSetChipByIndex(0x0039, 9)
    ChrSetChipByIndex(0x003A, 9)
    ChrSetChipByIndex(0x003B, 9)
    ChrSetChipByIndex(0x003C, 9)
    ChrSetChipByIndex(0x003D, 9)
    ChrSetChipByIndex(0x003E, 9)
    ChrSetChipByIndex(0x003F, 9)
    ChrSetChipByIndex(0x0040, 9)
    ChrSetChipByIndex(0x0041, 9)
    ChrSetChipByIndex(0x0042, 9)
    ChrSetChipByIndex(0x0043, 9)
    ChrSetChipByIndex(0x0044, 9)
    ChrSetChipByIndex(0x0045, 9)
    ChrSetChipByIndex(0x0046, 9)
    ChrSetChipByIndex(0x0047, 9)
    ChrSetChipByIndex(0x0048, 9)
    ChrSetChipByIndex(0x0049, 9)
    ChrSetChipByIndex(0x004A, 9)
    ChrSetChipByIndex(0x004B, 9)
    ChrSetChipByIndex(0x004C, 9)
    ChrSetChipByIndex(0x004D, 9)
    ChrSetChipByIndex(0x004E, 9)
    ChrSetChipByIndex(0x004F, 9)
    ChrSetChipByIndex(0x0050, 9)
    ChrSetChipByIndex(0x0051, 9)
    ChrSetChipByIndex(0x0052, 9)
    ChrSetChipByIndex(0x0053, 9)
    ChrSetChipByIndex(0x0054, 9)
    ChrSetChipByIndex(0x0055, 9)
    ChrSetChipByIndex(0x0056, 9)
    ChrSetChipByIndex(0x0057, 9)
    ChrSetChipByIndex(0x0058, 9)
    ChrSetChipByIndex(0x0059, 9)
    ChrSetChipByIndex(0x005A, 9)
    ChrSetChipByIndex(0x005B, 9)
    ChrSetChipByIndex(0x005C, 9)
    ChrSetChipByIndex(0x005D, 9)
    ChrSetChipByIndex(0x005E, 9)
    ChrSetChipByIndex(0x005F, 9)
    ChrSetChipByIndex(0x0060, 9)
    ChrSetChipByIndex(0x0061, 9)
    ChrSetChipByIndex(0x0062, 9)
    ChrSetChipByIndex(0x0063, 9)
    ChrSetChipByIndex(0x0064, 9)
    ChrSetChipByIndex(0x0065, 9)
    ChrSetChipByIndex(0x0066, 9)
    ChrSetChipByIndex(0x0067, 9)
    ChrSetChipByIndex(0x0068, 9)
    ChrSetChipByIndex(0x0069, 9)
    ChrSetChipByIndex(0x006A, 9)
    ChrSetChipByIndex(0x006B, 9)
    ChrSetChipByIndex(0x006C, 9)
    ChrSetChipByIndex(0x006D, 9)
    ChrSetChipByIndex(0x006E, 9)
    ChrSetChipByIndex(0x006F, 9)
    ChrSetChipByIndex(0x0070, 9)
    ChrSetChipByIndex(0x0071, 9)
    ChrSetChipByIndex(0x0072, 9)
    ChrSetChipByIndex(0x0073, 9)
    ChrSetChipByIndex(0x0074, 9)
    ChrSetChipByIndex(0x0075, 9)
    ChrSetChipByIndex(0x0076, 9)
    ChrSetChipByIndex(0x0077, 9)
    ChrSetChipByIndex(0x0078, 9)
    ChrSetChipByIndex(0x0079, 9)
    ChrSetChipByIndex(0x007A, 9)
    ChrSetChipByIndex(0x007B, 9)
    ChrSetChipByIndex(0x007C, 9)
    ChrSetChipByIndex(0x007D, 9)
    ChrSetChipByIndex(0x007E, 9)
    ChrSetChipByIndex(0x0015, 10)
    ChrSetChipByIndex(0x0016, 10)
    ChrSetPos(0x0017, -7460, 0, 138890, 0)
    ChrSetPos(0x0018, 3360, 0, 138630, 0)
    ChrSetPos(0x0019, -7650, 0, 153070, 0)
    ChrSetPos(0x001A, 3510, 0, 153050, 0)
    ChrSetPos(0x001B, -18530, 0, 142310, 0)
    ChrSetPos(0x001C, 15560, 0, 143270, 0)
    ChrSetPos(0x001D, -19230, 0, 157310, 0)
    ChrSetPos(0x001E, 14300, 0, 157350, 0)
    ChrSetPos(0x001F, -8090, 0, 167010, 0)
    ChrSetPos(0x0020, 3690, 0, 166830, 0)
    ChrSetPos(0x0021, 2670, 0, 183120, 0)
    ChrSetPos(0x0022, -8410, 0, 183060, 0)
    ChrSetPos(0x0023, -19940, 0, 174900, 0)
    ChrSetPos(0x0024, 12450, 0, 174010, 0)
    LoadEffect(0x00, 'map\\\\mp109_00.eff')
    LoadEffect(0x01, 'map\\\\onsen00.eff')
    PlayEffect(0x00, 0xFF, 0x0017, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0017, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0018, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0018, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0019, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0019, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001A, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001A, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001B, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001B, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001C, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001C, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001D, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001D, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001E, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001E, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001F, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001F, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0020, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0020, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0021, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0021, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0022, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0022, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0023, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0023, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0024, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0024, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0017, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0017, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0018, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0018, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0019, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0019, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001A, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001A, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001B, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001B, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001C, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001C, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001D, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001D, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001E, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001E, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001F, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001F, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0020, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0020, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0021, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0021, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0022, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0022, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0023, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0023, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0024, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0024, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    ChrSetPos(0x0027, -7630, 0, 191450, 180)
    ChrSetPos(0x0028, -5660, -50, 191450, 180)
    ChrSetPos(0x0029, -3630, 0, 191450, 180)
    ChrSetPos(0x002A, -1730, 90, 191450, 180)
    ChrSetPos(0x002B, 230, -30, 191450, 180)
    ChrSetPos(0x002C, 2070, -30, 191450, 180)
    ChrSetPos(0x002D, -7630, 40, 193600, 180)
    ChrSetPos(0x002E, -5660, 20, 193600, 180)
    ChrSetPos(0x002F, -3630, -20, 193600, 180)
    ChrSetPos(0x0030, -1730, 50, 193600, 180)
    ChrSetPos(0x0031, 230, -20, 193600, 180)
    ChrSetPos(0x0032, 2070, -50, 193600, 180)
    ChrSetPos(0x0033, -7630, 30, 195750, 180)
    ChrSetPos(0x0034, -5660, 10, 195750, 180)
    ChrSetPos(0x0035, -3630, 20, 195750, 180)
    ChrSetPos(0x0036, -1730, 70, 195750, 180)
    ChrSetPos(0x0037, 230, -10, 195750, 180)
    ChrSetPos(0x0038, 2070, -30, 195750, 180)
    ChrSetPos(0x0039, -7630, -20, 197900, 180)
    ChrSetPos(0x003A, -5660, -40, 197900, 180)
    ChrSetPos(0x003B, -3630, -40, 197900, 180)
    ChrSetPos(0x003C, -1730, 40, 197900, 180)
    ChrSetPos(0x003D, 230, -40, 197900, 180)
    ChrSetPos(0x003E, 2070, -20, 197900, 180)
    ChrSetPos(0x003F, -7630, -40, 200050, 180)
    ChrSetPos(0x0040, -5660, 0, 200050, 180)
    ChrSetPos(0x0041, -3630, 30, 200050, 180)
    ChrSetPos(0x0042, -1730, 60, 200050, 180)
    ChrSetPos(0x0043, 230, 10, 200050, 180)
    ChrSetPos(0x0044, 2070, -20, 200050, 180)
    ChrSetPos(0x0045, 4000, 0, 191450, 180)
    ChrSetPos(0x0046, 5930, -50, 191450, 180)
    ChrSetPos(0x0047, 7900, 0, 191450, 180)
    ChrSetPos(0x0048, 9800, 90, 191450, 180)
    ChrSetPos(0x0049, 11700, -30, 191450, 180)
    ChrSetPos(0x004A, 13540, -30, 191450, 180)
    ChrSetPos(0x004B, 4000, 40, 193600, 180)
    ChrSetPos(0x004C, 5930, 20, 193600, 180)
    ChrSetPos(0x004D, 7900, -20, 193600, 180)
    ChrSetPos(0x004E, 9800, 50, 193600, 180)
    ChrSetPos(0x004F, 11700, -20, 193600, 180)
    ChrSetPos(0x0050, 13540, -50, 193600, 180)
    ChrSetPos(0x0051, 4000, 30, 195750, 180)
    ChrSetPos(0x0052, 5930, 10, 195750, 180)
    ChrSetPos(0x0053, 7900, 20, 195750, 180)
    ChrSetPos(0x0054, 9800, 70, 195750, 180)
    ChrSetPos(0x0055, 11700, -10, 195750, 180)
    ChrSetPos(0x0056, 13540, -30, 195750, 180)
    ChrSetPos(0x0057, 4000, -20, 197900, 180)
    ChrSetPos(0x0058, 5930, -40, 197900, 180)
    ChrSetPos(0x0059, 7900, -40, 197900, 180)
    ChrSetPos(0x005A, 9800, 40, 197900, 180)
    ChrSetPos(0x005B, 11700, -40, 197900, 180)
    ChrSetPos(0x005C, 13540, -20, 197900, 180)
    ChrSetPos(0x005D, 4000, -40, 200050, 180)
    ChrSetPos(0x005E, 5930, 0, 200050, 180)
    ChrSetPos(0x005F, 7900, 30, 200050, 180)
    ChrSetPos(0x0060, 9800, 60, 200050, 180)
    ChrSetPos(0x0061, 11700, 10, 200050, 180)
    ChrSetPos(0x0062, 13540, -20, 200050, 180)
    ChrSetPos(0x0063, -19030, 0, 191450, 180)
    ChrSetPos(0x0064, -17150, -50, 191450, 180)
    ChrSetPos(0x0065, -15270, 0, 191450, 180)
    ChrSetPos(0x0066, -13390, 90, 191450, 180)
    ChrSetPos(0x0067, -11510, -30, 191450, 180)
    ChrSetPos(0x0068, -9600, -30, 191450, 180)
    ChrSetPos(0x0069, -19030, 40, 193600, 180)
    ChrSetPos(0x006A, -17150, 20, 193600, 180)
    ChrSetPos(0x006B, -15270, -20, 193600, 180)
    ChrSetPos(0x006C, -13390, 50, 193600, 180)
    ChrSetPos(0x006D, -11510, -20, 193600, 180)
    ChrSetPos(0x006E, -9600, -50, 193600, 180)
    ChrSetPos(0x006F, -19030, 30, 195750, 180)
    ChrSetPos(0x0070, -17150, 10, 195750, 180)
    ChrSetPos(0x0071, -15270, 20, 195750, 180)
    ChrSetPos(0x0072, -13390, 70, 195750, 180)
    ChrSetPos(0x0073, -11510, -10, 195750, 180)
    ChrSetPos(0x0074, -9600, -30, 195750, 180)
    ChrSetPos(0x0075, -19030, -20, 197900, 180)
    ChrSetPos(0x0076, -17150, -40, 197900, 180)
    ChrSetPos(0x0077, -15270, -40, 197900, 180)
    ChrSetPos(0x0078, -13390, 40, 197900, 180)
    ChrSetPos(0x0079, -11510, -40, 197900, 180)
    ChrSetPos(0x007A, -9600, -20, 197900, 180)
    ChrSetPos(0x007B, -15270, 30, 200050, 180)
    ChrSetPos(0x007C, -13390, 60, 200050, 180)
    ChrSetPos(0x007D, -11510, 10, 200050, 180)
    ChrSetPos(0x007E, -9600, -20, 200050, 180)
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
    ChrClearFlags(0x0049, 0x0080)
    ChrClearFlags(0x004A, 0x0080)
    ChrClearFlags(0x004B, 0x0080)
    ChrClearFlags(0x004C, 0x0080)
    ChrClearFlags(0x004D, 0x0080)
    ChrClearFlags(0x004E, 0x0080)
    ChrClearFlags(0x004F, 0x0080)
    ChrClearFlags(0x0050, 0x0080)
    ChrClearFlags(0x0051, 0x0080)
    ChrClearFlags(0x0052, 0x0080)
    ChrClearFlags(0x0053, 0x0080)
    ChrClearFlags(0x0054, 0x0080)
    ChrClearFlags(0x0055, 0x0080)
    ChrClearFlags(0x0056, 0x0080)
    ChrClearFlags(0x0057, 0x0080)
    ChrClearFlags(0x0058, 0x0080)
    ChrClearFlags(0x0059, 0x0080)
    ChrClearFlags(0x005A, 0x0080)
    ChrClearFlags(0x005B, 0x0080)
    ChrClearFlags(0x005C, 0x0080)
    ChrClearFlags(0x005D, 0x0080)
    ChrClearFlags(0x005E, 0x0080)
    ChrClearFlags(0x005F, 0x0080)
    ChrClearFlags(0x0060, 0x0080)
    ChrClearFlags(0x0061, 0x0080)
    ChrClearFlags(0x0062, 0x0080)
    ChrClearFlags(0x0063, 0x0080)
    ChrClearFlags(0x0064, 0x0080)
    ChrClearFlags(0x0065, 0x0080)
    ChrClearFlags(0x0066, 0x0080)
    ChrClearFlags(0x0067, 0x0080)
    ChrClearFlags(0x0068, 0x0080)
    ChrClearFlags(0x0069, 0x0080)
    ChrClearFlags(0x006A, 0x0080)
    ChrClearFlags(0x006B, 0x0080)
    ChrClearFlags(0x006C, 0x0080)
    ChrClearFlags(0x006D, 0x0080)
    ChrClearFlags(0x006E, 0x0080)
    ChrClearFlags(0x006F, 0x0080)
    ChrClearFlags(0x0070, 0x0080)
    ChrClearFlags(0x0071, 0x0080)
    ChrClearFlags(0x0072, 0x0080)
    ChrClearFlags(0x0073, 0x0080)
    ChrClearFlags(0x0074, 0x0080)
    ChrClearFlags(0x0075, 0x0080)
    ChrClearFlags(0x0076, 0x0080)
    ChrClearFlags(0x0077, 0x0080)
    ChrClearFlags(0x0078, 0x0080)
    ChrClearFlags(0x0079, 0x0080)
    ChrClearFlags(0x007A, 0x0080)
    ChrClearFlags(0x007B, 0x0080)
    ChrClearFlags(0x007C, 0x0080)
    ChrClearFlags(0x007D, 0x0080)
    ChrClearFlags(0x007E, 0x0080)
    ChrSetFlags(0x0027, 0x0200)
    ChrSetFlags(0x0028, 0x0200)
    ChrSetFlags(0x0029, 0x0200)
    ChrSetFlags(0x002A, 0x0200)
    ChrSetFlags(0x002B, 0x0200)
    ChrSetFlags(0x002C, 0x0200)
    ChrSetFlags(0x002D, 0x0200)
    ChrSetFlags(0x002E, 0x0200)
    ChrSetFlags(0x002F, 0x0200)
    ChrSetFlags(0x0030, 0x0200)
    ChrSetFlags(0x0031, 0x0200)
    ChrSetFlags(0x0032, 0x0200)
    ChrSetFlags(0x0033, 0x0200)
    ChrSetFlags(0x0034, 0x0200)
    ChrSetFlags(0x0035, 0x0200)
    ChrSetFlags(0x0036, 0x0200)
    ChrSetFlags(0x0037, 0x0200)
    ChrSetFlags(0x0038, 0x0200)
    ChrSetFlags(0x0039, 0x0200)
    ChrSetFlags(0x003A, 0x0200)
    ChrSetFlags(0x003B, 0x0200)
    ChrSetFlags(0x003C, 0x0200)
    ChrSetFlags(0x003D, 0x0200)
    ChrSetFlags(0x003E, 0x0200)
    ChrSetFlags(0x003F, 0x0200)
    ChrSetFlags(0x0040, 0x0200)
    ChrSetFlags(0x0041, 0x0200)
    ChrSetFlags(0x0042, 0x0200)
    ChrSetFlags(0x0043, 0x0200)
    ChrSetFlags(0x0044, 0x0200)
    ChrSetFlags(0x0045, 0x0200)
    ChrSetFlags(0x0046, 0x0200)
    ChrSetFlags(0x0047, 0x0200)
    ChrSetFlags(0x0048, 0x0200)
    ChrSetFlags(0x0049, 0x0200)
    ChrSetFlags(0x004A, 0x0200)
    ChrSetFlags(0x004B, 0x0200)
    ChrSetFlags(0x004C, 0x0200)
    ChrSetFlags(0x004D, 0x0200)
    ChrSetFlags(0x004E, 0x0200)
    ChrSetFlags(0x004F, 0x0200)
    ChrSetFlags(0x0050, 0x0200)
    ChrSetFlags(0x0051, 0x0200)
    ChrSetFlags(0x0052, 0x0200)
    ChrSetFlags(0x0053, 0x0200)
    ChrSetFlags(0x0054, 0x0200)
    ChrSetFlags(0x0055, 0x0200)
    ChrSetFlags(0x0056, 0x0200)
    ChrSetFlags(0x0057, 0x0200)
    ChrSetFlags(0x0058, 0x0200)
    ChrSetFlags(0x0059, 0x0200)
    ChrSetFlags(0x005A, 0x0200)
    ChrSetFlags(0x005B, 0x0200)
    ChrSetFlags(0x005C, 0x0200)
    ChrSetFlags(0x005D, 0x0200)
    ChrSetFlags(0x005E, 0x0200)
    ChrSetFlags(0x005F, 0x0200)
    ChrSetFlags(0x0060, 0x0200)
    ChrSetFlags(0x0061, 0x0200)
    ChrSetFlags(0x0062, 0x0200)
    ChrSetFlags(0x0063, 0x0200)
    ChrSetFlags(0x0064, 0x0200)
    ChrSetFlags(0x0065, 0x0200)
    ChrSetFlags(0x0066, 0x0200)
    ChrSetFlags(0x0067, 0x0200)
    ChrSetFlags(0x0068, 0x0200)
    ChrSetFlags(0x0069, 0x0200)
    ChrSetFlags(0x006A, 0x0200)
    ChrSetFlags(0x006B, 0x0200)
    ChrSetFlags(0x006C, 0x0200)
    ChrSetFlags(0x006D, 0x0200)
    ChrSetFlags(0x006E, 0x0200)
    ChrSetFlags(0x006F, 0x0200)
    ChrSetFlags(0x0070, 0x0200)
    ChrSetFlags(0x0071, 0x0200)
    ChrSetFlags(0x0072, 0x0200)
    ChrSetFlags(0x0073, 0x0200)
    ChrSetFlags(0x0074, 0x0200)
    ChrSetFlags(0x0075, 0x0200)
    ChrSetFlags(0x0076, 0x0200)
    ChrSetFlags(0x0077, 0x0200)
    ChrSetFlags(0x0078, 0x0200)
    ChrSetFlags(0x0079, 0x0200)
    ChrSetFlags(0x007A, 0x0200)
    ChrSetFlags(0x007B, 0x0200)
    ChrSetFlags(0x007C, 0x0200)
    ChrSetFlags(0x007D, 0x0200)
    ChrSetFlags(0x007E, 0x0200)
    CameraMove(-2280, 20, 175640, 0)
    OP_67(0, 6080, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    CreateThread(0x0017, 0x03, 0x00, func_0E_74D2)
    Sleep(1500)

    PlaySE(271, 0x01, 0x64)
    PlaySE(272, 0x01, 0x5A)
    CreateThread(0x0027, 0x03, 0x00, func_0F_7702)
    CreateThread(0x0045, 0x03, 0x00, func_10_7A7D)
    CreateThread(0x0063, 0x03, 0x00, func_11_7DF8)
    WaitForThreadExit(0x0027, 0x0003)
    WaitForThreadExit(0x0045, 0x0003)
    WaitForThreadExit(0x0063, 0x0003)
    OP_C8(0x0200, 0x0046, 'C_PLAC25._CH', 0x00, 0x03E8)
    ShowPlaceName('哈肯大门')
    FadeIn(1000, 0)

    @scena.Lambda('lambda_2A39')
    def lambda_2A39():
        CameraMove(-3610, -30, 118060, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A39)

    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    CameraMove(-1640, 90, 110610, 0)
    OP_67(0, 4500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(45000, 0)
    OP_6E(267, 0)
    LoadEffect(0x00, 'battle\\\\btbomb00.eff')
    PlayEffect(0x01, 0xFF, 0x0017, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0017, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0018, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0018, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0019, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0019, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001A, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001A, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001B, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001B, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001C, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001C, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001D, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001D, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001E, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001E, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001F, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x001F, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0020, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0020, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0021, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0021, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0022, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0022, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0023, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0023, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0024, 1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0024, -1050, 4000, 1800, 0, 30, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    ChrSetPos(0x000F, -1440, 40, 53120, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x0015, -630, 30, 51290, 0)
    ChrSetPos(0x0016, -2300, 50, 51290, 0)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x000E, -2040, 40, 115000, 180)
    ChrClearFlags(0x000E, 0x0080)

    @scena.Lambda('lambda_30D3')
    def lambda_30D3():
        ChrWalkTo(0x00FE, -1830, 50, 95750, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_30D3)

    ChrSetPos(0x0027, -2870, -20, 116520, 180)
    ChrSetPos(0x0028, -1230, 30, 116650, 180)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0028, 0x0080)
    ChrClearFlags(0x0027, 0x0200)
    ChrClearFlags(0x0028, 0x0200)

    @scena.Lambda('lambda_3124')
    def lambda_3124():
        ChrWalkTo(0x00FE, -2770, 50, 98150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_3124)

    @scena.Lambda('lambda_313F')
    def lambda_313F():
        ChrWalkTo(0x00FE, -890, 0, 98150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_313F)

    OP_0D()

    @scena.Lambda('lambda_315B')
    def lambda_315B():
        CameraMove(20, 20, 49800, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_315B)

    @scena.Lambda('lambda_3173')
    def lambda_3173():
        OP_67(0, 3950, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3173)

    @scena.Lambda('lambda_318B')
    def lambda_318B():
        CameraSetDistance(3000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_318B)

    @scena.Lambda('lambda_319B')
    def lambda_319B():
        OP_6C(141000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_319B)

    OP_6E(511, 10000)
    Sleep(1000)

    Fade(500)
    ChrSetFlags(0x0045, 0x0080)
    ChrSetFlags(0x0046, 0x0080)
    ChrSetFlags(0x0047, 0x0080)
    ChrSetFlags(0x0048, 0x0080)
    ChrSetFlags(0x0049, 0x0080)
    ChrSetFlags(0x004A, 0x0080)
    ChrSetFlags(0x004B, 0x0080)
    ChrSetFlags(0x004C, 0x0080)
    ChrSetFlags(0x004D, 0x0080)
    ChrSetFlags(0x004E, 0x0080)
    ChrSetFlags(0x004F, 0x0080)
    ChrSetFlags(0x0050, 0x0080)
    ChrSetFlags(0x0051, 0x0080)
    ChrSetFlags(0x0052, 0x0080)
    ChrSetFlags(0x0053, 0x0080)
    ChrSetFlags(0x0054, 0x0080)
    ChrSetFlags(0x0055, 0x0080)
    ChrSetFlags(0x0056, 0x0080)
    ChrSetFlags(0x0057, 0x0080)
    ChrSetFlags(0x0058, 0x0080)
    ChrSetFlags(0x0059, 0x0080)
    ChrSetFlags(0x005A, 0x0080)
    ChrSetFlags(0x005B, 0x0080)
    ChrSetFlags(0x005C, 0x0080)
    ChrSetFlags(0x005D, 0x0080)
    ChrSetFlags(0x005E, 0x0080)
    ChrSetFlags(0x005F, 0x0080)
    ChrSetFlags(0x0060, 0x0080)
    ChrSetFlags(0x0061, 0x0080)
    ChrSetFlags(0x0062, 0x0080)
    ChrSetFlags(0x0063, 0x0080)
    ChrSetFlags(0x0064, 0x0080)
    ChrSetFlags(0x0065, 0x0080)
    ChrSetFlags(0x0066, 0x0080)
    ChrSetFlags(0x0067, 0x0080)
    ChrSetFlags(0x0068, 0x0080)
    ChrSetFlags(0x0069, 0x0080)
    ChrSetFlags(0x006A, 0x0080)
    ChrSetFlags(0x006B, 0x0080)
    ChrSetFlags(0x006C, 0x0080)
    ChrSetFlags(0x006D, 0x0080)
    ChrSetFlags(0x006E, 0x0080)
    ChrSetFlags(0x006F, 0x0080)
    ChrSetFlags(0x0070, 0x0080)
    ChrSetFlags(0x0071, 0x0080)
    ChrSetFlags(0x0072, 0x0080)
    ChrSetFlags(0x0073, 0x0080)
    ChrSetFlags(0x0074, 0x0080)
    ChrSetFlags(0x0075, 0x0080)
    ChrSetFlags(0x0076, 0x0080)
    ChrSetFlags(0x0077, 0x0080)
    ChrSetFlags(0x0078, 0x0080)
    ChrSetFlags(0x0079, 0x0080)
    ChrSetFlags(0x007A, 0x0080)
    ChrSetFlags(0x007B, 0x0080)
    ChrSetFlags(0x007C, 0x0080)
    ChrSetFlags(0x007D, 0x0080)
    ChrSetFlags(0x007E, 0x0080)
    CameraMove(-1840, 20, 98080, 0)
    OP_67(0, 2800, -10000, 0)
    CameraSetDistance(2029, 0)
    OP_6C(359000, 0)
    OP_6E(554, 0)
    ChrSetPos(0x000F, -1500, 80, 82610, 0)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x000F,
        (
            '#0600380643V#162F#5P解释一下吧！\n',
            '赛克斯·范德尔中将！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600380644V为何帝国军的师团\n',
            '会出现在这里！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600380645V刚刚签订了互不侵犯条约，\n',
            '可别说你已经忘了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380646V#882F#5P摩尔根将军……\n',
            '想得到解释的\n',
            '倒不如说是我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600380647V#161F#5P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380648V#884F#5P前些日子，帝国南部街道上\n',
            '的导力器全部无法工作了，\n',
            '而且异常现象持续不断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380649V这是因出现在贵国上空的\n',
            '巨大谜之物体而造成的，\n',
            '我们收到了这样的报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380650V#880F这到底是怎么一回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600380651V#166F#5P……这没什么好问的，\n',
            '就如你刚才所说的那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600380652V我们王国也正因为突然出现的灾难\n',
            '而处于混乱状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380653V#884F#5P看得出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380654V#882F但这灾祸正在侵蚀我们帝国\n',
            '的领土也是事实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380655V因此，我们会在这里的理由\n',
            '你们应该也能够理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600380656V#160F#5P你们……\n',
            '打算乘虚而入吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380657V#884F#5P我先说在前头，\n',
            '帝国方没这个意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380658V#881F有可疑的犯罪组织\n',
            '趁着这异常现象在王国内\n',
            '四处捣乱，这些我也听说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380659V作为缔结了互不侵犯条约的同盟国，\n',
            '希望能够出份力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380660V我们帝国政府\n',
            '正是这样的意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600380661V#162F#5P真是笑话……\n',
            '那么那些战车是什么！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600380662V蒸气驱动的战车\n',
            '我至今为止就没听说过！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600380663V为什么那种东西恰巧\n',
            '会在这种情形下被派遣到这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380664V#884F#5P这……我只能说是军事机密吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380665V#881F然而，正因为有这战车，\n',
            '才能缓和市民们的不安，\n',
            '它正适合解救贵国的困境，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380666V您能理解吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600380667V#166F#5P可…可恶…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000C, -800, 0, 82000, 0)

    NpcTalk(
        0x000C,
        '女孩的声音',
        (
            '#0060380668V#5P……你们这么费心，\n',
            '我感到十分高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600380669V#161F#5P！？',
            TxtCtl.Enter,
        ),
    )

    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CloseMessageWindow()
    Sleep(1000)

    Fade(1000)
    CameraMove(110, -20, 18300, 0)
    OP_67(0, 5340, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(139000, 0)
    OP_6E(302, 0)
    ChrSetPos(0x000F, -1440, 40, 53120, 0)
    ChrSetPos(0x000C, 140, -10, 19820, 0)
    ChrSetPos(0x0101, -420, -30, 18190, 0)
    ChrSetPos(0x0102, 790, 60, 18260, 0)
    ChrSetPos(0x0008, -1400, -20, 17170, 0)
    ChrSetPos(0x000A, 1680, 40, 16900, 0)
    ChrSetPos(0x000B, -830, -20, 15200, 0)
    ChrSetPos(0x0009, 1270, 20, 15600, 0)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_3A64')
    def lambda_3A64():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3A64)

    @scena.Lambda('lambda_3A7F')
    def lambda_3A7F():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3A7F)

    @scena.Lambda('lambda_3A9A')
    def lambda_3A9A():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3A9A)

    @scena.Lambda('lambda_3AB5')
    def lambda_3AB5():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3AB5)

    @scena.Lambda('lambda_3AD0')
    def lambda_3AD0():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3AD0)

    @scena.Lambda('lambda_3AEB')
    def lambda_3AEB():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3AEB)

    @scena.Lambda('lambda_3B06')
    def lambda_3B06():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3B06)

    @scena.Lambda('lambda_3B21')
    def lambda_3B21():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_3B21')

    DispatchAsync2(0x000F, 0x0001, lambda_3B21)

    ChrSetDirection(0x0015, 180, 0)
    ChrSetDirection(0x0016, 180, 0)
    OP_0D()
    CameraMove(-50, 60, 23000, 3000)
    Fade(1000)
    CameraMove(640, 10, 51040, 0)
    OP_67(0, 4740, -10000, 0)
    CameraSetDistance(3040, 0)
    OP_6C(135000, 0)
    OP_6E(322, 0)
    CreateThread(0x000C, 0x01, 0x00, func_03_733A)
    CreateThread(0x0101, 0x01, 0x00, func_04_7374)
    CreateThread(0x0102, 0x01, 0x00, func_05_739A)
    CreateThread(0x0008, 0x01, 0x00, func_06_73C0)
    CreateThread(0x000A, 0x01, 0x00, func_07_73E6)
    CreateThread(0x0009, 0x01, 0x00, func_08_740C)
    CreateThread(0x000B, 0x01, 0x00, func_09_7432)
    OP_0D()
    Sleep(1000)

    CreateThread(0x0015, 0x01, 0x00, func_0A_7458)
    CreateThread(0x0016, 0x01, 0x00, func_0B_7474)
    WaitForThreadExit(0x000C, 0x0001)
    OP_62(0x000F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000F,
        (
            '#0600380670V#161F#4P什…什么…！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600380671V（公、公主殿下！？\n',
            '  怎么会在这里！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3C4B')
    def lambda_3C4B():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3C4B)

    OP_C5(0x00, 0, 0, 640, 512, 75, 0, 768, 512, 0, 0, 640, 512, 0x00FFFFFF, 0x00, 'C_VIS224._CH')
    OP_C6(0x00, 0x00, 55000, 50000, 0)
    OP_C6(0x00, 0x00, 105000, 50000, 500)
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('科洛蒂娅公主')

    Talk(
        (
            '#0060380672V（摩尔根将军，您辛苦了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380673V（这里的谈判\n',
            '  可以交给我吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('摩尔根将军')

    Talk(
        (
            '#0600380674V#161F（可、可是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x03, 16777215, 250, 0)
    TerminateThread(0x000F, 0x01)
    ChrSetDirection(0x000F, 180, 400)
    Sleep(300)

    ChrTalk(
        0x000F,
        (
            '#0600380675V#162F#6P（而且为什么\n',
            '  连你们都在这里！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380676V#1006F#2P（算是科洛丝的护卫吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380677V#1040F#2P（还有，万不得已的时候\n',
            '  我们打算进行调停。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600380678V#160F#6P（……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380679V#1167F#5P（不成熟的我或许无法\n',
            '  胜任交涉的任务……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380680V#1162F（然而，身为王太女，我想现在应该是\n',
            '  履行王太女义务的时候了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380681V（总之……拜托您了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600380682V#163F#6P（……明白了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 90, 400)
    Sleep(300)

    ChrTalk(
        0x000F,
        (
            '#0600380683V#166F#4P（但是，现在不知道\n',
            '  对方何时会发动攻击。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600380684V（万不得已的时候请立即\n',
            '  做好退向大门的准备。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380685V#1168F#5P（……明白了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000C, 0, 400)
    Sleep(500)

    @scena.Lambda('lambda_4008')
    def lambda_4008():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_4008')

    DispatchAsync2(0x000F, 0x0001, lambda_4008)

    @scena.Lambda('lambda_4019')
    def lambda_4019():
        CameraMove(-380, 80, 55800, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4019)

    @scena.Lambda('lambda_4031')
    def lambda_4031():
        OP_67(0, 5920, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4031)

    @scena.Lambda('lambda_4049')
    def lambda_4049():
        CameraSetDistance(2120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4049)

    @scena.Lambda('lambda_4059')
    def lambda_4059():
        OP_6C(32000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4059)

    @scena.Lambda('lambda_4069')
    def lambda_4069():
        OP_6E(414, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_4069)

    ChrWalkTo(0x000C, -810, 10, 55140, 1500, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x000F, 0x01)

    @scena.Lambda('lambda_4096')
    def lambda_4096():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_4096)

    @scena.Lambda('lambda_40A4')
    def lambda_40A4():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_40A4)

    ChrSetDirection(0x0016, 0, 400)
    ChrSetPos(0x000E, -1230, 60, 73610, 180)
    ChrSetFlags(0x000E, 0x0080)

    ChrTalk(
        0x000E,
        (
            '#0690380686V#880F看来交涉对象\n',
            '似乎换人了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380687V看起来，好像是\n',
            '身份相当高贵的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380688V#1167F#4P幸会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380689V#1162F我的名字是\n',
            '科洛蒂娅·冯·奥赛雷丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380690V身为利贝尔女王艾莉茜雅的孙女，\n',
            '前几天刚被立为下任女王。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380691V#883F#3S！！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380692V这、这真是失敬！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380693V#882F在下名为\n',
            '赛克斯·范德尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380694V埃雷波尼亚帝国军——\n',
            '第３师团所属的中将。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380695V#1160F#4P您就是……\n',
            '久闻大名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-190, 20, 50280, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010380696V#1015F#6P（那个大叔，很有名吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380697V#1042F#2P（『独眼赛克斯』……\n',
            '是帝国屈指可数的名将啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-1840, 20, 98080, 0)
    OP_67(0, 2800, -10000, 0)
    CameraSetDistance(2029, 0)
    OP_6C(359000, 0)
    OP_6E(554, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000C, -1500, 80, 82610, 0)
    ChrSetPos(0x000E, -1830, 50, 95750, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0690380698V#883F#5P不过，以前\n',
            '曾有幸见过殿下的照片……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380699V您剪过头发了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380700V#1165F#5P非常抱歉……\n',
            '我刚刚完成王位继承的仪式。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380701V#1382F请视之为一名女子在面对重任时\n',
            '表达决心的方式吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380702V#884F#5P不、不过这形象\n',
            '也非常适合您啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380703V#881F那……\n',
            '衷心祝贺您\n',
            '成为王太女殿下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380704V#1168F#5P非常感谢，中将。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-820, 30, 53250, 0)
    OP_67(0, 2970, -10000, 0)
    CameraSetDistance(1750, 0)
    OP_6C(180000, 0)
    OP_6E(554, 0)
    ChrSetPos(0x000C, -810, 10, 55140, 0)
    ChrSetPos(0x000E, -800, 0, 67260, 180)
    ChrSetPos(0x0101, -900, 80, 47870, 0)
    ChrSetPos(0x0102, 60, 80, 47660, 0)
    ChrSetPos(0x0008, -1730, 20, 46400, 0)
    ChrSetPos(0x000A, 810, -30, 46380, 0)
    ChrSetPos(0x0009, 1400, 50, 45360, 0)
    ChrSetPos(0x000B, -100, 80, 44800, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0690380705V#882F#5P那么……王太女殿下\n',
            '怎么会出现在这种地方？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0690380706V是和摩尔根将军一样\n',
            '来向我们抗议的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380707V#1167F#5P不……\n',
            '并没有这个打算。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380708V帝国南部的居民\n',
            '想必也经历了\n',
            '不少不安的事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380709V#1169F夜晚的黑暗、寒冷、信息的断绝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380710V全都是十分\n',
            '令人不安的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380711V#880F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380712V#1162F#5P然而，希望你们考虑一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380713V如果贵国的军队就这样进入\n',
            '我国的话，将会造成何种局面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380714V#1167F原本，我们全国就处在\n',
            '比贵国更加混乱的状况下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380715V就算你们没有其它意图，\n',
            '但因此而动摇的市民也绝不会在少数……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380716V#1163F若是导致误解了贵国的善意，\n',
            '我认为这对民众是莫大的损害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380717V#883F#5P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380718V#1160F#5P目前，我们\n',
            '将以摸索、解决这次的异常现象\n',
            '作为最优先的事项。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380719V而对于前面所说的犯罪组织，\n',
            '我们也能够以自己的力量来应对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380720V#1167F为了避免互不侵犯条约\n',
            '所培养出的友情产生无意义的裂痕……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380721V#1162F请你们暂时\n',
            '给我们一点时间好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380722V#884F#5P………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000D, -1200, 0, 67260, 180)

    NpcTalk(
        0x000D,
        '青年的声音',
        (
            '#0040380723V#5P……很遗憾，\n',
            '这只是你们的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    CameraMove(-2390, 10, 114680, 0)
    OP_67(0, 7930, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(0, 0)
    OP_6E(440, 0)
    ChrSetPos(0x0010, -2720, -20, 116010, 180)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x000E, -1830, 50, 95750, 180)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000D, -1960, 50, 114500, 180)

    @scena.Lambda('lambda_4B0B')
    def lambda_4B0B():
        ChrWalkTo(0x00FE, -1870, 10, 102420, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4B0B)

    @scena.Lambda('lambda_4B26')
    def lambda_4B26():
        ChrWalkTo(0x00FE, -2750, 30, 103720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_4B26)

    OP_0D()

    @scena.Lambda('lambda_4B42')
    def lambda_4B42():
        CameraMove(-2000, 100, 103900, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4B42)

    @scena.Lambda('lambda_4B5A')
    def lambda_4B5A():
        OP_67(0, 3090, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4B5A)

    @scena.Lambda('lambda_4B72')
    def lambda_4B72():
        CameraSetDistance(2760, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4B72)

    @scena.Lambda('lambda_4B82')
    def lambda_4B82():
        OP_6E(340, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4B82)

    ChrSetDirection(0x000E, 0, 400)
    ChrSetDirection(0x0027, 0, 400)
    ChrSetDirection(0x0028, 0, 400)
    Sleep(2000)

    CreateThread(0x0027, 0x00, 0x00, func_0C_7495)
    CreateThread(0x0028, 0x00, 0x00, func_0D_74B1)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000E,
        (
            '#0690380724V#883F#6P……皇子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C5(0x01, 0, 0, 640, 512, 75, 0, 768, 512, 0, 0, 640, 512, 0x00FFFFFF, 0x00, 'C_VIS223._CH')
    OP_C6(0x01, 0x00, 70000, 50000, 0)
    OP_C6(0x01, 0x00, 120000, 50000, 500)
    OP_C6(0x01, 0x03, -1, 1000, 0)
    Sleep(1200)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('穿军装的青年')

    Talk(
        (
            '#0040380725V这里就交给我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380726V你退下，中将。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('赛克斯中将')

    Talk(
        (
            '#0690380727V#884F……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x01, 0x03, 16777215, 250, 0)
    Sleep(500)

    Fade(500)
    CameraMove(1670, -30, 48330, 0)
    OP_67(0, 4510, -10000, 0)
    CameraSetDistance(3270, 0)
    OP_6C(135000, 0)
    OP_6E(304, 0)
    ChrSetPos(0x0101, -1300, 80, 47870, 0)
    ChrSetPos(0x0102, 360, 80, 47660, 0)
    ChrSetPos(0x0008, -1530, 20, 46400, 0)
    ChrSetPos(0x000A, 610, -30, 46380, 0)
    ChrSetPos(0x0009, 1350, 50, 45360, 0)
    ChrSetPos(0x000B, 0, 80, 44800, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010380728V#1020F#5P……咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030380729V#023F#2P不会吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050380730V#055F#5P开玩笑吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-20, 10, 101410, 0)
    OP_67(0, 4580, -10000, 0)
    CameraSetDistance(3350, 0)
    OP_6C(44000, 0)
    OP_6E(299, 0)

    @scena.Lambda('lambda_4E40')
    def lambda_4E40():
        CameraMove(-990, 20, 95740, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4E40)

    @scena.Lambda('lambda_4E58')
    def lambda_4E58():
        CameraSetDistance(2890, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4E58)

    @scena.Lambda('lambda_4E68')
    def lambda_4E68():
        ChrWalkTo(0x00FE, -1930, 50, 94710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4E68)

    Sleep(200)

    @scena.Lambda('lambda_4E88')
    def lambda_4E88():
        ChrWalkTo(0x00FE, -1500, 20, 97080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_4E88)

    Sleep(500)

    ChrSetDirection(0x000E, 90, 400)

    @scena.Lambda('lambda_4EAF')
    def lambda_4EAF():
        ChrMoveTo(0x00FE, -3380, -40, 95890, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4EAF)

    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)
    ChrSetDirection(0x000E, 180, 400)
    WaitForThreadExit(0x0010, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    ChrSetDirection(0x0027, 180, 400)
    ChrSetDirection(0x0028, 180, 400)

    NpcTalk(
        0x000D,
        '穿军装的青年',
        (
            '#0040380731V#894F#5P幸会。\n',
            '科洛蒂娅公主殿下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380732V#895F我是埃雷波尼亚皇帝尤肯特之子，\n',
            '奥利维特·莱泽·亚诺尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    ChrSetPos(0x0101, -5000, 10, 85000, 0)
    ChrSetPos(0x0008, -5000, 10, 85000, 0)

    ChrTalk(
        0x0101,
        (
            '#0010380733V#1020F#1P！！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380734V#1005F（皇帝之子……\n',
            '  那、那不就是皇子殿下～！？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380735V（雪拉姐，你知道的吗！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030380736V#023F#1P（怎、怎么可能知道！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030380737V#025F（我还以为一定是\n',
            '  帝国派来的情报员……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-1840, 20, 98080, 0)
    OP_67(0, 2800, -10000, 0)
    CameraSetDistance(2029, 0)
    OP_6C(359000, 0)
    OP_6E(554, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000D, -1850, 50, 94710, 180)
    ChrSetPos(0x0010, -850, 20, 97080, 180)
    ChrSetPos(0x000E, -2850, -20, 96930, 180)
    ChrSetPos(0x000C, -1500, 80, 82610, 0)
    ChrSetPos(0x0101, -1600, 10, 82610, 0)
    ChrSetPos(0x0102, -1500, 10, 82610, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0060380738V#1164F#5P奥利维特皇子……\n',
            '虽然只知道名号。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380739V#891F#5P呵呵，虽说是皇子，\n',
            '但并不是正室所生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380740V很少出席正式场合，\n',
            '所以不知道长相也不足为奇。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380741V#895F不过，话虽如此，\n',
            '也还是吃了一惊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380742V虽然最终还是无缘，\n',
            '但至少也是曾经许婚的对象，\n',
            '还以为至少会知道长相呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380743V#1020F#5P！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380744V#1019F（什、什么～！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380745V#1043F#2P（是吗……\n',
            '  上校说过的那件事吗。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380746V#1163F#5P是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380747V#1167F虽然这件事我并未得知，\n',
            '但真是对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380748V#894F#5P听说这门婚事是在\n',
            '女王陛下不知道的情况下进行的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380749V所以请不必在意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380750V#896F但是……\n',
            '此次的事态就没有那么简单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380751V#1163F#5P……啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380752V#896F#5P科洛蒂娅公主。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380753V现在，帝国正在流传着\n',
            '怎样的传闻，您知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380754V#1169F#5P……不，我孤陋寡闻了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380755V#899F#5P那么我来告诉您吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380756V#897F远方看见的那个巨大构造物……\n',
            '传闻是王国军研制的新兵器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380757V#1164F#5P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380758V#899F#5P『利贝尔军发明了\n',
            '  能够停止导力的跨时代新兵器。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380759V『他们似乎想使用那座兵器\n',
            '  谋划着对１０年前的报复。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380760V#897F──这种传闻\n',
            '正在帝国境内广泛地流传着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380761V#1163F#5P怎、怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380762V#1166F这是误解！\n',
            '我们怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380763V#896F#5P那么……\n',
            '您能证明这是误解吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380764V#1169F#5P……唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380765V#899F#5P既然无法做到，\n',
            '那也只好我们自行\n',
            '做出相应的对策了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380766V不仅如此，如果传言是真的，\n',
            '那就是利用互不侵犯条约来掩人耳目，\n',
            '暗中却策划着重大的背信行为。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380767V#896F呵呵……那样的话，我们\n',
            '进行正当防卫，不也是理所当然的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(1670, -30, 48330, 0)
    OP_67(0, 4550, -10000, 0)
    CameraSetDistance(3270, 0)
    OP_6C(135000, 0)
    OP_6E(304, 0)
    ChrSetPos(0x0101, -1300, 80, 47870, 0)
    ChrSetPos(0x0008, -1530, 20, 46400, 0)
    ChrSetPos(0x000C, -810, 10, 55140, 0)
    ChrSetPos(0x0102, 360, 80, 47660, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    PlaySE(47, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010380768V#1005F#2P#4S你适可而止吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_58E5')
    def lambda_58E5():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_58E5')

    DispatchAsync2(0x0102, 0x0001, lambda_58E5)

    Sleep(50)

    @scena.Lambda('lambda_58FB')
    def lambda_58FB():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_58FB')

    DispatchAsync2(0x000C, 0x0001, lambda_58FB)

    Sleep(50)

    @scena.Lambda('lambda_5911')
    def lambda_5911():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_5911')

    DispatchAsync2(0x0009, 0x0001, lambda_5911)

    Sleep(50)

    @scena.Lambda('lambda_5927')
    def lambda_5927():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_5927')

    DispatchAsync2(0x000A, 0x0001, lambda_5927)

    Sleep(50)

    @scena.Lambda('lambda_593D')
    def lambda_593D():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_593D')

    DispatchAsync2(0x000F, 0x0001, lambda_593D)

    ChrTalk(
        0x0102,
        (
            '#0020380769V#1044F#5P艾丝蒂尔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0070380770V#065F#5P姐，姐姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_599D')
    def lambda_599D():
        CameraMove(-1800, 50, 54200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_599D)

    @scena.Lambda('lambda_59B5')
    def lambda_59B5():
        CameraSetDistance(2950, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_59B5)

    ChrWalkTo(0x0101, -2540, 40, 55190, 6000, 0x00)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x000A, 0x01)
    ChrSetDirection(0x0102, 0, 400)
    ChrSetDirection(0x000A, 0, 400)
    ChrSetDirection(0x000F, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010380771V#1005F#2P我们没出声，\n',
            '你竟然就开始得意忘形，信口开河！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380772V奥利维尔也大致明白\n',
            '我们的情况吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380773V怎么还能说出\n',
            '那么可恶的话来！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380774V#1163F#5P艾、艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000D, -5500, 20, 67000, 180)

    ChrTalk(
        0x000D,
        (
            '#0040380775V#897F#2P哎呀……你是谁？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380776V好像认识我一样，\n',
            '是在哪个舞会上见过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380777V#1004F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000C, 0, 400)

    ChrTalk(
        0x000D,
        (
            '#0040380778V#890F#2P不，以贵族来说\n',
            '似乎略欠些气质……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380779V唔，怎么看都是\n',
            '平民的女儿啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380780V#891F那，你是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010380781V#1019F#2P……好家伙。\n',
            '要装傻到底是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380782V既然你这么说，\n',
            '我也有我的做法!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380783V#895F#2P噢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5FD3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010380784V#1005F#2P我的名字叫\n',
            '艾丝蒂尔·布莱特！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380785V是从属于利贝尔游击士协会\n',
            '的Ａ级游击士！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380786V就让我彻底从中立的立场\n',
            '来介入这个问题吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetDirection(0x000C, 270, 400)

    ChrTalk(
        0x000C,
        (
            '#0060380787V#1164F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0041050033V#898F#2P哦，Ａ级游击士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380788V#891F（……哼哼。\n',
            '　做得不错嘛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380789V#1004F#2P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380790V#899F#2P失、失敬了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380791V#897F所谓的Ａ级，无论在各国的游击士协会\n',
            '都是只有最顶级的实力者才会\n',
            '被授予的等级啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380792V老实说，像你这样的少女竟然也是Ａ级游击士，\n',
            '实在让人很难相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380793V#1006F#2P那样的话，就请您\n',
            '同游击士协会进行询问对质好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380794V不过在那期间，\n',
            '交涉就要暂时中断了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380795V#895F#2P呼……不必了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380796V#896F你说要站在中立的立场上介入,\n',
            '那这个状况下你打算怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6807')

    def _loc_5FD3(): pass

    label('loc_5FD3')

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_61D5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010380784V#1005F#2P我的名字叫\n',
            '艾丝蒂尔·布莱特！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380798V是从属于利贝尔游击士协会\n',
            '的Ｂ级游击士！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380786V就让我彻底从中立的立场\n',
            '来介入这个问题吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetDirection(0x000C, 270, 400)

    ChrTalk(
        0x000C,
        (
            '#0060380787V#1164F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380801V#898F#2P原来如此，是游击士吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380802V#895F嗯，Ｂ级的话，\n',
            '确实是相当高的等级，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380803V#1002F#2P还是不能信任吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380804V#894F#2P哪里的话，失敬了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380805V#896F你说要站在中立的立场上介入,\n',
            '那这个状况下你打算怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6807')

    def _loc_61D5(): pass

    label('loc_61D5')

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_637A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010380784V#1005F#2P我的名字叫\n',
            '艾丝蒂尔·布莱特！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380807V是从属于利贝尔游击士协会\n',
            '的Ｃ级游击士！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380786V就让我彻底从中立的立场\n',
            '来介入这个问题吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetDirection(0x000C, 270, 400)

    ChrTalk(
        0x000C,
        (
            '#0060380787V#1164F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380810V#895F#2P原来如此，是游击士吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380811V#894F嗯，Ｃ级的话，\n',
            '也算是有一定功绩的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380796V#896F你说要站在中立的立场上介入,\n',
            '那这个状况下你打算怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6807')

    def _loc_637A(): pass

    label('loc_637A')

    If(
        (
            (Expr.PushValueByIndex, 0x2F),
            (Expr.PushLong, 0x6),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_65BC',
    )

    ChrTalk(
        0x0101,
        (
            '#0010380784V#1005F#2P我的名字叫\n',
            '艾丝蒂尔·布莱特！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380814V是从属于利贝尔游击士协会\n',
            '的Ｄ级游击士！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380786V就让我彻底从中立的立场\n',
            '来介入这个问题吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetDirection(0x000C, 270, 400)

    ChrTalk(
        0x000C,
        (
            '#0060380787V#1164F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380817V#895F#2P喔，是游击士吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380818V#894F嗯……我听说游击士的等级\n',
            '从Ｇ级到Ａ级共有七个等级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380819V#896F区区一个Ｄ级游击士的话，\n',
            '你认为会有多大的信服力呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380820V#1026F#2P那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380821V#890F#2P算了，继续说下去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380822V你说站在中立的立场上介入，\n',
            '那这个状况下你打算怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6807')

    def _loc_65BC(): pass

    label('loc_65BC')

    ChrTalk(
        0x0101,
        (
            '#0010380784V#1005F#2P我的名字叫\n',
            '艾丝蒂尔·布莱特！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380824V是从属于利贝尔游击士协会\n',
            '的Ｅ级游击士！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380786V就让我彻底从中立的立场\n',
            '来介入这个问题吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetDirection(0x000C, 270, 400)

    ChrTalk(
        0x000C,
        (
            '#0060380787V#1164F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380827V#898F#2P喔，是游击士吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380828V#895F嗯……我听说游击士的等级\n',
            '从Ｇ级到Ａ级共有七个等级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380829V你这种等级连中流都排不上，\n',
            '又有什么好说的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380830V#1019F#2P呜……那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380831V#891F#2P算了，看在你拥有如此胆量\n',
            '的面子上，就继续说下去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380832V#895F你说站在中立的立场上介入,\n',
            '那这个状况下你打算怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6807(): pass

    label('loc_6807')

    ChrSetDirection(0x000C, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010380833V#1005F#2P那个浮游都市\n',
            '不是利贝尔的兵器。\n',
            '我在此正式宣言！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380834V以我的『游击士徽章』作担保！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380835V#895F#2P噢……了不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380836V#899F游击士协会的发言确实\n',
            '有着不可忽视的影响力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380837V#897F然而这个宣言\n',
            '有多少根据呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380838V#1007F#2P不需要根据，因为\n',
            '从头到尾我们都亲眼见到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380839V#1002F让浮游都市出现的\n',
            '就是现在在利贝尔暗中活动着的\n',
            '一个叫『噬身之蛇』结社组织。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380840V我们正和王国军协力\n',
            '阻止他们的阴谋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380841V#1006F想知道详细情况的话，我们向帝国政府\n',
            '提出报告书也没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380842V#894F#2P唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380843V这样一说\n',
            '不得不稍微考虑一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380844V#896F但你似乎\n',
            '忽略了最关键的事情吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380845V#1026F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380846V#897F#2P假设那个什么结社\n',
            '是犯人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380847V那么你们到底有没有\n',
            '阻止这个异常现象的方法呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010380848V#1003F#2P这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380849V#895F#2P如果没有，我们\n',
            '也不可能袖手旁观。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380850V蒸气坦克装载的\n',
            '是火药式的大炮。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380851V要攻陷那个浮游都市，\n',
            '你不认为正合适吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380852V#1020F#2P开、开玩笑吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380853V大炮什么的怎么可能\n',
            '打下那个巨大的城市！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380854V#896F#2P呵呵……\n',
            '不试试看怎么知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380855V#894F无论如何……\n',
            '现在有一件事可以确定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380856V#897F就是你们\n',
            '并没有拒绝我们善意行动\n',
            '的理由和实力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380857V#1003F#2P可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380858V#1162F#5P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380859V#1167F那么……\n',
            '只要能证明就可以了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380860V#898F#2P噢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380861V#1162F#5P只要我们\n',
            '能够证明可以独立查明那个\n',
            '浮游都市的可能性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380862V在时间上就可以给我们\n',
            '一些宽限吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0040380863V#899F#2P唔，这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380864V#895F虽然只是暂时的，\n',
            '但也不得不如此了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-990, 20, 95740, 0)
    OP_67(0, 4580, -10000, 0)
    CameraSetDistance(3350, 0)
    OP_6C(44000, 0)
    OP_6E(299, 0)
    ChrSetPos(0x000D, -1930, 50, 94710, 180)
    ChrSetPos(0x0010, -1500, 20, 97080, 180)
    ChrSetPos(0x000E, -3070, -20, 96930, 180)
    OP_0D()
    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0690380865V#883F#5P（皇、皇子……！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 270, 400)
    Sleep(300)

    ChrTalk(
        0x000D,
        (
            '#0040380866V#896F#2P（镇定，中将。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380867V（面对缔结了互不侵犯条约的对方，\n',
            '　这是必要的礼仪吧。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380868V（而且要他们能够证明才行。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0690380869V#884F#5P（……是。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 180, 400)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0040380870V#899F#5P那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380871V#895F只要你们能够拿出王国拥有独力查明这个问题\n',
            '的可能性，我便保证暂时撤退。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040380872V以『黄金之军马』徽章，\n',
            '以及我身为皇族的名誉为担保。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0160380873V这份宣言，我收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0027, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0028, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    CameraMove(390, -20, 49480, 0)
    OP_67(0, 4550, -10000, 0)
    CameraSetDistance(3600, 0)
    OP_6C(135000, 0)
    OP_6E(304, 0)
    ChrSetPos(0x0102, 360, 80, 47660, 0)
    ChrSetPos(0x0008, -1530, 20, 46400, 0)
    ChrSetPos(0x000A, 610, -30, 46380, 0)
    ChrSetPos(0x0009, 1350, 50, 45360, 0)
    ChrSetPos(0x000B, 0, 80, 44800, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010380874V#1004F#5P刚、刚才的声音是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030380875V#023F#2P难不成……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0080380876V#070F#2P啊啊……不会错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050380877V#055F#5P喂喂，真的假的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380878V#1044F#5P……父亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_23(0x010F)
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x733A
@scena.Code('func_03_733A')
def func_03_733A():
    ChrSetPos(0x000C, -1360, 30, 43020, 0)
    ChrWalkTo(0x00FE, -500, 50, 49330, 2000, 0x00)
    ChrWalkTo(0x00FE, 0, 20, 53090, 2000, 0x00)

    Return()

# id: 0x0004 offset: 0x7374
@scena.Code('func_04_7374')
def func_04_7374():
    ChrSetPos(0x0101, -1300, 40, 40490, 0)
    ChrWalkTo(0x00FE, -1300, 80, 47870, 2000, 0x00)

    Return()

# id: 0x0005 offset: 0x739A
@scena.Code('func_05_739A')
def func_05_739A():
    ChrSetPos(0x0102, 360, 20, 41150, 0)
    ChrWalkTo(0x00FE, 360, 80, 47660, 2000, 0x00)

    Return()

# id: 0x0006 offset: 0x73C0
@scena.Code('func_06_73C0')
def func_06_73C0():
    ChrSetPos(0x0008, -1530, -20, 38220, 0)
    ChrWalkTo(0x00FE, -1530, 20, 46400, 2000, 0x00)

    Return()

# id: 0x0007 offset: 0x73E6
@scena.Code('func_07_73E6')
def func_07_73E6():
    ChrSetPos(0x000A, 610, 20, 39320, 0)
    ChrWalkTo(0x00FE, 610, -30, 46380, 2000, 0x00)

    Return()

# id: 0x0008 offset: 0x740C
@scena.Code('func_08_740C')
def func_08_740C():
    ChrSetPos(0x0009, 1350, 20, 37510, 0)
    ChrWalkTo(0x00FE, 1350, 50, 45360, 2000, 0x00)

    Return()

# id: 0x0009 offset: 0x7432
@scena.Code('func_09_7432')
def func_09_7432():
    ChrSetPos(0x000B, 0, 30, 35900, 0)
    ChrWalkTo(0x00FE, 0, 80, 44800, 2000, 0x00)

    Return()

# id: 0x000A offset: 0x7458
@scena.Code('func_0A_7458')
def func_0A_7458():
    ChrSetDirection(0x00FE, 270, 400)
    ChrMoveTo(0x00FE, 1600, -20, 50600, 2000, 0x00)

    Return()

# id: 0x000B offset: 0x7474
@scena.Code('func_0B_7474')
def func_0B_7474():
    Sleep(100)

    ChrSetDirection(0x00FE, 90, 400)
    ChrMoveTo(0x00FE, -3370, 30, 50630, 2000, 0x00)

    Return()

# id: 0x000C offset: 0x7495
@scena.Code('func_0C_7495')
def func_0C_7495():
    ChrSetDirection(0x00FE, 90, 400)
    ChrMoveTo(0x00FE, -3900, 20, 98320, 2000, 0x00)

    Return()

# id: 0x000D offset: 0x74B1
@scena.Code('func_0D_74B1')
def func_0D_74B1():
    Sleep(100)

    ChrSetDirection(0x00FE, 270, 400)
    ChrMoveTo(0x00FE, 40, 10, 98140, 2000, 0x00)

    Return()

# id: 0x000E offset: 0x74D2
@scena.Code('func_0E_74D2')
def func_0E_74D2():
    @scena.Lambda('lambda_74D8')
    def lambda_74D8():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_74D8)

    Sleep(170)

    @scena.Lambda('lambda_74F8')
    def lambda_74F8():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_74F8)

    @scena.Lambda('lambda_7513')
    def lambda_7513():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_7513)

    Sleep(200)

    @scena.Lambda('lambda_7533')
    def lambda_7533():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_7533)

    @scena.Lambda('lambda_754E')
    def lambda_754E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_754E)

    Sleep(160)

    @scena.Lambda('lambda_756E')
    def lambda_756E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_756E)

    @scena.Lambda('lambda_7589')
    def lambda_7589():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_7589)

    Sleep(230)

    @scena.Lambda('lambda_75A9')
    def lambda_75A9():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_75A9)

    @scena.Lambda('lambda_75C4')
    def lambda_75C4():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_75C4)

    Sleep(150)

    @scena.Lambda('lambda_75E4')
    def lambda_75E4():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_75E4)

    @scena.Lambda('lambda_75FF')
    def lambda_75FF():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_75FF)

    Sleep(180)

    @scena.Lambda('lambda_761F')
    def lambda_761F():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_761F)

    @scena.Lambda('lambda_763A')
    def lambda_763A():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_763A)

    Sleep(150)

    @scena.Lambda('lambda_765A')
    def lambda_765A():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_765A)

    WaitForThreadExit(0x0017, 0x0001)
    OP_72(0x0003, 0x0020)
    WaitForThreadExit(0x0018, 0x0001)
    OP_72(0x0004, 0x0020)
    WaitForThreadExit(0x001B, 0x0001)
    OP_72(0x0005, 0x0020)
    WaitForThreadExit(0x001C, 0x0001)
    OP_72(0x0006, 0x0020)
    WaitForThreadExit(0x0019, 0x0001)
    OP_72(0x0007, 0x0020)
    WaitForThreadExit(0x001A, 0x0001)
    OP_72(0x0008, 0x0020)
    WaitForThreadExit(0x001D, 0x0001)
    OP_72(0x0009, 0x0020)
    WaitForThreadExit(0x001E, 0x0001)
    OP_72(0x000A, 0x0020)
    WaitForThreadExit(0x001F, 0x0001)
    OP_72(0x000B, 0x0020)
    WaitForThreadExit(0x0020, 0x0001)
    OP_72(0x000C, 0x0020)
    WaitForThreadExit(0x0023, 0x0001)
    OP_72(0x000D, 0x0020)
    WaitForThreadExit(0x0024, 0x0001)
    OP_72(0x000E, 0x0020)
    WaitForThreadExit(0x0021, 0x0001)
    OP_72(0x000F, 0x0020)
    WaitForThreadExit(0x0022, 0x0001)
    OP_72(0x0010, 0x0020)
    OP_23(0x010F)
    OP_23(0x0110)

    Return()

# id: 0x000F offset: 0x7702
@scena.Code('func_0F_7702')
def func_0F_7702():
    @scena.Lambda('lambda_7708')
    def lambda_7708():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_7708)

    Sleep(80)

    @scena.Lambda('lambda_7728')
    def lambda_7728():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_7728)

    @scena.Lambda('lambda_7743')
    def lambda_7743():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_7743)

    Sleep(50)

    @scena.Lambda('lambda_7763')
    def lambda_7763():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0001, lambda_7763)

    Sleep(100)

    @scena.Lambda('lambda_7783')
    def lambda_7783():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_7783)

    @scena.Lambda('lambda_779E')
    def lambda_779E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_779E)

    Sleep(50)

    @scena.Lambda('lambda_77BE')
    def lambda_77BE():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_77BE)

    Sleep(40)

    @scena.Lambda('lambda_77DE')
    def lambda_77DE():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0031, 0x0001, lambda_77DE)

    @scena.Lambda('lambda_77F9')
    def lambda_77F9():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002F, 0x0001, lambda_77F9)

    Sleep(70)

    @scena.Lambda('lambda_7819')
    def lambda_7819():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0030, 0x0001, lambda_7819)

    @scena.Lambda('lambda_7834')
    def lambda_7834():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x002E, 0x0001, lambda_7834)

    Sleep(80)

    @scena.Lambda('lambda_7854')
    def lambda_7854():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0032, 0x0001, lambda_7854)

    @scena.Lambda('lambda_786F')
    def lambda_786F():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0033, 0x0001, lambda_786F)

    Sleep(60)

    @scena.Lambda('lambda_788F')
    def lambda_788F():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0037, 0x0001, lambda_788F)

    @scena.Lambda('lambda_78AA')
    def lambda_78AA():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0034, 0x0001, lambda_78AA)

    Sleep(80)

    @scena.Lambda('lambda_78CA')
    def lambda_78CA():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0036, 0x0001, lambda_78CA)

    @scena.Lambda('lambda_78E5')
    def lambda_78E5():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0038, 0x0001, lambda_78E5)

    Sleep(100)

    @scena.Lambda('lambda_7905')
    def lambda_7905():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0035, 0x0001, lambda_7905)

    Sleep(30)

    @scena.Lambda('lambda_7925')
    def lambda_7925():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003E, 0x0001, lambda_7925)

    @scena.Lambda('lambda_7940')
    def lambda_7940():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003A, 0x0001, lambda_7940)

    Sleep(80)

    @scena.Lambda('lambda_7960')
    def lambda_7960():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003C, 0x0001, lambda_7960)

    @scena.Lambda('lambda_797B')
    def lambda_797B():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0039, 0x0001, lambda_797B)

    Sleep(90)

    @scena.Lambda('lambda_799B')
    def lambda_799B():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003B, 0x0001, lambda_799B)

    @scena.Lambda('lambda_79B6')
    def lambda_79B6():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003D, 0x0001, lambda_79B6)

    Sleep(100)

    @scena.Lambda('lambda_79D6')
    def lambda_79D6():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0042, 0x0001, lambda_79D6)

    @scena.Lambda('lambda_79F1')
    def lambda_79F1():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x003F, 0x0001, lambda_79F1)

    Sleep(30)

    @scena.Lambda('lambda_7A11')
    def lambda_7A11():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0040, 0x0001, lambda_7A11)

    @scena.Lambda('lambda_7A2C')
    def lambda_7A2C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0043, 0x0001, lambda_7A2C)

    Sleep(60)

    @scena.Lambda('lambda_7A4C')
    def lambda_7A4C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0041, 0x0001, lambda_7A4C)

    @scena.Lambda('lambda_7A67')
    def lambda_7A67():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0044, 0x0001, lambda_7A67)

    Return()

# id: 0x0010 offset: 0x7A7D
@scena.Code('func_10_7A7D')
def func_10_7A7D():
    @scena.Lambda('lambda_7A83')
    def lambda_7A83():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0046, 0x0001, lambda_7A83)

    Sleep(80)

    @scena.Lambda('lambda_7AA3')
    def lambda_7AA3():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0047, 0x0001, lambda_7AA3)

    @scena.Lambda('lambda_7ABE')
    def lambda_7ABE():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0049, 0x0001, lambda_7ABE)

    Sleep(50)

    @scena.Lambda('lambda_7ADE')
    def lambda_7ADE():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0048, 0x0001, lambda_7ADE)

    Sleep(100)

    @scena.Lambda('lambda_7AFE')
    def lambda_7AFE():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0045, 0x0001, lambda_7AFE)

    @scena.Lambda('lambda_7B19')
    def lambda_7B19():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004A, 0x0001, lambda_7B19)

    Sleep(50)

    @scena.Lambda('lambda_7B39')
    def lambda_7B39():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004B, 0x0001, lambda_7B39)

    Sleep(40)

    @scena.Lambda('lambda_7B59')
    def lambda_7B59():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004F, 0x0001, lambda_7B59)

    @scena.Lambda('lambda_7B74')
    def lambda_7B74():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004D, 0x0001, lambda_7B74)

    Sleep(70)

    @scena.Lambda('lambda_7B94')
    def lambda_7B94():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004E, 0x0001, lambda_7B94)

    @scena.Lambda('lambda_7BAF')
    def lambda_7BAF():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x004C, 0x0001, lambda_7BAF)

    Sleep(80)

    @scena.Lambda('lambda_7BCF')
    def lambda_7BCF():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0050, 0x0001, lambda_7BCF)

    @scena.Lambda('lambda_7BEA')
    def lambda_7BEA():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0051, 0x0001, lambda_7BEA)

    Sleep(60)

    @scena.Lambda('lambda_7C0A')
    def lambda_7C0A():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0055, 0x0001, lambda_7C0A)

    @scena.Lambda('lambda_7C25')
    def lambda_7C25():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0052, 0x0001, lambda_7C25)

    Sleep(80)

    @scena.Lambda('lambda_7C45')
    def lambda_7C45():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0054, 0x0001, lambda_7C45)

    @scena.Lambda('lambda_7C60')
    def lambda_7C60():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0056, 0x0001, lambda_7C60)

    Sleep(100)

    @scena.Lambda('lambda_7C80')
    def lambda_7C80():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0053, 0x0001, lambda_7C80)

    Sleep(30)

    @scena.Lambda('lambda_7CA0')
    def lambda_7CA0():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005C, 0x0001, lambda_7CA0)

    @scena.Lambda('lambda_7CBB')
    def lambda_7CBB():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0058, 0x0001, lambda_7CBB)

    Sleep(80)

    @scena.Lambda('lambda_7CDB')
    def lambda_7CDB():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005A, 0x0001, lambda_7CDB)

    @scena.Lambda('lambda_7CF6')
    def lambda_7CF6():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0057, 0x0001, lambda_7CF6)

    Sleep(90)

    @scena.Lambda('lambda_7D16')
    def lambda_7D16():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0059, 0x0001, lambda_7D16)

    @scena.Lambda('lambda_7D31')
    def lambda_7D31():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005B, 0x0001, lambda_7D31)

    Sleep(100)

    @scena.Lambda('lambda_7D51')
    def lambda_7D51():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0060, 0x0001, lambda_7D51)

    @scena.Lambda('lambda_7D6C')
    def lambda_7D6C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005D, 0x0001, lambda_7D6C)

    Sleep(30)

    @scena.Lambda('lambda_7D8C')
    def lambda_7D8C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005E, 0x0001, lambda_7D8C)

    @scena.Lambda('lambda_7DA7')
    def lambda_7DA7():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0061, 0x0001, lambda_7DA7)

    Sleep(60)

    @scena.Lambda('lambda_7DC7')
    def lambda_7DC7():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x005F, 0x0001, lambda_7DC7)

    @scena.Lambda('lambda_7DE2')
    def lambda_7DE2():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0062, 0x0001, lambda_7DE2)

    Return()

# id: 0x0011 offset: 0x7DF8
@scena.Code('func_11_7DF8')
def func_11_7DF8():
    Sleep(80)

    @scena.Lambda('lambda_7E03')
    def lambda_7E03():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0065, 0x0001, lambda_7E03)

    @scena.Lambda('lambda_7E1E')
    def lambda_7E1E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0067, 0x0001, lambda_7E1E)

    Sleep(50)

    @scena.Lambda('lambda_7E3E')
    def lambda_7E3E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0066, 0x0001, lambda_7E3E)

    Sleep(100)

    @scena.Lambda('lambda_7E5E')
    def lambda_7E5E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0068, 0x0001, lambda_7E5E)

    Sleep(50)

    Sleep(40)

    @scena.Lambda('lambda_7E83')
    def lambda_7E83():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x006D, 0x0001, lambda_7E83)

    @scena.Lambda('lambda_7E9E')
    def lambda_7E9E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x006B, 0x0001, lambda_7E9E)

    Sleep(70)

    @scena.Lambda('lambda_7EBE')
    def lambda_7EBE():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x006C, 0x0001, lambda_7EBE)

    Sleep(80)

    @scena.Lambda('lambda_7EDE')
    def lambda_7EDE():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x006E, 0x0001, lambda_7EDE)

    Sleep(60)

    @scena.Lambda('lambda_7EFE')
    def lambda_7EFE():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0073, 0x0001, lambda_7EFE)

    Sleep(80)

    @scena.Lambda('lambda_7F1E')
    def lambda_7F1E():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0072, 0x0001, lambda_7F1E)

    @scena.Lambda('lambda_7F39')
    def lambda_7F39():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0074, 0x0001, lambda_7F39)

    Sleep(100)

    @scena.Lambda('lambda_7F59')
    def lambda_7F59():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0071, 0x0001, lambda_7F59)

    Sleep(30)

    @scena.Lambda('lambda_7F79')
    def lambda_7F79():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x007A, 0x0001, lambda_7F79)

    Sleep(80)

    @scena.Lambda('lambda_7F99')
    def lambda_7F99():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0078, 0x0001, lambda_7F99)

    Sleep(90)

    @scena.Lambda('lambda_7FB9')
    def lambda_7FB9():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0077, 0x0001, lambda_7FB9)

    @scena.Lambda('lambda_7FD4')
    def lambda_7FD4():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0079, 0x0001, lambda_7FD4)

    Sleep(100)

    @scena.Lambda('lambda_7FF4')
    def lambda_7FF4():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x007C, 0x0001, lambda_7FF4)

    Sleep(30)

    @scena.Lambda('lambda_8014')
    def lambda_8014():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x007D, 0x0001, lambda_8014)

    Sleep(60)

    @scena.Lambda('lambda_8034')
    def lambda_8034():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x007B, 0x0001, lambda_8034)

    @scena.Lambda('lambda_804F')
    def lambda_804F():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x007E, 0x0001, lambda_804F)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

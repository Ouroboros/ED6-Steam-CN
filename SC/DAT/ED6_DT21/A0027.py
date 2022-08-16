import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import A0027_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('A0027   ._SN')

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
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP'),
        ('ED6_DT27/CH04611._CH', 'ED6_DT27/CH04611P._CP'),
        ('ED6_DT27/CH04612._CH', 'ED6_DT27/CH04612P._CP'),
        ('ED6_DT27/CH04613._CH', 'ED6_DT27/CH04613P._CP'),
        ('ED6_DT27/CH04614._CH', 'ED6_DT27/CH04614P._CP'),
        ('ED6_DT27/CH04615._CH', 'ED6_DT27/CH04615P._CP'),
        ('ED6_DT27/CH04616._CH', 'ED6_DT27/CH04616P._CP'),
        ('ED6_DT27/CH04613._CH', 'ED6_DT27/CH04613P._CP'),
        ('ED6_DT27/CH04613._CH', 'ED6_DT27/CH04613P._CP'),
        ('ED6_DT27/CH04613._CH', 'ED6_DT27/CH04613P._CP'),
        ('ED6_DT27/CH04620._CH', 'ED6_DT27/CH04620P._CP'),
        ('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP'),
        ('ED6_DT27/CH04622._CH', 'ED6_DT27/CH04622P._CP'),
        ('ED6_DT27/CH04623._CH', 'ED6_DT27/CH04623P._CP'),
        ('ED6_DT27/CH04624._CH', 'ED6_DT27/CH04624P._CP'),
        ('ED6_DT27/CH04625._CH', 'ED6_DT27/CH04625P._CP'),
        ('ED6_DT27/CH04626._CH', 'ED6_DT27/CH04626P._CP'),
        ('ED6_DT27/CH04623._CH', 'ED6_DT27/CH04623P._CP'),
        ('ED6_DT27/CH04623._CH', 'ED6_DT27/CH04623P._CP'),
        ('ED6_DT27/CH04623._CH', 'ED6_DT27/CH04623P._CP'),
        ('ED6_DT27/CH04630._CH', 'ED6_DT27/CH04630P._CP'),
        ('ED6_DT27/CH04631._CH', 'ED6_DT27/CH04631P._CP'),
        ('ED6_DT27/CH04632._CH', 'ED6_DT27/CH04632P._CP'),
        ('ED6_DT27/CH04633._CH', 'ED6_DT27/CH04633P._CP'),
        ('ED6_DT27/CH04634._CH', 'ED6_DT27/CH04634P._CP'),
        ('ED6_DT27/CH04635._CH', 'ED6_DT27/CH04635P._CP'),
        ('ED6_DT27/CH04636._CH', 'ED6_DT27/CH04636P._CP'),
        ('ED6_DT27/CH04633._CH', 'ED6_DT27/CH04633P._CP'),
        ('ED6_DT27/CH04633._CH', 'ED6_DT27/CH04633P._CP'),
        ('ED6_DT27/CH04633._CH', 'ED6_DT27/CH04633P._CP'),
        ('ED6_DT27/CH04640._CH', 'ED6_DT27/CH04640P._CP'),
        ('ED6_DT27/CH04641._CH', 'ED6_DT27/CH04641P._CP'),
        ('ED6_DT27/CH04642._CH', 'ED6_DT27/CH04642P._CP'),
        ('ED6_DT27/CH04643._CH', 'ED6_DT27/CH04643P._CP'),
        ('ED6_DT27/CH04644._CH', 'ED6_DT27/CH04644P._CP'),
        ('ED6_DT27/CH04645._CH', 'ED6_DT27/CH04645P._CP'),
        ('ED6_DT27/CH04646._CH', 'ED6_DT27/CH04646P._CP'),
        ('ED6_DT27/CH04643._CH', 'ED6_DT27/CH04643P._CP'),
        ('ED6_DT27/CH04643._CH', 'ED6_DT27/CH04643P._CP'),
        ('ED6_DT27/CH04643._CH', 'ED6_DT27/CH04643P._CP'),
        ('ED6_DT27/CH04750._CH', 'ED6_DT27/CH04750P._CP'),
        ('ED6_DT27/CH04751._CH', 'ED6_DT27/CH04751P._CP'),
        ('ED6_DT27/CH04752._CH', 'ED6_DT27/CH04752P._CP'),
        ('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP'),
        ('ED6_DT27/CH04754._CH', 'ED6_DT27/CH04754P._CP'),
        ('ED6_DT27/CH04755._CH', 'ED6_DT27/CH04755P._CP'),
        ('ED6_DT27/CH04756._CH', 'ED6_DT27/CH04756P._CP'),
        ('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP'),
        ('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP'),
        ('ED6_DT27/CH04753._CH', 'ED6_DT27/CH04753P._CP'),
        ('ED6_DT27/CH04820._CH', 'ED6_DT27/CH04820P._CP'),
        ('ED6_DT27/CH04821._CH', 'ED6_DT27/CH04821P._CP'),
        ('ED6_DT27/CH04822._CH', 'ED6_DT27/CH04822P._CP'),
        ('ED6_DT27/CH04823._CH', 'ED6_DT27/CH04823P._CP'),
        ('ED6_DT27/CH04824._CH', 'ED6_DT27/CH04824P._CP'),
        ('ED6_DT27/CH04825._CH', 'ED6_DT27/CH04825P._CP'),
        ('ED6_DT27/CH04826._CH', 'ED6_DT27/CH04826P._CP'),
        ('ED6_DT27/CH04823._CH', 'ED6_DT27/CH04823P._CP'),
        ('ED6_DT27/CH04823._CH', 'ED6_DT27/CH04823P._CP'),
        ('ED6_DT27/CH04823._CH', 'ED6_DT27/CH04823P._CP'),
    ]

# id: 0x10001 offset: 0x28A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '04610强化猎兵Ａ待机',
            x                   = 4000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04611强化猎兵Ａ移动',
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
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04612强化猎兵Ａ攻击',
            x                   = 4000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04613强化猎兵Ａ被弹开',
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
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04614强化猎兵Ａ倒下',
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
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04615强化猎兵Ａ魔法咏唱',
            x                   = 4000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04616强化猎兵Ａ魔法发射',
            x                   = 4000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04620强化猎兵Ｂ待机',
            x                   = 8000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04621强化猎兵Ｂ移动',
            x                   = 8000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04622强化猎兵Ｂ攻击',
            x                   = 8000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04623强化猎兵Ｂ被弹开',
            x                   = 8000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04624强化猎兵Ｂ倒下',
            x                   = 8000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04625强化猎兵Ｂ魔法咏唱',
            x                   = 8000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04626强化猎兵Ｂ魔法发射',
            x                   = 8000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04630强化猎兵克鲁茨待机',
            x                   = 12000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04631强化猎兵克鲁茨移动',
            x                   = 12000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04632强化猎兵克鲁茨攻击',
            x                   = 12000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04633强化猎兵克鲁茨被弹开',
            x                   = 12000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04634强化猎兵克鲁茨倒下',
            x                   = 12000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04635强化猎兵克鲁茨魔法咏唱',
            x                   = 12000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04636强化猎兵克鲁茨魔法发射',
            x                   = 12000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000C,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04640强化猎兵卡露娜待机',
            x                   = 16000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04641强化猎兵卡露娜移动',
            x                   = 16000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04642强化猎兵卡露娜攻击',
            x                   = 16000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000D,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04643强化猎兵卡露娜被弹开',
            x                   = 16000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04644强化猎兵卡露娜倒下',
            x                   = 16000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04645强化猎兵卡露娜魔法咏唱',
            x                   = 16000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04646强化猎兵卡露娜魔法发射',
            x                   = 16000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000E,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04750强化猎兵基尔巴特待机',
            x                   = 20000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04751强化猎兵基尔巴特移动',
            x                   = 20000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04752强化猎兵基尔巴特攻击',
            x                   = 20000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000F,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04753强化猎兵基尔巴特被弹开',
            x                   = 20000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04754强化猎兵基尔巴特倒下',
            x                   = 20000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04755强化猎兵基尔巴特魔法咏唱',
            x                   = 20000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 45,
            chipIndex           = 45,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04756强化猎兵基尔巴特魔法发射',
            x                   = 20000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 46,
            chipIndex           = 46,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0010,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04820强化猎兵库拉茨待机',
            x                   = 24000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 50,
            chipIndex           = 50,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04821强化猎兵库拉茨移动',
            x                   = 24000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 51,
            chipIndex           = 51,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04822强化猎兵库拉茨攻击',
            x                   = 24000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 52,
            chipIndex           = 52,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0011,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04823强化猎兵库拉茨被弹开',
            x                   = 24000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 53,
            chipIndex           = 53,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04824强化猎兵库拉茨倒下',
            x                   = 24000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 54,
            chipIndex           = 54,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04825强化猎兵库拉茨魔法咏唱',
            x                   = 24000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 55,
            chipIndex           = 55,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '04826强化猎兵库拉茨魔法发射',
            x                   = 24000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 56,
            chipIndex           = 56,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0012,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
    )

# id: 0x10002 offset: 0x7CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x7CA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x7CA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x7CA
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x7CB
@scena.Code('func_01_7CB')
def func_01_7CB():
    Return()

# id: 0x0002 offset: 0x7CC
@scena.Code('func_02_7CC')
def func_02_7CC():
    ExecExpressionWithReg(
        0x0065,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x65),
            Expr.Return,
        ),
        (0x00000000, 'loc_801'),
        (0x00000001, 'loc_809'),
        (0x00000002, 'loc_811'),
        (0x00000003, 'loc_819'),
        (0x00000004, 'loc_821'),
        (0x00000005, 'loc_829'),
        (0x00000006, 'loc_831'),
        (0x00000007, 'loc_839'),
        (-1, 'loc_841'),
    )

    def _loc_801(): pass

    label('loc_801')

    Sleep(100)

    Jump('loc_841')

    def _loc_809(): pass

    label('loc_809')

    Sleep(121)

    Jump('loc_841')

    def _loc_811(): pass

    label('loc_811')

    Sleep(132)

    Jump('loc_841')

    def _loc_819(): pass

    label('loc_819')

    Sleep(153)

    Jump('loc_841')

    def _loc_821(): pass

    label('loc_821')

    Sleep(164)

    Jump('loc_841')

    def _loc_829(): pass

    label('loc_829')

    Sleep(175)

    Jump('loc_841')

    def _loc_831(): pass

    label('loc_831')

    Sleep(186)

    Jump('loc_841')

    def _loc_839(): pass

    label('loc_839')

    Sleep(197)

    Jump('loc_841')

    def _loc_841(): pass

    label('loc_841')

    Return()

# id: 0x0003 offset: 0x842
@scena.Code('func_03_842')
def func_03_842():
    Call(0, 0x0002)
    def _loc_846(): pass

    label('loc_846')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_85B',
    )

    OP_99(0x00FE, 0x00, 0x07, 2000)

    Jump('loc_846')

    def _loc_85B(): pass

    label('loc_85B')

    Return()

# id: 0x0004 offset: 0x85C
@scena.Code('func_04_85C')
def func_04_85C():
    Call(0, 0x0002)
    def _loc_860(): pass

    label('loc_860')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_87A',
    )

    OP_99(0x00FE, 0x00, 0x00, 1500)
    Sleep(500)

    Jump('loc_860')

    def _loc_87A(): pass

    label('loc_87A')

    Return()

# id: 0x0005 offset: 0x87B
@scena.Code('func_05_87B')
def func_05_87B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_895',
    )

    OP_99(0x00FE, 0x00, 0x03, 1000)
    Sleep(500)

    Jump('func_05_87B')

    def _loc_895(): pass

    label('loc_895')

    Return()

# id: 0x0006 offset: 0x896
@scena.Code('func_06_896')
def func_06_896():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8E2',
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

    Sleep(100)

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

    Sleep(100)

    Jump('func_06_896')

    def _loc_8E2(): pass

    label('loc_8E2')

    Return()

# id: 0x0007 offset: 0x8E3
@scena.Code('func_07_8E3')
def func_07_8E3():
    Call(0, 0x0002)
    def _loc_8E7(): pass

    label('loc_8E7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8FC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_8E7')

    def _loc_8FC(): pass

    label('loc_8FC')

    Return()

# id: 0x0008 offset: 0x8FD
@scena.Code('func_08_8FD')
def func_08_8FD():
    Call(0, 0x0002)
    def _loc_901(): pass

    label('loc_901')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9BC',
    )

    ChrSetChipByIndex(0x00FE, 5)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ChrSetChipByIndex(0x00FE, 6)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    Sleep(1000)

    Jump('loc_901')

    def _loc_9BC(): pass

    label('loc_9BC')

    Return()

# id: 0x0009 offset: 0x9BD
@scena.Code('func_09_9BD')
def func_09_9BD():
    Call(0, 0x0002)
    def _loc_9C1(): pass

    label('loc_9C1')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9D6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_9C1')

    def _loc_9D6(): pass

    label('loc_9D6')

    Return()

# id: 0x000A offset: 0x9D7
@scena.Code('func_0A_9D7')
def func_0A_9D7():
    Call(0, 0x0002)
    def _loc_9DB(): pass

    label('loc_9DB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A96',
    )

    ChrSetChipByIndex(0x00FE, 15)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ChrSetChipByIndex(0x00FE, 16)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    Sleep(1000)

    Jump('loc_9DB')

    def _loc_A96(): pass

    label('loc_A96')

    Return()

# id: 0x000B offset: 0xA97
@scena.Code('func_0B_A97')
def func_0B_A97():
    Call(0, 0x0002)
    def _loc_A9B(): pass

    label('loc_A9B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AB0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_A9B')

    def _loc_AB0(): pass

    label('loc_AB0')

    Return()

# id: 0x000C offset: 0xAB1
@scena.Code('func_0C_AB1')
def func_0C_AB1():
    Call(0, 0x0002)
    def _loc_AB5(): pass

    label('loc_AB5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B70',
    )

    ChrSetChipByIndex(0x00FE, 25)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ChrSetChipByIndex(0x00FE, 26)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    Sleep(1000)

    Jump('loc_AB5')

    def _loc_B70(): pass

    label('loc_B70')

    Return()

# id: 0x000D offset: 0xB71
@scena.Code('func_0D_B71')
def func_0D_B71():
    Call(0, 0x0002)
    def _loc_B75(): pass

    label('loc_B75')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B8A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_B75')

    def _loc_B8A(): pass

    label('loc_B8A')

    Return()

# id: 0x000E offset: 0xB8B
@scena.Code('func_0E_B8B')
def func_0E_B8B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C46',
    )

    ChrSetChipByIndex(0x00FE, 35)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ChrSetChipByIndex(0x00FE, 36)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    Sleep(1000)

    Jump('func_0E_B8B')

    def _loc_C46(): pass

    label('loc_C46')

    Return()

# id: 0x000F offset: 0xC47
@scena.Code('func_0F_C47')
def func_0F_C47():
    Call(0, 0x0002)
    def _loc_C4B(): pass

    label('loc_C4B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C60',
    )

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_C4B')

    def _loc_C60(): pass

    label('loc_C60')

    Return()

# id: 0x0010 offset: 0xC61
@scena.Code('func_10_C61')
def func_10_C61():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D1C',
    )

    ChrSetChipByIndex(0x00FE, 45)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ChrSetChipByIndex(0x00FE, 46)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    Sleep(1000)

    Jump('func_10_C61')

    def _loc_D1C(): pass

    label('loc_D1C')

    Return()

# id: 0x0011 offset: 0xD1D
@scena.Code('func_11_D1D')
def func_11_D1D():
    Call(0, 0x0002)
    def _loc_D21(): pass

    label('loc_D21')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D36',
    )

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_D21')

    def _loc_D36(): pass

    label('loc_D36')

    Return()

# id: 0x0012 offset: 0xD37
@scena.Code('func_12_D37')
def func_12_D37():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DF2',
    )

    ChrSetChipByIndex(0x00FE, 55)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

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

    Sleep(100)

    ChrSetChipByIndex(0x00FE, 56)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    Sleep(1000)

    Jump('func_12_D37')

    def _loc_DF2(): pass

    label('loc_DF2')

    Return()

# id: 0x0013 offset: 0xDF3
@scena.Code('func_13_DF3')
def func_13_DF3():
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

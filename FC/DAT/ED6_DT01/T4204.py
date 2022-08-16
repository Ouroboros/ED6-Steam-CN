import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4204_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4204   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4204.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH02340._CH', 'ED6_DT07/CH02340P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH02450._CH', 'ED6_DT07/CH02450P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT06/CH20030._CH', 'ED6_DT06/CH20030P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT06/CH20040._CH', 'ED6_DT06/CH20040P._CP'),
        ('ED6_DT06/CH20060._CH', 'ED6_DT06/CH20060P._CP'),
        ('ED6_DT07/CH00004._CH', 'ED6_DT07/CH00004P._CP'),
        ('ED6_DT06/CH20148._CH', 'ED6_DT06/CH20148P._CP'),
        ('ED6_DT06/CH20149._CH', 'ED6_DT06/CH20149P._CP'),
        ('ED6_DT06/CH20150._CH', 'ED6_DT06/CH20150P._CP'),
        ('ED6_DT06/CH20151._CH', 'ED6_DT06/CH20151P._CP'),
        ('ED6_DT06/CH20152._CH', 'ED6_DT06/CH20152P._CP'),
        ('ED6_DT06/CH20153._CH', 'ED6_DT06/CH20153P._CP'),
        ('ED6_DT06/CH20154._CH', 'ED6_DT06/CH20154P._CP'),
    ]

# id: 0x10001 offset: 0x21A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '特务兵',
            x                   = -870,
            z                   = 19750,
            y                   = 107200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 910,
            z                   = 19750,
            y                   = 107200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '希尔丹夫人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '凯诺娜上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '科洛丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '雪拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '金',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '拉赛尔博士',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '卡西乌斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '奈尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '希德少校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '尤莉亚中尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '艾莉茜雅女王',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '米蕾奴夫人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '克劳斯市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '科林兹校长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '约修亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '特务艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务艇影子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x71A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x71A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -4710,
            y           = 18000,
            z           = 94670,
            range       = 5130,
            dword_10    = 0x00003E80,
            dword_14    = 0x00016A1C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = -4340,
            y           = 19000,
            z           = 105990,
            range       = 4220,
            dword_10    = 0x00004650,
            dword_14    = 0x0001933E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -4280,
            y           = 16000,
            z           = 78500,
            range       = 5010,
            dword_10    = 0x000032C8,
            dword_14    = 0x0001270A,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = -4730,
            y           = 18000,
            z           = 98010,
            range       = 4880,
            dword_10    = 0x00003E80,
            dword_14    = 0x00017534,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = -33010,
            y           = 15000,
            z           = 79090,
            range       = -37530,
            dword_10    = 0x00004268,
            dword_14    = 0x00011882,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = -4340,
            y           = 21000,
            z           = 108990,
            range       = 4220,
            dword_10    = 0x00004268,
            dword_14    = 0x00019EF6,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000013,
        ),
    )

# id: 0x10004 offset: 0x7DA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x7DA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Return,
        ),
        'loc_818',
    )

    ChrSetChipByIndex(0x002D, 32)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetPos(0x002D, -42970, 16000, 81320, 270)
    ChrSetFlags(0x002D, 0x0004)

    @scena.Lambda('lambda_0807')
    def lambda_0807():
        OP_99(0x00FE, 0x00, 0x07, 800)
        Yield()

        Jump('lambda_0807')

    DispatchAsync2(0x002D, 0x0001, lambda_0807)

    Event(0, func_11_3F6C)

    def _loc_818(): pass

    label('loc_818')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_829',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)

    def _loc_829(): pass

    label('loc_829')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_837',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_07_2A53)

    def _loc_837(): pass

    label('loc_837')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_845',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0B_2F4D)

    def _loc_845(): pass

    label('loc_845')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_853',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_0F_39F9)

    def _loc_853(): pass

    label('loc_853')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_86A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, func_10_3EA3)

    def _loc_86A(): pass

    label('loc_86A')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_87A'),
        (0x00000065, 'loc_890'),
        (-1, 'loc_8A6'),
    )

    def _loc_87A(): pass

    label('loc_87A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 5, 0x63D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_88D',
    )

    SetScenaFlags(ScenaFlag(0x00C7, 5, 0x63D))
    Event(0, func_03_97C)

    def _loc_88D(): pass

    label('loc_88D')

    Jump('loc_8A6')

    def _loc_890(): pass

    label('loc_890')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 5, 0x645)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8A3',
    )

    SetScenaFlags(ScenaFlag(0x00C8, 5, 0x645))
    Event(0, func_06_2142)

    def _loc_8A3(): pass

    label('loc_8A3')

    Jump('loc_8A6')

    def _loc_8A6(): pass

    label('loc_8A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8D0',
    )

    ChrSetChipByIndex(0x0000, 1)
    ChrSetChipByIndex(0x0001, 2)
    ChrSetChipByIndex(0x0138, 3)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_8D0(): pass

    label('loc_8D0')

    Return()

# id: 0x0001 offset: 0x8D1
@scena.Code('func_01_8D1')
def func_01_8D1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Return,
        ),
        'loc_8E9',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_8F9')

    def _loc_8E9(): pass

    label('loc_8E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_8F9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8F9(): pass

    label('loc_8F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 6, 0x666)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_965',
    )

    OP_1B(0x00, 0x00, 0x000D)
    OP_A1(0x002E, 0x0000)
    OP_A1(0x002F, 0x0001)
    OP_72(0x0000, 0x0004)
    OP_72(0x0000, 0x0002)
    OP_71(0x0000, 0x0400)
    OP_71(0x0000, 0x0040)
    OP_72(0x0001, 0x0004)
    OP_72(0x0001, 0x0002)
    OP_71(0x0001, 0x0400)
    OP_71(0x0001, 0x0040)
    ChrSetPos(0x002E, 2320, 12050, 57280, 56)
    ChrSetPos(0x002F, 2320, 12050, 57280, 56)
    OP_6F(0x0000, 1200)

    def _loc_965(): pass

    label('loc_965')

    Return()

# id: 0x0002 offset: 0x966
@scena.Code('func_02_966')
def func_02_966():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_97B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_966')

    def _loc_97B(): pass

    label('loc_97B')

    Return()

# id: 0x0003 offset: 0x97C
@scena.Code('func_03_97C')
def func_03_97C():
    EventBegin(0x00)
    CameraMove(-43010, 16000, 79950, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(8050, 0)
    OP_6C(69000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, 29890, 9500, 76540, 0)
    ChrSetPos(0x0102, 31020, 9500, 76540, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_09EC')
    def lambda_09EC():
        CameraMove(31020, 10750, 79090, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09EC)

    @scena.Lambda('lambda_0A04')
    def lambda_0A04():
        OP_6C(45000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0A04)

    Sleep(7500)

    @scena.Lambda('lambda_0A19')
    def lambda_0A19():
        ChrWalkTo(0x00FE, 29500, 12000, 86790, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A19)

    Sleep(400)

    @scena.Lambda('lambda_0A39')
    def lambda_0A39():
        ChrWalkTo(0x00FE, 29790, 12000, 85470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A39)

    WaitForThreadExit(0x0101, 0x0002)
    Fade(1000)
    CameraMove(29640, 12000, 86120, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 270, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrSetDirection(0x0102, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010120375V#008F哇啊～……好美……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120370V这里就是王城的空中庭园啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120371V#010F是啊……湖面一览无余，\n',
            '还可以俯瞰格兰赛尔周围的城邑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120378V#019F想来参观的人肯定很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120379V#007F呼～如果不是处于这种关头，\n',
            '本可以好好欣赏这里的景色的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120380V#006F现在还是优先完成任务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xBFA
@scena.Code('func_04_BFA')
def func_04_BFA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 6, 0x63E)),
            Expr.Return,
        ),
        'loc_C02',
    )

    Return()

    def _loc_C02(): pass

    label('loc_C02')

    SetScenaFlags(ScenaFlag(0x00C7, 6, 0x63E))
    OP_28(0x0049, 0x01, 0x0400)
    EventBegin(0x00)
    ChrSetDirection(0x0101, 0, 0)
    ChrSetDirection(0x0102, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#0010120441V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120442V#012F看来这里就是女王宫了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C6D')
    def lambda_0C6D():
        ChrSetDirection(0x00FE, 0, 0)
        Yield()

        Jump('lambda_0C6D')

    DispatchAsync2(0x0101, 0x0002, lambda_0C6D)

    @scena.Lambda('lambda_0C7E')
    def lambda_0C7E():
        ChrSetDirection(0x00FE, 0, 0)
        Yield()

        Jump('lambda_0C7E')

    DispatchAsync2(0x0102, 0x0002, lambda_0C7E)

    @scena.Lambda('lambda_0C8F')
    def lambda_0C8F():
        ChrWalkTo(0x00FE, 880, 18000, 103610, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C8F)

    @scena.Lambda('lambda_0CAA')
    def lambda_0CAA():
        ChrWalkTo(0x00FE, -650, 18000, 103480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0CAA)

    @scena.Lambda('lambda_0CC5')
    def lambda_0CC5():
        OP_6C(33000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0CC5)

    CameraMove(-160, 19000, 105620, 3000)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2620120383V唔……你们是什么人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630120444V哦……他们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010120445V#006F没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120386V我们两个是公爵邀请的客人……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0102,
        (
            '#0020120387V#010F这里就是陛下居住的女王宫对吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630120448V……是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120389V不过这几天\n',
            '陛下的身体欠佳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120390V想要晋见是不行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120451V#506F这、这样啊～\n',
            '没有想到陛下会身体不适呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120392V这么说来，\n',
            '可得小心照料～才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120393V#010F请问一下，\n',
            '科洛蒂娅公主也在里面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120394V不，里面是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 800)

    ChrTalk(
        0x0009,
        (
            '#2630120455V……喂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120396V哦哦，\n',
            '公主正在细心地看护着陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120397V当然也就没有空闲\n',
            '来招呼你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000A, 280, 20000, 111970, 0)

    NpcTalk(
        0x000A,
        '女性的声音',
        (
            '#0650120458V#4P……请问，\n',
            '你们在那里做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrClearFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_1040')
    def lambda_1040():
        ChrWalkTo(0x00FE, 130, 19500, 106810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1040)

    @scena.Lambda('lambda_105B')
    def lambda_105B():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_105B')

    DispatchAsync2(0x0008, 0x0001, lambda_105B)

    @scena.Lambda('lambda_106C')
    def lambda_106C():
        ChrWalkTo(0x00FE, -1540, 19750, 107050, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_106C)

    @scena.Lambda('lambda_1087')
    def lambda_1087():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1087')

    DispatchAsync2(0x0009, 0x0001, lambda_1087)

    @scena.Lambda('lambda_1098')
    def lambda_1098():
        ChrWalkTo(0x00FE, -1500, 19250, 106220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1098)

    WaitForThreadExit(0x0009, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#2620120459V#3P夫人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630120460V#3P您这就要回去了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000A, 0x0002)
    ChrTurnDirection(0x000A, 0x0008, 400)

    NpcTalk(
        0x000A,
        '中年女性',
        (
            '#0650120461V#710F#2P晚宴很快就要开始了，\n',
            '我得先回休息室准备一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120402V对了，这两位客人是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120463V#3P武术大会优胜组的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120464V#3P只不过是些游击士罢了，\n',
            '但也还算是邀请的客人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120465V#009F哼，什么叫只不过是游击士……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '中年女性',
        (
            '#0650120466V#717F#2P#5S岂能如此无礼！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(200)

    NpcTalk(
        0x000A,
        '中年女性',
        (
            '#0650120467V#717F#2P你这就等同于在侮辱\n',
            '邀请客人的公爵大人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0009,
        (
            '#2630120468V#3P不……我们不是那个意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '中年女性',
        (
            '#0650120469V#717F#2P虽说是由公爵大人邀请而来的，\n',
            '但只要是王城的来访者，就是陛下的客人！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120410V这一点是绝对不能忘记的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120471V#3P明、明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120472V#506F（好、好惊人的气势……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120473V#012F（难道这个人就是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120474V#3P可是夫人……\n',
            '他们要想进去是肯定不行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120475V#3P这一点上校说得很清楚了，\n',
            '您也应该很明白吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '中年女性',
        (
            '#0650120476V#716F#2P……这个我已经听腻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 180, 400)

    @scena.Lambda('lambda_14CE')
    def lambda_14CE():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_14CE')

    DispatchAsync2(0x0101, 0x0001, lambda_14CE)

    @scena.Lambda('lambda_14DF')
    def lambda_14DF():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_14DF')

    DispatchAsync2(0x0102, 0x0001, lambda_14DF)

    ChrWalkTo(0x000A, 140, 18500, 104760, 2000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    NpcTalk(
        0x000A,
        '中年女性',
        (
            '#0650120477V#710F#5P非常抱歉，两位客人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120478V因为加强戒备的缘故，\n',
            '所以最近禁止其他人接近女王宫。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120419V如果可以的话，\n',
            '晚宴开始之前请在房间里等候好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120480V#004F啊……好、好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120421V#010F明白了。\n',
            '还是这样比较好一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020120482V#015F……实在是对不起。\n',
            '我们带来了不少麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#2620120423V哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#2630120484V知道就好，人要知趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0008, 400)

    NpcTalk(
        0x000A,
        '中年女性',
        (
            '#0650120485V#714F#2P……………………（怒视）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120426V……那么\n',
            '这就请回吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(470, 15250, 86110, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0101, -620, 15500, 86640, 180)
    ChrSetPos(0x0102, 1430, 15500, 86590, 180)
    ChrSetPos(0x000A, 310, 15000, 85930, 180)

    @scena.Lambda('lambda_1775')
    def lambda_1775():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1775')

    DispatchAsync2(0x0101, 0x0001, lambda_1775)

    @scena.Lambda('lambda_1786')
    def lambda_1786():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1786')

    DispatchAsync2(0x0102, 0x0001, lambda_1786)

    @scena.Lambda('lambda_1797')
    def lambda_1797():
        ChrWalkTo(0x00FE, -220, 14000, 80290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1797)

    @scena.Lambda('lambda_17B2')
    def lambda_17B2():
        ChrWalkTo(0x00FE, -910, 14000, 81230, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_17B2)

    @scena.Lambda('lambda_17CD')
    def lambda_17CD():
        ChrWalkTo(0x00FE, 490, 14000, 81580, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_17CD)

    @scena.Lambda('lambda_17E8')
    def lambda_17E8():
        CameraMove(-90, 14000, 81270, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_17E8)

    WaitForThreadExit(0x000A, 0x0001)
    ChrSetDirection(0x000A, 0, 400)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0102, 0x0002)

    NpcTalk(
        0x000A,
        '中年女性',
        (
            '#0650120487V#711F……他们做出那样丢脸的事，\n',
            '让你们见笑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120488V真是对不起，还没有自我介绍。\n',
            '我的名字叫希尔丹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120429V我是这个格兰赛尔城的女管家，\n',
            '主要就是监督侍女的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120490V#501F果然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120431V#010F原来您就是希尔丹夫人啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120492V#712F哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120433V对不起，请问\n',
            '我们曾经认识吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120494V#006F哎……\n',
            '是从别人那里听说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x000A, 600, 2000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '尤莉亚的介绍信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(0x036C, 1)
    ChrMoveTo(0x0101, -910, 14000, 81230, 2000, 0x00)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0650120495V#712F这个笔迹是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120496V#006F嗯，凭那个笔迹就可以判断是谁写的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120437V#010F这封介绍信以及胸前的游击士徽章\n',
            '就是我们两人身份的证明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120498V#713F我明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120499V#710F在这儿不太方便，\n',
            '先回侍女的休息室谈谈吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120440V到那儿再向你们请教详细的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4254._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x1B86
@scena.Code('func_05_1B86')
def func_05_1B86():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 3, 0x643)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1B93',
    )

    Return()

    def _loc_1B93(): pass

    label('loc_1B93')

    OP_28(0x004A, 0x01, 0x0080)
    EventBegin(0x00)
    Fade(1000)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0102, 3)
    ChrSetChipByIndex(0x0138, 1)
    ChrSetPos(0x0138, 10, 18500, 104700, 0)
    ChrSetPos(0x0101, -470, 18000, 103350, 0)
    ChrSetPos(0x0102, 740, 18000, 103280, 0)
    CameraMove(-70, 19000, 105810, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2620121048V希尔丹夫人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630121049V都这么晚了，\n',
            '找陛下还有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121050V#710F我把陛下吩咐过要送来的\n',
            '红茶和一些餐具都带来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121051V#713F陛下被如此限制了自由，\n',
            '所以我的工作也相对多了起来。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121052V很忙碌啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630121053V哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630121054V以前没有见过这两个人啊，\n',
            '是新来的侍女吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121055V#710F公爵大人之前说过要招多一些人手，\n',
            '这两个是新来的实习侍女。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121056V今天才进入城里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121057V哦呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630121058V唔～\n',
            '的确好可爱哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121059V#474F你、你们好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121060V#336F………………（点头示意）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121061V哦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121062V怎么总觉得这两个人\n',
            '好像在哪里见过呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121063V#323F（不好……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121064V#714F……对年轻的姑娘\n',
            '那样目不转睛地盯着是什么意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121065V难道是在动一些歪念头吗？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121066V再这样下去的话，\n',
            '我可要向公爵大人和上校抗议了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#2620121067V不、不要这样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630121068V我们作为王国军的精英\n',
            '怎么会那样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121069V#713F没有最好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121070V#710F我说，你们好了没有，\n',
            '可以让我们进去了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121071V刚才对不起！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetDirection(0x0008, 90, 400)

    @scena.Lambda('lambda_2081')
    def lambda_2081():
        ChrMoveTo(0x00FE, -2300, 19750, 107200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2081)

    ChrTalk(
        0x0009,
        (
            '#2630121072V请进去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 270, 400)

    @scena.Lambda('lambda_20BF')
    def lambda_20BF():
        ChrMoveTo(0x00FE, 2350, 19750, 107200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_20BF)

    FadeOut(2000, 0, -1)

    @scena.Lambda('lambda_20E4')
    def lambda_20E4():
        ChrMoveToRelative(0x00FE, 0, 0, 10000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_20E4)

    Sleep(50)

    @scena.Lambda('lambda_2104')
    def lambda_2104():
        ChrMoveToRelative(0x00FE, 0, 0, 10000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2104)

    @scena.Lambda('lambda_211F')
    def lambda_211F():
        ChrMoveToRelative(0x00FE, 0, 0, 10000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_211F)

    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4270._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x2142
@scena.Code('func_06_2142')
def func_06_2142():
    EventBegin(0x00)
    CameraMove(-220, 20000, 107550, 0)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetPos(0x0008, -2390, 19750, 107200, 180)
    ChrSetPos(0x0009, 2290, 19750, 107200, 180)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)

    @scena.Lambda('lambda_218F')
    def lambda_218F():
        ChrTurnDirection(0x00FE, 0x0138, 0)
        Yield()

        Jump('lambda_218F')

    DispatchAsync2(0x0008, 0x0002, lambda_218F)

    @scena.Lambda('lambda_21A0')
    def lambda_21A0():
        ChrTurnDirection(0x00FE, 0x0138, 0)
        Yield()

        Jump('lambda_21A0')

    DispatchAsync2(0x0009, 0x0002, lambda_21A0)

    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0102, 3)
    ChrSetChipByIndex(0x0138, 1)
    ChrSetPos(0x0101, -990, 20000, 110860, 180)
    ChrSetPos(0x0102, 1070, 20000, 111050, 0)
    ChrSetPos(0x0138, 120, 20000, 110230, 180)

    @scena.Lambda('lambda_21F3')
    def lambda_21F3():
        ChrWalkTo(0x00FE, 190, 19250, 106340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_21F3)

    @scena.Lambda('lambda_220E')
    def lambda_220E():
        ChrWalkTo(0x00FE, -480, 19750, 107280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_220E)

    @scena.Lambda('lambda_2229')
    def lambda_2229():
        ChrWalkTo(0x00FE, 860, 19750, 107280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2229)

    WaitForThreadExit(0x0138, 0x0001)
    ChrTurnDirection(0x0138, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#2620121331V希尔丹夫人。\n',
            '这就要回去了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121332V#710F嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121333V总之，我希望你们\n',
            '在陛下面前不要有什么闪失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121052V哦……这么的严肃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121335V不过您请放心。\n',
            '因为我们都是爱国将士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121336V#713F那就没有什么再要拜托的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121337V那么我们这就告辞了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121338V#474F再、再～见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 135, 400)

    ChrTalk(
        0x0102,
        (
            '#0020121339V#336F……告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0138, 180, 400)

    @scena.Lambda('lambda_23E9')
    def lambda_23E9():
        CameraMove(230, 19000, 105820, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_23E9)

    @scena.Lambda('lambda_2401')
    def lambda_2401():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_2401)

    Sleep(100)

    @scena.Lambda('lambda_2421')
    def lambda_2421():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2421)

    @scena.Lambda('lambda_243C')
    def lambda_243C():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_243C)

    @scena.Lambda('lambda_2457')
    def lambda_2457():
        ChrMoveTo(0x00FE, -870, 19750, 107200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2457)

    Sleep(100)

    @scena.Lambda('lambda_2477')
    def lambda_2477():
        ChrMoveTo(0x00FE, 910, 19750, 107200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2477)

    Sleep(1100)

    ChrTalk(
        0x0008,
        (
            '#2620121340V啊，两位姑娘。',
            TxtCtl.Enter,
        ),
    )

    ChrClearFlags(0x0008, 0x0004)
    ChrClearFlags(0x0009, 0x0004)
    Sleep(200)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CloseMessageWindow()

    @scena.Lambda('lambda_24FC')
    def lambda_24FC():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_24FC)

    @scena.Lambda('lambda_250A')
    def lambda_250A():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_250A)

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121341V#324F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121342V突然想起一件事呢，\n',
            '就是还没有问你们的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121343V告诉我们好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121344V#473F嗯，这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

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
        10,
        0,
        (
            TXT(0x00, '【莱娜】\n'),
            TXT(0x01, '【雪拉】\n'),
            TXT(0x02, '【朵洛希】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_262A'),
        (0x00000001, 'loc_26B1'),
        (0x00000002, 'loc_277E'),
        (-1, 'loc_2811'),
    )

    def _loc_262A(): pass

    label('loc_262A')

    SetScenaFlags(ScenaFlag(0x00CE, 6, 0x676))

    ChrTalk(
        0x0008,
        (
            '#2620121345V哦……？\n',
            '很不错的名字嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121346V和你很是般配啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121347V#328F啊，那个……\n',
            '谢谢你们夸奖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2811')

    def _loc_26B1(): pass

    label('loc_26B1')

    SetScenaFlags(ScenaFlag(0x00CE, 7, 0x677))

    ChrTalk(
        0x0008,
        (
            '#2620121348V哦～\n',
            '真是个性感的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121349V不过本人好像比名字要逊色一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121350V#325F少、少管闲事！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121351V#474F……啊，不是呢，哦呵呵。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121352V我一定会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2811')

    def _loc_277E(): pass

    label('loc_277E')

    SetScenaFlags(ScenaFlag(0x00CF, 0, 0x678))

    ChrTalk(
        0x0008,
        (
            '#2620121353V唔……\n',
            '比较流行的名字啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121354V可是说实话，\n',
            '这名字感觉和你不是很般配……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121355V#327F（也许是吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2811')

    def _loc_2811(): pass

    label('loc_2811')

    ChrTalk(
        0x0009,
        (
            '#2630121356V那边的那位\n',
            '黑发的姑娘呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121357V#336F……我的名字叫做卡玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630121358V叫卡玲……\n',
            '好可爱的名字哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121359V#331F多谢夸奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121360V……我对自己的名字\n',
            '也是非常的喜欢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630121361V是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630121362V对、对了。\n',
            '我是特务部队的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121363V#713F难道又把我刚才的话当作耳边风了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121364V这种无聊的搭讪方式，\n',
            '就是居心不良的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630121365V不，我可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121366V#714F……………………（怒视）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121367V……请吧，\n',
            '回去的路上请注意安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0009, 0x02)
    ChrSetDirection(0x0008, 180, 0)
    ChrSetDirection(0x0009, 180, 0)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    EventEnd(0x00)
    ChrSetChipByIndex(0x0000, 1)
    ChrSetChipByIndex(0x0001, 2)
    ChrSetChipByIndex(0x0138, 3)

    Return()

# id: 0x0007 offset: 0x2A53
@scena.Code('func_07_2A53')
def func_07_2A53():
    EventBegin(0x00)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x000B, 20, 12000, 47110, 180)
    ChrSetPos(0x0008, 940, 12000, 48110, 180)
    ChrSetPos(0x0009, -900, 12000, 48050, 180)
    ChrSetPos(0x000C, -60, 12000, 49430, 180)
    ChrSetPos(0x000D, 930, 12000, 50530, 180)
    ChrSetPos(0x000E, 930, 12000, 52440, 180)
    ChrSetPos(0x000F, 910, 12000, 54110, 180)
    ChrSetPos(0x0010, -890, 12000, 50560, 180)
    ChrSetPos(0x0011, -890, 12000, 52310, 180)
    ChrSetPos(0x0012, -890, 12000, 54310, 180)
    CameraMove(-20, 12000, 47150, 0)
    OP_67(0, 5910, -10000, 0)
    OP_6C(45000, 0)
    CameraSetDistance(3400, 0)
    OP_6E(280, 0)

    ChrTalk(
        0x000B,
        (
            '#180F这、这怎么可能……！\n',
            '为什么城门会自动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '上、上尉！\n',
            '怎么办！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这样下去的话\n',
            '敌人会冲入城内的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2BE8')
    def lambda_2BE8():
        CameraMove(-150, 12000, 49950, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2BE8)

    @scena.Lambda('lambda_2C00')
    def lambda_2C00():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2C00)

    @scena.Lambda('lambda_2C0E')
    def lambda_2C0E():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2C0E)

    ChrSetDirection(0x000B, 0, 400)

    ChrTalk(
        0x000B,
        (
            '#0611100001V#180F第一小队留下，\n',
            '其余的立刻赶往大门！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610131160V绝对不能让敌人冲进城内！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '明、明白！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2C95')
    def lambda_2C95():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2C95')

    DispatchAsync2(0x000D, 0x0001, lambda_2C95)

    @scena.Lambda('lambda_2CA6')
    def lambda_2CA6():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2CA6')

    DispatchAsync2(0x000E, 0x0001, lambda_2CA6)

    @scena.Lambda('lambda_2CB7')
    def lambda_2CB7():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2CB7')

    DispatchAsync2(0x000F, 0x0001, lambda_2CB7)

    @scena.Lambda('lambda_2CC8')
    def lambda_2CC8():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2CC8')

    DispatchAsync2(0x0010, 0x0001, lambda_2CC8)

    @scena.Lambda('lambda_2CD9')
    def lambda_2CD9():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2CD9')

    DispatchAsync2(0x0011, 0x0001, lambda_2CD9)

    @scena.Lambda('lambda_2CEA')
    def lambda_2CEA():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2CEA')

    DispatchAsync2(0x0012, 0x0001, lambda_2CEA)

    ChrWalkTo(0x000C, 2310, 12000, 49510, 5000, 0x00)
    ChrWalkTo(0x000C, 2310, 12000, 50680, 5000, 0x00)
    CreateThread(0x000D, 0x01, 0x00, func_08_2EC8)
    CreateThread(0x0010, 0x01, 0x00, func_08_2EC8)
    ChrWalkTo(0x000C, 2310, 12000, 52390, 5000, 0x00)
    CreateThread(0x000E, 0x01, 0x00, func_09_2EF1)
    CreateThread(0x0011, 0x01, 0x00, func_09_2EF1)
    ChrWalkTo(0x000C, 2310, 12000, 55190, 5000, 0x00)
    CreateThread(0x000F, 0x01, 0x00, func_0A_2F1F)
    CreateThread(0x0012, 0x01, 0x00, func_0A_2F1F)

    @scena.Lambda('lambda_2D75')
    def lambda_2D75():
        ChrWalkTo(0x00FE, 2350, 12000, 71700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2D75)

    CameraMove(90, 12000, 48130, 1000)

    ChrTalk(
        0x000B,
        (
            '#180F可恶，太丢脸了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610131163V在阁下回来之前\n',
            '无论如何也不能被击败……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_2E21')
    def lambda_2E21():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2E21)

    @scena.Lambda('lambda_2E2F')
    def lambda_2E2F():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2E2F)

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '上、上尉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '特……是特务飞行艇！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 180, 400)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#180F糟糕了！\n',
            '那个才是主力部队吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    NewScene('ED6_DT01/E0500._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x2EC8
@scena.Code('func_08_2EC8')
def func_08_2EC8():
    ChrWalkTo(0x00FE, 2350, 12000, 50630, 5000, 0x00)
    ChrWalkTo(0x00FE, 2350, 12000, 71700, 5000, 0x00)

    Return()

# id: 0x0009 offset: 0x2EF1
@scena.Code('func_09_2EF1')
def func_09_2EF1():
    Sleep(800)

    ChrWalkTo(0x00FE, 2290, 12000, 52370, 5000, 0x00)
    ChrWalkTo(0x00FE, 2350, 12000, 71700, 5000, 0x00)

    Return()

# id: 0x000A offset: 0x2F1F
@scena.Code('func_0A_2F1F')
def func_0A_2F1F():
    Sleep(1300)

    ChrWalkTo(0x00FE, 2290, 12000, 54260, 5000, 0x00)
    ChrWalkTo(0x00FE, 2350, 12000, 71700, 5000, 0x00)

    Return()

# id: 0x000B offset: 0x2F4D
@scena.Code('func_0B_2F4D')
def func_0B_2F4D():
    EventBegin(0x00)
    FormationDelMember(0x01, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationAddMember(0x00, 0xFF)
    FormationAddMember(0x02, 0xFF)
    FormationAddMember(0x04, 0xFF)
    CameraMove(610, 15350, 55470, 0)
    OP_67(0, 5210, -10000, 0)
    CameraSetDistance(3400, 0)
    OP_6C(29000, 0)
    OP_6E(413, 0)
    ChrSetPos(0x0008, -8650, 12000, 56840, 79)
    ChrSetPos(0x000B, -8029, 12000, 58490, 125)
    ChrSetPos(0x0009, -6650, 12000, 57720, 46)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_2FE6')
    def lambda_2FE6():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2FE6')

    DispatchAsync2(0x000B, 0x0001, lambda_2FE6)

    @scena.Lambda('lambda_2FF7')
    def lambda_2FF7():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2FF7')

    DispatchAsync2(0x0008, 0x0001, lambda_2FF7)

    @scena.Lambda('lambda_3008')
    def lambda_3008():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_3008')

    DispatchAsync2(0x0009, 0x0001, lambda_3008)

    ChrSetPos(0x0101, 2880, 15350, 57740, 147)
    ChrSetPos(0x0103, 2880, 15350, 57740, 147)
    ChrSetPos(0x0105, 2880, 15350, 57740, 147)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0103, 7)
    ChrSetChipByIndex(0x0105, 9)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_3064')
    def lambda_3064():
        OP_67(0, 7370, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0103, 0x0003, lambda_3064)

    OP_6F(0x0000, 241)
    OP_70(0x0000, 360)
    OP_73(0x0000)
    OP_6F(0x0000, 1140)
    OP_70(0x0000, 1200)
    OP_73(0x0000)

    @scena.Lambda('lambda_309E')
    def lambda_309E():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_309E')

    DispatchAsync2(0x0101, 0x0001, lambda_309E)

    @scena.Lambda('lambda_30AF')
    def lambda_30AF():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_30AF')

    DispatchAsync2(0x0105, 0x0001, lambda_30AF)

    @scena.Lambda('lambda_30C0')
    def lambda_30C0():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_30C0')

    DispatchAsync2(0x0103, 0x0001, lambda_30C0)

    @scena.Lambda('lambda_30D1')
    def lambda_30D1():
        CameraMove(-7590, 12000, 54940, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_30D1)

    @scena.Lambda('lambda_30E9')
    def lambda_30E9():
        OP_6E(291, 4000)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_30E9)

    @scena.Lambda('lambda_30F9')
    def lambda_30F9():
        ChrWalkTo(0x00FE, -4940, 12710, 53260, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_30F9)

    Sleep(400)

    @scena.Lambda('lambda_3119')
    def lambda_3119():
        ChrWalkTo(0x00FE, -7230, 12000, 51440, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_3119)

    Sleep(400)

    @scena.Lambda('lambda_3139')
    def lambda_3139():
        ChrWalkTo(0x00FE, -5870, 12000, 52050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_3139)

    WaitForThreadExit(0x0101, 0x0002)

    @scena.Lambda('lambda_3159')
    def lambda_3159():
        ChrJumpTo(0x00FE, -7040, 12000, 52700, 1000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3159)

    WaitForThreadExit(0x0103, 0x0002)

    @scena.Lambda('lambda_317C')
    def lambda_317C():
        ChrWalkTo(0x00FE, -8580, 12000, 52480, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_317C)

    WaitForThreadExit(0x0105, 0x0002)

    @scena.Lambda('lambda_319C')
    def lambda_319C():
        ChrWalkTo(0x00FE, -7830, 12000, 51430, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_319C)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x000B,
        (
            '#180F艾、艾丝蒂尔·布莱特！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610131168V以及……科洛蒂娅殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F凯诺娜上尉！\n',
            '又来麻烦你了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060940010V#040F我们是来……\n',
            '营救我祖母的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#180F不、不要欺人太甚了，小丫头们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    Battle(0x000003A8, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_32B3'),
        (-1, 'loc_32B6'),
    )

    def _loc_32B3(): pass

    label('loc_32B3')

    OP_B4(0x00)

    Return()

    def _loc_32B6(): pass

    label('loc_32B6')

    EventBegin(0x00)
    CameraMove(-7800, 12000, 57810, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(3400, 0)
    OP_6C(9000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x000B, -9230, 12000, 57550, 258)
    ChrSetPos(0x0008, -9060, 12000, 59260, 302)
    ChrSetPos(0x0009, -7670, 12000, 59020, 103)
    ChrSetPos(0x0101, -6550, 12000, 56030, 282)
    ChrSetPos(0x0103, -8180, 12000, 54960, 331)
    ChrSetPos(0x0105, -7070, 12000, 54530, 325)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 36)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0008, 35)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 35)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x0009, 0x0001)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 65535)

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0103, 65535)

    ExecExpressionWithValue(
        0x0105,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0105, 65535)

    ChrTalk(
        0x0103,
        (
            '#020F真令人毛骨悚然……\n',
            '好一个可怕的女人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131173V到底是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F理查德上校的副官。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131175V是只典型的狐狸精。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F原来如此，这种感觉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '接下来……目标女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F好的，赶快走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004E, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x34AE
@scena.Code('func_0C_34AE')
def func_0C_34AE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 2, 0x662)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_34BB',
    )

    Return()

    def _loc_34BB(): pass

    label('loc_34BB')

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00CC, 2, 0x662))
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x000E, 13020, 14000, 78670, 270)
    ChrSetPos(0x000F, 14450, 14000, 79840, 270)
    ChrSetPos(0x0010, 14130, 14000, 77880, 270)

    ChrTalk(
        0x000E,
        (
            '来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '在那儿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x0101, 1230, 14000, 77770, 90)
    ChrSetPos(0x0103, -420, 14000, 78370, 90)
    ChrSetPos(0x0105, -300, 14000, 77020, 90)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0103, 7)
    ChrSetChipByIndex(0x0105, 9)
    CameraMove(6360, 14000, 78900, 2000)

    ChrTalk(
        0x0101,
        (
            '#000F哇，又来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F哼，装腔作势的家伙们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000E, 34)
    ChrSetChipByIndex(0x000F, 34)
    ChrSetChipByIndex(0x0010, 34)

    @scena.Lambda('lambda_35C1')
    def lambda_35C1():
        CameraMove(2650, 14000, 77790, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35C1)

    @scena.Lambda('lambda_35D9')
    def lambda_35D9():
        ChrWalkTo(0x00FE, -20520, 14000, 78060, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_35D9)

    @scena.Lambda('lambda_35F4')
    def lambda_35F4():
        ChrWalkTo(0x00FE, -20520, 14000, 78060, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_35F4)

    @scena.Lambda('lambda_360F')
    def lambda_360F():
        ChrWalkTo(0x00FE, -20520, 14000, 78060, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_360F)

    Sleep(500)

    Battle(0x000003A9, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_3642'),
        (-1, 'loc_3645'),
    )

    def _loc_3642(): pass

    label('loc_3642')

    OP_B4(0x00)

    Return()

    def _loc_3645(): pass

    label('loc_3645')

    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    ChrSetPos(0x0101, 1230, 14000, 77770, 90)
    ChrSetPos(0x0103, -420, 14000, 78370, 90)
    ChrSetPos(0x0105, -300, 14000, 77020, 90)
    ChrSetPos(0x000E, 3390, 14000, 79480, 146)
    ChrSetPos(0x000F, 3080, 14000, 77370, 283)
    ChrSetPos(0x0010, 5260, 14000, 77990, 28)
    Sleep(500)

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x36DC
@scena.Code('func_0D_36DC')
def func_0D_36DC():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3734',
    )

    ChrTalk(
        0x0105,
        (
            '#040F艾丝蒂尔！\n',
            '这边是去城内的路！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F我们要赶快去女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37BE')

    def _loc_3734(): pass

    label('loc_3734')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_376B',
    )

    ChrTalk(
        0x0105,
        (
            '#040F不行……！\n',
            '必须赶快去女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37BE')

    def _loc_376B(): pass

    label('loc_376B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37BE',
    )

    ChrTalk(
        0x0103,
        (
            '#020F哎呀，这边\n',
            '不是女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350004V#000F嗯，在西北方！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37BE(): pass

    label('loc_37BE')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000E offset: 0x37DA
@scena.Code('func_0E_37DA')
def func_0E_37DA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 4, 0x664)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_37E7',
    )

    Return()

    def _loc_37E7(): pass

    label('loc_37E7')

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00CC, 4, 0x664))
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, -870, 19750, 107400, 180)
    ChrSetPos(0x0009, 910, 19750, 107400, 180)
    Fade(1000)
    ChrSetPos(0x0101, 100, 17250, 98400, 0)
    ChrSetPos(0x0103, -1300, 17000, 97610, 0)
    ChrSetPos(0x0105, 1670, 17000, 97720, 0)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0103, 7)
    ChrSetChipByIndex(0x0105, 9)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0103, 0x1000)
    ChrClearFlags(0x0105, 0x1000)
    CameraMove(290, 18000, 103070, 0)

    ChrTalk(
        0x0008,
        (
            '来、来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '此路不通！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F但……\n',
            '我们必须要通过这里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F再阻拦的话\n',
            '就把你们打飞！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_38EF')
    def lambda_38EF():
        CameraMove(2650, 14000, 77790, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38EF)

    @scena.Lambda('lambda_3907')
    def lambda_3907():
        ChrWalkTo(0x00FE, -310, 19250, 128630, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3907)

    @scena.Lambda('lambda_3922')
    def lambda_3922():
        ChrWalkTo(0x00FE, -310, 19250, 128630, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_3922)

    @scena.Lambda('lambda_393D')
    def lambda_393D():
        ChrWalkTo(0x00FE, -310, 19250, 128630, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_393D)

    Sleep(500)

    Battle(0x000003A9, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_3970'),
        (-1, 'loc_3973'),
    )

    def _loc_3970(): pass

    label('loc_3970')

    OP_B4(0x00)

    Return()

    def _loc_3973(): pass

    label('loc_3973')

    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    ChrSetPos(0x0008, -2290, 19000, 105820, 236)
    ChrSetPos(0x0009, 2930, 18000, 103750, 112)
    ChrSetPos(0x0101, -10, 18000, 103540, 351)
    ChrSetPos(0x0103, -1250, 18000, 101680, 4)
    ChrSetPos(0x0105, 1290, 18000, 101820, 5)
    Sleep(500)

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x39F9
@scena.Code('func_0F_39F9')
def func_0F_39F9():
    EventBegin(0x00)
    FadeIn(2000, 0)
    CameraMove(30, 12000, 67150, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x07, 0xFF)
    ChrSetPos(0x0101, -6690, 12000, 53510, 0)
    ChrSetPos(0x0102, -6380, 12000, 54650, 0)
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
    ChrSetPos(0x0014, -7210, 12000, 58180, 0)
    ChrSetPos(0x0015, -9680, 12000, 54680, 0)
    ChrSetPos(0x0016, -7920, 12000, 56380, 0)
    ChrSetPos(0x0017, -10390, 12000, 56310, 0)
    ChrSetPos(0x0018, 6170, 12000, 53150, 0)
    ChrSetPos(0x0019, 6210, 12000, 53870, 0)
    ChrSetPos(0x001A, -7990, 12000, 54100, 0)
    ChrSetPos(0x001B, -10220, 12000, 52510, 0)
    ChrSetPos(0x001C, -6470, 12000, 48980, 0)
    ChrSetPos(0x001D, -1110, 12000, 70820, 0)
    ChrSetPos(0x001E, 1020, 12000, 70710, 0)
    ChrSetPos(0x001F, 10, 12000, 71740, 0)
    ChrSetPos(0x0020, 20, 12000, 67080, 0)
    ChrSetPos(0x0013, 650, 12000, 67820, 0)
    ChrSetPos(0x0021, 6760, 12000, 57310, 0)
    ChrSetPos(0x0022, 5980, 12000, 57880, 0)
    ChrSetPos(0x0023, 7530, 12000, 55190, 0)
    ChrSetPos(0x0024, 6470, 12000, 55570, 0)
    ChrSetPos(0x0025, 9010, 12000, 57270, 0)
    ChrSetPos(0x0026, 9250, 12000, 55950, 0)
    ChrSetPos(0x0027, -4290, 14000, 77250, 180)
    ChrSetPos(0x0028, 4190, 14000, 77300, 180)
    ChrSetPos(0x0029, -4270, 12000, 70900, 180)
    ChrSetPos(0x002A, 4210, 12000, 70900, 180)

    @scena.Lambda('lambda_3C8B')
    def lambda_3C8B():
        ChrWalkTo(0x00FE, -1110, 12000, 53820, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_3C8B)

    @scena.Lambda('lambda_3CA6')
    def lambda_3CA6():
        ChrWalkTo(0x00FE, 1020, 12000, 53710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_3CA6)

    @scena.Lambda('lambda_3CC1')
    def lambda_3CC1():
        ChrWalkTo(0x00FE, 10, 12000, 54740, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_3CC1)

    @scena.Lambda('lambda_3CDC')
    def lambda_3CDC():
        ChrWalkTo(0x00FE, 20, 12000, 50080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_3CDC)

    @scena.Lambda('lambda_3CF7')
    def lambda_3CF7():
        ChrWalkTo(0x00FE, 650, 12000, 50820, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_3CF7)

    @scena.Lambda('lambda_3D12')
    def lambda_3D12():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3D12')

    DispatchAsync2(0x0101, 0x0001, lambda_3D12)

    @scena.Lambda('lambda_3D23')
    def lambda_3D23():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3D23')

    DispatchAsync2(0x0102, 0x0001, lambda_3D23)

    @scena.Lambda('lambda_3D34')
    def lambda_3D34():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3D34')

    DispatchAsync2(0x0014, 0x0001, lambda_3D34)

    @scena.Lambda('lambda_3D45')
    def lambda_3D45():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3D45')

    DispatchAsync2(0x0015, 0x0001, lambda_3D45)

    @scena.Lambda('lambda_3D56')
    def lambda_3D56():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3D56')

    DispatchAsync2(0x0016, 0x0001, lambda_3D56)

    @scena.Lambda('lambda_3D67')
    def lambda_3D67():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3D67')

    DispatchAsync2(0x0017, 0x0001, lambda_3D67)

    @scena.Lambda('lambda_3D78')
    def lambda_3D78():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3D78')

    DispatchAsync2(0x0018, 0x0001, lambda_3D78)

    @scena.Lambda('lambda_3D89')
    def lambda_3D89():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3D89')

    DispatchAsync2(0x0019, 0x0001, lambda_3D89)

    @scena.Lambda('lambda_3D9A')
    def lambda_3D9A():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3D9A')

    DispatchAsync2(0x001A, 0x0001, lambda_3D9A)

    @scena.Lambda('lambda_3DAB')
    def lambda_3DAB():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3DAB')

    DispatchAsync2(0x001B, 0x0001, lambda_3DAB)

    @scena.Lambda('lambda_3DBC')
    def lambda_3DBC():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3DBC')

    DispatchAsync2(0x001C, 0x0001, lambda_3DBC)

    @scena.Lambda('lambda_3DCD')
    def lambda_3DCD():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3DCD')

    DispatchAsync2(0x0021, 0x0001, lambda_3DCD)

    @scena.Lambda('lambda_3DDE')
    def lambda_3DDE():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3DDE')

    DispatchAsync2(0x0022, 0x0001, lambda_3DDE)

    @scena.Lambda('lambda_3DEF')
    def lambda_3DEF():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3DEF')

    DispatchAsync2(0x0023, 0x0001, lambda_3DEF)

    @scena.Lambda('lambda_3E00')
    def lambda_3E00():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3E00')

    DispatchAsync2(0x0024, 0x0001, lambda_3E00)

    @scena.Lambda('lambda_3E11')
    def lambda_3E11():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3E11')

    DispatchAsync2(0x0025, 0x0001, lambda_3E11)

    @scena.Lambda('lambda_3E22')
    def lambda_3E22():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_3E22')

    DispatchAsync2(0x0026, 0x0001, lambda_3E22)

    @scena.Lambda('lambda_3E33')
    def lambda_3E33():
        CameraMove(-1510, 12000, 54280, 9000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3E33)

    @scena.Lambda('lambda_3E4B')
    def lambda_3E4B():
        OP_6E(342, 9000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_3E4B)

    WaitForThreadExit(0x0000, 0x0002)
    Sleep(1000)

    @scena.Lambda('lambda_3E65')
    def lambda_3E65():
        CameraMove(0, 12000, 47170, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3E65)

    ChrWalkTo(0x0020, 30, 12000, 47230, 1000, 0x00)
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x3EA3
@scena.Code('func_10_3EA3')
def func_10_3EA3():
    EventBegin(0x00)
    FadeIn(2000, 0)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    CameraMove(-670, 4500, 47060, 0)
    OP_67(0, 2670, -10000, 0)
    CameraSetDistance(2470, 0)
    OP_6C(338000, 0)
    OP_6E(538, 0)

    @scena.Lambda('lambda_3EFB')
    def lambda_3EFB():
        OP_67(0, 6660, -10000, 16000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3EFB)

    @scena.Lambda('lambda_3F13')
    def lambda_3F13():
        CameraSetDistance(5000, 16000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3F13)

    @scena.Lambda('lambda_3F23')
    def lambda_3F23():
        CameraMove(390, 14500, 76830, 16000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3F23)

    Sleep(2000)

    @scena.Lambda('lambda_3F40')
    def lambda_3F40():
        OP_6C(50000, 14000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3F40)

    Sleep(10000)

    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4261._SN', 107, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x3F6C
@scena.Code('func_11_3F6C')
def func_11_3F6C():
    OP_1F(0x64, 0x000000C8)

    Return()

# id: 0x0012 offset: 0x3F73
@scena.Code('func_12_3F73')
def func_12_3F73():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F7C',
    )

    Return()

    def _loc_3F7C(): pass

    label('loc_3F7C')

    EventBegin(0x00)
    ChrSetFlags(0x002D, 0x0040)
    ChrSetChipByIndex(0x002D, 32)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetPos(0x002D, -42970, 16000, 81320, 270)
    ChrSetFlags(0x002D, 0x0004)

    @scena.Lambda('lambda_3FA9')
    def lambda_3FA9():
        OP_99(0x00FE, 0x00, 0x07, 800)
        Yield()

        Jump('lambda_3FA9')

    DispatchAsync2(0x002D, 0x0001, lambda_3FA9)

    Fade(1000)
    CameraMove(-47380, 16000, 81820, 0)
    OP_67(0, 5390, -10000, 0)
    CameraSetDistance(1470, 0)
    OP_6C(45000, 0)
    OP_6E(532, 0)

    @scena.Lambda('lambda_3FFE')
    def lambda_3FFE():
        CameraMove(-44280, 16000, 81720, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3FFE)

    WaitForThreadExit(0x0101, 0x0002)
    OP_20(0x000007D0)
    OP_21()
    TerminateThread(0x002D, 0xFF)
    Sleep(1000)

    ChrSetPos(0x0101, -34850, 16000, 75130, 0)

    @scena.Lambda('lambda_403B')
    def lambda_403B():
        CameraMove(-42280, 16000, 81720, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_403B)

    @scena.Lambda('lambda_4053')
    def lambda_4053():
        ChrWalkTo(0x00FE, -41300, 16000, 81000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4053)

    Sleep(2000)

    ExecExpressionWithValue(
        0x002D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x002D, 33)
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x002D, 400)
    Sleep(500)

    ChrTurnDirection(0x002D, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x002D,
        (
            '#0020141333V#011F……啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141334V今天的夜色真美啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141335V#501F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141336V还是这首曲子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141337V『星之所在』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020141338V#015F我曾经失去了许多东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141339V只有这首曲子、这支口琴，\n',
            '至今仍陪伴着我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141340V所以，我会经常吹起它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130273V#580F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020141342V#010F我是不是该履行约定了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141343V和你相遇之前……我所经历过的事情……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141344V现在，我全部告诉你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141345V#004F约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141346V#002F嗯……我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x002D,
        (
            '#0020141347V#013F不过，故事稍微有点长……\n',
            '即使这样……你也不会介意吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141348V#006F当然……\n',
            '我肯定会认真地听到最后的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020141349V#019F谢谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141350V#011F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x002D, 0xFF)

    @scena.Lambda('lambda_438C')
    def lambda_438C():
        OP_6C(86000, 3000)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_438C)

    Sleep(1500)

    ChrSetDirection(0x002D, 270, 400)
    ChrClearFlags(0x002D, 0x0001)
    ChrWalkTo(0x002D, -43520, 15900, 81370, 800, 0x00)
    ChrSetChipByIndex(0x002D, 39)
    ChrSetFlags(0x002D, 0x0002)
    ChrSetSubChip(0x002D, 8)
    WaitForThreadExit(0x002D, 0x0001)
    OP_99(0x002D, 0x08, 0x0A, 800)
    PlayBGM(91)
    Sleep(1000)

    ChrTalk(
        0x002D,
        (
            '#0020141351V#015F很久以前，在某个地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141352V在某个地方，有一个男孩。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020141353V',
            (TxtCtl.SetColor, 0xC),
            '一个非常爱撒娇、个性懦弱，\n',
            '而且没有任何长处的男孩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141354V不过，因为和最重要的亲人生活在一起，\n',
            '男孩每天都过得非常幸福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD('ED6_DT04/C_VIS028._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020141355V但是，因为某件事的发生，\n',
            '男孩的心完全地破碎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141356V丧失了言语和感情，\n',
            '连饭也不吃地每天只吹着口琴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141357V照顾他的人无论多么地努力，\n',
            '也只能看着男孩一天比一天衰弱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_AD('ED6_DT04/C_VIS029._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020141358V就在这时，一个魔法师出现在男孩面前。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141359V『我可以治好这孩子的心。』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141360V『不过要向我付出代价。』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141361V就这样，男孩被交托给魔法师。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000000C8)
    Sleep(2000)

    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020141362V破碎的心被重新整合在一起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141363V然而，魔法师也将男孩的存在肆意地修改。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141364V终于，当得到新的心的时候——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141365V男孩变成了一个杀手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD('ED6_DT04/C_VIS030._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020141366V在两年的时间里，\n',
            '男孩每天都在不断地杀人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141367V曾经将几十人的部队暗中全灭。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141368V曾经潜入守卫森严的某国大臣的住宅，\n',
            '将大臣的喉咙切断。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141369V有时还使用炸药，\n',
            '将无辜的人们卷入灾难之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141370V不知何时起，男孩从一个普通的杀手\n',
            '化身为一只可怕的怪物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141371V不知何时起，男孩被称作『漆黑之牙』，\n',
            '变成了一个令人恐惧的存在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000000C8)
    Sleep(2000)

    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020141372V之后，男孩接到了魔法师的命令，\n',
            '去暗杀某个目标人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD('ED6_DT04/C_VIS031._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020141373V那是一个曾经守卫了女王治理的国家，\n',
            '成功地击退了北方大国侵略的英雄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141374V同时也是大陆上拥有特别称号的\n',
            '四个游击士的其中一个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141375V——但是，那个人实在太强大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141376V就像小猫被老虎轻松闪避一样，\n',
            '男孩一下子就被目标人物击退了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000000C8)
    Sleep(2000)

    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020141377V在任务失败的男孩面前，\n',
            '出现了魔法师派来的手下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141378V他们是为了解决\n',
            '被目标人物看到真面目的男孩而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141379V但是，有一个人将他们赶走，\n',
            '还救下了男孩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD('ED6_DT04/C_VIS032._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020141380V他正是男孩暗杀失败的那个目标人物。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141381V之后，男孩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0020141382V被那个人带到了自己的家里，\n',
            '而且，还和一个女孩相遇了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x00000064)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    Sleep(500)

    ChrTalk(
        0x002D,
        (
            '#0020141383V#015F在那个家里，男孩过着幸福的生活。\n',
            '是如同梦境一样的、五年的幸福时光。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141384V也许，对那个男孩来说，\n',
            '那是一场他不被允许去拥有的美梦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141385V所以，梦终究会消失。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141386V回到现实的时刻也已经迫近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x002D, 0x0A, 0x08, 800)
    Sleep(500)

    Fade(500)
    ChrSetPos(0x002D, -43500, 16000, 81370, 270)
    ChrSetChipByIndex(0x002D, 33)
    ChrClearFlags(0x002D, 0x0002)
    ChrSetSubChip(0x002D, 0)
    OP_0D()

    @scena.Lambda('lambda_4D65')
    def lambda_4D65():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x002D, 0x0001, lambda_4D65)

    Sleep(1000)

    ChrTurnDirection(0x002D, 0x0101, 400)
    WaitForThreadExit(0x002D, 0x0001)

    ChrTalk(
        0x002D,
        (
            '#0020141387V#011F到这里……故事就结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141388V谢谢你……\n',
            '能够一直坚持着听到最后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141389V#580F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141390V#506F……哎……啊哈…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141391V究竟……哪些才是真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020141392V#015F全部，都是真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141393V我的心已经破碎了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141394V我的手沾满了血。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141395V还有暗杀你的父亲失败。\n',
            '……所有所有的事，都是真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141396V#013F而且……\n',
            '到现在也仍一直在背叛着你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141397V#580F！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020141398V#590F男孩真的是无可救药的怪物。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141399V不管到哪里……\n',
            '都只会带来不幸和灾厄……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141400V他就是这样污秽的存在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141401V#580F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020141402V#011F所以……\n',
            '男孩决定要踏上旅途。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141403V为了不再使那些让自己做了\n',
            '如此幸福的美梦的人被卷进来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141404V也为了阻止那个\n',
            '制造了自己这种怪物的邪恶魔法师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x002D, 0x0002)
    ChrSetFlags(0x002D, 0x1000)
    ChrSetChipByIndex(0x002D, 40)

    @scena.Lambda('lambda_50E0')
    def lambda_50E0():
        OP_99(0x00FE, 0x00, 0x07, 1200)
        Yield()

        Jump('lambda_50E0')

    DispatchAsync2(0x002D, 0x0001, lambda_50E0)

    @scena.Lambda('lambda_50F3')
    def lambda_50F3():
        ChrMoveTo(0x00FE, -41970, 16000, 81000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0002, lambda_50F3)

    Sleep(500)

    ChrSetFlags(0x002D, 0x0001)
    WaitForThreadExit(0x002D, 0x0002)
    PlaySE(143, 0x00, 0x50)
    TerminateThread(0x002D, 0x01)
    ChrClearFlags(0x002D, 0x1000)
    ChrClearFlags(0x002D, 0x0002)
    ChrSetChipByIndex(0x002D, 33)
    ChrSetSubChip(0x002D, 0)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 42)
    ChrSetFlags(0x0101, 0x0002)
    Sleep(500)

    @scena.Lambda('lambda_514E')
    def lambda_514E():
        ChrMoveTo(0x00FE, -43300, 16000, 81000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0002, lambda_514E)

    Sleep(1000)

    ChrClearFlags(0x002D, 0x0001)
    WaitForThreadExit(0x002D, 0x0002)
    ChrSetSubChip(0x0101, 30)
    Sleep(100)

    ChrSetSubChip(0x0101, 31)
    Sleep(100)

    ChrSetSubChip(0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010141405V#580F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020141406V#011F这是让我将人的心一直保持到最后的东西。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141407V但是，我已经不需要它了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141408V所以，希望你能收下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141409V#019F虽然可能算不上这五年来的谢礼……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141410V不过，我想总比什么都没有要好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141411V#002F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x00, 0x02, 800)
    OP_9E(0x0101, 15, 0, 300, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010141412V#582F…………你说够了没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020101214V#014F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 43)

    @scena.Lambda('lambda_5341')
    def lambda_5341():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_5341')

    DispatchAsync2(0x0101, 0x0001, lambda_5341)

    ChrSetFlags(0x0101, 0x1000)
    ChrMoveTo(0x0101, -42300, 16000, 81000, 3000, 0x00)
    TerminateThread(0x0101, 0x01)
    ChrSetSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010141414V#005F#3S#2P你究竟说够了没有！',
            TxtCtl.Enter,
        ),
    )

    ChrSetChipByIndex(0x0101, 42)
    OP_99(0x0101, 0x03, 0x04, 1000)
    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010141415V#003F#2P说什么在做梦……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141416V难道……到现在为止的事情，\n',
            '全部都不是真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x12, 0x14, 800)
    OP_99(0x0101, 0x13, 0x12, 800)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010141417V#508F#2P过去怎么了！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141418V心破碎了！？\n',
            '那又怎么样！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020121200V#013F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x06, 0x08, 800)
    OP_99(0x0101, 0x07, 0x06, 800)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010141420V#005F#2P看着我！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141421V看着我的眼睛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141422V#003F我一直……\n',
            '把那男孩的事情看在眼里！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141423V好的地方、不好的地方我都清楚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141424V男孩不管承受怎样的痛苦，\n',
            '都会抱着坚定决心努力下去的地方我也清楚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010141425V#504F#2P#3S因为……\n',
            '我喜欢那样的约修亚！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020141426V#014F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x09, 0x10, 1500)

    @scena.Lambda('lambda_5639')
    def lambda_5639():
        OP_99(0x00FE, 0x0E, 0x10, 800)
        Yield()

        Jump('lambda_5639')

    DispatchAsync2(0x0101, 0x0001, lambda_5639)

    ChrTalk(
        0x0101,
        (
            '#0010141427V#583F#2P所以，我绝对不会让你一个人去的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141428V就这样丢下我、不理会我的感受，\n',
            '自己一个人背负着痛苦地离开！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    ChrSetSubChip(0x0101, 17)
    Sleep(50)

    ChrSetSubChip(0x0101, 18)
    Sleep(150)

    ChrSetSubChip(0x0101, 19)
    Sleep(50)

    ChrSetSubChip(0x0101, 20)
    Sleep(50)

    ChrSetSubChip(0x0101, 18)

    ChrTalk(
        0x0101,
        (
            '#0010141429V#583F#3S#2P我绝对不允许！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020141430V#012F……艾丝蒂尔………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141431V#015F……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5794')
    def lambda_5794():
        CameraMove(-41780, 16000, 81720, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5794)

    OP_99(0x0101, 0x15, 0x18, 1200)

    @scena.Lambda('lambda_57B5')
    def lambda_57B5():
        ChrWalkTo(0x00FE, -42780, 16000, 81000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0002, lambda_57B5)

    Sleep(500)

    ChrSetFlags(0x002D, 0x0001)
    WaitForThreadExit(0x002D, 0x0002)
    Fade(500)
    OP_20(0x000007D0)
    ChrSetPos(0x002D, -42300, 16000, 81000, 90)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x002D, 0x0002)
    ChrSetChipByIndex(0x002D, 41)
    ChrSetSubChip(0x002D, 0)
    OP_0D()
    OP_99(0x002D, 0x00, 0x02, 1800)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010141432V#004F#2P啊……？',
            TxtCtl.Enter,
        ),
    )

    OP_99(0x002D, 0x03, 0x04, 1500)
    CloseMessageWindow()
    OP_21()
    PlayBGM(80)
    Sleep(1000)

    Fade(1000)

    @scena.Lambda('lambda_5855')
    def lambda_5855():
        CameraSetDistance(1300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5855)

    ChrSetSubChip(0x002D, 5)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010141433V#2P………啊………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x002D, 0x05, 0x06, 800)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010141434V#2P（………约修亚…………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1500)

    ChrSetSubChip(0x002D, 5)
    Sleep(500)

    ChrClearFlags(0x0101, 0x0080)
    ChrSetChipByIndex(0x0101, 42)
    ChrSetSubChip(0x0101, 26)
    ChrSetPos(0x0101, -42000, 16000, 81000, 270)
    ChrClearFlags(0x002D, 0x0002)
    ChrSetPos(0x002D, -42780, 16000, 81000, 90)
    ChrSetChipByIndex(0x002D, 33)
    ChrSetSubChip(0x002D, 0)

    @scena.Lambda('lambda_593E')
    def lambda_593E():
        CameraSetDistance(1500, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_593E)

    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x0101, -41200, 16000, 81000, 300, 5000)
    ChrJumpTo(0x0101, -40800, 16000, 81000, 100, 4000)
    OP_99(0x0101, 0x1A, 0x1D, 1200)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    ChrSetSubChip(0x0101, 25)
    OP_0D()

    @scena.Lambda('lambda_599A')
    def lambda_599A():
        OP_6C(55000, 60000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_599A)

    @scena.Lambda('lambda_59AA')
    def lambda_59AA():
        CameraSetDistance(1300, 60000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_59AA)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010141435V#580F#2P刚才……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141436V流进嘴里的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x002D,
        (
            '#0020141437V#591F……是即时生效的催眠药。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141438V没有副作用，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    Sleep(250)

    FadeIn(250, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010141439V#584F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 44)
    PlaySE(209, 0x00, 0x50)
    OP_99(0x0101, 0x00, 0x03, 1000)
    Sleep(1000)

    OP_99(0x0101, 0x03, 0x05, 800)

    ChrTalk(
        0x0101,
        (
            '#0010141440V#584F#2P为……为什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x05, 0x07, 800)

    ChrTalk(
        0x0101,
        (
            '#0010141441V#584F#2P……为什么用那样的东西……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x002D,
        (
            '#0020141442V#594F我的艾丝蒂尔……\n',
            '你就像太阳那样的耀眼、那样的眩目。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141443V和你在一起虽然很幸福、很快乐，\n',
            '但同时，也会感到很痛苦、很无奈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141444V就像强光可以产生浓重的影子一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141445V越是和你在一起的时候，\n',
            '我就越会不由得意识到自己可憎的本性……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141446V所以，我有时也会想，\n',
            '如果我们没有相遇过就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x07, 0x09, 800)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010141447V#585F#2P……怎么会………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5CAE')
    def lambda_5CAE():
        CameraMove(-41280, 16000, 81720, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5CAE)

    ChrMoveTo(0x002D, -42000, 16000, 81100, 1000, 0x00)
    ChrSetChipByIndex(0x002D, 45)
    ChrSetFlags(0x002D, 0x0002)

    ExecExpressionWithValue(
        0x002D,
        0x28,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    OP_99(0x002D, 0x00, 0x02, 1200)
    Sleep(800)

    ChrTalk(
        0x002D,
        (
            '#0020141448V#592F#6P不过，现在不一样了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141449V我很感激能和你相遇。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141450V虽然，我不得不从如此珍爱的你身边逃走……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141451V但是，我会比任何人都更加地想念你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x09, 0x0B, 800)

    ChrTalk(
        0x0101,
        (
            '#0010141452V#585F#2P……约修亚……约修亚………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x002D,
        (
            '#0020141453V#593F#6P一直以来，真的很感谢你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141454V从第一次见到你的时候起……\n',
            '我就一直深深地喜欢着你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_99(0x002D, 0x02, 0x05, 1200)
    OP_0D()
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020141455V',
            (TxtCtl.SetColor, 0x0),
            '——再见了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_20(0x00000FA0)
    OP_21()

    ExecExpressionWithValue(
        0x002D,
        0x28,
        (
            (Expr.PushLong, 0x20),
            Expr.Not,
            Expr.And2,
            Expr.Return,
        ),
    )

    CameraMove(-89960, 14000, -12180, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(0, 0)
    OP_0D()
    OP_21()
    PlayMovie(0x00, 'ed6_dt17.dat')
    def _loc_5F24(): pass

    label('loc_5F24')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_60A2',
    )

    Sleep(10)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Return,
        ),
        'loc_609F',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '')
    Sleep(500)

    WaitEffect(0x15, 0x00)
    OP_AD('ED6_DT04/C_VIS039._CH', 0x0000, 0x0000, 0x000000C8)
    Sleep(2000)

    OP_56(0x03)
    FadeIn(0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　 　　 ～　关于通关存档的保存　～\n',
            '　　 　　　　建立通关存档后，可以在标题画面中读取，\n',
            '　　  　　　　 从而继承各项数据，开始二周目游戏。',
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        170,
        100,
        0,
        (
            TXT(0x00, '【保存通关存档】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6051',
    )

    SaveClearData()

    def _loc_6051(): pass

    label('loc_6051')

    Sleep(1000)

    OP_AE(0x000001F4)
    FadeIn(0, 0)
    PlayMovie(0x00, 'ed6_dt18.dat')
    def _loc_6073(): pass

    label('loc_6073')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_609F',
    )

    Sleep(10)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Return,
        ),
        'loc_609C',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '')
    Sleep(1500)

    OP_B4(0x01)

    def _loc_609C(): pass

    label('loc_609C')

    Jump('loc_6073')

    def _loc_609F(): pass

    label('loc_609F')

    Jump('loc_5F24')

    def _loc_60A2(): pass

    label('loc_60A2')

    Return()

# id: 0x0013 offset: 0x60A3
@scena.Code('func_13_60A3')
def func_13_60A3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 3, 0x643)),
            (Expr.Eval, "OP_42(0x0037)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_613B',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0008,
        (
            '#2620120501V哦，希尔丹夫人。\n',
            '还有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120502V我们会好好保护陛下的。\n',
            '请放心吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_61CE')

    def _loc_613B(): pass

    label('loc_613B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 6, 0x63E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_61CE',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#2620120503V女王宫附近\n',
            '禁止无关人等接近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120504V就算想见陛下\n',
            '也是不允许的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    ChrSetDirection(0x0008, 180, 0)
    Sleep(50)

    EventEnd(0x04)

    def _loc_61CE(): pass

    label('loc_61CE')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

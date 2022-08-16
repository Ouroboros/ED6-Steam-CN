import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4201   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4201.x'
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
        ('ED6_DT06/CH20143._CH', 'ED6_DT06/CH20143P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
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
        ('ED6_DT06/CH20127._CH', 'ED6_DT06/CH20127P._CP'),
        ('ED6_DT06/CH20030._CH', 'ED6_DT06/CH20030P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT06/CH20040._CH', 'ED6_DT06/CH20040P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00280._CH', 'ED6_DT07/CH00280P._CP'),
        ('ED6_DT07/CH00281._CH', 'ED6_DT07/CH00281P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT06/CH20128._CH', 'ED6_DT06/CH20128P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
    ]

# id: 0x10001 offset: 0x212
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
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
            dword_10            = 31,
            chipIndex           = 31,
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
            dword_10            = 31,
            chipIndex           = 31,
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
            dword_10            = 31,
            chipIndex           = 31,
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
            dword_10            = 43,
            chipIndex           = 43,
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
            dword_10            = 43,
            chipIndex           = 43,
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
            dword_10            = 31,
            chipIndex           = 31,
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
            dword_10            = 31,
            chipIndex           = 31,
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
            dword_10            = 31,
            chipIndex           = 31,
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
            dword_10            = 43,
            chipIndex           = 43,
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
            dword_10            = 43,
            chipIndex           = 43,
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
            name                = '修理员佩顿',
            x                   = 1110,
            z                   = 15350,
            y                   = 56390,
            direction           = 235,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
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

# id: 0x10002 offset: 0x7B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x7B2
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
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -4340,
            y           = 19000,
            z           = 105990,
            range       = 4220,
            dword_10    = 0x00004650,
            dword_14    = 0x0001933E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -4280,
            y           = 16000,
            z           = 78500,
            range       = 5010,
            dword_10    = 0x000032C8,
            dword_14    = 0x0001270A,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = -4730,
            y           = 18000,
            z           = 98010,
            range       = 4880,
            dword_10    = 0x00003E80,
            dword_14    = 0x00017534,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000F,
        ),
        ScenaEventData(
            x           = 32759,
            y           = 15500,
            z           = 76820,
            range       = 35080,
            dword_10    = 0x00004074,
            dword_14    = 0x000116D4,
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

# id: 0x10004 offset: 0x872
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x872
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_889',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_08_28B9)

    def _loc_889(): pass

    label('loc_889')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_8A0',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0C_2EB9)

    def _loc_8A0(): pass

    label('loc_8A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_8AE',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_10_3FAF)

    def _loc_8AE(): pass

    label('loc_8AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_8BC',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, func_11_4529)

    def _loc_8BC(): pass

    label('loc_8BC')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_8CC'),
        (0x00000065, 'loc_8E2'),
        (-1, 'loc_8F8'),
    )

    def _loc_8CC(): pass

    label('loc_8CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 5, 0x63D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8DF',
    )

    SetScenaFlags(ScenaFlag(0x00C7, 5, 0x63D))
    Event(0, func_04_C87)

    def _loc_8DF(): pass

    label('loc_8DF')

    Jump('loc_8F8')

    def _loc_8E2(): pass

    label('loc_8E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 5, 0x645)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8F5',
    )

    SetScenaFlags(ScenaFlag(0x00C8, 5, 0x645))
    Event(0, func_07_212F)

    def _loc_8F5(): pass

    label('loc_8F5')

    Jump('loc_8F8')

    def _loc_8F8(): pass

    label('loc_8F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Return,
        ),
        'loc_909',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)

    def _loc_909(): pass

    label('loc_909')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_91D',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)

    Jump('loc_947')

    def _loc_91D(): pass

    label('loc_91D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_947',
    )

    ChrSetChipByIndex(0x0000, 1)
    ChrSetChipByIndex(0x0001, 2)
    ChrSetChipByIndex(0x0138, 3)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_947(): pass

    label('loc_947')

    Return()

# id: 0x0001 offset: 0x948
@scena.Code('func_01_948')
def func_01_948():
    OP_71(0x0000, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_965',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_97A')

    def _loc_965(): pass

    label('loc_965')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_97A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x58),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_97A(): pass

    label('loc_97A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 6, 0x666)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B5A',
    )

    OP_1B(0x00, 0x00, 0x000E)
    OP_A1(0x0033, 0x0000)
    OP_A1(0x0034, 0x0001)
    OP_72(0x0000, 0x0004)
    OP_72(0x0000, 0x0002)
    OP_71(0x0000, 0x0400)
    OP_71(0x0000, 0x0040)
    OP_72(0x0001, 0x0004)
    OP_72(0x0001, 0x0002)
    OP_71(0x0001, 0x0400)
    OP_71(0x0001, 0x0040)
    ChrSetPos(0x0033, 2320, 12050, 57280, 56)
    ChrSetPos(0x0034, 2320, 12050, 57280, 56)
    ChrClearFlags(0x0032, 0x0080)
    ChrSetFlags(0x0032, 0x0004)
    ChrSetFlags(0x0032, 0x0400)
    OP_6F(0x0000, 360)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 1, 0x661)),
            Expr.Return,
        ),
        'loc_A5C',
    )

    ChrSetPos(0x0008, -7920, 12000, 56580, 94)
    ChrSetPos(0x0009, -9260, 12000, 57540, 284)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0008, 35)
    ChrSetChipByIndex(0x0009, 35)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0009, 0x0800)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)

    def _loc_A5C(): pass

    label('loc_A5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 2, 0x662)),
            Expr.Return,
        ),
        'loc_AF3',
    )

    ChrSetPos(0x000E, 3890, 14000, 79000, 146)
    ChrSetPos(0x000F, 3080, 14000, 77370, 283)
    ChrSetPos(0x0010, 6700, 14000, 78300, 358)

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000E, 35)
    ChrSetChipByIndex(0x000F, 35)
    ChrSetChipByIndex(0x0010, 35)
    ChrClearFlags(0x000E, 0x0001)
    ChrClearFlags(0x000F, 0x0001)
    ChrClearFlags(0x0010, 0x0001)
    ChrSetFlags(0x000E, 0x0800)
    ChrSetFlags(0x000F, 0x0800)
    ChrSetFlags(0x0010, 0x0800)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    def _loc_AF3(): pass

    label('loc_AF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 4, 0x664)),
            Expr.Return,
        ),
        'loc_B5A',
    )

    ChrSetPos(0x0011, -2160, 18000, 102100, 309)
    ChrSetPos(0x0012, 2230, 18000, 101600, 82)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0011, 0x0001)
    ChrClearFlags(0x0012, 0x0001)
    ChrSetFlags(0x0011, 0x0800)
    ChrSetFlags(0x0012, 0x0800)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0011, 35)
    ChrSetChipByIndex(0x0012, 35)

    def _loc_B5A(): pass

    label('loc_B5A')

    Return()

# id: 0x0002 offset: 0xB5B
@scena.Code('func_02_B5B')
def func_02_B5B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B70',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_B5B')

    def _loc_B70(): pass

    label('loc_B70')

    Return()

# id: 0x0003 offset: 0xB71
@scena.Code('func_03_B71')
def func_03_B71():
    TalkBegin(0x0032)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '改造·换钱\n'),
            TXT(0x02, '购买道具\n'),
            TXT(0x03, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BDC',
    )

    OP_0D()
    OP_A9(0x6C)
    OP_56(0x00)
    TalkEnd(0x0032)

    Return()

    def _loc_BDC(): pass

    label('loc_BDC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BF2',
    )

    OP_0D()
    OP_A9(0x6D)
    OP_56(0x00)
    TalkEnd(0x0032)

    Return()

    def _loc_BF2(): pass

    label('loc_BF2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C03',
    )

    TalkEnd(0x0032)

    Return()

    def _loc_C03(): pass

    label('loc_C03')

    ChrTalk(
        0x0032,
        (
            '我带了一些可以调整大家的\n',
            '导力器的工具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0032,
        (
            '还有，我也准备了一些装备和道具，\n',
            '虽然种类不算很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0032,
        (
            '有需要的话请说一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0032)

    Return()

# id: 0x0004 offset: 0xC87
@scena.Code('func_04_C87')
def func_04_C87():
    EventBegin(0x00)
    CameraMove(31020, 10750, 79090, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, 29890, 10750, 79270, 0)
    ChrSetPos(0x0102, 31020, 10750, 79090, 0)

    @scena.Lambda('lambda_0CEE')
    def lambda_0CEE():
        ChrWalkTo(0x00FE, 27830, 12000, 94950, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0CEE)

    @scena.Lambda('lambda_0D09')
    def lambda_0D09():
        ChrWalkTo(0x00FE, 29230, 12000, 94990, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0D09)

    @scena.Lambda('lambda_0D24')
    def lambda_0D24():
        CameraMove(29660, 12000, 100020, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D24)

    @scena.Lambda('lambda_0D3C')
    def lambda_0D3C():
        OP_67(0, 5000, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D3C)

    @scena.Lambda('lambda_0D54')
    def lambda_0D54():
        OP_6C(12000, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0D54)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010120369V#000F哇啊～……好美……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120370V这里就是王城的空中庭园啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020120371V#010F是啊……湖面一览无余，\n',
            '还可以俯瞰格兰赛尔周围的城邑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120372V想来参观的人肯定很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120373V#000F呼～如果不是处于这种时刻，\n',
            '本可以好好欣赏这里的景色的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120374V现在还是优先完成任务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0xEA6
@scena.Code('func_05_EA6')
def func_05_EA6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 6, 0x63E)),
            Expr.Return,
        ),
        'loc_EAE',
    )

    Return()

    def _loc_EAE(): pass

    label('loc_EAE')

    SetScenaFlags(ScenaFlag(0x00C7, 6, 0x63E))
    OP_28(0x0049, 0x01, 0x0400)
    EventBegin(0x00)
    ChrSetDirection(0x0101, 0, 0)
    ChrSetDirection(0x0102, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#0010120381V#000F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120382V#010F看来这里就是女王宫了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F19')
    def lambda_0F19():
        ChrWalkTo(0x00FE, -850, 18000, 103480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F19)

    @scena.Lambda('lambda_0F34')
    def lambda_0F34():
        ChrWalkTo(0x00FE, 1080, 18000, 103610, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0F34)

    CameraMove(0, 20000, 107640, 3000)
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
            '#2630120384V哦……他们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010120385V#000F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120386V我们俩是公爵\n',
            '邀请的客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020120387V#010F这里就是陛下居住的\n',
            '女王宫对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630120388V……是的。',
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
            '#0010120391V#000F讨、讨厌啦～\n',
            '没有想到陛下会身体不适呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120392V这么说来，可得\n',
            '小心照料～才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120393V#010F对了，科洛蒂娅公主\n',
            '也在里面吗？',
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
            '#2630120395V……喂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120396V哦哦，公主正在细心的\n',
            '看护着陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120397V当然也就没有空\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000A, 280, 20000, 111970, 0)

    ChrTalk(
        0x000A,
        (
            '#0650120398V……你们在那里\n',
            '做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_1248')
    def lambda_1248():
        ChrWalkTo(0x00FE, 130, 19500, 106810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1248)

    @scena.Lambda('lambda_1263')
    def lambda_1263():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1263')

    DispatchAsync2(0x0008, 0x0001, lambda_1263)

    @scena.Lambda('lambda_1274')
    def lambda_1274():
        ChrWalkTo(0x00FE, -1540, 19750, 107050, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1274)

    @scena.Lambda('lambda_128F')
    def lambda_128F():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_128F')

    DispatchAsync2(0x0009, 0x0001, lambda_128F)

    @scena.Lambda('lambda_12A0')
    def lambda_12A0():
        ChrWalkTo(0x00FE, -1500, 19250, 106220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_12A0)

    WaitForThreadExit(0x000A, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#2620120399V夫人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630120400V您这就要回去了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000A, 0x0002)

    ChrTalk(
        0x000A,
        (
            '#0650120401V#710F很快晚宴就要开始了，\n',
            '我得暂且先回休息室去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120402V对了，这两位客人是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120403V武术大会优胜组的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120404V只不过是些游击士罢了，\n',
            '但也还算是邀请的客人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120405V#000F哼，什么叫只不过是游击士……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0008, 400)

    ChrTalk(
        0x000A,
        (
            '#0650120406V没礼貌的东西！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120407V你这就等于是在侮辱\n',
            '王城邀请的客人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2620120408V不……我们不是那个意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120409V虽说是由公爵大人邀请而来的，\n',
            '但只要是王城的来访者，就是陛下的客人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120410V这一点是绝对不能忘记的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120411V明、明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120412V#000F（好、好惊人的气势……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120413V#010F（难道这个人就是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120414V可是夫人……\n',
            '他们要想进去是肯定不行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620120415V这一点上校是说清楚了的，\n',
            '您也应该很明白的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120416V……这个我已经听烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000A, 140, 18750, 105490, 2000, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0650120417V非常抱歉，客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120418V因为加强戒备的缘故，\n',
            '所以接近女王宫是被禁止的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120419V如果可以的话，晚宴开始之前\n',
            '请在房间里等候好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120420V#000F啊……好、好的。',
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

    ChrTalk(
        0x0102,
        (
            '#0020120422V#010F劳您费心了。\n',
            '我们带来了不少麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#2620120423V哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2630120424V知道就好，人要知趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0008, 400)

    ChrTalk(
        0x000A,
        (
            '#0650120425V……………………（怒视）',
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
    ChrSetPos(0x0101, -620, 15500, 86640, 180)
    ChrSetPos(0x0102, 1430, 15500, 86590, 180)
    ChrSetPos(0x000A, 310, 15000, 85930, 180)

    @scena.Lambda('lambda_1894')
    def lambda_1894():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1894')

    DispatchAsync2(0x0101, 0x0001, lambda_1894)

    @scena.Lambda('lambda_18A5')
    def lambda_18A5():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_18A5')

    DispatchAsync2(0x0102, 0x0001, lambda_18A5)

    @scena.Lambda('lambda_18B6')
    def lambda_18B6():
        ChrWalkTo(0x00FE, -220, 14000, 80290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_18B6)

    @scena.Lambda('lambda_18D1')
    def lambda_18D1():
        ChrWalkTo(0x00FE, -910, 14000, 81230, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_18D1)

    @scena.Lambda('lambda_18EC')
    def lambda_18EC():
        ChrWalkTo(0x00FE, 490, 14000, 81580, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_18EC)

    @scena.Lambda('lambda_1907')
    def lambda_1907():
        CameraMove(-90, 14000, 81270, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1907)

    WaitForThreadExit(0x000A, 0x0001)
    ChrSetDirection(0x000A, 0, 400)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x000A,
        (
            '#0650120427V……他们做出那样丢脸的事，\n',
            '让你们见笑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120428V请允许我先自我介绍一下。\n',
            '我的名字叫希尔丹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120429V我是这个格兰赛尔城的女管家，\n',
            '主要就是监督侍女们工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120430V#000F果然是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120431V#010F原来您就是\n',
            '希尔丹夫人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120432V#710F哦……',
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
            '#0010120434V#000F啊……\n',
            '是从别人那里听说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x000A, 600, 2000, 0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '尤莉亚的介绍信\n',
            '交出了给了希尔丹夫人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveTo(0x0101, -910, 14000, 81230, 2000, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0650120435V#710F这个笔迹是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120436V#000F嗯，凭那个笔迹就可以判断是谁写的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120437V#010F这封介绍信以及游击士徽章\n',
            '就是我们身份的证明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650120438V#710F我明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120439V在这儿不太方便，\n',
            '先回侍女们的休息室吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120440V到那里再向你们请教详细的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4214._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x1C50
@scena.Code('func_06_1C50')
def func_06_1C50():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 3, 0x643)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1C5D',
    )

    Return()

    def _loc_1C5D(): pass

    label('loc_1C5D')

    SetScenaFlags(ScenaFlag(0x00C8, 3, 0x643))
    OP_28(0x004A, 0x01, 0x0080)
    EventBegin(0x00)
    Fade(1000)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0102, 3)
    ChrSetChipByIndex(0x0138, 1)
    ChrSetPos(0x0138, 10, 18500, 104830, 0)
    ChrSetPos(0x0101, -470, 18000, 103350, 0)
    ChrSetPos(0x0102, 740, 18000, 103280, 0)
    CameraMove(-70, 19000, 105810, 3000)

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
            '这么晚了\n',
            '找陛下还有社么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121050V#710F我把陛下吩咐过的红茶\n',
            '和一些食品带来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650860001V在这样的事态下，\n',
            '陛下竟然也被如此\n',
            '的限制了自由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121052V很严格啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '以前没有见过的生面孔啊，\n',
            '那边的是侍女吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121055V#710F遵照公爵大人的命令补充的\n',
            '新来的实习侍女。',
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
            '#2620121057V哦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唔～唔，\n',
            '的确好可爱哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F你、你们好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F…………………（点头示意）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121061V哎呀……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0008, 0, 0, -500, 1000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#2620121062V怎么总觉得\n',
            '在哪儿见过呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 800)

    ChrTalk(
        0x0101,
        (
            '#000F（不好……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F……对年轻的姑娘那样\n',
            '目不转睛的盯着是什么意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121065V难不成是在\n',
            '动一些歪念头吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121066V在这样下去我可要向公爵大人\n',
            '还有上校抗议了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1FCC')
    def lambda_1FCC():
        ChrSetDirection(0x00FE, 0, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FCC)

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
            '作为王国军精英\n',
            '的我们怎么会那样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F没有最好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我说，你们好了没有，\n',
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

    @scena.Lambda('lambda_2081')
    def lambda_2081():
        ChrMoveTo(0x00FE, -2300, 19500, 106900, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2081)

    ChrTalk(
        0x0009,
        (
            '请进去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_20AC')
    def lambda_20AC():
        ChrMoveTo(0x00FE, 2350, 19500, 106810, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_20AC)

    FadeOut(2000, 0, -1)

    @scena.Lambda('lambda_20D1')
    def lambda_20D1():
        ChrMoveToRelative(0x00FE, 0, 0, 10000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_20D1)

    Sleep(50)

    @scena.Lambda('lambda_20F1')
    def lambda_20F1():
        ChrMoveToRelative(0x00FE, 0, 0, 10000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_20F1)

    @scena.Lambda('lambda_210C')
    def lambda_210C():
        ChrMoveToRelative(0x00FE, 0, 0, 10000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_210C)

    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4230._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x212F
@scena.Code('func_07_212F')
def func_07_212F():
    EventBegin(0x00)
    CameraMove(-220, 20000, 107550, 0)
    ChrSetPos(0x0008, -2390, 19500, 107000, 180)
    ChrSetPos(0x0009, 2290, 19500, 106980, 180)

    @scena.Lambda('lambda_216A')
    def lambda_216A():
        ChrTurnDirection(0x00FE, 0x0138, 0)
        Yield()

        Jump('lambda_216A')

    DispatchAsync2(0x0008, 0x0002, lambda_216A)

    @scena.Lambda('lambda_217B')
    def lambda_217B():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_217B')

    DispatchAsync2(0x0009, 0x0002, lambda_217B)

    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0102, 3)
    ChrSetChipByIndex(0x0138, 1)
    ChrSetPos(0x0101, -990, 20000, 110860, 180)
    ChrSetPos(0x0102, 1070, 20000, 111050, 0)
    ChrSetPos(0x0138, 120, 20000, 110230, 180)

    @scena.Lambda('lambda_21CE')
    def lambda_21CE():
        ChrWalkTo(0x00FE, 190, 19250, 106340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_21CE)

    @scena.Lambda('lambda_21E9')
    def lambda_21E9():
        ChrWalkTo(0x00FE, -480, 19750, 107280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21E9)

    @scena.Lambda('lambda_2204')
    def lambda_2204():
        ChrWalkTo(0x00FE, 860, 19750, 107280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2204)

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
            '#0650121333V我希望你们\n',
            '在陛下面前不要有什么闪失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121052V很严格啊……',
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
            '#710F那就没有什么再要拜托的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121337V那么我们\n',
            '这就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#000F再、再－见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 135, 400)

    ChrTalk(
        0x0102,
        (
            '#010F……告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2389')
    def lambda_2389():
        CameraMove(230, 19000, 105820, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2389)

    @scena.Lambda('lambda_23A1')
    def lambda_23A1():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_23A1)

    Sleep(100)

    @scena.Lambda('lambda_23C1')
    def lambda_23C1():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_23C1)

    @scena.Lambda('lambda_23DC')
    def lambda_23DC():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_23DC)

    @scena.Lambda('lambda_23F7')
    def lambda_23F7():
        ChrMoveTo(0x00FE, -870, 19750, 107400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_23F7)

    @scena.Lambda('lambda_2412')
    def lambda_2412():
        ChrMoveTo(0x00FE, 910, 19750, 107400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2412)

    Sleep(1300)

    ChrTalk(
        0x0008,
        (
            '#2620121340V啊，两位姑娘。',
            TxtCtl.Enter,
        ),
    )

    Sleep(200)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CloseMessageWindow()

    @scena.Lambda('lambda_248D')
    def lambda_248D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_248D)

    @scena.Lambda('lambda_249B')
    def lambda_249B():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_249B)

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121342V突然想起还没有询问\n',
            '你们的名字。',
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
            '#000F嗯，这个……',
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
            TXT(0x00, '莱娜\n'),
            TXT(0x01, '雪拉\n'),
            TXT(0x02, '朵洛希\n'),
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
        (0x00000000, 'loc_258B'),
        (0x00000001, 'loc_2606'),
        (0x00000002, 'loc_26B2'),
        (-1, 'loc_2731'),
    )

    def _loc_258B(): pass

    label('loc_258B')

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
            '#000F啊，那个……\n',
            '真是非常感谢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2731')

    def _loc_2606(): pass

    label('loc_2606')

    SetScenaFlags(ScenaFlag(0x00CE, 7, 0x677))

    ChrTalk(
        0x0008,
        (
            '#2620121348V哦，是个\n',
            '不怎么样的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121349V失败就失败在名字上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F少、少管闲事！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……好吗，呵呵呵。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121352V我会努力做一个好女人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2731')

    def _loc_26B2(): pass

    label('loc_26B2')

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
            '#2620121354V可说实话，感觉和你\n',
            '不是很般配……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（也许是吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2731')

    def _loc_2731(): pass

    label('loc_2731')

    ChrTalk(
        0x0009,
        (
            '那边的那位\n',
            '黑发的姑娘呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……我的名字叫做卡玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '叫卡玲……\n',
            '好可爱的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121360V……我对自己的名字\n',
            '也非常喜欢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '对、对了。\n',
            '我是特务部队的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F你还明白这一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121364V这一切\n',
            '就是因为居心不良。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不，我可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F……………………（怒视）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620121367V……请吧，\n',
            '这就请回吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    ChrSetChipByIndex(0x0000, 1)
    ChrSetChipByIndex(0x0001, 2)
    ChrSetChipByIndex(0x0138, 3)

    Return()

# id: 0x0008 offset: 0x28B9
@scena.Code('func_08_28B9')
def func_08_28B9():
    EventBegin(0x00)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_6F(0x0002, 450)
    OP_72(0x0002, 0x0010)
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
    ChrSetFlags(0x0008, 0x0001)
    ChrSetFlags(0x0009, 0x0001)
    ChrSetPos(0x000B, 20, 12000, 46990, 180)
    ChrSetPos(0x0008, 940, 12000, 48110, 180)
    ChrSetPos(0x0009, -900, 12000, 48110, 180)
    ChrSetChipByIndex(0x0008, 42)
    ChrSetChipByIndex(0x0009, 42)
    ChrSetPos(0x000C, -60, 12000, 51430, 180)
    ChrSetPos(0x000D, 930, 12000, 52730, 180)
    ChrSetPos(0x000E, 930, 12000, 54640, 180)
    ChrSetPos(0x000F, 910, 12000, 56310, 180)
    ChrSetPos(0x0010, -890, 12000, 52760, 180)
    ChrSetPos(0x0011, -890, 12000, 54510, 180)
    ChrSetPos(0x0012, -890, 12000, 56510, 180)
    ChrSetFlags(0x0032, 0x0080)
    CameraMove(-1980, 12000, 40200, 0)
    OP_67(0, 4910, -10000, 0)
    CameraSetDistance(2680, 0)
    OP_6C(51000, 0)
    OP_6E(280, 0)
    CameraMove(10, 12000, 46910, 2000)

    ChrTalk(
        0x000B,
        (
            '#0610131156V#187F#5P这、这怎么可能……！\n',
            '为什么城门会自动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2660131157V#5P上、上尉！\n',
            '怎么办！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2660131158V这样下去的话\n',
            '敌人会冲入城内的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2AB8')
    def lambda_2AB8():
        CameraMove(-10, 12000, 48330, 800)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2AB8)

    ChrSetDirection(0x000B, 0, 600)
    WaitForThreadExit(0x000B, 0x0002)

    ChrTalk(
        0x000B,
        (
            '#0610131159V#185F#2P第一小队留下，\n',
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
            '#2660131161V#5P明、明白！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2B60')
    def lambda_2B60():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2B60')

    DispatchAsync2(0x000D, 0x0001, lambda_2B60)

    @scena.Lambda('lambda_2B71')
    def lambda_2B71():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2B71')

    DispatchAsync2(0x000E, 0x0001, lambda_2B71)

    @scena.Lambda('lambda_2B82')
    def lambda_2B82():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2B82')

    DispatchAsync2(0x000F, 0x0001, lambda_2B82)

    @scena.Lambda('lambda_2B93')
    def lambda_2B93():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2B93')

    DispatchAsync2(0x0010, 0x0001, lambda_2B93)

    @scena.Lambda('lambda_2BA4')
    def lambda_2BA4():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2BA4')

    DispatchAsync2(0x0011, 0x0001, lambda_2BA4)

    @scena.Lambda('lambda_2BB5')
    def lambda_2BB5():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_2BB5')

    DispatchAsync2(0x0012, 0x0001, lambda_2BB5)

    ChrSetChipByIndex(0x000C, 34)
    ChrWalkTo(0x000C, 2310, 12000, 51510, 6000, 0x00)
    ChrWalkTo(0x000C, 2310, 12000, 52680, 6000, 0x00)
    CreateThread(0x000D, 0x01, 0x00, func_09_2E25)
    CreateThread(0x0010, 0x01, 0x00, func_09_2E25)
    ChrWalkTo(0x000C, 2310, 12000, 54390, 6000, 0x00)
    CreateThread(0x000E, 0x01, 0x00, func_0A_2E53)
    CreateThread(0x0011, 0x01, 0x00, func_0A_2E53)
    ChrWalkTo(0x000C, 2310, 12000, 57190, 6000, 0x00)
    CreateThread(0x000F, 0x01, 0x00, func_0B_2E86)
    CreateThread(0x0012, 0x01, 0x00, func_0B_2E86)

    @scena.Lambda('lambda_2C45')
    def lambda_2C45():
        ChrWalkTo(0x00FE, 2350, 12000, 73700, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2C45)

    CameraMove(10, 12000, 46910, 1000)

    ChrTalk(
        0x000B,
        (
            '#0610131162V#186F#2P可恶，太丢脸了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610131163V在上校回来之前，\n',
            '无论如何也不能让那些人得逞……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#2620131164V#5P上、上尉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630131165V#5P是、是特务飞艇！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrSetDirection(0x000B, 180, 600)

    ChrTalk(
        0x000B,
        (
            '#0610131166V#187F#5P糟糕了！\n',
            '那个才是主力部队吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2DD1')
    def lambda_2DD1():
        CameraMove(-9190, 19050, 36880, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2DD1)

    @scena.Lambda('lambda_2DE9')
    def lambda_2DE9():
        OP_67(0, 3900, -10000, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2DE9)

    @scena.Lambda('lambda_2E01')
    def lambda_2E01():
        CameraSetDistance(3220, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_2E01)

    Sleep(1000)

    FadeOut(500, 0, -1)
    OP_0D()
    NewScene('ED6_DT01/E0500._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x2E25
@scena.Code('func_09_2E25')
def func_09_2E25():
    ChrSetChipByIndex(0x00FE, 34)
    ChrWalkTo(0x00FE, 2350, 12000, 52630, 6000, 0x00)
    ChrWalkTo(0x00FE, 2350, 12000, 73700, 6000, 0x00)

    Return()

# id: 0x000A offset: 0x2E53
@scena.Code('func_0A_2E53')
def func_0A_2E53():
    Sleep(800)

    ChrSetChipByIndex(0x00FE, 34)
    ChrWalkTo(0x00FE, 2290, 12000, 54370, 6000, 0x00)
    ChrWalkTo(0x00FE, 2350, 12000, 73700, 6000, 0x00)

    Return()

# id: 0x000B offset: 0x2E86
@scena.Code('func_0B_2E86')
def func_0B_2E86():
    Sleep(1300)

    ChrSetChipByIndex(0x00FE, 34)
    ChrWalkTo(0x00FE, 2290, 12000, 56260, 5000, 0x00)
    ChrWalkTo(0x00FE, 2350, 12000, 73700, 5000, 0x00)

    Return()

# id: 0x000C offset: 0x2EB9
@scena.Code('func_0C_2EB9')
def func_0C_2EB9():
    EventBegin(0x00)
    ChrSetFlags(0x0032, 0x0080)
    FormationDelMember(0x01, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationAddMember(0x00, 0xFF)
    FormationAddMember(0x04, 0xFF)
    FormationAddMember(0x02, 0xFF)
    CameraMove(1980, 20950, 57340, 0)
    OP_67(0, 9340, -10000, 0)
    CameraSetDistance(3400, 0)
    OP_6C(340000, 0)
    OP_6E(413, 0)
    ChrSetPos(0x0008, -8810, 12000, 57910, 79)
    ChrSetPos(0x000B, -7640, 12000, 58590, 125)
    ChrSetPos(0x0009, -6650, 12000, 57720, 46)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0008, 0x0001)
    ChrSetFlags(0x0009, 0x0001)

    @scena.Lambda('lambda_2F61')
    def lambda_2F61():
        ChrTurnDirection(0x00FE, 0x0105, 0)
        Yield()

        Jump('lambda_2F61')

    DispatchAsync2(0x000B, 0x0001, lambda_2F61)

    @scena.Lambda('lambda_2F72')
    def lambda_2F72():
        ChrTurnDirection(0x00FE, 0x0103, 0)
        Yield()

        Jump('lambda_2F72')

    DispatchAsync2(0x0008, 0x0001, lambda_2F72)

    @scena.Lambda('lambda_2F83')
    def lambda_2F83():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2F83')

    DispatchAsync2(0x0009, 0x0001, lambda_2F83)

    ChrSetChipByIndex(0x000B, 40)
    ChrSetChipByIndex(0x0008, 38)
    ChrSetChipByIndex(0x0009, 38)
    OP_A1(0x0033, 0x0000)
    OP_A1(0x0034, 0x0001)
    OP_72(0x0000, 0x0004)
    OP_72(0x0000, 0x0002)
    OP_71(0x0000, 0x0400)
    OP_71(0x0000, 0x0040)
    OP_72(0x0001, 0x0004)
    OP_72(0x0001, 0x0002)
    OP_71(0x0001, 0x0400)
    OP_71(0x0001, 0x0040)
    OP_6F(0x0000, 1021)
    ChrSetFlags(0x0033, 0x0004)
    ChrSetFlags(0x0034, 0x0004)
    ChrSetFlags(0x0033, 0x0040)
    ChrSetFlags(0x0034, 0x0040)
    ChrSetPos(0x0101, 2880, 15350, 57740, 147)
    ChrSetPos(0x0103, 2880, 15350, 57740, 147)
    ChrSetPos(0x0105, 2880, 15350, 57740, 147)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0103, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    ChrSetPos(0x0033, 2320, 22050, 57280, 56)
    ChrSetPos(0x0034, 2320, 12050, 57280, 56)

    @scena.Lambda('lambda_3068')
    def lambda_3068():
        CameraMove(610, 15350, 55470, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3068)

    @scena.Lambda('lambda_3080')
    def lambda_3080():
        OP_67(0, 5210, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3080)

    @scena.Lambda('lambda_3098')
    def lambda_3098():
        OP_6C(29000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_3098)

    FadeIn(2000, 0)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 1110)
    PlaySE(204, 0x00, 0x64)
    PlayEffect(0x01, 0x01, 0x0034, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrMoveToRelativeAsync(0x0033, 0, -3000, 0, 3000, 0x00)
    ChrMoveToRelativeAsync(0x0033, 0, -2000, 0, 2500, 0x00)
    ChrMoveToRelativeAsync(0x0033, 0, -1000, 0, 2000, 0x00)
    PlayEffect(0x01, 0x02, 0x0034, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    ChrMoveToRelativeAsync(0x0033, 0, -2000, 0, 2000, 0x00)
    ChrMoveToRelativeAsync(0x0033, 0, -1000, 0, 1500, 0x00)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    ChrMoveTo(0x0033, 2320, 12050, 57280, 1000, 0x00)
    PlaySE(200, 0x00, 0x64)
    OP_23(0x0079)
    OP_7C(0, 100, 3000, 100)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0103, 7)
    ChrSetChipByIndex(0x0105, 9)

    @scena.Lambda('lambda_31D2')
    def lambda_31D2():
        OP_67(0, 7370, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0103, 0x0003, lambda_31D2)

    PlaySE(118, 0x00, 0x64)
    OP_B0(0x0000, 0x78)
    OP_6F(0x0000, 61)
    OP_70(0x0000, 230)
    OP_73(0x0000)
    OP_B0(0x0000, 0x3C)
    OP_6F(0x0000, 231)
    OP_70(0x0000, 360)
    OP_73(0x0000)
    PlaySE(106, 0x00, 0x64)
    OP_6F(0x0000, 1140)
    OP_70(0x0000, 1200)
    OP_73(0x0000)

    @scena.Lambda('lambda_322F')
    def lambda_322F():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_322F')

    DispatchAsync2(0x0101, 0x0001, lambda_322F)

    @scena.Lambda('lambda_3240')
    def lambda_3240():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_3240')

    DispatchAsync2(0x0105, 0x0001, lambda_3240)

    @scena.Lambda('lambda_3251')
    def lambda_3251():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_3251')

    DispatchAsync2(0x0103, 0x0001, lambda_3251)

    @scena.Lambda('lambda_3262')
    def lambda_3262():
        CameraMove(-7140, 12000, 55690, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3262)

    @scena.Lambda('lambda_327A')
    def lambda_327A():
        OP_6E(577, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_327A)

    @scena.Lambda('lambda_328A')
    def lambda_328A():
        OP_67(0, 5360, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0003, lambda_328A)

    @scena.Lambda('lambda_32A2')
    def lambda_32A2():
        OP_6C(13000, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_32A2)

    @scena.Lambda('lambda_32B2')
    def lambda_32B2():
        CameraSetDistance(1600, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_32B2)

    ChrClearFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_32C7')
    def lambda_32C7():
        ChrWalkTo(0x00FE, -4940, 12710, 53260, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_32C7)

    Sleep(300)

    ChrClearFlags(0x0103, 0x0080)

    @scena.Lambda('lambda_32EC')
    def lambda_32EC():
        ChrWalkTo(0x00FE, -7230, 12000, 51440, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_32EC)

    Sleep(300)

    ChrClearFlags(0x0105, 0x0080)

    @scena.Lambda('lambda_3311')
    def lambda_3311():
        ChrWalkTo(0x00FE, -5870, 12000, 52050, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_3311)

    WaitForThreadExit(0x0101, 0x0002)

    @scena.Lambda('lambda_3331')
    def lambda_3331():
        ChrJumpTo(0x00FE, -7040, 12000, 52700, 1000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3331)

    WaitForThreadExit(0x0103, 0x0002)

    @scena.Lambda('lambda_3354')
    def lambda_3354():
        ChrWalkTo(0x00FE, -8580, 12000, 52480, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_3354)

    WaitForThreadExit(0x0105, 0x0002)

    @scena.Lambda('lambda_3374')
    def lambda_3374():
        ChrWalkTo(0x00FE, -7830, 12000, 51430, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_3374)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x000B,
        (
            '#0610131167V#187F艾、艾丝蒂尔·布莱特！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610131168V还有……科洛蒂娅殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131169V#006F凯诺娜上尉！又来麻烦你了哦！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131170V#042F我们是来……\n',
            '营救我的祖母大人的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0610131171V#186F不、不要欺人太甚了，小丫头！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x1000)
    ChrSetChipByIndex(0x0101, 6)

    @scena.Lambda('lambda_3494')
    def lambda_3494():
        OP_92(0x00FE, 0x0009, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3494)

    Sleep(10)

    ChrSetFlags(0x0103, 0x1000)
    ChrSetChipByIndex(0x0103, 8)

    @scena.Lambda('lambda_34B8')
    def lambda_34B8():
        OP_92(0x00FE, 0x0008, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_34B8)

    Sleep(10)

    ChrSetFlags(0x0105, 0x1000)
    ChrSetChipByIndex(0x0105, 10)

    @scena.Lambda('lambda_34DC')
    def lambda_34DC():
        OP_92(0x00FE, 0x000B, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_34DC)

    Sleep(20)

    ChrSetChipByIndex(0x0008, 39)

    @scena.Lambda('lambda_34FB')
    def lambda_34FB():
        OP_92(0x00FE, 0x0103, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_34FB)

    Sleep(10)

    ChrSetChipByIndex(0x0009, 39)

    @scena.Lambda('lambda_351A')
    def lambda_351A():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_351A)

    Sleep(10)

    ChrSetChipByIndex(0x000B, 41)

    @scena.Lambda('lambda_3539')
    def lambda_3539():
        OP_92(0x00FE, 0x0105, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3539)

    Sleep(200)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0103, 0x1000)
    ChrClearFlags(0x0105, 0x1000)
    Battle(0x000003A8, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_358D'),
        (-1, 'loc_3590'),
    )

    def _loc_358D(): pass

    label('loc_358D')

    OP_B4(0x00)

    Return()

    def _loc_3590(): pass

    label('loc_3590')

    EventBegin(0x00)
    CameraMove(-6850, 12000, 58770, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x000B, -7520, 12000, 58240, 12)
    ChrSetPos(0x0008, -7920, 12000, 56580, 94)
    ChrSetPos(0x0009, -9260, 12000, 57540, 284)
    ChrSetPos(0x0101, -5430, 12000, 58450, 270)
    ChrSetPos(0x0103, -5750, 12000, 60040, 225)
    ChrSetPos(0x0105, -4860, 12000, 59500, 270)
    ChrSetFlags(0x000B, 0x0800)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0009, 0x0800)

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
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0103,
        (
            '#0030131172V#023F真令人毛骨悚然……\n',
            '好一个可怕的女人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131173V她究竟是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131174V#009F理查德上校的副官。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131175V是只典型的母狐狸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131176V#025F原来如此，可以感觉出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131177V#020F接下来……目标女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131178V#042F好的，赶快走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004E, 0x01, 0x0002)
    ChrClearFlags(0x0032, 0x0080)
    OP_6F(0x0000, 360)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x37F2
@scena.Code('func_0D_37F2')
def func_0D_37F2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 2, 0x662)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_37FF',
    )

    Return()

    def _loc_37FF(): pass

    label('loc_37FF')

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00CC, 2, 0x662))
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x000E, 13020, 14000, 78670, 270)
    ChrSetPos(0x000F, 14450, 14000, 79840, 270)
    ChrSetPos(0x0010, 14130, 14000, 77880, 270)
    ChrSetChipByIndex(0x000E, 38)
    ChrSetChipByIndex(0x000F, 37)
    ChrSetChipByIndex(0x0010, 37)

    ChrTalk(
        0x000E,
        (
            '#4300131179V#3P来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#4310131180V#3P在那儿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    ChrSetPos(0x0101, 1230, 14000, 77770, 90)
    ChrSetPos(0x0103, -420, 14000, 78370, 90)
    ChrSetPos(0x0105, -300, 14000, 77020, 90)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0103, 7)
    ChrSetChipByIndex(0x0105, 9)
    CameraMove(6360, 14000, 78900, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010131181V#004F#5P哇，又来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131182V#024F#5P哼，装腔作势的家伙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000E, 39)
    ChrSetChipByIndex(0x000F, 34)
    ChrSetChipByIndex(0x0010, 34)

    @scena.Lambda('lambda_3954')
    def lambda_3954():
        CameraMove(8500, 14000, 78900, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3954)

    @scena.Lambda('lambda_396C')
    def lambda_396C():
        OP_92(0x00FE, 0x000E, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_396C)

    Sleep(10)

    @scena.Lambda('lambda_3986')
    def lambda_3986():
        OP_92(0x00FE, 0x0010, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3986)

    Sleep(10)

    @scena.Lambda('lambda_39A0')
    def lambda_39A0():
        OP_92(0x00FE, 0x000F, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_39A0)

    Sleep(20)

    @scena.Lambda('lambda_39BA')
    def lambda_39BA():
        ChrWalkTo(0x00FE, -20520, 14000, 78060, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_39BA)

    Sleep(10)

    @scena.Lambda('lambda_39DA')
    def lambda_39DA():
        ChrWalkTo(0x00FE, -20520, 14000, 78060, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_39DA)

    Sleep(10)

    @scena.Lambda('lambda_39FA')
    def lambda_39FA():
        ChrWalkTo(0x00FE, -20520, 14000, 78060, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_39FA)

    Sleep(500)

    Battle(0x000003B1, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_3A2D'),
        (-1, 'loc_3A30'),
    )

    def _loc_3A2D(): pass

    label('loc_3A2D')

    OP_B4(0x00)

    Return()

    def _loc_3A30(): pass

    label('loc_3A30')

    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    ChrSetPos(0x0101, 1780, 14000, 78680, 90)
    ChrSetPos(0x0103, 1780, 14000, 78680, 90)
    ChrSetPos(0x0105, 1780, 14000, 78680, 90)
    CameraMove(1780, 14000, 78680, 0)
    ChrSetPos(0x000E, 3890, 14000, 79000, 146)
    ChrSetPos(0x000F, 3080, 14000, 77370, 283)
    ChrSetPos(0x0010, 6700, 14000, 78300, 358)

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000E, 35)

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000F, 35)

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0010, 35)
    ChrClearFlags(0x000E, 0x0001)
    ChrClearFlags(0x000F, 0x0001)
    ChrClearFlags(0x0010, 0x0001)
    ChrSetFlags(0x000E, 0x0800)
    ChrSetFlags(0x000F, 0x0800)
    ChrSetFlags(0x0010, 0x0800)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    FadeIn(1000, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x3B2B
@scena.Code('func_0E_3B2B')
def func_0E_3B2B():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BB0',
    )

    ChrSetDirection(0x0101, 180, 0)
    ChrTurnDirection(0x0105, 0x0101, 0)
    ChrTurnDirection(0x0103, 0x0101, 0)

    ChrTalk(
        0x0105,
        (
            '#0060131186V#043F艾丝蒂尔！\n',
            '这边是去城内的路！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131187V#022F我们要赶快去女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C82')

    def _loc_3BB0(): pass

    label('loc_3BB0')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C08',
    )

    ChrSetDirection(0x0105, 180, 0)
    ChrTurnDirection(0x0101, 0x0105, 0)
    ChrTurnDirection(0x0103, 0x0105, 0)

    ChrTalk(
        0x0105,
        (
            '#0060131188V#042F不行……！\n',
            '必须赶快去女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C82')

    def _loc_3C08(): pass

    label('loc_3C08')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C82',
    )

    ChrSetDirection(0x0103, 180, 0)
    ChrTurnDirection(0x0101, 0x0103, 0)
    ChrTurnDirection(0x0105, 0x0103, 0)

    ChrTalk(
        0x0103,
        (
            '#0030131189V#023F哎呀，\n',
            '这边不是女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131190V#005F嗯，在北边的高台上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C82(): pass

    label('loc_3C82')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000F offset: 0x3C9E
@scena.Code('func_0F_3C9E')
def func_0F_3C9E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 4, 0x664)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3CAB',
    )

    Return()

    def _loc_3CAB(): pass

    label('loc_3CAB')

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00CC, 4, 0x664))
    Fade(1000)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0011, -870, 19000, 105680, 180)
    ChrSetPos(0x0012, 850, 19000, 105680, 180)
    ChrSetChipByIndex(0x0011, 37)
    ChrSetChipByIndex(0x0012, 37)
    ChrSetPos(0x0101, 100, 17250, 98200, 0)
    ChrSetPos(0x0103, -1300, 17000, 97610, 0)
    ChrSetPos(0x0105, 1670, 17000, 97720, 0)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0103, 7)
    ChrSetChipByIndex(0x0105, 9)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0103, 0x1000)
    ChrClearFlags(0x0105, 0x1000)
    CameraMove(290, 18000, 103070, 0)
    OP_67(0, 7390, -10000, 0)
    CameraSetDistance(2280, 0)
    OP_6C(30000, 0)
    OP_6E(420, 0)
    OP_0D()

    ChrTalk(
        0x0011,
        (
            '#4320131191V来、来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#4330131192V此路不通！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131193V#042F#2P可是……\n',
            '我们必须要通过这里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131194V#005F#2P再阻拦的话就把你们打飞！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3E24')
    def lambda_3E24():
        CameraMove(360, 18750, 105100, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3E24)

    @scena.Lambda('lambda_3E3C')
    def lambda_3E3C():
        ChrWalkTo(0x00FE, -310, 19250, 128630, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3E3C)

    Sleep(50)

    @scena.Lambda('lambda_3E5C')
    def lambda_3E5C():
        ChrWalkTo(0x00FE, -310, 19250, 128630, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3E5C)

    Sleep(50)

    @scena.Lambda('lambda_3E7C')
    def lambda_3E7C():
        ChrWalkTo(0x00FE, -310, 19250, 128630, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_3E7C)

    Sleep(500)

    Battle(0x000003B2, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_3EAF'),
        (-1, 'loc_3EB2'),
    )

    def _loc_3EAF(): pass

    label('loc_3EAF')

    OP_B4(0x00)

    Return()

    def _loc_3EB2(): pass

    label('loc_3EB2')

    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    ChrSetPos(0x0011, -2160, 18000, 102100, 309)
    ChrSetPos(0x0012, 2230, 18000, 101600, 82)
    ChrClearFlags(0x0011, 0x0001)
    ChrClearFlags(0x0012, 0x0001)
    ChrSetFlags(0x0011, 0x0800)
    ChrSetFlags(0x0012, 0x0800)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0011, 35)

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0012, 35)
    ChrSetPos(0x0101, -90, 18000, 102000, 0)
    ChrSetPos(0x0103, -90, 18000, 102000, 0)
    ChrSetPos(0x0105, -90, 18000, 102000, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    CameraMove(-90, 18000, 102000, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0010 offset: 0x3FAF
@scena.Code('func_10_3FAF')
def func_10_3FAF():
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
    ChrClearFlags(0x002B, 0x0080)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrClearFlags(0x002E, 0x0080)
    ChrClearFlags(0x002F, 0x0080)
    ChrClearFlags(0x0030, 0x0080)
    ChrSetPos(0x0014, -7210, 12000, 58180, 0)
    ChrSetPos(0x0015, -9680, 12000, 54680, 0)
    ChrSetPos(0x0016, -7920, 12000, 56380, 0)
    ChrSetPos(0x0017, -10390, 12000, 56310, 0)
    ChrSetPos(0x0018, 6170, 12000, 53150, 0)
    ChrSetPos(0x0019, 6210, 12000, 53870, 0)
    ChrSetPos(0x001A, -7990, 12000, 54100, 0)
    ChrSetPos(0x001B, -7550, 12000, 49770, 0)
    ChrSetPos(0x001C, -6470, 12000, 48980, 0)
    ChrSetPos(0x001D, -1110, 12000, 70820, 0)
    ChrSetPos(0x001E, 1020, 12000, 70710, 0)
    ChrSetPos(0x001F, 10, 12000, 71740, 0)
    ChrSetPos(0x0020, 20, 12000, 67080, 0)
    ChrSetPos(0x0013, 650, 12000, 68820, 0)
    ChrSetPos(0x0021, 6760, 12000, 57310, 0)
    ChrSetPos(0x0022, 5980, 12000, 57880, 0)
    ChrSetPos(0x0023, 7530, 12000, 55190, 0)
    ChrSetPos(0x0024, 6470, 12000, 55570, 0)
    ChrSetPos(0x0025, 9010, 12000, 57270, 0)
    ChrSetPos(0x0026, 9250, 12000, 55950, 0)
    ChrSetPos(0x0027, -2750, 12000, 62800, 90)
    ChrSetPos(0x0028, -2750, 12000, 61200, 90)
    ChrSetPos(0x0029, -2750, 12000, 59600, 90)
    ChrSetPos(0x002A, -2750, 12000, 58000, 90)
    ChrSetPos(0x002B, -2750, 12000, 56400, 90)
    ChrSetPos(0x002C, 2750, 12000, 62800, 270)
    ChrSetPos(0x002D, 2750, 12000, 61200, 270)
    ChrSetPos(0x002E, 2750, 12000, 59600, 270)
    ChrSetPos(0x002F, 2750, 12000, 58000, 270)
    ChrSetPos(0x0030, 2750, 12000, 56400, 270)

    @scena.Lambda('lambda_42C5')
    def lambda_42C5():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_42C5')

    DispatchAsync2(0x002A, 0x0000, lambda_42C5)

    @scena.Lambda('lambda_42D8')
    def lambda_42D8():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_42D8')

    DispatchAsync2(0x002B, 0x0000, lambda_42D8)

    @scena.Lambda('lambda_42EB')
    def lambda_42EB():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_42EB')

    DispatchAsync2(0x002F, 0x0000, lambda_42EB)

    @scena.Lambda('lambda_42FE')
    def lambda_42FE():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_42FE')

    DispatchAsync2(0x0030, 0x0000, lambda_42FE)

    @scena.Lambda('lambda_4311')
    def lambda_4311():
        ChrWalkTo(0x00FE, -1110, 12000, 53820, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_4311)

    @scena.Lambda('lambda_432C')
    def lambda_432C():
        ChrWalkTo(0x00FE, 1020, 12000, 53710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_432C)

    @scena.Lambda('lambda_4347')
    def lambda_4347():
        ChrWalkTo(0x00FE, 10, 12000, 54740, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_4347)

    @scena.Lambda('lambda_4362')
    def lambda_4362():
        ChrWalkTo(0x00FE, 20, 12000, 50080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4362)

    @scena.Lambda('lambda_437D')
    def lambda_437D():
        ChrWalkTo(0x00FE, 650, 12000, 51820, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_437D)

    @scena.Lambda('lambda_4398')
    def lambda_4398():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4398')

    DispatchAsync2(0x0101, 0x0001, lambda_4398)

    @scena.Lambda('lambda_43A9')
    def lambda_43A9():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_43A9')

    DispatchAsync2(0x0102, 0x0001, lambda_43A9)

    @scena.Lambda('lambda_43BA')
    def lambda_43BA():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_43BA')

    DispatchAsync2(0x0014, 0x0001, lambda_43BA)

    @scena.Lambda('lambda_43CB')
    def lambda_43CB():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_43CB')

    DispatchAsync2(0x0015, 0x0001, lambda_43CB)

    @scena.Lambda('lambda_43DC')
    def lambda_43DC():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_43DC')

    DispatchAsync2(0x0016, 0x0001, lambda_43DC)

    @scena.Lambda('lambda_43ED')
    def lambda_43ED():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_43ED')

    DispatchAsync2(0x0017, 0x0001, lambda_43ED)

    @scena.Lambda('lambda_43FE')
    def lambda_43FE():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_43FE')

    DispatchAsync2(0x0018, 0x0001, lambda_43FE)

    @scena.Lambda('lambda_440F')
    def lambda_440F():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_440F')

    DispatchAsync2(0x0019, 0x0001, lambda_440F)

    @scena.Lambda('lambda_4420')
    def lambda_4420():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4420')

    DispatchAsync2(0x001A, 0x0001, lambda_4420)

    @scena.Lambda('lambda_4431')
    def lambda_4431():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4431')

    DispatchAsync2(0x001B, 0x0001, lambda_4431)

    @scena.Lambda('lambda_4442')
    def lambda_4442():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4442')

    DispatchAsync2(0x001C, 0x0001, lambda_4442)

    @scena.Lambda('lambda_4453')
    def lambda_4453():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4453')

    DispatchAsync2(0x0021, 0x0001, lambda_4453)

    @scena.Lambda('lambda_4464')
    def lambda_4464():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4464')

    DispatchAsync2(0x0022, 0x0001, lambda_4464)

    @scena.Lambda('lambda_4475')
    def lambda_4475():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4475')

    DispatchAsync2(0x0023, 0x0001, lambda_4475)

    @scena.Lambda('lambda_4486')
    def lambda_4486():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4486')

    DispatchAsync2(0x0024, 0x0001, lambda_4486)

    @scena.Lambda('lambda_4497')
    def lambda_4497():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4497')

    DispatchAsync2(0x0025, 0x0001, lambda_4497)

    @scena.Lambda('lambda_44A8')
    def lambda_44A8():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_44A8')

    DispatchAsync2(0x0026, 0x0001, lambda_44A8)

    @scena.Lambda('lambda_44B9')
    def lambda_44B9():
        CameraMove(-1510, 12000, 54280, 9000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_44B9)

    @scena.Lambda('lambda_44D1')
    def lambda_44D1():
        OP_6E(342, 9000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_44D1)

    WaitForThreadExit(0x0000, 0x0002)
    Sleep(1000)

    @scena.Lambda('lambda_44EB')
    def lambda_44EB():
        CameraMove(0, 12000, 47170, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_44EB)

    ChrWalkTo(0x0020, 30, 12000, 47230, 1000, 0x00)
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x4529
@scena.Code('func_11_4529')
def func_11_4529():
    EventBegin(0x00)
    CameraMove(20, 12000, 70880, 0)
    OP_67(0, -2830, -10000, 0)
    CameraSetDistance(4410, 0)
    OP_6C(359000, 0)
    OP_6E(612, 0)

    @scena.Lambda('lambda_456E')
    def lambda_456E():
        OP_67(0, 6070, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_456E)

    @scena.Lambda('lambda_4586')
    def lambda_4586():
        OP_6C(35000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4586)

    Sleep(8000)

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4221._SN', 107, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x45A2
@scena.Code('func_12_45A2')
def func_12_45A2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_45AB',
    )

    Return()

    def _loc_45AB(): pass

    label('loc_45AB')

    EventBegin(0x00)
    OP_77(0x41, 0x64, 0x82, 0x00, 0x00000000)

    ExecExpressionWithVar(
        0x1B,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000004)
    ChrSetFlags(0x0031, 0x0040)
    ChrSetChipByIndex(0x0031, 32)
    ChrClearFlags(0x0031, 0x0080)
    ChrSetPos(0x0031, 43230, 16000, 80440, 270)
    ChrSetFlags(0x0031, 0x0004)

    @scena.Lambda('lambda_45EF')
    def lambda_45EF():
        OP_99(0x00FE, 0x00, 0x07, 800)
        Yield()

        Jump('lambda_45EF')

    DispatchAsync2(0x0031, 0x0001, lambda_45EF)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0031, 400)
    Sleep(1000)

    @scena.Lambda('lambda_4625')
    def lambda_4625():
        CameraMove(40260, 16000, 79530, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4625)

    @scena.Lambda('lambda_463D')
    def lambda_463D():
        ChrWalkTo(0x00FE, 37240, 16000, 78660, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_463D)

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0031, 400)
    Sleep(500)

    Fade(3000)
    OP_6C(69000, 3000)
    Sleep(2000)

    TerminateThread(0x0031, 0xFF)
    Fade(1000)

    ExecExpressionWithValue(
        0x0031,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0031, 33)

    ChrTalk(
        0x0031,
        (
            '#010F啊……艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141334V真是个美丽的夜晚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141336V还是这首曲子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '『星之所在』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F虽然我曾经丢掉了很多东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141339V不过，只有这首曲子\n',
            '和这个口琴一直伴随着我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141340V所以会经常吹起它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#0020141342V#010F我是不是该履行约定了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141343V与你相遇之前\n',
            '我都做了些什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141344V现在我要全部说出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯……我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_484B')
    def lambda_484B():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_484B')

    DispatchAsync2(0x0031, 0x0001, lambda_484B)

    @scena.Lambda('lambda_485C')
    def lambda_485C():
        ChrWalkTo(0x00FE, 43260, 16000, 81730, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_485C)

    Sleep(200)

    @scena.Lambda('lambda_487C')
    def lambda_487C():
        CameraMove(43230, 16000, 81140, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_487C)

    WaitForThreadExit(0x0101, 0x0002)
    ChrTurnDirection(0x0101, 0x0031, 300)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0031,
        (
            '#010F不过，故事稍微有点长……\n',
            '这样也没关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F当然……\n',
            '我肯定会认真地听到最后的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F谢谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141350V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0031, 0xFF)
    ChrSetDirection(0x0031, 90, 300)
    Sleep(500)

    ChrTalk(
        0x0031,
        (
            '#010F很久以前，在某个地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在某个地方\n',
            '有一个男孩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()

    ChrTalk(
        0x0031,
        (
            '#010F因为某件事，\n',
            '心破碎了的男孩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '丧失了言语和感情，饭也不吃，\n',
            '只是天天在吹着口琴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '照顾他的人努力都是白费，\n',
            '男孩也日渐衰弱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这时在这个男孩面前，\n',
            '出现了一个魔法师。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '『让我来把这孩子的心治好吧。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '『只不过需要向我付出代价。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就这样，\n',
            '男孩被交给了魔法师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F破碎的心被重新结合在了一起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可是，魔法师\n',
            '将男孩的存在肆意地修改。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '然后，当得到新的心的时候——\n',
            '男孩变成了一个杀手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F在两年的时间里，\n',
            '男孩每天都在不断地杀人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '曾经将几十人的部队\n',
            '在暗中全灭。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '曾经潜入由强壮的护卫\n',
            '严密看守的某国大臣的住宅，\n',
            '将大臣的喉咙切断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '有时还使用炸药，\n',
            '将无辜的人们卷入。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不知何时起，男孩\n',
            '成为了叫做『漆黑之牙』的，\n',
            '令人恐惧的存在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……『漆黑之牙』………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F之后，男孩接到魔法师的命令，\n',
            '去暗杀某个目标人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那是以前守卫了女王治理的国家\n',
            '不被北方大国侵占的英雄。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '拥有整个大陆只有四个人才有的\n',
            '特别称号的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F但是，那个目标实在太强大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '像小猫被老虎轻松避开一样，\n',
            '男孩被击退了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在落败的男孩面前，\n',
            '魔法师的手下出现了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他们是来结果\n',
            '被目标看到了真面目的男孩的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是，有人将他们赶走\n',
            '并救下了男孩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他正是男孩暗杀失败的\n',
            '那个目标人物游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '然后，男孩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141382V被带到了他的家里，\n',
            '和一个女孩相遇了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0031,
        (
            '#010F在那个家里，\n',
            '男孩在五年间得到了美妙的梦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141384V真的是对那个男孩来说\n',
            '不应该拥有的梦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141385V不过，梦总会醒来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141386V回到现实的时刻已经迫近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0031, 0x0101, 400)

    ChrTalk(
        0x0031,
        (
            '#010F到这里……故事就结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141388V谢谢……\n',
            '一直坚持着听到最后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……哎……哈哈…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141391V那个……到哪儿为止是真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F全部——都是真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141393V我的心已经破碎了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我的手沾满了血。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141395V以及暗杀你的父亲失败，\n',
            '都是真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且……到目前为止\n',
            '一直在背叛着你们，也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F男孩是真正意义上的\n',
            '无可救药的存在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141399V不管在哪里，\n',
            '都会带来不幸和灾厄……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就是这样污秽的存在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F所以……\n',
            '男孩要去旅行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141403V为了不让使自己作了\n',
            '如此幸福的美梦的人们被卷进来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141404V也为了阻止制造自己这样存在的\n',
            '那个坏魔法师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0031, 43280, 16000, 81190, 1000, 0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚将自己的口琴\n',
            '放在了艾丝蒂尔手中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveTo(0x0031, 43230, 16000, 80440, 1000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#000F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F那是让我将人的心\n',
            '一直保持到最后的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141407V已经不需要了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141408V所以请你收下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然可能算不上\n',
            '这５年来的礼物……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141410V我想总比什么都没有好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '…………给我适可而止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_534A')
    def lambda_534A():
        CameraMove(43230, 16000, 80820, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_534A)

    @scena.Lambda('lambda_5362')
    def lambda_5362():
        OP_6E(259, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5362)

    ChrWalkTo(0x0101, 43290, 16000, 81060, 3000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#000F你有完没完了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '说什么在做梦……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '难道……到现在为止的事情，\n',
            '不是真的吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '过去怎么了！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141418V心破碎了！？\n',
            '那又怎么样！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F看着我！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141421V看着我的眼睛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我一直……\n',
            '看着那个男孩的所做所为！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141423V是好是坏我都知道！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '男孩不管有什么样的痛苦，\n',
            '都会抱着必死的决心努力的事情我也知道！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为……\n',
            '我喜欢那样的约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F所以，绝对不会让你一个人去的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '丢下我，不管我的心情，\n',
            '就这样消失？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那是绝对不允许的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F……艾丝蒂尔………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F………啊………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（………约修亚…………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F什么……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141436V流进嘴里的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F……是及时生效的\n',
            ' ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141438V没有副作用，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120381V#000F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F为……为什么……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……为什么用那样的东西……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F我的艾丝蒂尔……\n',
            '你就像太阳一样的眩目，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141443V和你在一起虽然很幸福，\n',
            '不过同时也感到很痛苦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141444V就像强光可以产生浓重的影子一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141445V和你在一起的时候，\n',
            '我就会不断想起\n',
            '自己可憎的本性来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141446V所以，我有时会想，\n',
            '如果没有相遇过就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……怎么会………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F不过，现在不一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141449V我很感激能和你相遇。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141450V虽然我不得不从\n',
            '这样重要的女孩身边逃走……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141451V不过，我会比谁都更想念你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……约修亚……约修亚………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0031,
        (
            '#010F一直以来，真的很感谢你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141454V从相遇的时候起……\n',
            '我也一直喜欢着你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)

    ChrTalk(
        0x0031,
        (
            '#010F——再见了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x0013 offset: 0x5934
@scena.Code('func_13_5934')
def func_13_5934():
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
        'loc_59CC',
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

    Jump('loc_5A5F')

    def _loc_59CC(): pass

    label('loc_59CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 6, 0x63E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5A5F',
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

    def _loc_5A5F(): pass

    label('loc_5A5F')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

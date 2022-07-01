import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0037_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0037   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '00320王国军士兵待机'),
    TXT(0x02, '00321王国军士兵移动'),
    TXT(0x03, '00322王国军士兵攻击'),
    TXT(0x04, '00323王国军士兵被弹开'),
    TXT(0x05, '00324王国军士兵倒下'),
    TXT(0x06, '00325王国军士兵魔法咏唱'),
    TXT(0x07, '00328王国军士兵魔法发射'),
    TXT(0x08, '00330王国军士官待机'),
    TXT(0x09, '00331王国军士官移动'),
    TXT(0x0A, '00332王国军士官攻击'),
    TXT(0x0B, '00333王国军士官被弹开'),
    TXT(0x0C, '00334王国军士官倒下'),
    TXT(0x0D, '00335王国军士官魔法咏唱'),
    TXT(0x0E, '00338王国军士官魔法发射'),
    TXT(0x0F, '00340特务兵待机'),
    TXT(0x10, '00341特务兵移动'),
    TXT(0x11, '00342特务兵攻击'),
    TXT(0x12, '00343特务兵被弹开'),
    TXT(0x13, '00344特务兵倒下'),
    TXT(0x14, '00345特务兵魔法咏唱'),
    TXT(0x15, '00348特务兵魔法发射'),
    TXT(0x16, '00260洛伦斯待机'),
    TXT(0x17, '00261洛伦斯移动'),
    TXT(0x18, '00262洛伦斯攻击'),
    TXT(0x19, '00263洛伦斯被弹开'),
    TXT(0x1A, '00264洛伦斯倒下'),
    TXT(0x1B, '00265洛伦斯魔法咏唱'),
    TXT(0x1C, '00268洛伦斯魔法发射'),
    TXT(0x1D, '00270理查德上校待机'),
    TXT(0x1E, '00271理查德上校移动'),
    TXT(0x1F, '00272理查德上校攻击'),
    TXT(0x20, '00273理查德上校被弹开'),
    TXT(0x21, '00274理查德上校倒下'),
    TXT(0x22, '00275理查德上校魔法咏唱'),
    TXT(0x23, '00276理查德上校魔法发射'),
    TXT(0x24, '00280凯诺娜上尉待机'),
    TXT(0x25, '00281凯诺娜上尉移动'),
    TXT(0x26, '00282凯诺娜上尉攻击'),
    TXT(0x27, '00283凯诺娜上尉被弹开'),
    TXT(0x28, '00284凯诺娜上尉倒下'),
    TXT(0x29, '00285凯诺娜上尉魔法咏唱'),
    TXT(0x2A, '00288凯诺娜上尉魔法发射'),
    TXT(0x2B, '00430王国军士官Ｂ待机'),
    TXT(0x2C, '00431王国军士官Ｂ移动'),
    TXT(0x2D, '00432王国军士官Ｂ攻击'),
    TXT(0x2E, '00433王国军士官Ｂ被弹开'),
    TXT(0x2F, '00434王国军士官Ｂ倒下'),
    TXT(0x30, '00435王国军士官Ｂ魔法咏唱'),
    TXT(0x31, '00438王国军士官Ｂ魔法发射'),
    TXT(0x32, '00440特务兵Ｂ待机'),
    TXT(0x33, '00441特务兵Ｂ移动'),
    TXT(0x34, '00442特务兵Ｂ攻击'),
    TXT(0x35, '00443特务兵Ｂ被弹开'),
    TXT(0x36, '00444特务兵Ｂ倒下'),
    TXT(0x37, '00445特务兵Ｂ魔法咏唱'),
    TXT(0x38, '00448特务兵Ｂ魔法发射'),
    TXT(0x39, '00500特务兵Ｃ中队长待机'),
    TXT(0x3A, '00501特务兵Ｃ中队长移动'),
    TXT(0x3B, '00502特务兵Ｃ中队长攻击'),
    TXT(0x3C, '00503特务兵Ｃ中队长被弹开'),
    TXT(0x3D, '00504特务兵Ｃ中队长倒下'),
    TXT(0x3E, '00505特务兵Ｃ中队长魔法咏唱'),
    TXT(0x3F, '00508特务兵Ｃ中队长魔法发射'),
    TXT(0x40, ''),
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

# id: 0xFFFF offset: 0xE50
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
        ('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP'),
        ('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP'),
        ('ED6_DT07/CH00322._CH', 'ED6_DT07/CH00322P._CP'),
        ('ED6_DT07/CH00323._CH', 'ED6_DT07/CH00323P._CP'),
        ('ED6_DT07/CH00324._CH', 'ED6_DT07/CH00324P._CP'),
        ('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP'),
        ('ED6_DT07/CH00326._CH', 'ED6_DT07/CH00326P._CP'),
        ('ED6_DT07/CH00330._CH', 'ED6_DT07/CH00330P._CP'),
        ('ED6_DT07/CH00331._CH', 'ED6_DT07/CH00331P._CP'),
        ('ED6_DT07/CH00332._CH', 'ED6_DT07/CH00332P._CP'),
        ('ED6_DT07/CH00333._CH', 'ED6_DT07/CH00333P._CP'),
        ('ED6_DT07/CH00334._CH', 'ED6_DT07/CH00334P._CP'),
        ('ED6_DT07/CH00335._CH', 'ED6_DT07/CH00335P._CP'),
        ('ED6_DT07/CH00336._CH', 'ED6_DT07/CH00336P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00342._CH', 'ED6_DT07/CH00342P._CP'),
        ('ED6_DT07/CH00343._CH', 'ED6_DT07/CH00343P._CP'),
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
        ('ED6_DT07/CH00345._CH', 'ED6_DT07/CH00345P._CP'),
        ('ED6_DT07/CH00346._CH', 'ED6_DT07/CH00346P._CP'),
        ('ED6_DT07/CH00260._CH', 'ED6_DT07/CH00260P._CP'),
        ('ED6_DT07/CH00261._CH', 'ED6_DT07/CH00261P._CP'),
        ('ED6_DT07/CH00262._CH', 'ED6_DT07/CH00262P._CP'),
        ('ED6_DT07/CH00263._CH', 'ED6_DT07/CH00263P._CP'),
        ('ED6_DT07/CH00264._CH', 'ED6_DT07/CH00264P._CP'),
        ('ED6_DT07/CH00265._CH', 'ED6_DT07/CH00265P._CP'),
        ('ED6_DT07/CH00266._CH', 'ED6_DT07/CH00266P._CP'),
        ('ED6_DT07/CH00270._CH', 'ED6_DT07/CH00270P._CP'),
        ('ED6_DT07/CH00271._CH', 'ED6_DT07/CH00271P._CP'),
        ('ED6_DT07/CH00272._CH', 'ED6_DT07/CH00272P._CP'),
        ('ED6_DT07/CH00273._CH', 'ED6_DT07/CH00273P._CP'),
        ('ED6_DT07/CH00274._CH', 'ED6_DT07/CH00274P._CP'),
        ('ED6_DT07/CH00275._CH', 'ED6_DT07/CH00275P._CP'),
        ('ED6_DT07/CH00276._CH', 'ED6_DT07/CH00276P._CP'),
        ('ED6_DT07/CH00280._CH', 'ED6_DT07/CH00280P._CP'),
        ('ED6_DT07/CH00281._CH', 'ED6_DT07/CH00281P._CP'),
        ('ED6_DT07/CH00282._CH', 'ED6_DT07/CH00282P._CP'),
        ('ED6_DT07/CH00283._CH', 'ED6_DT07/CH00283P._CP'),
        ('ED6_DT07/CH00284._CH', 'ED6_DT07/CH00284P._CP'),
        ('ED6_DT07/CH00285._CH', 'ED6_DT07/CH00285P._CP'),
        ('ED6_DT07/CH00286._CH', 'ED6_DT07/CH00286P._CP'),
        ('ED6_DT07/CH00430._CH', 'ED6_DT07/CH00430P._CP'),
        ('ED6_DT07/CH00431._CH', 'ED6_DT07/CH00431P._CP'),
        ('ED6_DT07/CH00432._CH', 'ED6_DT07/CH00432P._CP'),
        ('ED6_DT07/CH00433._CH', 'ED6_DT07/CH00433P._CP'),
        ('ED6_DT07/CH00434._CH', 'ED6_DT07/CH00434P._CP'),
        ('ED6_DT07/CH00435._CH', 'ED6_DT07/CH00435P._CP'),
        ('ED6_DT07/CH00436._CH', 'ED6_DT07/CH00436P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT07/CH00442._CH', 'ED6_DT07/CH00442P._CP'),
        ('ED6_DT07/CH00443._CH', 'ED6_DT07/CH00443P._CP'),
        ('ED6_DT07/CH00444._CH', 'ED6_DT07/CH00444P._CP'),
        ('ED6_DT07/CH00445._CH', 'ED6_DT07/CH00445P._CP'),
        ('ED6_DT07/CH00446._CH', 'ED6_DT07/CH00446P._CP'),
        ('ED6_DT07/CH00278._CH', 'ED6_DT07/CH00278P._CP'),
        ('ED6_DT07/CH00500._CH', 'ED6_DT07/CH00500P._CP'),
        ('ED6_DT07/CH00501._CH', 'ED6_DT07/CH00501P._CP'),
        ('ED6_DT07/CH00502._CH', 'ED6_DT07/CH00502P._CP'),
        ('ED6_DT07/CH00503._CH', 'ED6_DT07/CH00503P._CP'),
        ('ED6_DT07/CH00504._CH', 'ED6_DT07/CH00504P._CP'),
        ('ED6_DT07/CH00505._CH', 'ED6_DT07/CH00505P._CP'),
        ('ED6_DT07/CH00506._CH', 'ED6_DT07/CH00506P._CP'),
    ]

# id: 0x10002 offset: 0x2AA
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
            initScenaIndex      = 0x0006,
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
            x                   = 8000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 8,
            chipIndex           = 8,
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
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
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
            dword_10            = 11,
            chipIndex           = 11,
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
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000C,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
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
            dword_10            = 15,
            chipIndex           = 15,
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
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 18,
            chipIndex           = 18,
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
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000D,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000E,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
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
            dword_10            = 25,
            chipIndex           = 25,
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
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000F,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0010,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
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
            dword_10            = 29,
            chipIndex           = 29,
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
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
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
            dword_10            = 32,
            chipIndex           = 32,
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
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0011,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0012,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0014,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 24000,
            z                   = 0,
            y                   = 28000,
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
            x                   = 28000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 45,
            chipIndex           = 45,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 46,
            chipIndex           = 46,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 47,
            chipIndex           = 47,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0016,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 28000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 48,
            chipIndex           = 48,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0017,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 49,
            chipIndex           = 49,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 50,
            chipIndex           = 50,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 51,
            chipIndex           = 51,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 52,
            chipIndex           = 52,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 53,
            chipIndex           = 53,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 54,
            chipIndex           = 54,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0018,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 32000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 55,
            chipIndex           = 55,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0019,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 57,
            chipIndex           = 57,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 58,
            chipIndex           = 58,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 59,
            chipIndex           = 59,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 60,
            chipIndex           = 60,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 61,
            chipIndex           = 61,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 24000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 62,
            chipIndex           = 62,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001A,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 36000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 63,
            chipIndex           = 63,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
    )

# id: 0x10003 offset: 0xA8A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0xA8B
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xA8C
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AA1',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000009C4)

    Jump('ReInit')

    def _loc_AA1(): pass

    label('loc_AA1')

    Return()

# id: 0x0003 offset: 0xAA2
@scena.Code('func_03_AA2')
def func_03_AA2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AB7',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000BB8)

    Jump('func_03_AA2')

    def _loc_AB7(): pass

    label('loc_AB7')

    Return()

# id: 0x0004 offset: 0xAB8
@scena.Code('func_04_AB8')
def func_04_AB8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AD2',
    )

    OP_99(0x00FE, 0x00, 0x00, 0x000005DC)
    Sleep(500)

    Jump('func_04_AB8')

    def _loc_AD2(): pass

    label('loc_AD2')

    Return()

# id: 0x0005 offset: 0xAD3
@scena.Code('func_05_AD3')
def func_05_AD3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AED',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    Sleep(500)

    Jump('func_05_AD3')

    def _loc_AED(): pass

    label('loc_AED')

    Return()

# id: 0x0006 offset: 0xAEE
@scena.Code('func_06_AEE')
def func_06_AEE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B08',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000578)
    Sleep(500)

    Jump('func_06_AEE')

    def _loc_B08(): pass

    label('loc_B08')

    Return()

# id: 0x0007 offset: 0xB09
@scena.Code('func_07_B09')
def func_07_B09():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B23',
    )

    OP_99(0x00FE, 0x00, 0x0B, 0x00000960)
    Sleep(500)

    Jump('func_07_B09')

    def _loc_B23(): pass

    label('loc_B23')

    Return()

# id: 0x0008 offset: 0xB24
@scena.Code('func_08_B24')
def func_08_B24():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B47',
    )

    OP_8D(0x00FE, 4000, 20000, 24000, 28000, 1500)

    Jump('func_08_B24')

    def _loc_B47(): pass

    label('loc_B47')

    Return()

# id: 0x0009 offset: 0xB48
@scena.Code('func_09_B48')
def func_09_B48():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B5D',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_09_B48')

    def _loc_B5D(): pass

    label('loc_B5D')

    Return()

# id: 0x000A offset: 0xB5E
@scena.Code('func_0A_B5E')
def func_0A_B5E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B86',
    )

    SetChrChipByIndex(0x00FE, 0)
    OP_99(0x00FE, 0x00, 0x07, 0x000009C4)
    SetChrChipByIndex(0x00FE, 6)
    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('func_0A_B5E')

    def _loc_B86(): pass

    label('loc_B86')

    Return()

# id: 0x000B offset: 0xB87
@scena.Code('func_0B_B87')
def func_0B_B87():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B9C',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_0B_B87')

    def _loc_B9C(): pass

    label('loc_B9C')

    Return()

# id: 0x000C offset: 0xB9D
@scena.Code('func_0C_B9D')
def func_0C_B9D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BD3',
    )

    SetChrChipByIndex(0x00FE, 12)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 13)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_0C_B9D')

    def _loc_BD3(): pass

    label('loc_BD3')

    Return()

# id: 0x000D offset: 0xBD4
@scena.Code('func_0D_BD4')
def func_0D_BD4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BE9',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_0D_BD4')

    def _loc_BE9(): pass

    label('loc_BE9')

    Return()

# id: 0x000E offset: 0xBEA
@scena.Code('func_0E_BEA')
def func_0E_BEA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C20',
    )

    SetChrChipByIndex(0x00FE, 19)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 20)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_0E_BEA')

    def _loc_C20(): pass

    label('loc_C20')

    Return()

# id: 0x000F offset: 0xC21
@scena.Code('func_0F_C21')
def func_0F_C21():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C36',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_0F_C21')

    def _loc_C36(): pass

    label('loc_C36')

    Return()

# id: 0x0010 offset: 0xC37
@scena.Code('func_10_C37')
def func_10_C37():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C6D',
    )

    SetChrChipByIndex(0x00FE, 26)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 27)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_10_C37')

    def _loc_C6D(): pass

    label('loc_C6D')

    Return()

# id: 0x0011 offset: 0xC6E
@scena.Code('func_11_C6E')
def func_11_C6E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C83',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_11_C6E')

    def _loc_C83(): pass

    label('loc_C83')

    Return()

# id: 0x0012 offset: 0xC84
@scena.Code('func_12_C84')
def func_12_C84():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CBA',
    )

    SetChrChipByIndex(0x00FE, 33)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 34)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_12_C84')

    def _loc_CBA(): pass

    label('loc_CBA')

    Return()

# id: 0x0013 offset: 0xCBB
@scena.Code('func_13_CBB')
def func_13_CBB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CD0',
    )

    OP_99(0x00FE, 0x00, 0x0B, 0x000003E8)

    Jump('func_13_CBB')

    def _loc_CD0(): pass

    label('loc_CD0')

    Return()

# id: 0x0014 offset: 0xCD1
@scena.Code('func_14_CD1')
def func_14_CD1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CE6',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_14_CD1')

    def _loc_CE6(): pass

    label('loc_CE6')

    Return()

# id: 0x0015 offset: 0xCE7
@scena.Code('func_15_CE7')
def func_15_CE7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D1D',
    )

    SetChrChipByIndex(0x00FE, 40)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 41)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_15_CE7')

    def _loc_D1D(): pass

    label('loc_D1D')

    Return()

# id: 0x0016 offset: 0xD1E
@scena.Code('func_16_D1E')
def func_16_D1E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D33',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_16_D1E')

    def _loc_D33(): pass

    label('loc_D33')

    Return()

# id: 0x0017 offset: 0xD34
@scena.Code('func_17_D34')
def func_17_D34():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D6A',
    )

    SetChrChipByIndex(0x00FE, 47)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 48)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_17_D34')

    def _loc_D6A(): pass

    label('loc_D6A')

    Return()

# id: 0x0018 offset: 0xD6B
@scena.Code('func_18_D6B')
def func_18_D6B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D80',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_18_D6B')

    def _loc_D80(): pass

    label('loc_D80')

    Return()

# id: 0x0019 offset: 0xD81
@scena.Code('func_19_D81')
def func_19_D81():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DB7',
    )

    SetChrChipByIndex(0x00FE, 54)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 55)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_19_D81')

    def _loc_DB7(): pass

    label('loc_DB7')

    Return()

# id: 0x001A offset: 0xDB8
@scena.Code('func_1A_DB8')
def func_1A_DB8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DCD',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)

    Jump('func_1A_DB8')

    def _loc_DCD(): pass

    label('loc_DCD')

    Return()

# id: 0x001B offset: 0xDCE
@scena.Code('func_1B_DCE')
def func_1B_DCE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E04',
    )

    SetChrChipByIndex(0x00FE, 62)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    SetChrChipByIndex(0x00FE, 63)
    OP_99(0x00FE, 0x00, 0x01, 0x000003E8)
    Sleep(1000)

    Jump('func_1B_DCE')

    def _loc_E04(): pass

    label('loc_E04')

    Return()

# id: 0x001C offset: 0xE05
@scena.Code('func_1C_E05')
def func_1C_E05():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗷—',
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

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0058_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0058   ._SN')

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
        ('ED6_DT09/CH11000._CH', 'ED6_DT09/CH11000P._CP'),
        ('ED6_DT09/CH11001._CH', 'ED6_DT09/CH11001P._CP'),
        ('ED6_DT09/CH11002._CH', 'ED6_DT09/CH11002P._CP'),
        ('ED6_DT09/CH11003._CH', 'ED6_DT09/CH11003P._CP'),
        ('ED6_DT09/CH11004._CH', 'ED6_DT09/CH11004P._CP'),
        ('ED6_DT09/CH11010._CH', 'ED6_DT09/CH11010P._CP'),
        ('ED6_DT09/CH11011._CH', 'ED6_DT09/CH11011P._CP'),
        ('ED6_DT09/CH11012._CH', 'ED6_DT09/CH11012P._CP'),
        ('ED6_DT09/CH11013._CH', 'ED6_DT09/CH11013P._CP'),
        ('ED6_DT09/CH11014._CH', 'ED6_DT09/CH11014P._CP'),
        ('ED6_DT09/CH11020._CH', 'ED6_DT09/CH11020P._CP'),
        ('ED6_DT09/CH11021._CH', 'ED6_DT09/CH11021P._CP'),
        ('ED6_DT09/CH11022._CH', 'ED6_DT09/CH11022P._CP'),
        ('ED6_DT09/CH11023._CH', 'ED6_DT09/CH11023P._CP'),
        ('ED6_DT09/CH11024._CH', 'ED6_DT09/CH11024P._CP'),
        ('ED6_DT09/CH11030._CH', 'ED6_DT09/CH11030P._CP'),
        ('ED6_DT09/CH11031._CH', 'ED6_DT09/CH11031P._CP'),
        ('ED6_DT09/CH11032._CH', 'ED6_DT09/CH11032P._CP'),
        ('ED6_DT09/CH11033._CH', 'ED6_DT09/CH11033P._CP'),
        ('ED6_DT09/CH11034._CH', 'ED6_DT09/CH11034P._CP'),
        ('ED6_DT09/CH11040._CH', 'ED6_DT09/CH11040P._CP'),
        ('ED6_DT09/CH11041._CH', 'ED6_DT09/CH11041P._CP'),
        ('ED6_DT09/CH11042._CH', 'ED6_DT09/CH11042P._CP'),
        ('ED6_DT09/CH11043._CH', 'ED6_DT09/CH11043P._CP'),
        ('ED6_DT09/CH11044._CH', 'ED6_DT09/CH11044P._CP'),
        ('ED6_DT09/CH11050._CH', 'ED6_DT09/CH11050P._CP'),
        ('ED6_DT09/CH11051._CH', 'ED6_DT09/CH11051P._CP'),
        ('ED6_DT09/CH11052._CH', 'ED6_DT09/CH11052P._CP'),
        ('ED6_DT09/CH11053._CH', 'ED6_DT09/CH11053P._CP'),
        ('ED6_DT09/CH11054._CH', 'ED6_DT09/CH11054P._CP'),
        ('ED6_DT09/CH11060._CH', 'ED6_DT09/CH11060P._CP'),
        ('ED6_DT09/CH11061._CH', 'ED6_DT09/CH11061P._CP'),
        ('ED6_DT09/CH11062._CH', 'ED6_DT09/CH11062P._CP'),
        ('ED6_DT09/CH11063._CH', 'ED6_DT09/CH11063P._CP'),
        ('ED6_DT09/CH11064._CH', 'ED6_DT09/CH11064P._CP'),
    ]

# id: 0x10001 offset: 0x1C2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '11000待机',
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
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11001移动',
            x                   = 4000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11002攻击',
            x                   = 4000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11003被弹开',
            x                   = 4000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11004倒下',
            x                   = 4000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11010待机',
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
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11011移动',
            x                   = 8000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11012攻击',
            x                   = 8000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11013被弹开',
            x                   = 8000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11014倒下',
            x                   = 8000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11020待机',
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
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11021移动',
            x                   = 12000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11022攻击',
            x                   = 12000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11023被弹开',
            x                   = 12000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11024倒下',
            x                   = 12000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11030待机',
            x                   = 16000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11031移动',
            x                   = 16000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11032攻击',
            x                   = 16000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11033被弹开',
            x                   = 16000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11034倒下',
            x                   = 16000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11040待机',
            x                   = 20000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11041移动',
            x                   = 20000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11042攻击',
            x                   = 20000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11043被弹开',
            x                   = 20000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11044倒下',
            x                   = 20000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11050待机',
            x                   = 24000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11051移动',
            x                   = 24000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11052攻击',
            x                   = 24000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11053被弹开',
            x                   = 24000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11054倒下',
            x                   = 24000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11060待机',
            x                   = 28000,
            z                   = 0,
            y                   = 2000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11061移动',
            x                   = 28000,
            z                   = 0,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11062攻击',
            x                   = 28000,
            z                   = 0,
            y                   = 10000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11063被弹开',
            x                   = 28000,
            z                   = 0,
            y                   = 14000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '11064倒下',
            x                   = 28000,
            z                   = 0,
            y                   = 18000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x622
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x622
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x622
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x622
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x623
@scena.Code('func_01_623')
def func_01_623():
    Return()

# id: 0x0002 offset: 0x624
@scena.Code('func_02_624')
def func_02_624():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_639',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_624')

    def _loc_639(): pass

    label('loc_639')

    Return()

# id: 0x0003 offset: 0x63A
@scena.Code('func_03_63A')
def func_03_63A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_64F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1400)

    Jump('func_03_63A')

    def _loc_64F(): pass

    label('loc_64F')

    Return()

# id: 0x0004 offset: 0x650
@scena.Code('func_04_650')
def func_04_650():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_673',
    )

    OP_8D(0x00FE, 4000, 20000, 24000, 30000, 1500)

    Jump('func_04_650')

    def _loc_673(): pass

    label('loc_673')

    Return()

# id: 0x0005 offset: 0x674
@scena.Code('func_05_674')
def func_05_674():
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

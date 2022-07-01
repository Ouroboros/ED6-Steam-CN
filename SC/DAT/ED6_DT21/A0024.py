import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import A0024_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('A0024   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '04580尤莉亚待机'),
    TXT(0x02, '04581尤莉亚移动'),
    TXT(0x03, '04582尤莉亚攻击'),
    TXT(0x04, '04583尤莉亚被弹开'),
    TXT(0x05, '04584尤莉亚倒下'),
    TXT(0x06, '04585尤莉亚魔法咏唱'),
    TXT(0x07, '04586尤莉亚魔法发射'),
    TXT(0x08, '04570穆拉待机'),
    TXT(0x09, '04571穆拉移动'),
    TXT(0x0A, '04572穆拉攻击'),
    TXT(0x0B, '04573穆拉被弹开'),
    TXT(0x0C, '04574穆拉倒下'),
    TXT(0x0D, '04575穆拉魔法咏唱'),
    TXT(0x0E, '04576穆拉魔法发射'),
    TXT(0x0F, '04590希德待机'),
    TXT(0x10, '04591希德移动'),
    TXT(0x11, '04592希德攻击'),
    TXT(0x12, '04593希德被弹开'),
    TXT(0x13, '04594希德倒下'),
    TXT(0x14, '04595希德魔法咏唱'),
    TXT(0x15, '04596希德魔法发射'),
    TXT(0x16, '04120凯诺娜待机'),
    TXT(0x17, '04121凯诺娜移动'),
    TXT(0x18, '04122凯诺娜攻击'),
    TXT(0x19, '04123凯诺娜被弹开'),
    TXT(0x1A, '04124凯诺娜倒下'),
    TXT(0x1B, '04125凯诺娜魔法咏唱'),
    TXT(0x1C, '04126凯诺娜魔法发射'),
    TXT(0x1D, ''),
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

# id: 0xFFFF offset: 0x94E
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
        ('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP'),
        ('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP'),
        ('ED6_DT27/CH04582._CH', 'ED6_DT27/CH04582P._CP'),
        ('ED6_DT27/CH04583._CH', 'ED6_DT27/CH04583P._CP'),
        ('ED6_DT27/CH04584._CH', 'ED6_DT27/CH04584P._CP'),
        ('ED6_DT27/CH04585._CH', 'ED6_DT27/CH04585P._CP'),
        ('ED6_DT27/CH04586._CH', 'ED6_DT27/CH04586P._CP'),
        ('ED6_DT27/CH04583._CH', 'ED6_DT27/CH04583P._CP'),
        ('ED6_DT27/CH04583._CH', 'ED6_DT27/CH04583P._CP'),
        ('ED6_DT27/CH04583._CH', 'ED6_DT27/CH04583P._CP'),
        ('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP'),
        ('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP'),
        ('ED6_DT27/CH04572._CH', 'ED6_DT27/CH04572P._CP'),
        ('ED6_DT27/CH04573._CH', 'ED6_DT27/CH04573P._CP'),
        ('ED6_DT27/CH04574._CH', 'ED6_DT27/CH04574P._CP'),
        ('ED6_DT27/CH04575._CH', 'ED6_DT27/CH04575P._CP'),
        ('ED6_DT27/CH04576._CH', 'ED6_DT27/CH04576P._CP'),
        ('ED6_DT27/CH04573._CH', 'ED6_DT27/CH04573P._CP'),
        ('ED6_DT27/CH04573._CH', 'ED6_DT27/CH04573P._CP'),
        ('ED6_DT27/CH04573._CH', 'ED6_DT27/CH04573P._CP'),
        ('ED6_DT27/CH04590._CH', 'ED6_DT27/CH04590P._CP'),
        ('ED6_DT27/CH04591._CH', 'ED6_DT27/CH04591P._CP'),
        ('ED6_DT27/CH04592._CH', 'ED6_DT27/CH04592P._CP'),
        ('ED6_DT27/CH04593._CH', 'ED6_DT27/CH04593P._CP'),
        ('ED6_DT27/CH04594._CH', 'ED6_DT27/CH04594P._CP'),
        ('ED6_DT27/CH04595._CH', 'ED6_DT27/CH04595P._CP'),
        ('ED6_DT27/CH04596._CH', 'ED6_DT27/CH04596P._CP'),
        ('ED6_DT27/CH04593._CH', 'ED6_DT27/CH04593P._CP'),
        ('ED6_DT27/CH04593._CH', 'ED6_DT27/CH04593P._CP'),
        ('ED6_DT27/CH04593._CH', 'ED6_DT27/CH04593P._CP'),
        ('ED6_DT27/CH04120._CH', 'ED6_DT27/CH04120P._CP'),
        ('ED6_DT27/CH04121._CH', 'ED6_DT27/CH04121P._CP'),
        ('ED6_DT27/CH04122._CH', 'ED6_DT27/CH04122P._CP'),
        ('ED6_DT27/CH04123._CH', 'ED6_DT27/CH04123P._CP'),
        ('ED6_DT27/CH04124._CH', 'ED6_DT27/CH04124P._CP'),
        ('ED6_DT27/CH04125._CH', 'ED6_DT27/CH04125P._CP'),
        ('ED6_DT27/CH04126._CH', 'ED6_DT27/CH04126P._CP'),
        ('ED6_DT27/CH04123._CH', 'ED6_DT27/CH04123P._CP'),
        ('ED6_DT27/CH04123._CH', 'ED6_DT27/CH04123P._CP'),
        ('ED6_DT27/CH04123._CH', 'ED6_DT27/CH04123P._CP'),
    ]

# id: 0x10002 offset: 0x1EA
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
            talkScenaIndex      = 0x000C,
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
            talkScenaIndex      = 0x000C,
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
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
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
            talkScenaIndex      = 0x000C,
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
            talkScenaIndex      = 0x000C,
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
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
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
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
    )

# id: 0x10003 offset: 0x56A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x56A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x56A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x56A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x56B
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x56C
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_581',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000640)

    Jump('ReInit')

    def _loc_581(): pass

    label('loc_581')

    Return()

# id: 0x0003 offset: 0x582
@scena.Code('func_03_582')
def func_03_582():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_597',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

    Jump('func_03_582')

    def _loc_597(): pass

    label('loc_597')

    Return()

# id: 0x0004 offset: 0x598
@scena.Code('func_04_598')
def func_04_598():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5B2',
    )

    OP_99(0x00FE, 0x00, 0x00, 0x000005DC)
    Sleep(500)

    Jump('func_04_598')

    def _loc_5B2(): pass

    label('loc_5B2')

    Return()

# id: 0x0005 offset: 0x5B3
@scena.Code('func_05_5B3')
def func_05_5B3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5CD',
    )

    OP_99(0x00FE, 0x00, 0x03, 0x000003E8)
    Sleep(500)

    Jump('func_05_5B3')

    def _loc_5CD(): pass

    label('loc_5CD')

    Return()

# id: 0x0006 offset: 0x5CE
@scena.Code('func_06_5CE')
def func_06_5CE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_61A',
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

    Jump('func_06_5CE')

    def _loc_61A(): pass

    label('loc_61A')

    Return()

# id: 0x0007 offset: 0x61B
@scena.Code('func_07_61B')
def func_07_61B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6D6',
    )

    SetChrChipByIndex(0x00FE, 5)

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

    SetChrChipByIndex(0x00FE, 6)

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

    Jump('func_07_61B')

    def _loc_6D6(): pass

    label('loc_6D6')

    Return()

# id: 0x0008 offset: 0x6D7
@scena.Code('func_08_6D7')
def func_08_6D7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_792',
    )

    SetChrChipByIndex(0x00FE, 15)

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

    SetChrChipByIndex(0x00FE, 16)

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

    Jump('func_08_6D7')

    def _loc_792(): pass

    label('loc_792')

    Return()

# id: 0x0009 offset: 0x793
@scena.Code('func_09_793')
def func_09_793():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_84E',
    )

    SetChrChipByIndex(0x00FE, 25)

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

    SetChrChipByIndex(0x00FE, 26)

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

    Jump('func_09_793')

    def _loc_84E(): pass

    label('loc_84E')

    Return()

# id: 0x000A offset: 0x84F
@scena.Code('func_0A_84F')
def func_0A_84F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_864',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000640)

    Jump('func_0A_84F')

    def _loc_864(): pass

    label('loc_864')

    Return()

# id: 0x000B offset: 0x865
@scena.Code('func_0B_865')
def func_0B_865():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_920',
    )

    SetChrChipByIndex(0x00FE, 35)

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

    SetChrChipByIndex(0x00FE, 36)

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

    Jump('func_0B_865')

    def _loc_920(): pass

    label('loc_920')

    Return()

# id: 0x000C offset: 0x921
@scena.Code('func_0C_921')
def func_0C_921():
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

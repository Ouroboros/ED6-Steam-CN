import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import A0000_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('A0000   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '12000待机'),
    TXT(0x02, '12001移动'),
    TXT(0x03, '12002攻击'),
    TXT(0x04, '12003伤害'),
    TXT(0x05, '12004倒下'),
    TXT(0x06, '12010待机'),
    TXT(0x07, '12011移动'),
    TXT(0x08, '12012攻击'),
    TXT(0x09, '12013伤害'),
    TXT(0x0A, '12014倒下'),
    TXT(0x0B, '12020待机'),
    TXT(0x0C, '12021移动'),
    TXT(0x0D, '12022攻击'),
    TXT(0x0E, '12023伤害'),
    TXT(0x0F, '12024倒下'),
    TXT(0x10, '12030待机'),
    TXT(0x11, '12031移动'),
    TXT(0x12, '12032攻击'),
    TXT(0x13, '12033伤害'),
    TXT(0x14, '12034倒下'),
    TXT(0x15, '12040待机'),
    TXT(0x16, '12041移动'),
    TXT(0x17, '12042攻击'),
    TXT(0x18, '12043伤害'),
    TXT(0x19, '12044倒下'),
    TXT(0x1A, ''),
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

# id: 0xFFFF offset: 0x10AF
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
        ('ED6_DT29/CH12000._CH', 'ED6_DT29/CH12000P._CP'),
        ('ED6_DT29/CH12001._CH', 'ED6_DT29/CH12001P._CP'),
        ('ED6_DT29/CH12002._CH', 'ED6_DT29/CH12002P._CP'),
        ('ED6_DT29/CH12003._CH', 'ED6_DT29/CH12003P._CP'),
        ('ED6_DT29/CH12004._CH', 'ED6_DT29/CH12004P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12010._CH', 'ED6_DT29/CH12010P._CP'),
        ('ED6_DT29/CH12011._CH', 'ED6_DT29/CH12011P._CP'),
        ('ED6_DT29/CH12012._CH', 'ED6_DT29/CH12012P._CP'),
        ('ED6_DT29/CH12013._CH', 'ED6_DT29/CH12013P._CP'),
        ('ED6_DT29/CH12014._CH', 'ED6_DT29/CH12014P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12020._CH', 'ED6_DT29/CH12020P._CP'),
        ('ED6_DT29/CH12021._CH', 'ED6_DT29/CH12021P._CP'),
        ('ED6_DT29/CH12022._CH', 'ED6_DT29/CH12022P._CP'),
        ('ED6_DT29/CH12023._CH', 'ED6_DT29/CH12023P._CP'),
        ('ED6_DT29/CH12024._CH', 'ED6_DT29/CH12024P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12030._CH', 'ED6_DT29/CH12030P._CP'),
        ('ED6_DT29/CH12031._CH', 'ED6_DT29/CH12031P._CP'),
        ('ED6_DT29/CH12032._CH', 'ED6_DT29/CH12032P._CP'),
        ('ED6_DT29/CH12033._CH', 'ED6_DT29/CH12033P._CP'),
        ('ED6_DT29/CH12034._CH', 'ED6_DT29/CH12034P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12040._CH', 'ED6_DT29/CH12040P._CP'),
        ('ED6_DT29/CH12041._CH', 'ED6_DT29/CH12041P._CP'),
        ('ED6_DT29/CH12042._CH', 'ED6_DT29/CH12042P._CP'),
        ('ED6_DT29/CH12043._CH', 'ED6_DT29/CH12043P._CP'),
        ('ED6_DT29/CH12044._CH', 'ED6_DT29/CH12044P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
    ]

# id: 0x10002 offset: 0x23A
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
            talkScenaIndex      = 0x0005,
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
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
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
            talkScenaIndex      = 0x0007,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            talkScenaIndex      = 0x0004,
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
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            talkScenaIndex      = 0x0004,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            talkScenaIndex      = 0x0004,
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
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            talkScenaIndex      = 0x0004,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            talkScenaIndex      = 0x0004,
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
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            talkScenaIndex      = 0x0004,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x55A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x55A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x55A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x55A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x55B
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x55C
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0000,
        (
            Expr.Rand,
            (Expr.PushLong, 0x6),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_589'),
        (0x00000001, 'loc_591'),
        (0x00000002, 'loc_599'),
        (0x00000003, 'loc_5A1'),
        (0x00000004, 'loc_5A9'),
        (0x00000005, 'loc_5B1'),
        (-1, 'loc_5B9'),
    )

    def _loc_589(): pass

    label('loc_589')

    Sleep(100)

    Jump('loc_5B9')

    def _loc_591(): pass

    label('loc_591')

    Sleep(100)

    Jump('loc_5B9')

    def _loc_599(): pass

    label('loc_599')

    Sleep(200)

    Jump('loc_5B9')

    def _loc_5A1(): pass

    label('loc_5A1')

    Sleep(300)

    Jump('loc_5B9')

    def _loc_5A9(): pass

    label('loc_5A9')

    Sleep(400)

    Jump('loc_5B9')

    def _loc_5B1(): pass

    label('loc_5B1')

    Sleep(500)

    Jump('loc_5B9')

    def _loc_5B9(): pass

    label('loc_5B9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5CE',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5B9')

    def _loc_5CE(): pass

    label('loc_5CE')

    Return()

# id: 0x0003 offset: 0x5CF
@scena.Code('func_03_5CF')
def func_03_5CF():
    Return()

# id: 0x0004 offset: 0x5D0
@scena.Code('func_04_5D0')
def func_04_5D0():
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

# id: 0x0005 offset: 0x5E1
@scena.Code('func_05_5E1')
def func_05_5E1():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#1Sあいうえお　#2Sあいうえお\n',
            '#3Sあいうえお　#4Sあいうえお　#5Sあいうえお\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sかきくけこ　#2Sかきくけこ\n',
            '#3Sかきくけこ　#4Sかきくけこ　#5Sかきくけこ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sさしすせそ　#2Sさしすせそ\n',
            '#3Sさしすせそ　#4Sさしすせそ　#5Sさしすせそ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sたちつてと　#2Sたちつてと\n',
            '#3Sたちつてと　#4Sたちつてと　#5Sたちつてと\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sなにぬねの　#2Sなにぬねの\n',
            '#3Sなにぬねの　#4Sなにぬねの　#5Sなにぬねの\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sはひふへほ　#2Sはひふへほ\n',
            '#3Sはひふへほ　#4Sはひふへほ　#5Sはひふへほ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sまみむめも　#2Sまみむめも\n',
            '#3Sまみむめも　#4Sまみむめも　#5Sまみむめも\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sやゆよ　#2Sやゆよ\n',
            '#3Sやゆよ　#4Sやゆよ　#5Sやゆよ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sらりるれろ　#2Sらりるれろ\n',
            '#3Sらりるれろ　#4Sらりるれろ　#5Sらりるれろ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sわをん　#2Sわをん\n',
            '#3Sわをん　#4Sわをん　#5Sわをん\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sがぎぐげご　#2Sがぎぐげご\n',
            '#3Sがぎぐげご　#4Sがぎぐげご　#5Sがぎぐげご\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sざじずぜぞ　#2Sざじずぜぞ\n',
            '#3Sざじずぜぞ　#4Sざじずぜぞ　#5Sざじずぜぞ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sだぢづでど　#2Sだぢづでど\n',
            '#3Sだぢづでど　#4Sだぢづでど　#5Sだぢづでど\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sばびぶべぼ　#2Sばびぶべぼ\n',
            '#3Sばびぶべぼ　#4Sばびぶべぼ　#5Sばびぶべぼ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sぱぴぷぺぽ　#2Sぱぴぷぺぽ\n',
            '#3Sぱぴぷぺぽ　#4Sぱぴぷぺぽ　#5Sぱぴぷぺぽ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sぁぃぅぇぉ　#2Sぁぃぅぇぉ\n',
            '#3Sぁぃぅぇぉ　#4Sぁぃぅぇぉ　#5Sぁぃぅぇぉ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sゃゅょっ　#2Sゃゅょっ\n',
            '#3Sゃゅょっ　#4Sゃゅょっ　#5Sゃゅょっ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xAF5
@scena.Code('func_06_AF5')
def func_06_AF5():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#1Sアイウエオ　#2Sアイウエオ\n',
            '#3Sアイウエオ　#4Sアイウエオ　#5Sアイウエオ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sカキクケコ　#2Sカキクケコ\n',
            '#3Sカキクケコ　#4Sカキクケコ　#5Sカキクケコ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sサシスセソ　#2Sサシスセソ\n',
            '#3Sサシスセソ　#4Sサシスセソ　#5Sサシスセソ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sタチツテト　#2Sタチツテト\n',
            '#3Sタチツテト　#4Sタチツテト　#5Sタチツテト\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sナニヌネノ　#2Sナニヌネノ\n',
            '#3Sナニヌネノ　#4Sナニヌネノ　#5Sナニヌネノ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sハヒフヘホ　#2Sハヒフヘホ\n',
            '#3Sハヒフヘホ　#4Sハヒフヘホ　#5Sハヒフヘホ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sマミムメモ#2Sマミムメモ\n',
            '#3Sマミムメモ#4Sマミムメモ#5Sマミムメモ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sヤユヨ　#2Sヤユヨ\n',
            '#3Sヤユヨ　#4Sヤユヨ　#5Sヤユヨ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sラリルレロ　#2Sラリルレロ\n',
            '#3Sラリルレロ　#4Sラリルレロ　#5Sラリルレロ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sワオン　#2Sワオン\n',
            '#3Sワオン　#4Sワオン　#5Sワオン\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sガギグゲゴ　#2Sガギグゲゴ\n',
            '#3Sガギグゲゴ　#4Sガギグゲゴ　#5Sガギグゲゴ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sザジズゼゾ　#2Sザジズゼゾ\n',
            '#3Sザジズゼゾ　#4Sザジズゼゾ　#5Sザジズゼゾ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sダヂヅデド　#2Sダヂヅデド\n',
            '#3Sダヂヅデド　#4Sダヂヅデド　#5Sダヂヅデド\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sバビブベボ　#2Sバビブベボ\n',
            '#3Sバビブベボ　#4Sバビブベボ　#5Sバビブベボ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sパピプペポ　#2Sパピプペポ\n',
            '#3Sパピプペポ　#4Sパピプペポ　#5Sパピプペポ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sァィゥェォ　#2Sァィゥェォ\n',
            '#3Sァィゥェォ　#4Sァィゥェォ　#5Sァィゥェォ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1Sャュョッ　#2Sャュョッ\n',
            '#3Sャュョッ　#4Sャュョッ　#5Sャュョッ\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1003
@scena.Code('func_07_1003')
def func_07_1003():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#5S要恢复原状就指定默认坐标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#5S吉米好帅～～！　我爱你～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#5S说什么傻话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#5S就这样冲进浮游都市！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2S只有枪杆值得信赖。',
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

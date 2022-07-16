import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1110   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '博尔德'),
    TXT(0x02, '莉咏'),
    TXT(0x03, '阿尔贝尔'),
    TXT(0x04, '库瓦诺老人'),
    TXT(0x05, '塞西尔婆婆'),
    TXT(0x06, '莫德娜'),
    TXT(0x07, '米拉诺'),
    TXT(0x08, '西蒙'),
    TXT(0x09, '拉娜'),
    TXT(0x0A, '艾尔珂'),
    TXT(0x0B, '王国军士兵'),
    TXT(0x0C, '王国军士兵'),
    TXT(0x0D, '王国军士兵'),
    TXT(0x0E, '特里诺'),
    TXT(0x0F, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1110.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4CC7
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
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 3000,
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01183._CH', 'ED6_DT07/CH01183P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -22100,
            z                   = 0,
            y                   = 69250,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -21340,
            z                   = 0,
            y                   = 72520,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -11200,
            z                   = 5250,
            y                   = 72600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -21700,
            z                   = 0,
            y                   = 3000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -16400,
            z                   = 0,
            y                   = -1700,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -18730,
            z                   = 0,
            y                   = 33060,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 19400,
            z                   = 0,
            y                   = 31200,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -21100,
            z                   = 0,
            y                   = 33600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 20970,
            z                   = 0,
            y                   = 67860,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 27100,
            z                   = 4000,
            y                   = 72200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -20715,
            z                   = 0,
            y                   = -1884,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -21300,
            z                   = 0,
            y                   = 66800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 21176,
            z                   = 0,
            y                   = 66028,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -21100,
            z                   = 0,
            y                   = 33600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
    )

# id: 0x10003 offset: 0x2DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2DA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x2DA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2DA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_2E9',
    )

    ClearChrFlags(0x0015, 0x0080)

    Jump('loc_3FD')

    def _loc_2E9(): pass

    label('loc_2E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_302',
    )

    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0008)
    ClearChrFlags(0x000F, 0x0080)

    Jump('loc_3FD')

    def _loc_302(): pass

    label('loc_302')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_316',
    )

    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000B, 0x0080)

    Jump('loc_3FD')

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_348',
    )

    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0010)
    SetChrFlags(0x0008, 0x0010)
    SetChrFlags(0x0009, 0x0010)
    SetChrFlags(0x000A, 0x0010)
    SetChrFlags(0x0010, 0x0010)
    SetChrFlags(0x0011, 0x0010)

    Jump('loc_3FD')

    def _loc_348(): pass

    label('loc_348')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_385',
    )

    SetChrPos(0x000D, 17400, 300, 28530, 270)
    SetChrPos(0x000E, -20530, 0, 33050, 180)
    SetChrPos(0x000C, -16400, 0, -1700, 90)

    Jump('loc_3FD')

    def _loc_385(): pass

    label('loc_385')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_3AA',
    )

    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0008)
    SetChrPos(0x000C, -16400, 0, -1700, 90)

    Jump('loc_3FD')

    def _loc_3AA(): pass

    label('loc_3AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_3DB',
    )

    SetChrFlags(0x000D, 0x0010)
    SetChrPos(0x000C, -16400, 0, -1700, 135)
    SetChrPos(0x000E, -23120, 0, 34500, 180)

    Jump('loc_3FD')

    def _loc_3DB(): pass

    label('loc_3DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_3FD',
    )

    SetChrPos(0x000B, -17620, 0, -680, 135)
    SetChrFlags(0x000B, 0x0010)
    SetChrFlags(0x000C, 0x0010)

    def _loc_3FD(): pass

    label('loc_3FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_499',
    )

    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0010, 20852, 0, 68000, 180)
    SetChrPos(0x0011, 21329, 0, 68470, 180)
    TerminateThread(0x0011, 0xFF)
    CreateThread(0x0011, 0x03, 0x00, 0x0002)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0008, -20868, 0, 68402, 180)
    SetChrPos(0x000A, -22006, 0, 68102, 135)
    SetChrPos(0x0009, -19902, 0, 68102, 225)
    TerminateThread(0x0008, 0xFF)
    CreateThread(0x0008, 0x03, 0x00, 0x0002)
    ClearChrFlags(0x0014, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrPos(0x000C, -21950, 0, -570, 135)

    def _loc_499(): pass

    label('loc_499')

    Return()

# id: 0x0001 offset: 0x49A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x49B
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4B0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_4B0(): pass

    label('loc_4B0')

    Return()

# id: 0x0003 offset: 0x4B1
@scena.Code('func_03_4B1')
def func_03_4B1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_4D0',
    )

    def _loc_4B8(): pass

    label('loc_4B8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4CD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_4B8')

    def _loc_4CD(): pass

    label('loc_4CD')

    Jump('loc_53F')

    def _loc_4D0(): pass

    label('loc_4D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_51C',
    )

    def _loc_4D7(): pass

    label('loc_4D7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_519',
    )

    ChrWalkTo(0x00FE, -23130, 0, 36620, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 500)
    ChrWalkTo(0x00FE, -23130, 0, 31660, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 500)

    Jump('loc_4D7')

    def _loc_519(): pass

    label('loc_519')

    Jump('loc_53F')

    def _loc_51C(): pass

    label('loc_51C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_53F',
    )

    OP_8D(0x00FE, 20900, 30000, 15300, 31700, 2000)

    Jump('loc_51C')

    def _loc_53F(): pass

    label('loc_53F')

    Return()

# id: 0x0004 offset: 0x540
@scena.Code('func_04_540')
def func_04_540():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_563',
    )

    OP_8D(0x00FE, 26200, 71400, 28400, 72600, 2000)

    Jump('func_04_540')

    def _loc_563(): pass

    label('loc_563')

    Return()

# id: 0x0005 offset: 0x564
@scena.Code('func_05_564')
def func_05_564():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_591',
    )

    def _loc_56B(): pass

    label('loc_56B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_58E',
    )

    OP_8D(0x00FE, 17430, 68790, 23880, 64870, 1500)

    Jump('loc_56B')

    def _loc_58E(): pass

    label('loc_58E')

    Jump('loc_5D3')

    def _loc_591(): pass

    label('loc_591')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_5B0',
    )

    def _loc_598(): pass

    label('loc_598')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5AD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_598')

    def _loc_5AD(): pass

    label('loc_5AD')

    Jump('loc_5D3')

    def _loc_5B0(): pass

    label('loc_5B0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5D3',
    )

    OP_8D(0x00FE, 17430, 68790, 23880, 64870, 1500)

    Jump('loc_5B0')

    def _loc_5D3(): pass

    label('loc_5D3')

    Return()

# id: 0x0006 offset: 0x5D4
@scena.Code('func_06_5D4')
def func_06_5D4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_62A',
    )

    def _loc_5DB(): pass

    label('loc_5DB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_627',
    )

    ChrWalkTo(0x00FE, -22800, 0, 72500, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, -20400, 0, 72420, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    Sleep(3000)

    Jump('loc_5DB')

    def _loc_627(): pass

    label('loc_627')

    Jump('loc_695')

    def _loc_62A(): pass

    label('loc_62A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_649',
    )

    def _loc_631(): pass

    label('loc_631')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_646',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_631')

    def _loc_646(): pass

    label('loc_646')

    Jump('loc_695')

    def _loc_649(): pass

    label('loc_649')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_695',
    )

    ChrWalkTo(0x00FE, -22800, 0, 72500, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, -20400, 0, 72420, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    Sleep(3000)

    Jump('loc_649')

    def _loc_695(): pass

    label('loc_695')

    Return()

# id: 0x0007 offset: 0x696
@scena.Code('func_07_696')
def func_07_696():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_7A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_738',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '特里诺那家伙\n',
            '终于平安回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样我就可以\n',
            '毫无顾虑地专心做生意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就碰到了那么点小麻烦， \n',
            '柏斯的商人不能就这样轻易泄气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_79F')

    def _loc_738(): pass

    label('loc_738')

    ChrTalk(
        0x00FE,
        (
            '这样我就可以\n',
            '毫无顾虑地专心做生意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就碰到了那么点小麻烦， \n',
            '柏斯的商人不能就这样轻易泄气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_79F(): pass

    label('loc_79F')

    Jump('loc_F0D')

    def _loc_7A2(): pass

    label('loc_7A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_951',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8CF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '尽管如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特里诺不在柏斯的话，\n',
            '总觉得哪里有些不对劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们小时候\n',
            '总是互相打打闹闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我们在商场上是对手，\n',
            '但是却好像有一种奇妙的连带感，\n',
            '这是千真万确的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以说柏斯的商业\n',
            '就是由我们两人支撑起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，如果他听到这番话，\n',
            '肯定要笑掉大牙了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94E')

    def _loc_8CF(): pass

    label('loc_8CF')

    ChrTalk(
        0x00FE,
        (
            '特里诺不在柏斯的话，\n',
            '总觉得哪里有些不对劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我们在商场上是对手，\n',
            '但是却好像有一种奇妙的连带感，\n',
            '这是千真万确的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_94E(): pass

    label('loc_94E')

    Jump('loc_F0D')

    def _loc_951(): pass

    label('loc_951')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_A99',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A36',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '飞艇的失踪再加上这次的强盗事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近的坏消息还真多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『赛希莉亚号』的复航\n',
            '是最近唯一令人高兴的话题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过对我们来说，\n',
            '到帝国去的国际航线不恢复的话\n',
            '就没办法继续做生意了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A96')

    def _loc_A36(): pass

    label('loc_A36')

    ChrTalk(
        0x00FE,
        (
            '不过对我们来说，\n',
            '到帝国去的国际航线不恢复的话\n',
            '就没办法继续做生意了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是很难办啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A96(): pass

    label('loc_A96')

    Jump('loc_F0D')

    def _loc_A99(): pass

    label('loc_A99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AEE',
    )

    ChrTurnDirection(0x0013, 0x0000, 0)

    ChrTalk(
        0x0013,
        (
            '#2440030344V我再问一会儿就结束了，\n',
            '你们要乖乖地等着哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0013, 0, 0)

    Jump('loc_F0D')

    def _loc_AEE(): pass

    label('loc_AEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_C4F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BF2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '由于柏斯领空被军队封锁了，\n',
            '影响了货物的进出交易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从帝国来的定期船\n',
            '也在国境附近被截停禁止进入……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样子下去\n',
            '我们就无法做生意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……米拉诺小姐即使在这种情况下\n',
            '似乎也能够精力充沛地工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '我可不能向她认输。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C4C')

    def _loc_BF2(): pass

    label('loc_BF2')

    ChrTalk(
        0x00FE,
        (
            '米拉诺小姐即使在这种情况下\n',
            '似乎也能够精力充沛地工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '我可不能向她认输。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C4C(): pass

    label('loc_C4C')

    Jump('loc_F0D')

    def _loc_C4F(): pass

    label('loc_C4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_D72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D44',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '特里诺好像\n',
            '乘坐了那艘失踪的飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然觉得有点对不起他，\n',
            '不过对我来说也许是个机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '借这个机会\n',
            '把特里诺的生意\n',
            '都揽到我这边来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米拉诺小姐\n',
            '现在相当有影响力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '那对父女关系到底是好还是坏呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D6F')

    def _loc_D44(): pass

    label('loc_D44')

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '那对父女关系到底是好还是坏呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D6F(): pass

    label('loc_D6F')

    Jump('loc_F0D')

    def _loc_D72(): pass

    label('loc_D72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_EAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E4F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我们家自古以来就是\n',
            '在这个柏斯以贸易起家的商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯的势力范围\n',
            '基本上被我家\n',
            '和特里诺家瓜分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过最近\n',
            '特里诺的女儿米拉诺小姐\n',
            '势力增长得也很快啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在已经形成\n',
            '三足鼎立之势了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EA9')

    def _loc_E4F(): pass

    label('loc_E4F')

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '特里诺的女儿米拉诺小姐\n',
            '势力增长得也很快啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在已经形成三足鼎立之势了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EA9(): pass

    label('loc_EA9')

    Jump('loc_F0D')

    def _loc_EAC(): pass

    label('loc_EAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_F0D',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然柏斯商人都喜欢自由自在，\n',
            '但是遵守约定是我们的信条。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，\n',
            '我们会十分守时。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F0D(): pass

    label('loc_F0D')

    TalkEnd(0x0008)

    Return()

# id: 0x0008 offset: 0xF11
@scena.Code('func_08_F11')
def func_08_F11():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_FC5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F8F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '原来那些蒙面男人\n',
            '就是传说中的空贼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们被抓住真是太好了。\n',
            '这样我就可以专注于我的事业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FC2')

    def _loc_F8F(): pass

    label('loc_F8F')

    ChrTalk(
        0x00FE,
        (
            '那么，这个月的销量\n',
            '一定要胜过强敌特里诺一家！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FC2(): pass

    label('loc_FC2')

    Jump('loc_151A')

    def _loc_FC5(): pass

    label('loc_FC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_105E',
    )

    ChrTalk(
        0x00FE,
        (
            '希望这个城市\n',
            '能够尽早恢复平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市场也渐渐变得冷清下来，\n',
            '这样下去这个月肯定会出现严重赤字了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上个月好不容易\n',
            '赢过了特里诺家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_151A')

    def _loc_105E(): pass

    label('loc_105E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_114A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10F3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上吓死我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了通风，\n',
            '我就把窗户打开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到有一伙蒙面的男人\n',
            '从窗户闯进屋子里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有好几个人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1147')

    def _loc_10F3(): pass

    label('loc_10F3')

    ChrTalk(
        0x00FE,
        (
            '为了通风，\n',
            '我就把窗户打开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到有一伙蒙面的男人\n',
            '从窗户闯进屋子里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1147(): pass

    label('loc_1147')

    Jump('loc_151A')

    def _loc_114A(): pass

    label('loc_114A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_119F',
    )

    ChrTurnDirection(0x0013, 0x0000, 0)

    ChrTalk(
        0x0013,
        (
            '#2440030344V我再问一会儿就结束了，\n',
            '你们要乖乖地等着哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0013, 0, 0)

    Jump('loc_151A')

    def _loc_119F(): pass

    label('loc_119F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_12D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1275',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我丈夫在买卖和谈判方面\n',
            '都进行得非常合理到位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而特里诺却完全相反。\n',
            '全都是靠劲头和感觉去拼的那种人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '米拉诺则是那两人综合起来的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '与梅贝尔市长属于同一种类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D3')

    def _loc_1275(): pass

    label('loc_1275')

    ChrTalk(
        0x00FE,
        (
            '在不久的将来，\n',
            '我们家的地位说不定会被米拉诺夺走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过呢，\n',
            '我们也绝不会轻易认输的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12D3(): pass

    label('loc_12D3')

    Jump('loc_151A')

    def _loc_12D6(): pass

    label('loc_12D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_13E4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1366',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '难道特里诺\n',
            '乘坐了那艘定期船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是对手，\n',
            '不过一直以来也都是老熟人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果他能够\n',
            '平安无事回来就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13E1')

    def _loc_1366(): pass

    label('loc_1366')

    ChrTalk(
        0x00FE,
        (
            '难道特里诺\n',
            '乘坐了那艘定期船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是对手，\n',
            '不过一直以来也都是老熟人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果他能够\n',
            '平安无事回来就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13E1(): pass

    label('loc_13E1')

    Jump('loc_151A')

    def _loc_13E4(): pass

    label('loc_13E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_14C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_148C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '米拉诺前一段时间\n',
            '到我们家来玩了。\n',
            '明明是那么可爱的女孩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在却是我们强大的商业对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果我家的阿尔贝尔\n',
            '也能有这样的气概就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14BD')

    def _loc_148C(): pass

    label('loc_148C')

    ChrTalk(
        0x00FE,
        (
            '真希望我家的儿子\n',
            '也能有米拉诺那样的气概啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14BD(): pass

    label('loc_14BD')

    Jump('loc_151A')

    def _loc_14C0(): pass

    label('loc_14C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_151A',
    )

    ChrTalk(
        0x00FE,
        (
            '自从军队实行戒严以来，\n',
            '都已经过了很久了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个月不用说又该是赤字了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_151A(): pass

    label('loc_151A')

    TalkEnd(0x0009)

    Return()

# id: 0x0009 offset: 0x151E
@scena.Code('func_09_151E')
def func_09_151E():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_15F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15AF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '卢安的杰尼丝王立学院\n',
            '有一个叫做社会系的专业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能学到专业的政治与经济知识，\n',
            '父亲说不定会同意\n',
            '让我去学校念书呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15EF')

    def _loc_15AF(): pass

    label('loc_15AF')

    ChrTalk(
        0x00FE,
        (
            '如果是社会系专业的话，\n',
            '父亲说不定会同意\n',
            '让我去学校念书呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15EF(): pass

    label('loc_15EF')

    Jump('loc_1AA8')

    def _loc_15F2(): pass

    label('loc_15F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_16B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1669',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '嗯～我要找个时间跟父母说一下\n',
            '我想去王立学院念书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过总觉得现在\n',
            '还不是说这件事的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16B0')

    def _loc_1669(): pass

    label('loc_1669')

    ChrTalk(
        0x00FE,
        (
            '如果父母不给我出学费的话，\n',
            '我就上不起学了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是难办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16B0(): pass

    label('loc_16B0')

    Jump('loc_1AA8')

    def _loc_16B3(): pass

    label('loc_16B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_176E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1730',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '昨天这附近\n',
            '发生了强盗事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '母亲好像看到犯人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才军队上来的人\n',
            '一直在询问有关的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176B')

    def _loc_1730(): pass

    label('loc_1730')

    ChrTalk(
        0x00FE,
        (
            '昨天这附近\n',
            '发生了强盗事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '母亲好像看到犯人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_176B(): pass

    label('loc_176B')

    Jump('loc_1AA8')

    def _loc_176E(): pass

    label('loc_176E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17C3',
    )

    ChrTurnDirection(0x0013, 0x0000, 0)

    ChrTalk(
        0x0013,
        (
            '#2440030344V我再问一会儿就结束了，\n',
            '你们要乖乖地等着哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0013, 0, 0)

    Jump('loc_1AA8')

    def _loc_17C3(): pass

    label('loc_17C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1825',
    )

    ChrTalk(
        0x00FE,
        (
            '父亲和母亲\n',
            '在为如今的状况而烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道米拉诺姐姐\n',
            '现在会做出什么样的对策呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA8')

    def _loc_1825(): pass

    label('loc_1825')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1904',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18BE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '失踪飞艇的乘客中\n',
            '好像有特里诺叔叔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他虽然和我家是商业上的竞争对手，\n',
            '不过毕竟是米拉诺姐姐的父亲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真是担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1901')

    def _loc_18BE(): pass

    label('loc_18BE')

    ChrTalk(
        0x00FE,
        (
            '米拉诺姐姐也\n',
            '正在担心叔叔的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能平安就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1901(): pass

    label('loc_1901')

    Jump('loc_1AA8')

    def _loc_1904(): pass

    label('loc_1904')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_19D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '父亲和母亲\n',
            '经常教训我，\n',
            '让我向米拉诺姐姐学习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是我……\n',
            '我并没有成为商人的打算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想去卢安的\n',
            '王立学院学习知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19CD')

    def _loc_199B(): pass

    label('loc_199B')

    ChrTalk(
        0x00FE,
        (
            '毕竟米拉诺姐姐\n',
            '从小就受到商业教育的熏陶…… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19CD(): pass

    label('loc_19CD')

    Jump('loc_1AA8')

    def _loc_19D0(): pass

    label('loc_19D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1AA8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A5A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '我父亲是\n',
            '从事对外贸易工作的商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们家族\n',
            '代代都是从事贸易行业的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是我……\n',
            '可能不适合成为商人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA8')

    def _loc_1A5A(): pass

    label('loc_1A5A')

    ChrTalk(
        0x00FE,
        (
            '我们家族\n',
            '代代都是从事贸易行业的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是我……\n',
            '可能不适合成为商人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AA8(): pass

    label('loc_1AA8')

    TalkEnd(0x000A)

    Return()

# id: 0x000A offset: 0x1AAC
@scena.Code('func_0A_1AAC')
def func_0A_1AAC():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1AD8',
    )

    ChrTalk(
        0x00FE,
        (
            '那么～\n',
            '这次去钓什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1AD8(): pass

    label('loc_1AD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1B4E',
    )

    ChrTalk(
        0x00FE,
        (
            '那家旅馆就在出城后向南走，\n',
            '沿着安塞尔新街走就能看到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为它就坐落在湖边，\n',
            '应该马上就能够看到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1B4E(): pass

    label('loc_1B4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BA0',
    )

    SetScenaFlags(ScenaFlag(0x0065, 5, 0x32D))
    OP_28(0x0037, 0x01, 0x0001)

    ChrTalk(
        0x0012,
        (
            '#2420030341V对不起，请让我们先办完事。\n',
            '去别的地方看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1BA0(): pass

    label('loc_1BA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1CA3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C40',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '男人嘛，不管长多大，\n',
            '仍然会有孩子气的一面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们永远都会追求\n',
            '他们心中的那份浪漫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对女人来说，\n',
            '可能永远也无法理解这种感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CA0')

    def _loc_1C40(): pass

    label('loc_1C40')

    ChrTalk(
        0x00FE,
        (
            '男人嘛，不管长多大，\n',
            '仍然会有孩子气的一面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对女人来说，\n',
            '可能永远也无法理解这种感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CA0(): pass

    label('loc_1CA0')

    Jump('loc_1E83')

    def _loc_1CA3(): pass

    label('loc_1CA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1DA0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D49',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '从柏斯出去往南走\n',
            '就能到达瓦雷利亚湖的北岸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '众所周知，\n',
            '瓦雷利亚湖是位于王国正中央的大湖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '湖里生存着\n',
            '各种各样的鱼类。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D9D')

    def _loc_1D49(): pass

    label('loc_1D49')

    ChrTalk(
        0x00FE,
        (
            '众所周知，\n',
            '瓦雷利亚湖是位于王国正中央的大湖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '湖里生存着\n',
            '各种各样的鱼类。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D9D(): pass

    label('loc_1D9D')

    Jump('loc_1E83')

    def _loc_1DA0(): pass

    label('loc_1DA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1DEE',
    )

    ChrTalk(
        0x00FE,
        (
            '老伴为什么\n',
            '这么容易生气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '血压上升\n',
            '对健康可没什么好处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1DEE(): pass

    label('loc_1DEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1E83',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E6F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '晚年培养一个兴趣\n',
            '是非常重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也不用那么生气吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '生气的话，\n',
            '满是皱纹的脸上会有更多皱纹的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E83')

    def _loc_1E6F(): pass

    label('loc_1E6F')

    ChrTalk(
        0x00FE,
        (
            '哦哦，可怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E83(): pass

    label('loc_1E83')

    TalkEnd(0x000B)

    Return()

# id: 0x000B offset: 0x1E87
@scena.Code('func_0B_1E87')
def func_0B_1E87():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1ED5',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '这几十年光想着怎么钓鱼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么就不觉得腻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_305D')

    def _loc_1ED5(): pass

    label('loc_1ED5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1FA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F71',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '那个人总是在我对他发脾气之后，\n',
            '就出去钓鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我啊，\n',
            '已经让自己好好振作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我看到他毫不在乎地回家，\n',
            '就忍不住发脾气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FA4')

    def _loc_1F71(): pass

    label('loc_1F71')

    ChrTalk(
        0x00FE,
        (
            '算了，反正他钓鱼的同时\n',
            '也在解决我买菜的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FA4(): pass

    label('loc_1FA4')

    Jump('loc_305D')

    def _loc_1FA7(): pass

    label('loc_1FA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_2E24',
    )

    SetScenaFlags(ScenaFlag(0x0067, 2, 0x33A))
    OP_28(0x0037, 0x01, 0x0010)
    OP_28(0x0037, 0x01, 0x0020)
    OP_28(0x0037, 0x01, 0x0040)
    OP_28(0x0037, 0x01, 0x0080)
    OP_28(0x0038, 0x04, 0x02)
    OP_28(0x0038, 0x04, 0x04)
    EventBegin(0x00)
    OP_69(0x00FE, 1000)

    ChrTalk(
        0x00FE,
        (
            '#1200030484V哎哟，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030485V你们不就是\n',
            '刚才来打听事情的游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030486V#000F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030487V刚才真是不好意思，\n',
            '没办法招呼你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030488V看起来，\n',
            '你们也是想打听昨晚的事情吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030489V#010F嗯。\n',
            '您愿意协助我们的调查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030490V啊啊，当然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x00FE, 13)
    SetChrSubChip(0x00FE, 0)
    SetChrFlags(0x00FE, 0x0004)
    SetChrPos(0x00FE, -19910, -150, 1594, 180)
    SetChrPos(0x0101, -18365, 0, 850, 270)
    SetChrPos(0x0102, -18365, 0, -120, 315)
    SetChrPos(0x0103, -20410, 0, -950, 0)
    SetChrPos(0x0104, -19334, 0, -950, 0)
    CameraMove(-19459, 0, 700, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1200030491V就在昨天的深夜，\n',
            '我听到门外好像有什么响声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030492V当时我以为敲门的是老头子。\n',
            '一想到他这个时候才回家，\n',
            '我当然是气冲冲地大力打开门啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030493V结果，我看到的却是\n',
            '一群刚从导力器工房里\n',
            '出来的蒙面男人。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030494V当时我可被他们吓死了，\n',
            '感觉心脏就像要停止似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030495V不过奇怪的是，那群蒙面人比我还害怕。\n',
            '慌慌张张地就往北门那边逃走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030496V#006F原来是这样啊……\n',
            '这么说那些家伙就是空贼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030497V#010F那么，您的屋子\n',
            '有没有受到什么特别的损失呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030498V没有，这算是不幸中的万幸吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030499V#020F可以再问一个问题吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030500V您的丈夫深夜才回家，\n',
            '是因为在酒馆喝醉了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030501V要是他敢的话，\n',
            '我绝对饶不了他！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030502V我家的老头子可不光爱喝酒，\n',
            '最近还迷上这种东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '塞西尔婆婆用右手\n',
            '做了几下上下摆臂的动作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0103, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030030503V#023F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030504V#001F啊，我知道⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030505V就是钓鱼，没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030506V#020F啊啊，原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030507V对！这还不止。\n',
            '为了钓鱼他可以连危险都不顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030508V昨天还为了钓什么胡瓜鱼，\n',
            '在南面的湖畔呆了大半天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030509V到现在还没回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030510V#004F啊，这样的话……\n',
            '那他还不知道昨天的事情吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030511V就是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030512V那老头子也真是的……\n',
            '回来之后我一定要他好看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000B, -19980, 0, -5070, 0)

    NpcTalk(
        0x000B,
        '老人的声音',
        (
            '#1210030513V喂～我回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_268C')
    def lambda_268C():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_268C)

    @scena.Lambda('lambda_269A')
    def lambda_269A():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_269A)

    @scena.Lambda('lambda_26A8')
    def lambda_26A8():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_26A8)

    @scena.Lambda('lambda_26B6')
    def lambda_26B6():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_26B6)

    OP_4A(0x000B, 255)
    SetChrFlags(0x000B, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    PlaySE(6, 0x00, 0x64)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_26E2')
    def lambda_26E2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_26E2)

    ChrWalkTo(0x000B, -20500, 0, -2645, 2000, 0x00)

    @scena.Lambda('lambda_2708')
    def lambda_2708():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2708')

    DispatchAsync2(0x0000, 0x0001, lambda_2708)

    @scena.Lambda('lambda_2719')
    def lambda_2719():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2719')

    DispatchAsync2(0x0001, 0x0001, lambda_2719)

    @scena.Lambda('lambda_272A')
    def lambda_272A():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_272A')

    DispatchAsync2(0x0002, 0x0001, lambda_272A)

    @scena.Lambda('lambda_273B')
    def lambda_273B():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_273B')

    DispatchAsync2(0x0003, 0x0001, lambda_273B)

    ChrTalk(
        0x000B,
        (
            '#1210030514V哈，哎呀哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030515V好不容易等了大半天，\n',
            '没想到最后栽在那些小孩手里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030516V哦？怎么了，今天来了这么多客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_27F0')
    def lambda_27F0():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 1000, 6000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_27F0)

    ChrTalk(
        0x00FE,
        (
            '#1200030517V#5S你这个死老头！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000B,
        (
            '#1210030518V什、什么事？\n',
            '突然冲着我这么大嚷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030519V别在客人面前失礼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030520V失礼的是你才对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030521V真是的，这种紧要关头\n',
            '你还能逍遥自在地到处游山玩水。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030522V啊？紧要关头？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030523V#010F其实是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '众人向库瓦诺老人\n',
            '讲述了昨晚发生的强盗事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrFlags(0x000B, 0x0040)
    SetChrPos(0x000B, -21250, 50, 300, 90)
    SetChrChipByIndex(0x000B, 12)
    SetChrSubChip(0x000B, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#1210030524V什么～空贼来抢劫了吗？\n',
            '这种事真是不得了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030525V不过嘛，一定是老太婆那招杰作——\n',
            '『气冲冲地大力打开门』吓走了那群空贼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030526V哇哈哈，遇到老太婆也算他们倒霉啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1200030527V你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030528V#004F别、别生气啊，老婆婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030529V不过，那些空贼在深夜大肆作乱，\n',
            '然后又突然神秘地消失……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030530V难道他所说的那件事\n',
            '和这案件有关？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030531V#014F他……\n',
            '请问您说的『他』是谁呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030532V啊啊，是我的一个钓友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030533V我那位钓友就在\n',
            '南面湖畔的旅馆落脚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030534V听说他在旅馆附近\n',
            '看到几个奇怪的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030535V#002F奇怪的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030536V#020F挺耐人寻味的嘛。\n',
            '可以详细讲给我们听听吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030537V这没问题……\n',
            '反正我也只是听别人说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030538V我那位钓友是在前天夜钓时\n',
            '偶然看到那些家伙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030539V夜深人静的时候，\n',
            '有几个家伙从旅馆门口走到外面的街道上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030540V不过奇怪的是，\n',
            '旅馆的人都说根本没有这样的客人在留宿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030541V#012F这么说来……\n',
            '的确是很奇怪啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030542V请问那家旅馆\n',
            '有没有发生过强盗事件呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030543V旅馆完全没有出现过\n',
            '像昨天那种骚动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030544V环境清净而且饭菜美味，\n',
            '是一个广受好评的休闲胜地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1210030545V而且还是一处很好的钓鱼场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_305D')

    def _loc_2E24(): pass

    label('loc_2E24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E84',
    )

    SetScenaFlags(ScenaFlag(0x0065, 5, 0x32D))
    OP_28(0x0037, 0x01, 0x0001)
    ChrTurnDirection(0x0012, 0x0000, 0)

    ChrTalk(
        0x0012,
        (
            '#2420030546V对不起，是我们先来的。\n',
            '你们到别的地方看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0012, 315, 0)

    Jump('loc_305D')

    def _loc_2E84(): pass

    label('loc_2E84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_2EE8',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '我为什么会选上那种人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是我人生最大的失败。\n',
            '我真是没用真是没用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_305D')

    def _loc_2EE8(): pass

    label('loc_2EE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_2F34',
    )

    ChrTalk(
        0x00FE,
        (
            '我家老头子说的话\n',
            '最好不要听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正净是一些\n',
            '吹牛皮的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_305D')

    def _loc_2F34(): pass

    label('loc_2F34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_2FB1',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，我家的老头子啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么招呼也没打就出去了，\n',
            '半天也不回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真的是一个没良心不顾家的老头啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_305D')

    def _loc_2FB1(): pass

    label('loc_2FB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_305D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3032',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_62(0x00FE, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哼！\n',
            '我也不会为那种事情生气！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我说过在出门之前\n',
            '至少跟我打声招呼再走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_305D')

    def _loc_3032(): pass

    label('loc_3032')

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '同样的话他准备让我讲多少年？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_305D(): pass

    label('loc_305D')

    TalkEnd(0x000C)

    Return()

# id: 0x000C offset: 0x3061
@scena.Code('func_0C_3061')
def func_0C_3061():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_311F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30DF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '被空贼抓走的老公\n',
            '终于平安回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空之女神爱德丝啊……\n',
            '十分感谢您……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_311C')

    def _loc_30DF(): pass

    label('loc_30DF')

    ChrTalk(
        0x00FE,
        (
            '被空贼抓走的老公\n',
            '终于平安回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_311C(): pass

    label('loc_311C')

    Jump('loc_3665')

    def _loc_311F(): pass

    label('loc_311F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_318D',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然平时总是东奔西走，\n',
            '但是他一不在身边心里总觉得不踏实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '求你了，老公……\n',
            '你快点回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3665')

    def _loc_318D(): pass

    label('loc_318D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_327F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3220',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '幸好我们家没有被殃及。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，这种非常时刻\n',
            '家里没有男人我还是有点不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米拉诺把西蒙带来，\n',
            '真是帮了我的大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_327C')

    def _loc_3220(): pass

    label('loc_3220')

    ChrTalk(
        0x00FE,
        (
            '这种非常时刻\n',
            '家里没有男人我还是有点不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米拉诺把西蒙带来，\n',
            '真是帮了我的大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_327C(): pass

    label('loc_327C')

    Jump('loc_3665')

    def _loc_327F(): pass

    label('loc_327F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_33A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3363',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '博尔德的太太\n',
            '正在协助她老公工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也帮我老公做过事情，\n',
            '但是我总是失败……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，我还是比较适合\n',
            '在家里做老公和米拉诺的后援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……没关系，\n',
            '现在那个人装着什么事\n',
            '都没发生的样子回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33A3')

    def _loc_3363(): pass

    label('loc_3363')

    ChrTalk(
        0x00FE,
        (
            '……没关系，\n',
            '现在那个人装着什么事\n',
            '都没发生的样子回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33A3(): pass

    label('loc_33A3')

    Jump('loc_3665')

    def _loc_33A6(): pass

    label('loc_33A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_3506',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34AF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '老公和米拉诺\n',
            '虽然相处得并不融洽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '我觉得他们只是互相不服输而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '米拉诺毕竟是他的女儿嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在她虽然表面上\n',
            '不情愿地接手了她父亲的工作，\n',
            '不过其实应该是出于同情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于我来说\n',
            '真的要感谢米拉诺才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3503')

    def _loc_34AF(): pass

    label('loc_34AF')

    ChrTalk(
        0x00FE,
        (
            '老公和米拉诺\n',
            '虽然相处得并不融洽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '我觉得他们只是互相不服输而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3503(): pass

    label('loc_3503')

    Jump('loc_3665')

    def _loc_3506(): pass

    label('loc_3506')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_35A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3568',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他乘坐的定期船\n',
            '竟然失踪了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我该怎么办才好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35A5')

    def _loc_3568(): pass

    label('loc_3568')

    ChrTalk(
        0x00FE,
        (
            '他乘坐的定期船\n',
            '竟然失踪了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我该怎么办才好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35A5(): pass

    label('loc_35A5')

    Jump('loc_3665')

    def _loc_35A8(): pass

    label('loc_35A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_3665',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_362E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '好奇怪啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '要是他现在回来就正好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女儿也在家，\n',
            '分开很久的一家人\n',
            '都可以齐聚一堂了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3665')

    def _loc_362E(): pass

    label('loc_362E')

    ChrTalk(
        0x00FE,
        (
            '难道是\n',
            '碰到什么事故了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是让人担心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3665(): pass

    label('loc_3665')

    TalkEnd(0x000D)

    Return()

# id: 0x000D offset: 0x3669
@scena.Code('func_0D_3669')
def func_0D_3669():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_36D3',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～虽然很烦，但是回来了就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果我没有接管这项工作，\n',
            '现在早就应该呆在卢安了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C44')

    def _loc_36D3(): pass

    label('loc_36D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_37B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_377D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '根据梅贝尔小姐所说的来看，\n',
            '定期船失踪很有可能是空贼团做的好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以赎金的数量来看，\n',
            '父亲多半还活着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样母亲也总算\n',
            '能够暂时安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37B0')

    def _loc_377D(): pass

    label('loc_377D')

    ChrTalk(
        0x00FE,
        (
            '你们是来调查\n',
            '这个事件的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜托你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37B0(): pass

    label('loc_37B0')

    Jump('loc_3C44')

    def _loc_37B3(): pass

    label('loc_37B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_389B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3851',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '哼，这次又是强盗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，我搞不明白。\n',
            '柏斯到底是怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……话说回来，\n',
            '居然没盯上我们家，\n',
            '强盗们事先的调查还不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3898')

    def _loc_3851(): pass

    label('loc_3851')

    ChrTalk(
        0x00FE,
        (
            '哼，这次又是强盗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，我搞不明白。\n',
            '柏斯到底是怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3898(): pass

    label('loc_3898')

    Jump('loc_3C44')

    def _loc_389B(): pass

    label('loc_389B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_3992',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3937',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '反过来说……\n',
            '飞艇的停航可能对我更有利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我父亲不在家的时候\n',
            '可以争取到足够的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁这个时候我会\n',
            '尽力处理我父亲的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_398F')

    def _loc_3937(): pass

    label('loc_3937')

    ChrTalk(
        0x00FE,
        (
            '我和我父亲都是\n',
            '从助手开始慢慢学做生意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '父亲的想法\n',
            '我现在大都能够体会得到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_398F(): pass

    label('loc_398F')

    Jump('loc_3C44')

    def _loc_3992(): pass

    label('loc_3992')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_3A8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A3F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '本来想把父亲的工作委任给西蒙的，\n',
            '不过他还差的很远。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是被博尔德大叔\n',
            '占了上风就糟糕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我必须得有一个助手。\n',
            '还是把他叫上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A8A')

    def _loc_3A3F(): pass

    label('loc_3A3F')

    ChrTalk(
        0x00FE,
        (
            '行商最重要就是信用第一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算自己的业绩不好，\n',
            '也不能连累其他人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A8A(): pass

    label('loc_3A8A')

    Jump('loc_3C44')

    def _loc_3A8D(): pass

    label('loc_3A8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_3B59',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B25',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '我的父亲乘坐了\n',
            '那艘失踪的定期船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他预约好的商谈\n',
            '应该怎么处理才好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，应该不会有事的，\n',
            '他一定会好好地活着的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B56')

    def _loc_3B25(): pass

    label('loc_3B25')

    ChrTalk(
        0x00FE,
        (
            '真是的，这个父亲，\n',
            '老是要让母亲为他担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B56(): pass

    label('loc_3B56')

    Jump('loc_3C44')

    def _loc_3B59(): pass

    label('loc_3B59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_3C44',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C01',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '我难得回一次家，\n',
            '老爸竟然不在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我尽早赶回了柏斯，\n',
            '父亲竟然还没有到家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且母亲她很担心呢，\n',
            '总之先到外面打听一下是怎么回事再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C44')

    def _loc_3C01(): pass

    label('loc_3C01')

    ChrTalk(
        0x00FE,
        (
            '我难得回一次家，\n',
            '老爸竟然不在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他明明是个很守时的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C44(): pass

    label('loc_3C44')

    TalkEnd(0x000E)

    Return()

# id: 0x000E offset: 0x3C48
@scena.Code('func_0E_3C48')
def func_0E_3C48():
    If(
        (
            (Expr.Eval, "OP_29(0x0013, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x0013, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0013, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014E)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C6E',
    )

    Call(0, 0x0015)

    Jump('loc_4205')

    def _loc_3C6E(): pass

    label('loc_3C6E')

    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_3D28',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0013, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_3CDB',
    )

    ChrTalk(
        0x00FE,
        (
            '各位，\n',
            '真的是多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空贼也被抓住了，\n',
            '这样我们又可以恢复正常的生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D25')

    def _loc_3CDB(): pass

    label('loc_3CDB')

    ChrTalk(
        0x00FE,
        (
            '闯入我家的蒙面男人们\n',
            '终于被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '被盗走的东西\n',
            '能够追回来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D25(): pass

    label('loc_3D25')

    Jump('loc_4202')

    def _loc_3D28(): pass

    label('loc_3D28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_3DB8',
    )

    ChrTalk(
        0x00FE,
        (
            '那可是枚非常重要的戒指……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '军队也好，游击士也行，\n',
            '总之希望他们能快点把强盗抓住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去，\n',
            '我根本没有办法安心生活……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4202')

    def _loc_3DB8(): pass

    label('loc_3DB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E09',
    )

    ChrTurnDirection(0x0014, 0x0000, 0)

    ChrTalk(
        0x0014,
        (
            '#2450030348V马上就问完了，\n',
            '你们可以不要打断我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0014, 0, 0)

    Jump('loc_4202')

    def _loc_3E09(): pass

    label('loc_3E09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_3F25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3EC8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '昨晚，\n',
            '我刚要哄孩子睡觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '突然有一群蒙面的男人\n',
            '破门而入……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我怕丈夫担心，\n',
            '就没有告诉他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，母亲的……母亲的遗物……\n',
            '一枚戒指被他们抢走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F22')

    def _loc_3EC8(): pass

    label('loc_3EC8')

    ChrTalk(
        0x00FE,
        (
            '我怕丈夫担心\n',
            '就没有告诉他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '母亲的……母亲的遗物……\n',
            '一枚戒指被他们抢走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F22(): pass

    label('loc_3F22')

    Jump('loc_4202')

    def _loc_3F25(): pass

    label('loc_3F25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_3F89',
    )

    ChrTalk(
        0x00FE,
        (
            '我丈夫的工作进展\n',
            '好像比想象中的要顺利得多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近脸上也生气勃勃，\n',
            '这样就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4202')

    def _loc_3F89(): pass

    label('loc_3F89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_40C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_405B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '自从他开始经营商店，\n',
            '在家的时间也增多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然在家的时候\n',
            '他也总是在整理商品\n',
            '或者清查账簿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是总比在军队时\n',
            '每周只回来一次要好得多了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '开店做生意\n',
            '也许不是什么坏事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40BD')

    def _loc_405B(): pass

    label('loc_405B')

    ChrTalk(
        0x00FE,
        (
            '自从他开始经营商店，\n',
            '在家的时间也增多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是总比在军队时\n',
            '每周只回来一次要好得多了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40BD(): pass

    label('loc_40BD')

    Jump('loc_4202')

    def _loc_40C0(): pass

    label('loc_40C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_41CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_415E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '我丈夫辞去了王国军的军官职务，\n',
            '在柏斯超市开了一家店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，我对此事是反对的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少，\n',
            '等孩子长大一点\n',
            '再这样做也不迟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41C7')

    def _loc_415E(): pass

    label('loc_415E')

    ChrTalk(
        0x00FE,
        (
            '我丈夫辞去了王国军的军官职务，\n',
            '在柏斯超市开了一家店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少，\n',
            '等孩子长大一点\n',
            '再这样做也不迟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41C7(): pass

    label('loc_41C7')

    Jump('loc_4202')

    def _loc_41CA(): pass

    label('loc_41CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_4202',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个人的商店\n',
            '是否在顺利营业呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4202(): pass

    label('loc_4202')

    TalkEnd(0x0010)

    def _loc_4205(): pass

    label('loc_4205')

    Return()

# id: 0x000F offset: 0x4206
@scena.Code('func_0F_4206')
def func_0F_4206():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_42A7',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0013, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_425C',
    )

    ChrTalk(
        0x00FE,
        (
            '不知道为什么\n',
            '妈妈好像变得有精神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿，太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42A4')

    def _loc_425C(): pass

    label('loc_425C')

    ChrTalk(
        0x00FE,
        (
            '不知道为什么\n',
            '街上的人们都很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，\n',
            '妈妈却显得很悲伤……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42A4(): pass

    label('loc_42A4')

    Jump('loc_4518')

    def _loc_42A7(): pass

    label('loc_42A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_42EB',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸，就不能早点回来吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '妈妈看上去好难过啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4518')

    def _loc_42EB(): pass

    label('loc_42EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_433C',
    )

    ChrTurnDirection(0x0014, 0x0000, 0)

    ChrTalk(
        0x0014,
        (
            '#2450030348V马上就问完了，\n',
            '你们可以不要打断我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0014, 0, 0)

    Jump('loc_4518')

    def _loc_433C(): pass

    label('loc_433C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_43C3',
    )

    OP_62(0x0011, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有一群不认识的人\n',
            '昨天闯进我家来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我好害怕好害怕，\n',
            '就和妈妈躲在床下面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4518')

    def _loc_43C3(): pass

    label('loc_43C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_4408',
    )

    ChrTalk(
        0x00FE,
        (
            '这次呀，\n',
            '妈妈会带我去爸爸的店里玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我好期待呀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4518')

    def _loc_4408(): pass

    label('loc_4408')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_4474',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸比在军队的时候\n',
            '有更多时间陪我玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我喜欢现在的爸爸。\n',
            '以前呢，他的脸色总是很可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4518')

    def _loc_4474(): pass

    label('loc_4474')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_44C1',
    )

    ChrTalk(
        0x00FE,
        (
            '什么时候我也能\n',
            '帮爸爸做衣服就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想成为爸爸的店员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4518')

    def _loc_44C1(): pass

    label('loc_44C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_4518',
    )

    ChrTalk(
        0x00FE,
        (
            '我爸爸的店里卖的衣服\n',
            '很多都是他自己做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的衣服\n',
            '也是爸爸给我做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4518(): pass

    label('loc_4518')

    TalkEnd(0x0011)

    Return()

# id: 0x0010 offset: 0x451C
@scena.Code('func_10_451C')
def func_10_451C():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_45C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_458C',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '米拉诺有急事\n',
            '去市长官邸找市长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实市长与米拉诺\n',
            '很久以前就是很好的朋友了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45BD')

    def _loc_458C(): pass

    label('loc_458C')

    ChrTalk(
        0x00FE,
        (
            '其实市长与米拉诺\n',
            '很久以前就是很好的朋友了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45BD(): pass

    label('loc_45BD')

    Jump('loc_461C')

    def _loc_45C0(): pass

    label('loc_45C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_461C',
    )

    ChrTalk(
        0x00FE,
        (
            '听说南街区被强盗洗劫，\n',
            '我还真是吓了一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为昨晚\n',
            '只有夫人一个人在家啊。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_461C(): pass

    label('loc_461C')

    TalkEnd(0x000F)

    Return()

# id: 0x0011 offset: 0x4620
@scena.Code('func_11_4620')
def func_11_4620():
    SetScenaFlags(ScenaFlag(0x0065, 5, 0x32D))
    OP_28(0x0037, 0x01, 0x0001)
    TalkBegin(0x0012)

    ChrTalk(
        0x00FE,
        (
            '#2420030340V我正在打听情报。\n',
            '能不能不要妨碍我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x0012 offset: 0x4660
@scena.Code('func_12_4660')
def func_12_4660():
    TalkBegin(0x0013)

    ChrTalk(
        0x00FE,
        (
            '#2440030342V哟，游击士小姐们。\n',
            '你们也是来打听情况的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2440030343V说真的，我们彼此都很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

# id: 0x0013 offset: 0x46C8
@scena.Code('func_13_46C8')
def func_13_46C8():
    TalkBegin(0x0014)

    ChrTalk(
        0x00FE,
        (
            '#2450030345V这个家有件贵重的纪念品\n',
            '被那些家伙们抢走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2450030346V啊呀呀……\n',
            '你们就当作什么都没听到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2450030347V反正你们可以\n',
            '直接去问这家的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0014)

    Return()

# id: 0x0014 offset: 0x4765
@scena.Code('func_14_4765')
def func_14_4765():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_485D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4839',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '终于回到自己的家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前被关在那种\n',
            '又阴暗又肮脏的地方，\n',
            '家的温暖真是让我全身都舒服呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来我的工作\n',
            '都被米拉诺那家伙处理掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～我也要精神十足地投入工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_485D')

    def _loc_4839(): pass

    label('loc_4839')

    ChrTalk(
        0x00FE,
        (
            '好～我也要精神十足地投入工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_485D(): pass

    label('loc_485D')

    TalkEnd(0x0015)

    Return()

# id: 0x0015 offset: 0x4861
@scena.Code('func_15_4861')
def func_15_4861():
    EventBegin(0x00)
    SetChrFlags(0x0010, 0x0010)
    TalkBegin(0x0010)
    ChrTurnDirection(0x0000, 0x0010, 0)
    ChrTurnDirection(0x0001, 0x0010, 0)

    ChrTalk(
        0x0101,
        (
            '#0010151325V#000F请问，您是拉娜小姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#1390151326V是的……我就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1390151327V请问找我有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151328V#000F是这样的，我们发现了一枚\n',
            '与您委托中描述的很相似的戒指。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151329V如果可以的话，\n',
            '请您确认一下好吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#1390151330V啊，真的吗……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '宝石戒指',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0010, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0010)

    ChrTalk(
        0x0010,
        (
            '#1390151331V哎呀…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1390151332V没想到……\n',
            '竟然还可以找回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151333V#010F这个就是您被盗的戒指吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x0010,
        (
            '#1390151334V嗯，就是它没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1390151335V这个戒指是我母亲的遗物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151336V#000F是这样啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151337V……很贵重的物品呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#1390151338V我真的没有想到，\n',
            '竟然还有人\n',
            '能够把它找回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1390151339V我该怎么表达\n',
            '对你们的感激之情呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151340V#001F呵呵，能够帮您取回这枚重要的戒指，\n',
            '我们也都很开心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151341V那么，\n',
            '这样委托就算完成了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1390151342V嗯，\n',
            '多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151343V#010F那么我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151344V#000F再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【被盗的戒指】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x014E, 1)
    OP_28(0x0013, 0x04, 0x10)
    OP_28(0x0013, 0x01, 0x0001)
    EventEnd(0x01)
    ClearChrFlags(0x0010, 0x0010)
    TalkEnd(0x0010)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

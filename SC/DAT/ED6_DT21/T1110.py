import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1110   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '莉咏'),
    TXT(0x02, '阿尔贝尔'),
    TXT(0x03, '博尔德'),
    TXT(0x04, '拉娜'),
    TXT(0x05, '艾尔珂'),
    TXT(0x06, '泊尔'),
    TXT(0x07, '塞西尔婆婆'),
    TXT(0x08, '库瓦诺老人'),
    TXT(0x09, '莫德娜'),
    TXT(0x0A, '米拉诺'),
    TXT(0x0B, '特里诺'),
    TXT(0x0C, '西蒙'),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1110.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0001
    header.entryFunction  = 0x0003
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1110_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3EE9
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01183._CH', 'ED6_DT07/CH01183P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
    ]

# id: 0x10002 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -21340,
            z                   = 0,
            y                   = 72520,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -11200,
            z                   = 5250,
            y                   = 72600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -22100,
            z                   = 0,
            y                   = 69250,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 20970,
            z                   = 0,
            y                   = 67860,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 27100,
            z                   = 4000,
            y                   = 72200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 20100,
            z                   = 0,
            y                   = 68410,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -16400,
            z                   = 0,
            y                   = -1700,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -22530,
            z                   = 0,
            y                   = -410,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -18730,
            z                   = 70,
            y                   = 33060,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 16329,
            z                   = 0,
            y                   = 31480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -21100,
            z                   = 0,
            y                   = 33600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 20200,
            z                   = 0,
            y                   = 30680,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
    )

# id: 0x10003 offset: 0x292
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x292
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x292
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x292
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2A1',
    )

    SetChrFlags(0x0009, 0x0080)

    Jump('loc_3C5')

    def _loc_2A1(): pass

    label('loc_2A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2BA',
    )

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0008, 0x0080)

    Jump('loc_3C5')

    def _loc_2BA(): pass

    label('loc_2BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2F0',
    )

    ClearChrFlags(0x0013, 0x0080)
    CreateThread(0x0013, 0x00, 0x06, 0x0002)
    SetChrFlags(0x000E, 0x0010)
    SetChrPos(0x000E, -22530, 0, 1020, 180)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000F, 0x0010)

    Jump('loc_3C5')

    def _loc_2F0(): pass

    label('loc_2F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_343',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000B, 12900, 0, 69780, 0)
    SetChrPos(0x000C, 22510, 0, 68280, 270)
    ClearChrFlags(0x0013, 0x0080)
    CreateThread(0x0013, 0x00, 0x06, 0x0002)
    SetChrPos(0x000E, -22530, 0, 1020, 180)
    ClearChrFlags(0x000F, 0x0080)

    Jump('loc_3C5')

    def _loc_343(): pass

    label('loc_343')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_3BE',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000B, 12900, 0, 69780, 0)
    SetChrPos(0x000C, 22510, 0, 68280, 270)
    ClearChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0013, 0x0040)
    SetChrFlags(0x0013, 0x0010)
    SetChrFlags(0x0013, 0x0004)
    SetChrChipByIndex(0x0013, 12)
    SetChrPos(0x0013, -20800, 0, 34930, 225)
    SetChrFlags(0x0011, 0x0010)
    SetChrPos(0x0011, -21830, 0, 35100, 90)

    Jump('loc_3C5')

    def _loc_3BE(): pass

    label('loc_3BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_3C5',
    )

    def _loc_3C5(): pass

    label('loc_3C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3CF',
    )

    Jump('loc_3E6')

    def _loc_3CF(): pass

    label('loc_3CF')

    If(
        (
            (Expr.Eval, "OP_29(0x007C, 0x01, 0x0002)"),
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3E6',
    )

    SetChrFlags(0x0011, 0x0080)

    def _loc_3E6(): pass

    label('loc_3E6')

    Return()

# id: 0x0001 offset: 0x3E7
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x3E8
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_41A',
    )

    def _loc_3F4(): pass

    label('loc_3F4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_417',
    )

    OP_8D(0x00FE, 20900, 30000, 15300, 31700, 2000)

    Jump('loc_3F4')

    def _loc_417(): pass

    label('loc_417')

    Jump('loc_41E')

    def _loc_41A(): pass

    label('loc_41A')

    Call(6, 0x0002)
    def _loc_41E(): pass

    label('loc_41E')

    Return()

# id: 0x0003 offset: 0x41F
@scena.Code('func_03_41F')
def func_03_41F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_451',
    )

    def _loc_42B(): pass

    label('loc_42B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_44E',
    )

    OP_8D(0x00FE, 21600, 67480, 22890, 69030, 2000)

    Jump('loc_42B')

    def _loc_44E(): pass

    label('loc_44E')

    Jump('loc_474')

    def _loc_451(): pass

    label('loc_451')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_474',
    )

    OP_8D(0x00FE, 26200, 71400, 28400, 72600, 2000)

    Jump('loc_451')

    def _loc_474(): pass

    label('loc_474')

    Return()

# id: 0x0004 offset: 0x475
@scena.Code('func_04_475')
def func_04_475():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4A7',
    )

    def _loc_481(): pass

    label('loc_481')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4A4',
    )

    OP_8D(0x00FE, 12210, 70500, 14370, 68720, 1500)

    Jump('loc_481')

    def _loc_4A4(): pass

    label('loc_4A4')

    Jump('loc_4CA')

    def _loc_4A7(): pass

    label('loc_4A7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4CA',
    )

    OP_8D(0x00FE, 17430, 68790, 23880, 64870, 1500)

    Jump('loc_4A7')

    def _loc_4CA(): pass

    label('loc_4CA')

    Return()

# id: 0x0005 offset: 0x4CB
@scena.Code('func_05_4CB')
def func_05_4CB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_567',
    )

    OP_8E(0x00FE, -22800, 0, 72500, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    Sleep(3000)

    OP_8E(0x00FE, -21620, 0, 72500, 2000, 0x00)
    OP_8E(0x00FE, -21020, 0, 72800, 2000, 0x00)
    OP_8E(0x00FE, -20800, 0, 72800, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    Sleep(3000)

    OP_8E(0x00FE, -21020, 0, 72800, 2000, 0x00)
    OP_8E(0x00FE, -21620, 0, 72500, 2000, 0x00)

    Jump('func_05_4CB')

    def _loc_567(): pass

    label('loc_567')

    Return()

# id: 0x0006 offset: 0x568
@scena.Code('func_06_568')
def func_06_568():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_68F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_632',
    )

    ChrTalk(
        0x00FE,
        (
            '从大局来考虑的话，\n',
            '老公的分析是正确的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是对市民来说，\n',
            '首先要考虑的还是生活问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像国际形势之类的问题\n',
            '大概没人会顾得了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许正因如此\n',
            '才会这么恐怖吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_68C')

    def _loc_632(): pass

    label('loc_632')

    ChrTalk(
        0x00FE,
        (
            '现在是最严重的是\n',
            '市民的照明和供暖问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '国际形势什么的，\n',
            '现在不是考虑的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_68C(): pass

    label('loc_68C')

    Jump('loc_ABE')

    def _loc_68F(): pass

    label('loc_68F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_75A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_70B',
    )

    ChrTalk(
        0x00FE,
        (
            '我家的导力器也全部\n',
            '停止运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我儿子阿尔贝尔\n',
            '虽然去了工房，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但似乎工房也不能\n',
            '修理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_757')

    def _loc_70B(): pass

    label('loc_70B')

    ChrTalk(
        0x00FE,
        (
            '我家的导力器也全部\n',
            '停止运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是修不好的话\n',
            '那可就真麻烦了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_757(): pass

    label('loc_757')

    Jump('loc_ABE')

    def _loc_75A(): pass

    label('loc_75A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_764',
    )

    Jump('loc_ABE')

    def _loc_764(): pass

    label('loc_764')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_86D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7C3',
    )

    ChrTalk(
        0x00FE,
        (
            '米拉诺现在\n',
            '真像个商人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望我家的阿尔贝尔\n',
            '也能变成像她那样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86A')

    def _loc_7C3(): pass

    label('loc_7C3')

    ChrTalk(
        0x00FE,
        (
            '米拉诺现在\n',
            '真像个商人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望我家的阿尔贝尔\n',
            '也能变成像她那样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，我相信他是大器晚成，\n',
            '以后一定会有出息的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以才会让他去\n',
            '王立学院进修。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_86A(): pass

    label('loc_86A')

    Jump('loc_ABE')

    def _loc_86D(): pass

    label('loc_86D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_93C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8C3',
    )

    ChrTalk(
        0x00FE,
        (
            '我们也都是从露天市场\n',
            '起家的商人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去支援也是自己的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_939')

    def _loc_8C3(): pass

    label('loc_8C3')

    ChrTalk(
        0x00FE,
        (
            '和特里诺家协力\n',
            '进行超市修复工作\n',
            '的支援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也都是从露天市场\n',
            '起家的商人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去支援也是自己的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_939(): pass

    label('loc_939')

    Jump('loc_ABE')

    def _loc_93C(): pass

    label('loc_93C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_98C',
    )

    ChrTalk(
        0x00FE,
        (
            '超市似乎\n',
            '发生了不得了的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老公慌慌张张地就\n',
            '跑出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ABE')

    def _loc_98C(): pass

    label('loc_98C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_ABE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9FD',
    )

    ChrTalk(
        0x00FE,
        (
            '博尔德家和特里诺家\n',
            '都是柏斯的著名商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然关系还算不错，\n',
            '但也是竞争激烈的商业劲敌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ABE')

    def _loc_9FD(): pass

    label('loc_9FD')

    ChrTalk(
        0x00FE,
        (
            '博尔德家和特里诺家\n',
            '都是柏斯的著名商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然关系还算不错，\n',
            '但也是竞争激烈的商业劲敌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近我们\n',
            '一直比较支持特里诺，不过…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为和帝国开展贸易，\n',
            '博尔德似乎开始扭转局面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_ABE(): pass

    label('loc_ABE')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0xAC2
@scena.Code('func_07_AC2')
def func_07_AC2():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_BA3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_B20',
    )

    ChrTalk(
        0x00FE,
        (
            '马上要开始真正的\n',
            '考前冲刺了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然信心十足，\n',
            '但还是很紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BA0')

    def _loc_B20(): pass

    label('loc_B20')

    ChrTalk(
        0x00FE,
        (
            '城里好像又\n',
            '恢复了活力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，我也开始努力\n',
            '准备考试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '父母对我抱有那么大期望，\n',
            '要是考砸的话，就太丢脸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_BA0(): pass

    label('loc_BA0')

    Jump('loc_F68')

    def _loc_BA3(): pass

    label('loc_BA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_CD9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_C12',
    )

    ChrTalk(
        0x00FE,
        (
            '总被拿来和米拉诺姐姐比较，\n',
            '也很令人头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟人和人是不一样的，\n',
            '怎么能比来比去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD6')

    def _loc_C12(): pass

    label('loc_C12')

    ChrTalk(
        0x00FE,
        (
            '虽然米拉诺姐姐\n',
            '确实很了不起…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但总让我和她比也有点…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我和姐姐\n',
            '完全是不同类型的两种人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果说我是性格内向话，\n',
            '那米拉诺姐姐就是外向性格的人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……感觉就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_CD6(): pass

    label('loc_CD6')

    Jump('loc_F68')

    def _loc_CD9(): pass

    label('loc_CD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_E01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_D4C',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天爸爸和特里诺先生\n',
            '一直在商谈支援什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏他们的决定，所以今天\n',
            '就开始修复工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DFE')

    def _loc_D4C(): pass

    label('loc_D4C')

    ChrTalk(
        0x00FE,
        (
            '昨天爸爸和特里诺先生\n',
            '一直在商谈支援什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏他们的决定，所以今天\n',
            '就开始修复工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看见这些，\n',
            '我忽然觉得商人其实也不坏…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过我还是当不了那种人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_DFE(): pass

    label('loc_DFE')

    Jump('loc_F68')

    def _loc_E01(): pass

    label('loc_E01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_E6D',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才爸爸他们\n',
            '惊慌地跑出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我爸爸很少\n',
            '会那么惊慌失措的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道发生什么大事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F68')

    def _loc_E6D(): pass

    label('loc_E6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_F68',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_EC3',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然爸爸希望我以后\n',
            '也成为商人…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但我自己却并没有那种打算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F68')

    def _loc_EC3(): pass

    label('loc_EC3')

    ChrTalk(
        0x00FE,
        (
            '我的父母希望我学习经济，\n',
            '所以让我进了\n',
            '王立学院读书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然爸爸希望我以后\n',
            '也成为商人…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但我自己却并没有那种打算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然如此，\n',
            '但我却并没有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_F68(): pass

    label('loc_F68')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0xF6C
@scena.Code('func_08_F6C')
def func_08_F6C():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_10A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_104E',
    )

    ChrTalk(
        0x00FE,
        (
            '现在很担心照明和供暖\n',
            '的问题啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国内出现这种状况，\n',
            '会有国际性的影响啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从军事方面说，利贝尔王国\n',
            '要是没有了飞行舰队那可是天大的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是以前的帝国的话，\n',
            '肯定马上就会攻来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_10A4')

    def _loc_104E(): pass

    label('loc_104E')

    ChrTalk(
        0x00FE,
        (
            '这次导力停止现象有着\n',
            '国际性的影响力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算只是照明和供暖问题\n',
            '也够我们受了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10A4(): pass

    label('loc_10A4')

    Jump('loc_16CE')

    def _loc_10A7(): pass

    label('loc_10A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_11E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_117E',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器不能使用…\n',
            '真是麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对利贝尔王国来说，\n',
            '导力器就等同于我们的生命线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果失去机能的话，\n',
            '会影响到无数事情的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……呼，总之要做好准备了，\n',
            '这次可不是能轻松解决的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_11E0')

    def _loc_117E(): pass

    label('loc_117E')

    ChrTalk(
        0x00FE,
        (
            '对利贝尔王国来说，\n',
            '导力器就等同于我们的生命线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果失去机能的话，\n',
            '会影响到无数事情的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11E0(): pass

    label('loc_11E0')

    Jump('loc_16CE')

    def _loc_11E3(): pass

    label('loc_11E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1318',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1264',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船刚恢复航运，\n',
            '和帝国的交易也再次开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是遗憾，没有获得\n',
            '预期的成果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次真是遗憾啊，。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1315')

    def _loc_1264(): pass

    label('loc_1264')

    ChrTalk(
        0x00FE,
        (
            '定期船刚恢复航运，\n',
            '和帝国的交易也再次开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是遗憾，没有获得\n',
            '预期的成果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '全是因为\n',
            '米拉诺小姐的努力才会如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，又多了一个\n',
            '令人头疼的竞争对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1315(): pass

    label('loc_1315')

    Jump('loc_16CE')

    def _loc_1318(): pass

    label('loc_1318')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_149C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1385',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船的停运\n',
            '也不能阻止米拉诺小姐的斗志啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，我也要仔细\n',
            '思考一下对应策略了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1499')

    def _loc_1385(): pass

    label('loc_1385')

    ChrTalk(
        0x00FE,
        (
            '定期船停运这件事\n',
            '对我来说，的确是件棘手的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和帝国的交易量正呈现增加趋势，\n',
            '就在这节骨眼上发生这样的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我和特里诺为了超市\n',
            '的支持工作一直忙个不停。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特里诺有个叫米拉诺的女儿。\n',
            '也许她会帮上些什么忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有个那么有出息的女儿，\n',
            '实在太让人羡慕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1499(): pass

    label('loc_1499')

    Jump('loc_16CE')

    def _loc_149C(): pass

    label('loc_149C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1599',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_14F3',
    )

    ChrTalk(
        0x00FE,
        (
            '修复工事马上\n',
            '就要开始了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '追加支援的资金\n',
            '也要赶快落实啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1596')

    def _loc_14F3(): pass

    label('loc_14F3')

    ChrTalk(
        0x00FE,
        (
            '修复工事马上\n',
            '就要开始了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所需要的材料\n',
            '我和特里诺已经提供了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过真正动工以后\n',
            '肯定马上又会不够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '追加支援的资金\n',
            '必须要好好思考一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1596(): pass

    label('loc_1596')

    Jump('loc_16CE')

    def _loc_1599(): pass

    label('loc_1599')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_16CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1638',
    )

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约也签定了，\n',
            '和帝国之间的交易更加宽松了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去的话，\n',
            '最近在生意上感觉落后特里诺不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁这个机会可以挽回局面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16CE')

    def _loc_1638(): pass

    label('loc_1638')

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约签署之后，\n',
            '和帝国之间的交易更加宽松了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我已经和帝国方面\n',
            '做了很长一段时间的生意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁这个机会，\n',
            '希望可以拓展业务规模。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_16CE(): pass

    label('loc_16CE')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x16D2
@scena.Code('func_09_16D2')
def func_09_16D2():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_178E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1749',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才去过了附近\n',
            '的工房，不过…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '场面非常混乱，\n',
            '只能回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎哪家都\n',
            '很困惑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_178B')

    def _loc_1749(): pass

    label('loc_1749')

    ChrTalk(
        0x00FE,
        (
            '因为工房那里很混乱，\n',
            '只能回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎哪家都\n',
            '很困惑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_178B(): pass

    label('loc_178B')

    Jump('loc_1BA7')

    def _loc_178E(): pass

    label('loc_178E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_18A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1843',
    )

    ChrTalk(
        0x00FE,
        (
            '照明设施没有了，\n',
            '一到晚上就什么也看不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '慌慌张张地去找油灯\n',
            '还真是好辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为怕黑，\n',
            '女儿一直哭个不停…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望能\n',
            '早点恢复原来的生活啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_18A1')

    def _loc_1843(): pass

    label('loc_1843')

    ChrTalk(
        0x00FE,
        (
            '照明设施没有了，\n',
            '一到晚上就什么也看不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器会瘫痪这种事，\n',
            '以前连想都没有想过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18A1(): pass

    label('loc_18A1')

    Jump('loc_1BA7')

    def _loc_18A4(): pass

    label('loc_18A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_195C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_18F5',
    )

    ChrTalk(
        0x00FE,
        (
            '老公今天带着\n',
            '女儿去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很想看看重新\n',
            '营业的超市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1959')

    def _loc_18F5(): pass

    label('loc_18F5')

    ChrTalk(
        0x00FE,
        (
            '老公今天带着\n',
            '女儿去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很想看看重新\n',
            '营业的超市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还好没给周围的店\n',
            '添麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1959(): pass

    label('loc_1959')

    Jump('loc_1BA7')

    def _loc_195C(): pass

    label('loc_195C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_19E4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1990',
    )

    ChrTalk(
        0x00FE,
        (
            '老公去北街区\n',
            '查看修复工事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19E1')

    def _loc_1990(): pass

    label('loc_1990')

    ChrTalk(
        0x00FE,
        (
            '老公去北街区\n',
            '查看修复工事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我丈夫真是\n',
            '对商业买卖很有兴趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_19E1(): pass

    label('loc_19E1')

    Jump('loc_1BA7')

    def _loc_19E4(): pass

    label('loc_19E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1A45',
    )

    ChrTalk(
        0x00FE,
        (
            '和他在一起这么长时间…\n',
            '真是好久没有这样过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，简直就像回到了恋人时代。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA7')

    def _loc_1A45(): pass

    label('loc_1A45')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1A97',
    )

    ChrTalk(
        0x00FE,
        (
            '超市竟然被\n',
            '怪物袭击了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……和平的日子\n',
            '为什么一去不复返了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA7')

    def _loc_1A97(): pass

    label('loc_1A97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1BA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1AED',
    )

    ChrTalk(
        0x00FE,
        (
            '我老公在超市\n',
            '经营服装店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是家名叫『泊尔·艾尔珂』的店哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA7')

    def _loc_1AED(): pass

    label('loc_1AED')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '啊～都是很不错的和服呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我老公在超市\n',
            '经营服装店哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '追求流行的话，\n',
            '那里的服装一定可以满足你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有兴趣的话\n',
            '请一定去光顾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1BA7(): pass

    label('loc_1BA7')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x1BAB
@scena.Code('func_0A_1BAB')
def func_0A_1BAB():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1C2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C0D',
    )

    ChrTalk(
        0x00FE,
        (
            '导力工房里\n',
            '全都是客人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸的店里\n',
            '要是也有那么多客人就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_1C2C')

    def _loc_1C0D(): pass

    label('loc_1C0D')

    ChrTalk(
        0x00FE,
        (
            '导力工房里\n',
            '全都是客人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C2C(): pass

    label('loc_1C2C')

    Jump('loc_1EE3')

    def _loc_1C2F(): pass

    label('loc_1C2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1CFC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CB1',
    )

    ChrTalk(
        0x00FE,
        (
            '家里一片漆黑，\n',
            '真是好可怕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力炉也不能用了，\n',
            '冷得要命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～\n',
            '为什么导力器都不能用了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_1CF9')

    def _loc_1CB1(): pass

    label('loc_1CB1')

    ChrTalk(
        0x00FE,
        (
            '家里一片漆黑，\n',
            '真是好可怕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～\n',
            '为什么导力器都不能用了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CF9(): pass

    label('loc_1CF9')

    Jump('loc_1EE3')

    def _loc_1CFC(): pass

    label('loc_1CFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1D73',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1D30',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸出去了，\n',
            '今天我留下看家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D70')

    def _loc_1D30(): pass

    label('loc_1D30')

    ChrTalk(
        0x00FE,
        (
            '爸爸出去了，\n',
            '今天我留下看家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～～好没意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1D70(): pass

    label('loc_1D70')

    Jump('loc_1EE3')

    def _loc_1D73(): pass

    label('loc_1D73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1E07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1DBA',
    )

    ChrTalk(
        0x00FE,
        (
            '超市真的\n',
            '好大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '是谁把它弄坏的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E04')

    def _loc_1DBA(): pass

    label('loc_1DBA')

    ChrTalk(
        0x00FE,
        (
            '超市被破坏了，\n',
            '所以爸爸也不用工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……是谁把它弄坏的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1E04(): pass

    label('loc_1E04')

    Jump('loc_1EE3')

    def _loc_1E07(): pass

    label('loc_1E07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1E72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1E33',
    )

    ChrTalk(
        0x00FE,
        (
            '今天爸爸\n',
            '会早回来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E6F')

    def _loc_1E33(): pass

    label('loc_1E33')

    ChrTalk(
        0x00FE,
        (
            '今天爸爸\n',
            '会早回来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿～要让他陪我一起玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1E6F(): pass

    label('loc_1E6F')

    Jump('loc_1EE3')

    def _loc_1E72(): pass

    label('loc_1E72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1EE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1EA0',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸在超市里\n',
            '卖洋装哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EE3')

    def _loc_1EA0(): pass

    label('loc_1EA0')

    ChrTalk(
        0x00FE,
        (
            '爸爸在超市里\n',
            '卖洋装哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我以后也想\n',
            '到爸爸的店里帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1EE3(): pass

    label('loc_1EE3')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x1EE7
@scena.Code('func_0B_1EE7')
def func_0B_1EE7():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2003',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1F5B',
    )

    ChrTalk(
        0x00FE,
        (
            '这也许是女神的意思吧，\n',
            '那么暂时就先停业好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一边照顾女儿，\n',
            '一边等着超市重新开门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2000')

    def _loc_1F5B(): pass

    label('loc_1F5B')

    ChrTalk(
        0x00FE,
        (
            '其他的商人都在\n',
            '找其它的地方继续营业。\n',
            '但我却准备暂时休息一阵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '服饰和日用品不同，\n',
            '偶尔停业也没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也许是女神的意思吧，\n',
            '还是好好休息一阵子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_2000(): pass

    label('loc_2000')

    Jump('loc_21A6')

    def _loc_2003(): pass

    label('loc_2003')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_21A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0348, 4, 0x1A44)),
            Expr.Return,
        ),
        'loc_2062',
    )

    ChrTalk(
        0x00FE,
        (
            '所幸客人们\n',
            '也顺利避难了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长的女佣小姐要是\n',
            '也能早点恢复就好了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21A6')

    def _loc_2062(): pass

    label('loc_2062')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊、你们……\n',
            '在超市时真是多谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不是你们的话\n',
            '也许就无法得救了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一定是女神\n',
            '的保佑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F嗯……\n',
            '能赶上真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1002F超市的各位\n',
            '已经平安避难了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，托你们的福，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都已经逃离了。\n',
            '现在暂时待在旅店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长的女佣小姐要是\n',
            '也能早点恢复就好了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A44)

    def _loc_21A6(): pass

    label('loc_21A6')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x21AA
@scena.Code('func_0C_21AA')
def func_0C_21AA():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2288',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_222D',
    )

    ChrTalk(
        0x00FE,
        (
            '老头子他去工房\n',
            '还没回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定又是去哪里\n',
            '偷懒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是再去钓鱼的话，\n',
            '这次就不让他进家门了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    Jump('loc_2285')

    def _loc_222D(): pass

    label('loc_222D')

    ChrTalk(
        0x00FE,
        (
            '明明都答应过不再去了，\n',
            '但又给忘掉了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，老头子他\n',
            '一天到晚什么都不干。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2285(): pass

    label('loc_2285')

    Jump('loc_298D')

    def _loc_2288(): pass

    label('loc_2288')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2373',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_231C',
    )

    ChrTalk(
        0x00FE,
        (
            '隔壁的特里诺家的导力器\n',
            '好象也出现故障了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像哪里都是\n',
            '这个样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还以为他老老实实在家，\n',
            '但老头子竟然去工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    Jump('loc_2370')

    def _loc_231C(): pass

    label('loc_231C')

    ChrTalk(
        0x00FE,
        (
            '本以为是导力器的故障，\n',
            '但老头子竟然去工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，\n',
            '应该马上就回来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2370(): pass

    label('loc_2370')

    Jump('loc_298D')

    def _loc_2373(): pass

    label('loc_2373')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_273C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0386, 3, 0x1C33)),
            Expr.Return,
        ),
        'loc_2420',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_23C9',
    )

    ChrTalk(
        0x00FE,
        (
            '钓杆的事\n',
            '不用在意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对老头子来说\n',
            '这样才是为他好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_241D')

    def _loc_23C9(): pass

    label('loc_23C9')

    ChrTalk(
        0x00FE,
        (
            '啊，是你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个钓杆\n',
            '随你们处置吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对老头子来说\n',
            '这样才是为他好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_241D(): pass

    label('loc_241D')

    Jump('loc_2739')

    def _loc_2420(): pass

    label('loc_2420')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2484',
    )

    ChrTalk(
        0x00FE,
        (
            '刚还在想去买东西，\n',
            '这才发现老头子不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是看见他的话，\n',
            '麻烦告诉我一声好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2739')

    def _loc_2484(): pass

    label('loc_2484')

    ChrTalk(
        0x00FE,
        (
            '哎呀，真是已经没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚还在想去买东西，\n',
            '这才发现老头子不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来得用绳子\n',
            '把他给绑住才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是看见他的话，\n',
            '麻烦告诉我一声好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0386, 2, 0x1C32)),
            (Expr.TestScenaFlags, ScenaFlag(0x0386, 3, 0x1C33)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2736',
    )

    ChrTalk(
        0x0101,
        (
            '#1011F啊，如果说是老爷爷的话，\n',
            '我在『川蝉亭』见到过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '什么？\n',
            '真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯、嗯……\n',
            '似乎是去钓鱼的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～果然啊，\n',
            '和我想的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谢谢你们。\n',
            '帮了我大忙啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，把这个拿去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['湖泊大帝Ⅱ世']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['湖泊大帝Ⅱ世'], 1)

    ChrTalk(
        0x0101,
        (
            '#1004F这、这是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是老头子珍藏的钓杆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经不想再把它\n',
            '留在家里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不用介意，拿走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1016F可、可是～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没关系啦，拿走吧。\n',
            '这样对老头子也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)
    OP_A2(0x1C33)

    def _loc_2736(): pass

    label('loc_2736')

    OP_A2(0x0006)

    def _loc_2739(): pass

    label('loc_2739')

    Jump('loc_298D')

    def _loc_273C(): pass

    label('loc_273C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_27D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2786',
    )

    ChrTalk(
        0x00FE,
        (
            '不然他除了钓鱼\n',
            '什么都不做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经拿他没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27CF')

    def _loc_2786(): pass

    label('loc_2786')

    ChrTalk(
        0x00FE,
        (
            '为什么我们非要去\n',
            '湖边小屋啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '钓鱼什么的\n',
            '一点兴趣也没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_27CF(): pass

    label('loc_27CF')

    Jump('loc_298D')

    def _loc_27D2(): pass

    label('loc_27D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2868',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_281A',
    )

    ChrTalk(
        0x00FE,
        (
            '老头子好像完全不\n',
            '清楚事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是那么悠闲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2865')

    def _loc_281A(): pass

    label('loc_281A')

    ChrTalk(
        0x00FE,
        (
            '老头子好像完全不\n',
            '清楚事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还那么担心他，\n',
            '简直就是笨蛋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_2865(): pass

    label('loc_2865')

    Jump('loc_298D')

    def _loc_2868(): pass

    label('loc_2868')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_292B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_28C9',
    )

    ChrTalk(
        0x00FE,
        (
            '老头子他就是个一根经，\n',
            '只知道钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，这样的人生\n',
            '还真是轻松啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2928')

    def _loc_28C9(): pass

    label('loc_28C9')

    ChrTalk(
        0x00FE,
        (
            '明明都发生了\n',
            '那么重大的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老头子他就是那种\n',
            '只知道钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一根经的性格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_2928(): pass

    label('loc_2928')

    Jump('loc_298D')

    def _loc_292B(): pass

    label('loc_292B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_298D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2955',
    )

    ChrTalk(
        0x00FE,
        (
            '老头子\n',
            '又去钓鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_298D')

    def _loc_2955(): pass

    label('loc_2955')

    ChrTalk(
        0x00FE,
        (
            '老头子\n',
            '又去钓鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这可以算是一种病了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_298D(): pass

    label('loc_298D')

    TalkEnd(0x000E)

    Return()

# id: 0x000D offset: 0x2991
@scena.Code('func_0D_2991')
def func_0D_2991():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2A40',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_29DE',
    )

    ChrTalk(
        0x00FE,
        (
            '『川蝉亭』真是个好地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '婆婆一定\n',
            '也很喜欢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3D')

    def _loc_29DE(): pass

    label('loc_29DE')

    ChrTalk(
        0x00FE,
        (
            '啊，婆婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不如两个人\n',
            '一起去『川蝉亭』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偶尔扔下家事，\n',
            '休息一下也不错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_2A3D(): pass

    label('loc_2A3D')

    Jump('loc_2AA3')

    def _loc_2A40(): pass

    label('loc_2A40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2AA3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2A68',
    )

    ChrTalk(
        0x00FE,
        (
            '超市究竟\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AA3')

    def _loc_2A68(): pass

    label('loc_2A68')

    ChrTalk(
        0x00FE,
        (
            '超市究竟\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我才刚回来，\n',
            '什么都不知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_2AA3(): pass

    label('loc_2AA3')

    TalkEnd(0x000F)

    Return()

# id: 0x000E offset: 0x2AA7
@scena.Code('func_0E_2AA7')
def func_0E_2AA7():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2B74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B15',
    )

    ChrTalk(
        0x00FE,
        (
            '利贝尔国内的流通网\n',
            '几乎已经全部瘫痪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '商品的安排全乱了，\n',
            '大家都忙得要死。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_2B71')

    def _loc_2B15(): pass

    label('loc_2B15')

    ChrTalk(
        0x00FE,
        (
            '利贝尔国内的流通网\n',
            '几乎已经全部瘫痪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想想日用品和食品的事，\n',
            '就让人很不安呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B71(): pass

    label('loc_2B71')

    Jump('loc_2F8D')

    def _loc_2B74(): pass

    label('loc_2B74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2C43',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BFC',
    )

    ChrTalk(
        0x00FE,
        (
            '城里的导力器好像已经\n',
            '全部瘫痪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且原因\n',
            '好像还是未知…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出现这样的骚乱，大家的心情\n',
            '我也可以理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_2C40')

    def _loc_2BFC(): pass

    label('loc_2BFC')

    ChrTalk(
        0x00FE,
        (
            '城里的导力器好像已经\n',
            '全部瘫痪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且原因\n',
            '好像还是未知…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C40(): pass

    label('loc_2C40')

    Jump('loc_2F8D')

    def _loc_2C43(): pass

    label('loc_2C43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2C96',
    )

    ChrTalk(
        0x00FE,
        (
            '今天准备去超市\n',
            '买东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总算是重新\n',
            '开始营业了，\n',
            '去买些东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F8D')

    def _loc_2C96(): pass

    label('loc_2C96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2D76',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2CF3',
    )

    ChrTalk(
        0x00FE,
        (
            '我们的人为了超市的复兴\n',
            '一直努力忙碌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过米拉诺已经\n',
            '完成了代理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D73')

    def _loc_2CF3(): pass

    label('loc_2CF3')

    ChrTalk(
        0x00FE,
        (
            '我们的人为了超市的复兴\n',
            '一直努力忙碌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过米拉诺已经\n',
            '完成了代理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前和博尔德一家可是\n',
            '一直处于对立地位的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_2D73(): pass

    label('loc_2D73')

    Jump('loc_2F8D')

    def _loc_2D76(): pass

    label('loc_2D76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2E70',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2DD9',
    )

    ChrTalk(
        0x00FE,
        (
            '我们的人和博尔德大叔\n',
            '正在协力做支援工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这就是\n',
            '柏斯商人的可贵之处了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E6D')

    def _loc_2DD9(): pass

    label('loc_2DD9')

    ChrTalk(
        0x00FE,
        (
            '我们的人和博尔德大叔\n',
            '正在协力做支援工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要是值得尊敬的人，\n',
            '即使是商业对手也可以协力合作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，这就是\n',
            '柏斯商人的可贵之处了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_2E6D(): pass

    label('loc_2E6D')

    Jump('loc_2F8D')

    def _loc_2E70(): pass

    label('loc_2E70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2F38',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2ECD',
    )

    ChrTalk(
        0x00FE,
        (
            '西蒙也在超市\n',
            '不幸受伤了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过只是轻伤而已，\n',
            '算是不幸中的万幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F35')

    def _loc_2ECD(): pass

    label('loc_2ECD')

    ChrTalk(
        0x00FE,
        (
            '西蒙也在超市\n',
            '不幸受伤了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然只是轻伤，但似乎\n',
            '还有人被压在瓦砾下了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是可怕啊… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_2F35(): pass

    label('loc_2F35')

    Jump('loc_2F8D')

    def _loc_2F38(): pass

    label('loc_2F38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2F8D',
    )

    ChrTalk(
        0x00FE,
        (
            '柏斯商人们的视线\n',
            '现在全都在帝国那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为此大家也都\n',
            '在拼命努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F8D(): pass

    label('loc_2F8D')

    TalkEnd(0x0010)

    Return()

# id: 0x000F offset: 0x2F91
@scena.Code('func_0F_2F91')
def func_0F_2F91():
    TalkBegin(0x0011)

    If(
        (
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FC7',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007C, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_2FC0',
    )

    Call(1, 0x0001)

    Jump('loc_2FC4')

    def _loc_2FC0(): pass

    label('loc_2FC0')

    Call(1, 0x0000)

    def _loc_2FC4(): pass

    label('loc_2FC4')

    Jump('loc_366E')

    def _loc_2FC7(): pass

    label('loc_2FC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_30C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3063',
    )

    ChrTalk(
        0x00FE,
        (
            '就算找到了替代的输送管道，\n',
            '接下来也会困难重重吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一会也只有去仓库\n',
            '使用人海战术运货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '西蒙要是回来的话\n',
            '就让他帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_30C5')

    def _loc_3063(): pass

    label('loc_3063')

    ChrTalk(
        0x00FE,
        (
            '就算找到了替代的输送管道，\n',
            '接下来也会困难重重吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一会也只有去仓库\n',
            '使用人海战术运货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30C5(): pass

    label('loc_30C5')

    Jump('loc_366E')

    def _loc_30C8(): pass

    label('loc_30C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_319F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_315A',
    )

    ChrTalk(
        0x00FE,
        (
            '城里出现奇怪现象，\n',
            '好象又是定期船事件…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老实说，\n',
            '我有种不好的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去的话，\n',
            '恐怕还会发生不得了的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_319C')

    def _loc_315A(): pass

    label('loc_315A')

    ChrTalk(
        0x00FE,
        (
            '呼，还有在空中出现\n',
            '的浮游岛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总让人有种\n',
            '不祥的预感呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_319C(): pass

    label('loc_319C')

    Jump('loc_366E')

    def _loc_319F(): pass

    label('loc_319F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_3299',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_3210',
    )

    ChrTalk(
        0x00FE,
        (
            '如我所想，飞船已经恢复了，\n',
            '和帝国商人的合作也大获成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '博尔德大叔\n',
            '这下可要后悔了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3296')

    def _loc_3210(): pass

    label('loc_3210')

    ChrTalk(
        0x00FE,
        (
            '啊哈哈哈～～\n',
            '这次真是不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如我所想，飞船已经恢复了，\n',
            '和帝国商人的合作也大获成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '博尔德大叔\n',
            '这下可要后悔了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_3296(): pass

    label('loc_3296')

    Jump('loc_366E')

    def _loc_3299(): pass

    label('loc_3299')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_33DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_3300',
    )

    ChrTalk(
        0x00FE,
        (
            '飞船什么时候恢复呢……\n',
            '关键就看这次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能让博尔德大叔\n',
            '他一个人笑到最后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33DB')

    def _loc_3300(): pass

    label('loc_3300')

    ChrTalk(
        0x00FE,
        (
            '可能的话我想先出手，\n',
            '和帝国的人缔结协议……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '假如恢复贸易有所延误的话，\n',
            '仓库的存货数量将难以承受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话虽这么说，什么也不做的话，\n',
            '笑到最后的就是博尔德大叔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '飞船什么时候恢复呢……\n',
            '关键就看这次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_33DB(): pass

    label('loc_33DB')

    Jump('loc_366E')

    def _loc_33DE(): pass

    label('loc_33DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_3529',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_346E',
    )

    ChrTalk(
        0x00FE,
        (
            '不愧是小姐，真有本事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我佩服的五体投地，\n',
            '不快点发展生意不行了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是一直发呆的话，\n',
            '博尔德大叔\n',
            '就什么都没了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3526')

    def _loc_346E(): pass

    label('loc_346E')

    ChrTalk(
        0x00FE,
        (
            '超市的修复工作，\n',
            '今早好像开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是小姐，\n',
            '手段之高明当真王国第一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，佩服归佩服，\n',
            '我也得快点去经营生意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是一直发呆的话，\n',
            '博尔德大叔\n',
            '就什么都没了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_3526(): pass

    label('loc_3526')

    Jump('loc_366E')

    def _loc_3529(): pass

    label('loc_3529')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_3581',
    )

    ChrTalk(
        0x00FE,
        (
            '西蒙，\n',
            '这点小事要忍耐，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么大个儿人哭得稀哩哗啦的，\n',
            '不觉得羞耻吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_366E')

    def _loc_3581(): pass

    label('loc_3581')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_366E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_35D3',
    )

    ChrTalk(
        0x00FE,
        (
            '和帝国间的贸易，\n',
            '是我们的弱点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想和老爸商量商量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_366E')

    def _loc_35D3(): pass

    label('loc_35D3')

    ChrTalk(
        0x00FE,
        (
            '和帝国间的贸易，\n',
            '对我们来说是弱点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这点上，博尔德叔叔，\n',
            '在很早以前就有一条很宽广的渠道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市的事\n',
            '交给西蒙，\n',
            '必须要制定出对策才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_366E(): pass

    label('loc_366E')

    TalkEnd(0x0011)

    Return()

# id: 0x0010 offset: 0x3672
@scena.Code('func_10_3672')
def func_10_3672():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_378E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_373E',
    )

    ChrTalk(
        0x00FE,
        (
            '当前最大的问题是流通。\n',
            '也就是搬运货物的手段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '火车和飞船都不行的话，\n',
            '那就什么也运不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们在某种程度上\n',
            '做过心理准备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但这比想象的还要\n',
            '严重也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    Jump('loc_378B')

    def _loc_373E(): pass

    label('loc_373E')

    ChrTalk(
        0x00FE,
        (
            '当前最大的问题是流通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '火车和飞船都不行的话，\n',
            '那就什么也运不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_378B(): pass

    label('loc_378B')

    Jump('loc_3C18')

    def _loc_378E(): pass

    label('loc_378E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3886',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3817',
    )

    ChrTalk(
        0x00FE,
        (
            '城里不仅是导力器，\n',
            '就连定期船好像也停了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易才重新和帝国商人\n',
            '开始做买卖……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这真是糟糕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    Jump('loc_3883')

    def _loc_3817(): pass

    label('loc_3817')

    ChrTalk(
        0x00FE,
        (
            '城里不仅是导力器，\n',
            '就连定期船好像也停了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话，等到恢复\n',
            '可能需要花费很长一段时间也说不定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3883(): pass

    label('loc_3883')

    Jump('loc_3C18')

    def _loc_3886(): pass

    label('loc_3886')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_3956',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_38E2',
    )

    ChrTalk(
        0x00FE,
        (
            '米拉诺出人意料的\n',
            '擅长和帝国商人打交道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊哈哈，不愧是我女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3953')

    def _loc_38E2(): pass

    label('loc_38E2')

    ChrTalk(
        0x00FE,
        (
            '米拉诺出人意料的\n',
            '擅长和帝国商人打交道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊哈哈，不愧是我女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '博尔德那家伙\n',
            '肯定很不甘心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_3953(): pass

    label('loc_3953')

    Jump('loc_3C18')

    def _loc_3956(): pass

    label('loc_3956')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3A35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_39B5',
    )

    ChrTalk(
        0x00FE,
        (
            '我们的贸易方针\n',
            '完全交给米拉诺了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望能够让博尔德那家伙\n',
            '大吃一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A32')

    def _loc_39B5(): pass

    label('loc_39B5')

    ChrTalk(
        0x00FE,
        (
            '这段时间\n',
            '修复超市的工作\n',
            '异常的繁忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的贸易方针\n',
            '完全交给米拉诺了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望能够让博尔德那家伙\n',
            '大吃一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_3A32(): pass

    label('loc_3A32')

    Jump('loc_3C18')

    def _loc_3A35(): pass

    label('loc_3A35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_3B36',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3A9A',
    )

    ChrTalk(
        0x00FE,
        (
            '和博尔德联手，\n',
            '修复工作总算开工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须得趁早计划一下\n',
            '接下来的支援策略。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B33')

    def _loc_3A9A(): pass

    label('loc_3A9A')

    ChrTalk(
        0x00FE,
        (
            '和博尔德联手，\n',
            '修复工作总算开工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在座的各位，\n',
            '假如无法筹集到建材的话，\n',
            '很快瓦斯就会不够用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须得趁早计划一下\n',
            '接下来的支援策略。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_3B33(): pass

    label('loc_3B33')

    Jump('loc_3C18')

    def _loc_3B36(): pass

    label('loc_3B36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_3C18',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3B8C',
    )

    ChrTalk(
        0x00FE,
        (
            '今后和帝国做生意是关键。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对抗博尔德，\n',
            '必须要耍点手段才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C18')

    def _loc_3B8C(): pass

    label('loc_3B8C')

    ChrTalk(
        0x00FE,
        (
            '有互不侵犯条约在，\n',
            '今后和帝国做生意是关键。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，应酬帝国商人\n',
            '从来就是博尔德的强项。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是的，这样我们也\n',
            '必须做点什么才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_3C18(): pass

    label('loc_3C18')

    TalkEnd(0x0012)

    Return()

# id: 0x0011 offset: 0x3C1C
@scena.Code('func_11_3C1C')
def func_11_3C1C():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3D81',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3C89',
    )

    ChrTalk(
        0x00FE,
        (
            '飞船没有恢复的这段时间\n',
            '对买卖来说是个很大的考验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米拉诺也在烦恼，真是少见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D7E')

    def _loc_3C89(): pass

    label('loc_3C89')

    ChrTalk(
        0x00FE,
        (
            '飞船没有恢复的这段时间\n',
            '对买卖来说是个很大的考验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '假如恢复工作延迟的话，\n',
            '虽然会有大量商品积压在库……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但现在大家都在观望，\n',
            '反而可以找到机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是冒着风险决一胜负呢，\n',
            '还是应该避开风险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米拉诺也正在烦恼，真是少见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_3D7E(): pass

    label('loc_3D7E')

    Jump('loc_3EC1')

    def _loc_3D81(): pass

    label('loc_3D81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_3E38',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3DAF',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '脖子还是很痛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E35')

    def _loc_3DAF(): pass

    label('loc_3DAF')

    ChrTalk(
        0x00FE,
        (
            '呵呵，因为在超市里\n',
            '受伤了这才痛呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还好只受了这点伤，\n',
            '我感谢还来不及呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但是，没办法啊。\n',
            '痛总归还是痛的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_3E35(): pass

    label('loc_3E35')

    Jump('loc_3EC1')

    def _loc_3E38(): pass

    label('loc_3E38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_3EC1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3E59',
    )

    ChrTalk(
        0x00FE,
        (
            '痛，好痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EC1')

    def _loc_3E59(): pass

    label('loc_3E59')

    ChrTalk(
        0x00FE,
        (
            '啊，真痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米，米拉诺。\n',
            '很感谢你帮我治疗，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但能不能稍微温柔点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……啊，痛啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_3EC1(): pass

    label('loc_3EC1')

    TalkEnd(0x0013)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

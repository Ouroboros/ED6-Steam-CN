import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3110   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3110.x'
    header.mapIndex       = 1
    header.bgm            = 13
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
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '露依赛',
            x                   = -1900,
            z                   = 4000,
            y                   = 23230,
            direction           = 254,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '乌缇',
            x                   = -100,
            z                   = 0,
            y                   = 25860,
            direction           = 263,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '索黛丽娅',
            x                   = -3290,
            z                   = 0,
            y                   = 2790,
            direction           = 224,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '米优',
            x                   = 23740,
            z                   = 0,
            y                   = 1040,
            direction           = 142,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '兰达',
            x                   = 23410,
            z                   = 150,
            y                   = 740,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '斯坦因',
            x                   = 27780,
            z                   = 0,
            y                   = 25700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '阿利瑟',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '温丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '乌尔斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
    )

# id: 0x10002 offset: 0x23A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x23A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x23A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x23A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_270',
    )

    ChrSetFlags(0x000A, 0x0080)
    CreateThread(0x000C, 0x00, 0x00, func_02_468)
    ChrSetPos(0x000C, 21930, 0, 2180, 138)
    ChrSetFlags(0x000C, 0x0010)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0010)

    Jump('loc_445')

    def _loc_270(): pass

    label('loc_270')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2A6',
    )

    ChrSetFlags(0x000A, 0x0080)
    CreateThread(0x000C, 0x00, 0x00, func_02_468)
    ChrSetPos(0x000C, 21930, 0, 2180, 138)
    ChrSetFlags(0x000C, 0x0010)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0010)

    Jump('loc_445')

    def _loc_2A6(): pass

    label('loc_2A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2BF',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)

    Jump('loc_445')

    def _loc_2BF(): pass

    label('loc_2BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2EE',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 28100, 0, 22440, 0)

    Jump('loc_445')

    def _loc_2EE(): pass

    label('loc_2EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_38A',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, -1800, 0, 21070, 263)
    CreateThread(0x0009, 0x00, 0x00, func_03_47E)
    ChrSetPos(0x0008, -1720, 0, 24500, 275)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -4050, 0, -3180, 348)
    ChrSetFlags(0x000F, 0x0010)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 26330, 4000, 25200, 76)
    ChrSetFlags(0x0010, 0x0010)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 27970, 4000, 25230, 275)
    ChrSetPos(0x000A, 21330, 0, 3950, 352)
    CreateThread(0x000A, 0x00, 0x00, func_02_468)

    Jump('loc_445')

    def _loc_38A(): pass

    label('loc_38A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3D3',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    CreateThread(0x000B, 0x00, 0x00, func_02_468)
    ChrSetPos(0x000B, -4740, 0, 2840, 90)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -3450, 0, 2830, 270)
    CreateThread(0x000F, 0x00, 0x00, func_02_468)

    Jump('loc_445')

    def _loc_3D3(): pass

    label('loc_3D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_3F1',
    )

    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)

    Jump('loc_445')

    def _loc_3F1(): pass

    label('loc_3F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_420',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0010)
    ChrSetPos(0x0011, -1800, 0, 21070, 263)

    Jump('loc_445')

    def _loc_420(): pass

    label('loc_420')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_434',
    )

    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000A, 0x0080)

    Jump('loc_445')

    def _loc_434(): pass

    label('loc_434')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_445',
    )

    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000A, 0x0080)

    def _loc_445(): pass

    label('loc_445')

    Return()

# id: 0x0001 offset: 0x446
@scena.Code('func_01_446')
def func_01_446():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_45E',
    )

    OP_B1('t3110_y')

    Jump('loc_467')

    def _loc_45E(): pass

    label('loc_45E')

    OP_B1('t3110_n')

    def _loc_467(): pass

    label('loc_467')

    Return()

# id: 0x0002 offset: 0x468
@scena.Code('func_02_468')
def func_02_468():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_47D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_468')

    def _loc_47D(): pass

    label('loc_47D')

    Return()

# id: 0x0003 offset: 0x47E
@scena.Code('func_03_47E')
def func_03_47E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4A1',
    )

    OP_8D(0x00FE, 290, 22470, 1800, 25300, 2000)

    Jump('func_03_47E')

    def _loc_4A1(): pass

    label('loc_4A1')

    Return()

# id: 0x0004 offset: 0x4A2
@scena.Code('func_04_4A2')
def func_04_4A2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4C5',
    )

    OP_8D(0x00FE, -1920, 1860, 2170, -2770, 2000)

    Jump('func_04_4A2')

    def _loc_4C5(): pass

    label('loc_4C5')

    Return()

# id: 0x0005 offset: 0x4C6
@scena.Code('func_05_4C6')
def func_05_4C6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4E9',
    )

    OP_8D(0x00FE, -4730, 3760, -1290, 1770, 2000)

    Jump('func_05_4C6')

    def _loc_4E9(): pass

    label('loc_4E9')

    Return()

# id: 0x0006 offset: 0x4EA
@scena.Code('func_06_4EA')
def func_06_4EA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_50D',
    )

    OP_8D(0x00FE, 20960, 3050, 25510, -530, 2000)

    Jump('func_06_4EA')

    def _loc_50D(): pass

    label('loc_50D')

    Return()

# id: 0x0007 offset: 0x50E
@scena.Code('func_07_50E')
def func_07_50E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_531',
    )

    OP_8D(0x00FE, -5320, 520, -1440, 630, 2000)

    Jump('func_07_50E')

    def _loc_531(): pass

    label('loc_531')

    Return()

# id: 0x0008 offset: 0x532
@scena.Code('func_08_532')
def func_08_532():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_58F',
    )

    TalkBegin(0x0008)

    ChrTalk(
        0x00FE,
        (
            '啊，今天早上也是神清气爽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作充实的话，\n',
            '就连睡醒的感觉也很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_1058')

    def _loc_58F(): pass

    label('loc_58F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_6C7',
    )

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_62A',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然能够参加\n',
            '新型导力引擎的开发，\n',
            '这样的机会绝没有第二次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔唔唔唔，\n',
            '不绞尽脑汁的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪里还有\n',
            '喝汤的空闲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C1')

    def _loc_62A(): pass

    label('loc_62A')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '呜呜，\n',
            '虽说我被调动到了\n',
            '开发导力引擎的工作岗位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是自己连一个有份量的主意\n',
            '都还没有提出呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，不行。\n',
            '这可不是发牢骚的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C1(): pass

    label('loc_6C1')

    TalkEnd(0x0008)

    Jump('loc_1058')

    def _loc_6C7(): pass

    label('loc_6C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_7EC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_749',
    )

    TalkBegin(0x0008)

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '总觉得今天外面很吵闹啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯，不行不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对现在的我来说\n',
            '可没有闲功夫注意别的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7E6')

    def _loc_749(): pass

    label('loc_749')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x0008)

    ChrTalk(
        0x00FE,
        (
            '啊～？\n',
            '要重新设计枪筒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，真麻烦，\n',
            '一点干劲也没有了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～女神爱德丝啊。\n',
            '就算是做梦也行，\n',
            '请让我被调到与飞艇有关的工作吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7E6(): pass

    label('loc_7E6')

    TalkEnd(0x0008)

    Jump('loc_1058')

    def _loc_7EC(): pass

    label('loc_7EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_86A',
    )

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x0008)

    ChrTalk(
        0x00FE,
        (
            '资料我带了，\n',
            '妹妹也拜托给乌尔斯了……嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了～\n',
            '差不多该去上班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '还是觉得很累。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_1058')

    def _loc_86A(): pass

    label('loc_86A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_A1F',
    )

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_8D2',
    )

    ChrTalk(
        0x00FE,
        (
            '导力自身停止运行这种事\n',
            '以前听也没听说过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在中央工房\n',
            '一定是乱成一团了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A19')

    def _loc_8D2(): pass

    label('loc_8D2')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '噢，提妲，早呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘻嘻～～\n',
            '昨晚的麻烦可真不小呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#562F呜呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真是的，\n',
            '不要再笑话我啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '玛多克工房长因为此事\n',
            '已经忙得不可开交了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过导力自身停止运行\n',
            '这种事还是第一次遇到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '演算室的威尔姆他们\n',
            '现在一定慌乱不堪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光是维护和检修\n',
            '那部演算导力器\n',
            '就够他们忙的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A19(): pass

    label('loc_A19')

    TalkEnd(0x0008)

    Jump('loc_1058')

    def _loc_A1F(): pass

    label('loc_A1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_EB2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_ACC',
    )

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x0008)

    ChrTalk(
        0x00FE,
        (
            '……嗯，\n',
            '结晶光学论集、结晶光学论集……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '那本书放到哪里了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，我进工房\n',
            '不是想要做导力枪啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜，工作真是辛苦呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_EAF')

    def _loc_ACC(): pass

    label('loc_ACC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 3, 0x573)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E3C',
    )

    SetScenaFlags(ScenaFlag(0x00AE, 3, 0x573))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    TalkBegin(0x0008)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B09',
    )

    ChrTalk(
        0x00FE,
        (
            '哎？\n',
            '提妲，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B41')

    def _loc_B09(): pass

    label('loc_B09')

    ChrTalk(
        0x00FE,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '哦，提妲。\n',
            '来这里有什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B41(): pass

    label('loc_B41')

    ChrTalk(
        0x0107,
        (
            '#064F露依赛姐姐\n',
            '你今天不用去设计室吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，刚才在整理\n',
            '正在设计中的导力枪资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提妲你是不是\n',
            '在给客人们带路啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F是呀，没错。\n',
            '正在回家的路上呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说到提妲的家，\n',
            '最近是不是太过于安静了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久没有发生爆炸\n',
            '或者瓦斯泄漏的事故了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#509F（……爆、爆炸？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#560F那、那个……虽说是爆炸，\n',
            '其实呢，也不是很严重的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '只是把窗户上的玻璃\n',
            '都炸飞了而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F唔……\n',
            '那个已经十分严重了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#019F……就是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0008, 400)

    ChrTalk(
        0x00FE,
        (
            '其实呀，\n',
            '我也对博士的新发明十分好奇呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果发明进入了测试阶段，\n',
            '一定会让邻居们听到\n',
            '叮叮当当的做实验的声音吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F啊，是的。\n',
            '总是一次次地给大家添麻烦呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#061F露依赛姐姐也在\n',
            '负责新型导力枪的研制工作吧，\n',
            '请一定要加油啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯。\n',
            '我看情况加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_EAF')

    def _loc_E3C(): pass

    label('loc_E3C')

    TalkBegin(0x0008)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E74',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，提妲。\n',
            '还在给客人带路吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAC')

    def _loc_E74(): pass

    label('loc_E74')

    ChrTalk(
        0x00FE,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '呀，提妲。\n',
            '还在给客人带路吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EAC(): pass

    label('loc_EAC')

    TalkEnd(0x0008)

    def _loc_EAF(): pass

    label('loc_EAF')

    Jump('loc_1058')

    def _loc_EB2(): pass

    label('loc_EB2')

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F54',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_4A(0x0009, 255)
    ChrTurnDirection(0x0009, 0x00FE, 400)

    ChrTalk(
        0x0009,
        (
            '姐姐，\n',
            '拜托收拾一下床铺吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这个样子，\n',
            '都不能睡午觉啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗。\n',
            '嗯，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在有点忙，一会儿收拾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0009, 255)

    Jump('loc_104E')

    def _loc_F54(): pass

    label('loc_F54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FF4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_4A(0x0009, 255)
    ChrTurnDirection(0x0009, 0x00FE, 400)

    ChrTalk(
        0x0009,
        (
            '喂！\n',
            '姐姐你听到了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '快·来·收·拾·啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0009, 400)

    ChrTalk(
        0x00FE,
        (
            '啊～～\n',
            '真是啰嗦呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正在找论文呢。\n',
            '拜托你安静点！',
            TxtCtl.Enter,
        ),
    )

    ChrSetDirection(0x00FE, 254, 400)
    CloseMessageWindow()
    OP_4B(0x0009, 255)

    Jump('loc_104E')

    def _loc_FF4(): pass

    label('loc_FF4')

    ChrTalk(
        0x00FE,
        (
            '……真是的，\n',
            '我妹妹总是啰嗦个不停。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她如果能像\n',
            '拉赛尔博士的孙女提妲一样就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_104E(): pass

    label('loc_104E')

    ChrSetDirection(0x0009, 263, 0)
    TalkEnd(0x0008)

    def _loc_1058(): pass

    label('loc_1058')

    Return()

# id: 0x0009 offset: 0x1059
@scena.Code('func_09_1059')
def func_09_1059():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1115',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10C2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '一睁开眼睛，\n',
            '就看见被子上\n',
            '压着一本很大的书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '怪不得睡得那么难受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_110F')

    def _loc_10C2(): pass

    label('loc_10C2')

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '姐姐为什么就不能\n',
            '把书给收拾好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明床边\n',
            '就有书架的嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_110F(): pass

    label('loc_110F')

    TalkEnd(0x00FE)

    Jump('loc_1ADF')

    def _loc_1115(): pass

    label('loc_1115')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_11DB',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_117D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '……姐姐也真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是工作有干劲的时候， \n',
            '也从来不会收拾一下东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11D5')

    def _loc_117D(): pass

    label('loc_117D')

    ChrTalk(
        0x00FE,
        (
            '唉，算了～\n',
            '还是拜托乌尔斯哥哥吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他是姐姐的男朋友，\n',
            '肯定要负一些连带责任的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11D5(): pass

    label('loc_11D5')

    TalkEnd(0x00FE)

    Jump('loc_1ADF')

    def _loc_11DB(): pass

    label('loc_11DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_12D6',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1284',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '我姐姐她昨晚\n',
            '为了工作的事头疼不已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过呢，\n',
            '喝了点汤之后好像就有好主意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，汤里面是不是放了什么\n',
            '能让人的脑袋变聪明的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D0')

    def _loc_1284(): pass

    label('loc_1284')

    ChrTalk(
        0x00FE,
        (
            '汤里面含有什么\n',
            '让脑子变聪明的东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '去问问琪爱拉老师吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12D0(): pass

    label('loc_12D0')

    TalkEnd(0x00FE)

    Jump('loc_1ADF')

    def _loc_12D6(): pass

    label('loc_12D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_13D4',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1378',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    TalkSetChrName('民家１')

    ChrTalk(
        0x00FE,
        (
            '真是奇怪，\n',
            '姐姐她突然变得很有干劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她的男朋友乌尔斯来了，\n',
            '也不去聊天，只顾着埋头工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……呜呜，感觉真糟糕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13CE')

    def _loc_1378(): pass

    label('loc_1378')

    ChrTalk(
        0x00FE,
        (
            '不过在这里抱怨也没用，\n',
            '还不如好好休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '乌尔斯哥哥做的汤\n',
            '真是很好喝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13CE(): pass

    label('loc_13CE')

    TalkEnd(0x00FE)

    Jump('loc_1ADF')

    def _loc_13D4(): pass

    label('loc_13D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1568',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14FD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_146C',
    )

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '听说工房那边\n',
            '出了什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提妲你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#063F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯、嗯！\n',
            '都没事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14FA')

    def _loc_146C(): pass

    label('loc_146C')

    ChrTalk(
        0x00FE,
        (
            '听说工房那边\n',
            '似乎是发生了什么事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的姐姐\n',
            '今天没有去工房上班，\n',
            '所以完全没有受伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平安无事虽然好，\n',
            '不过擅离岗位说不过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14FA(): pass

    label('loc_14FA')

    Jump('loc_1562')

    def _loc_14FD(): pass

    label('loc_14FD')

    ChrTalk(
        0x00FE,
        (
            '我的姐姐\n',
            '今天没有去工房上班，\n',
            '所以完全没有受伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平安无事虽然好，\n',
            '不过擅离岗位说不过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1562(): pass

    label('loc_1562')

    TalkEnd(0x00FE)

    Jump('loc_1ADF')

    def _loc_1568(): pass

    label('loc_1568')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1693',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_157C',
    )

    ChrSetFlags(0x00FE, 0x0010)

    def _loc_157C(): pass

    label('loc_157C')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1623',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0009, 0x0011, 400)

    ChrTalk(
        0x00FE,
        (
            '对了，乌尔斯哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '午饭做好的话，\n',
            '拜托你打扫一下床铺哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐她连书也不收拾，\n',
            '让我很头疼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 263, 400)
    ChrClearFlags(0x00FE, 0x0010)

    Jump('loc_168D')

    def _loc_1623(): pass

    label('loc_1623')

    ChrTalk(
        0x00FE,
        (
            '乌尔斯哥哥\n',
            '是姐姐的男朋友哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '他偏偏会跟这样的姐姐交往……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……还真的有点同情他呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_168D(): pass

    label('loc_168D')

    TalkEnd(0x00FE)

    Jump('loc_1ADF')

    def _loc_1693(): pass

    label('loc_1693')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_16EB',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '姐姐，\n',
            '你最好还是赶快去上班吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再磨蹭的话\n',
            '就会迟到了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Jump('loc_1ADF')

    def _loc_16EB(): pass

    label('loc_16EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1851',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17F0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '呼啊，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '呀，是提妲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F早上好，乌缇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提妲今天\n',
            '也要去工房工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嗯，是呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我今天要去\n',
            '协助爷爷工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，是吗。\n',
            '看来你真的很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真不愧是提妲啊。\n',
            '感觉就像是个著名研究员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_184B')

    def _loc_17F0(): pass

    label('loc_17F0')

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '嗯，提妲。\n',
            '看来你真的很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的姐姐有你一半就好了，\n',
            '她实在是太散漫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_184B(): pass

    label('loc_184B')

    TalkEnd(0x00FE)

    Jump('loc_1ADF')

    def _loc_1851(): pass

    label('loc_1851')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1A0D',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 4, 0x574)),
            Expr.Return,
        ),
        'loc_18C0',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～就算这样，\n',
            '姐姐也一点没有\n',
            '要收拾干净的意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实在是～\n',
            '一个吊儿郎当的姐姐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A07')

    def _loc_18C0(): pass

    label('loc_18C0')

    SetScenaFlags(ScenaFlag(0x00AE, 4, 0x574))

    ChrTalk(
        0x00FE,
        (
            '啊，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F乌缇，\n',
            '已经放学了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎，你在说什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天可不是主日学校上课的日子哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#065F咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提妲啊，\n',
            '你偶尔也得休息一下嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你也来学校吧。\n',
            '大家都等着你来玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F啊，嗯，不好意思。\n',
            '最近一直在工房帮忙工作……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是呢，\n',
            '有空的话我一定去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，那说定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A07(): pass

    label('loc_1A07')

    TalkEnd(0x00FE)

    Jump('loc_1ADF')

    def _loc_1A0D(): pass

    label('loc_1A0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A1A',
    )

    ChrSetFlags(0x00FE, 0x0010)

    def _loc_1A1A(): pass

    label('loc_1A1A')

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A8E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x00FE, 0x0008, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '姐姐还真是邋遢呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快把床铺收拾了吧～\n',
            '要不然就睡不了午觉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 263, 400)
    ChrClearFlags(0x00FE, 0x0010)

    Jump('loc_1ADC')

    def _loc_1A8E(): pass

    label('loc_1A8E')

    ChrTalk(
        0x00FE,
        (
            '我的姐姐\n',
            '真是行为散漫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你看吧，乱成这个样子。\n',
            '实在让人没话说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ADC(): pass

    label('loc_1ADC')

    TalkEnd(0x0009)

    def _loc_1ADF(): pass

    label('loc_1ADF')

    Return()

# id: 0x000A offset: 0x1AE0
@scena.Code('func_0A_1AE0')
def func_0A_1AE0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1C5F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1B54',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '最近都没见到拉赛尔博士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没准又是呆在研究室里闭门不出，\n',
            '埋头于某项发明吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C5C')

    def _loc_1B54(): pass

    label('loc_1B54')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '从雨果先生那里传来了消息，\n',
            '说是已经决定了共同参与\n',
            '导力引擎研究的人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然研究者好像是位年轻的女性，\n',
            '不过现今的世界上，性别和年龄都没有界限。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要看见那位拉赛尔博士，\n',
            '就会明白年龄已经无关紧要了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀……说起来\n',
            '最近都没见到拉赛尔博士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C5C(): pass

    label('loc_1C5C')

    Jump('loc_23CF')

    def _loc_1C5F(): pass

    label('loc_1C5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1D2C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1CD2',
    )

    ChrTalk(
        0x00FE,
        (
            '在这种时候，\n',
            '外出旅游的记忆就会浮现在脑海中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想再到海边的赌吧玩玩，\n',
            '好好放松一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D29')

    def _loc_1CD2(): pass

    label('loc_1CD2')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '呼呼，这样的话，\n',
            '合同书就算整理完了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '一个人干活的时候是最忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D29(): pass

    label('loc_1D29')

    Jump('loc_23CF')

    def _loc_1D2C(): pass

    label('loc_1D2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1E63',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1DD0',
    )

    ChrTalk(
        0x00FE,
        (
            '被盗走的……\n',
            '只有演算导力器吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说被犯人偷走了，\n',
            '不过他们也不懂得运用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为能够完美运用那个机器的人\n',
            '也只有拉赛尔博士一个人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E60')

    def _loc_1DD0(): pass

    label('loc_1DD0')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '真让人吃惊啊。\n',
            '听说中央工房那里出事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '万幸的是没有人受伤，\n',
            '但据说演算导力器被盗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，老实说，\n',
            '我也不太明白犯人的动机呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E60(): pass

    label('loc_1E60')

    Jump('loc_23CF')

    def _loc_1E63(): pass

    label('loc_1E63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1F85',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1EBC',
    )

    ChrTalk(
        0x00FE,
        (
            '今天大街上\n',
            '还真是热闹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是拉赛尔博士\n',
            '又做了什么试验啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F82')

    def _loc_1EBC(): pass

    label('loc_1EBC')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '昨天，\n',
            '我在工房认识了一个\n',
            '从卡尔瓦德共和国来的年轻商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他好像是个导力器商人，\n',
            '所以我想多向他打听一些事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后向共和国出口的飞艇\n',
            '也会继续增加吧。\n',
            '真想和他尽快建立好合作关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F82(): pass

    label('loc_1F82')

    Jump('loc_23CF')

    def _loc_1F85(): pass

    label('loc_1F85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_20EC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2017',
    )

    ChrTalk(
        0x00FE,
        (
            '我妻子索黛丽娅\n',
            '本来就很讨厌大型飞艇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看见了昨天的现象，\n',
            '她这种情绪更加严重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知不觉间\n',
            '就有了这么多影响了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20E9')

    def _loc_2017(): pass

    label('loc_2017')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '『如果正在飞行中的飞艇\n',
            '　真的像昨天晚上那样突然失去了导力，\n',
            '　那会怎么样呢……』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '妻子索黛丽娅这样问我，\n',
            '我也无言以对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她本来就\n',
            '十分害怕乘坐飞艇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为昨夜的事，\n',
            '她这种情绪更加严重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20E9(): pass

    label('loc_20E9')

    Jump('loc_23CF')

    def _loc_20EC(): pass

    label('loc_20EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_21FB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2151',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天的现象\n',
            '真的有点可怕呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有给来买飞艇的客人\n',
            '留下坏印象就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F8')

    def _loc_2151(): pass

    label('loc_2151')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我的工作就是\n',
            '飞艇买卖的中介。\n',
            '昨天的现象真有点让人害怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这事在飞艇飞行时发生，\n',
            '肯定会酿成大惨剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有给来买飞艇的客人\n',
            '留下坏印象就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21F8(): pass

    label('loc_21F8')

    Jump('loc_23CF')

    def _loc_21FB(): pass

    label('loc_21FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2226',
    )

    ChrTalk(
        0x00FE,
        (
            '好～\n',
            '休息完了就开始工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23CF')

    def _loc_2226(): pass

    label('loc_2226')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_232A',
    )

    ChrTalk(
        0x00FE,
        (
            '我的工作就是\n',
            '飞艇买卖的中介。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在『埃尔赛尤号』开始服役之前，\n',
            '我也在工房和亲卫队之间\n',
            '作了很多工作上的协调哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过自从试飞测试结束之后，\n',
            '我就再没有机会听到\n',
            '有关『埃尔赛尤号』的消息了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过只要知道它在顺利执行任务，\n',
            '我就安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23CF')

    def _loc_232A(): pass

    label('loc_232A')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我正好刚从\n',
            '卢安旅行回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我离开之后，\n',
            '『埃尔赛尤号』好像在卢安出现了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是可惜啊。\n',
            '要是在那再呆上一阵子，\n',
            '也许就能再次见到『埃尔赛尤号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23CF(): pass

    label('loc_23CF')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x23D3
@scena.Code('func_0B_23D3')
def func_0B_23D3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2497',
    )

    ChrTalk(
        0x00FE,
        (
            '我家孩子米优啊，\n',
            '上次对我说\n',
            '将来想进入中央工房……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '仔细问了问她，\n',
            '原来是想成为接待小姐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听她这么说，总算让人放心一点了。\n',
            '因为，怎么看那孩子\n',
            '也不像是当研究者的料呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A22')

    def _loc_2497(): pass

    label('loc_2497')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2538',
    )

    ChrTalk(
        0x00FE,
        (
            '那次事件之后，\n',
            '米优很快对工房有了兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果她是认真的话，\n',
            '不如和爷爷商量一下吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，不管怎么想\n',
            '我都不觉得那孩子可以进入工房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A22')

    def _loc_2538(): pass

    label('loc_2538')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_25ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2589',
    )

    ChrTalk(
        0x00FE,
        (
            '因为我当时在酒馆里面，\n',
            '所以我一点也不知道\n',
            '中央工房出了事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25EA')

    def _loc_2589(): pass

    label('loc_2589')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我家爷爷\n',
            '刚刚终于回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '白天泡在酒馆，\n',
            '到了晚上才回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得有点反常呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25EA(): pass

    label('loc_25EA')

    Jump('loc_2A22')

    def _loc_25ED(): pass

    label('loc_25ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_262B',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然袭击中央工房……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是谁干的好事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A22')

    def _loc_262B(): pass

    label('loc_262B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_273F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2673',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，说起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家爷爷，\n',
            '又跑到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_273C')

    def _loc_2673(): pass

    label('loc_2673')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '提妲。\n',
            '又要出去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊，是的。\n',
            '要去亚尔摩村呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，是吗？\n',
            '总是忙着工作，真辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁这次机会，\n',
            '把工作做完之后\n',
            '去好好泡泡温泉怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家爷爷\n',
            '也很喜欢\n',
            '那里的温泉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_273C(): pass

    label('loc_273C')

    Jump('loc_2A22')

    def _loc_273F(): pass

    label('loc_273F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_27D0',
    )

    ChrTalk(
        0x00FE,
        (
            '我问了一下我丈夫，\n',
            '要是飞艇上的导力停止的话会怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如我所料，\n',
            '丈夫答不上来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我说，\n',
            '飞艇这东西根本不能信赖啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A22')

    def _loc_27D0(): pass

    label('loc_27D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_28AA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2835',
    )

    ChrTalk(
        0x00FE,
        (
            '我在准备晚饭的时候，\n',
            '一下子没有导力了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器这东西，\n',
            '经常会吓人一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28A7')

    def _loc_2835(): pass

    label('loc_2835')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我在准备晚饭的时候，\n',
            '突然导力停止供应了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，多亏了这样，\n',
            '女儿丢下不管的炖汤\n',
            '最后才没有被烧干。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28A7(): pass

    label('loc_28A7')

    Jump('loc_2A22')

    def _loc_28AA(): pass

    label('loc_28AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2992',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2909',
    )

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '上学的时候，\n',
            '请在学习上多多帮助我们家米优啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜托了，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_298F')

    def _loc_2909(): pass

    label('loc_2909')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '哎呀，是提妲啊。\n',
            '欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的家人\n',
            '去卢安旅行回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米优她好像玩闹过头了，\n',
            '这孩子这么大了\n',
            '却还是个野丫头呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_298F(): pass

    label('loc_298F')

    Jump('loc_2A22')

    def _loc_2992(): pass

    label('loc_2992')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_29CB',
    )

    ChrTalk(
        0x00FE,
        (
            '从今天开始又要回到\n',
            '每天的忙碌生活之中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A22')

    def _loc_29CB(): pass

    label('loc_29CB')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我的家人\n',
            '去卢安旅行回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，大家看起来都玩得很开心，\n',
            '这真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A22(): pass

    label('loc_2A22')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x2A26
@scena.Code('func_0C_2A26')
def func_0C_2A26():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2AAB',
    )

    ChrTalk(
        0x00FE,
        (
            '我说爷爷啊。\n',
            '我想当工房接待处的服务小姐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爷爷，\n',
            '你在中央工房有很多熟人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '给我介绍一个信得过的人吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_310D')

    def _loc_2AAB(): pass

    label('loc_2AAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_2B18',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '考虑到将来，\n',
            '还是到中央工房工作最好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且受人注目的程度\n',
            '在蔡斯也应该是第一的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_310D')

    def _loc_2B18(): pass

    label('loc_2B18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2BD8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2B7B',
    )

    ChrTalk(
        0x00FE,
        (
            '不、不过\n',
            '我可不是在幸灾乐祸啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我只是觉得中央工房\n',
            '真～的是相当厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BD5')

    def _loc_2B7B(): pass

    label('loc_2B7B')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '听说了吗？\n',
            '中央工房的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是中央工房啊。\n',
            '在蔡斯那是\n',
            '最受人瞩目的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BD5(): pass

    label('loc_2BD5')

    Jump('loc_310D')

    def _loc_2BD8(): pass

    label('loc_2BD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2CC4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2C39',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '我将来也想在中央工房工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又有拉赛尔博士在，\n',
            '就不会无聊了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CC1')

    def _loc_2C39(): pass

    label('loc_2C39')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '我好羡慕提妲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#064F嗯？\n',
            '为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里每天都有事做啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜，很闲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CC1(): pass

    label('loc_2CC1')

    Jump('loc_310D')

    def _loc_2CC4(): pass

    label('loc_2CC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_2E03',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2D30',
    )

    ChrTalk(
        0x00FE,
        (
            '在见惯了的事物中，\n',
            '说不定也会存在着\n',
            '从来没见过的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唔，\n',
            '真是有哲理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E00')

    def _loc_2D30(): pass

    label('loc_2D30')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '虽然旅行已经结束了，\n',
            '又回到了平常的无聊生活，\n',
            '不过昨晚真是好刺激啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力停了，\n',
            '街上一片漆黑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无意间向上一望，\n',
            '发现星空真是美丽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为平时看不到这样的天空，\n',
            '所以觉得有些不可思议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E00(): pass

    label('loc_2E00')

    Jump('loc_310D')

    def _loc_2E03(): pass

    label('loc_2E03')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2F55',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2E87',
    )

    ChrTalk(
        0x00FE,
        (
            '我在和妈妈准备晚饭的时候，\n',
            '导力灯突然灭掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就到外面看了一下，\n',
            '周围一片漆黑的，\n',
            '那时侯可真急死我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F52')

    def _loc_2E87(): pass

    label('loc_2E87')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '我在和妈妈准备晚饭的时候，\n',
            '导力灯突然灭掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我慌慌张张地跑出去看，\n',
            '外面一片漆黑，真是急死我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#561F啊呀呀……\n',
            '对不起，米优。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '咦？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么\n',
            '提妲你要向我道歉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F52(): pass

    label('loc_2F52')

    Jump('loc_310D')

    def _loc_2F55(): pass

    label('loc_2F55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_30B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2FB0',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '无聊的日子又要开始了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '爷爷什么时候再带我出去玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30B0')

    def _loc_2FB0(): pass

    label('loc_2FB0')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '啊啊，真讨厌啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊，米优。\n',
            '到卢安旅行好玩吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '实在是太棒了！\n',
            '真是让人兴奋得不得了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到了要回蔡斯的时候，\n',
            '心情就一落千丈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等待着我的就是\n',
            '无聊的生活和主日学校的作业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F啊、啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30B0(): pass

    label('loc_30B0')

    Jump('loc_310D')

    def _loc_30B3(): pass

    label('loc_30B3')

    ChrTalk(
        0x00FE,
        (
            '妈妈要是也一起\n',
            '去卢安旅行就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这是不可能的。\n',
            '因为妈妈有飞艇恐惧症呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_310D(): pass

    label('loc_310D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x3111
@scena.Code('func_0D_3111')
def func_0D_3111():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_31FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3182',
    )

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '这可是我可爱的孙女的请求。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何，\n',
            '我也会如她所愿，\n',
            '让她能在工房工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31F7')

    def _loc_3182(): pass

    label('loc_3182')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '虽说有熟人……\n',
            '但大家都是搞技术的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '跟他们说接待处小姐的事\n',
            '大概也没有什么意义吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，这可为难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31F7(): pass

    label('loc_31F7')

    Jump('loc_3254')

    def _loc_31FA(): pass

    label('loc_31FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_3254',
    )

    ChrTalk(
        0x00FE,
        (
            '索黛丽娅，\n',
            '晚饭还没有好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天一天\n',
            '忙着和别人说话，\n',
            '肚子饿得受不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3254(): pass

    label('loc_3254')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x3258
@scena.Code('func_0E_3258')
def func_0E_3258():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_33F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3309',
    )

    ChrTalk(
        0x00FE,
        (
            '耶鲁克店长\n',
            '好像终于也开始\n',
            '认同我的理念了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他调整武器的技术很棒，\n',
            '是个了不起的鉴定人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但愿他能成为\n',
            '一个不拘小节，\n',
            '能够成就更大事业的商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33F4')

    def _loc_3309(): pass

    label('loc_3309')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '昨晚，我和耶鲁克店长\n',
            '商量了进货的情况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '终于，他也稍许表示出\n',
            '对我的理念的理解和赞同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '武器店做的可是\n',
            '关系到顾客生命的买卖。\n',
            '马马虎虎做出来的东西可不能使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从今往后，\n',
            '我也要坚持不懈地\n',
            '把这个想法传达给他才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33F4(): pass

    label('loc_33F4')

    Jump('loc_3CAE')

    def _loc_33F7(): pass

    label('loc_33F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_353C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_347C',
    )

    ChrTalk(
        0x00FE,
        (
            '我家温丝的内心似乎\n',
            '也憧憬着做一名研究者呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果他决定要走这条路的话，\n',
            '我希望他能成为一名视野广阔的学者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3539')

    def _loc_347C(): pass

    label('loc_347C')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '单单将性能提高的话，\n',
            '新技术是无法得到普及的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '初次在世界上进行推广的时候，\n',
            '应该注重易用性，好让更多人接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就像把七耀石\n',
            '利用在导力器的技术上，\n',
            '从而引起一场导力革命那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3539(): pass

    label('loc_3539')

    Jump('loc_3CAE')

    def _loc_353C(): pass

    label('loc_353C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_36B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_35F2',
    )

    ChrTalk(
        0x00FE,
        (
            '加鲁诺他\n',
            '好像也终于理解我那种\n',
            '重视武器可靠性的想法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他终于学会\n',
            '从使用者的角度来\n',
            '重新认识自己的研究了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉呀，要是耶鲁克店长\n',
            '也能早点注意到就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36B0')

    def _loc_35F2(): pass

    label('loc_35F2')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '今天早上加鲁诺他\n',
            '突然来拜访我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他对我说，终于理解了我的\n',
            '重视武器可靠性的方针呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他终于学会\n',
            '从使用者的角度来\n',
            '重新认识自己的研究了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许是什么事\n',
            '让他发生了转变吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36B0(): pass

    label('loc_36B0')

    Jump('loc_3CAE')

    def _loc_36B3(): pass

    label('loc_36B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_38A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_37B1',
    )

    ChrTalk(
        0x00FE,
        (
            '对于武器来说， \n',
            '最重要的就是可靠性和操作性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '紧急时刻，\n',
            '谁都能够自如地使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这对于使用者来说\n',
            '是最重要的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过竟然把还处于\n',
            '试制阶段的导力枪拿出来出售……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来加鲁诺他有必要\n',
            '站在使用者的角度\n',
            '来考虑一下问题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38A3')

    def _loc_37B1(): pass

    label('loc_37B1')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '今天，\n',
            '我要去和中央工房的加鲁诺面谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他似乎在向\n',
            '耶鲁克店长兜售试制品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要清楚地告诉他，\n',
            '在我的店里面\n',
            '只能销售让顾客放心的武器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '今天偏偏又发生了那样的事，\n',
            '没能和他见到面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会改天\n',
            '重新找个机会找他谈谈的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38A3(): pass

    label('loc_38A3')

    Jump('loc_3CAE')

    def _loc_38A6(): pass

    label('loc_38A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3990',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3911',
    )

    ChrTalk(
        0x00FE,
        (
            '工房周围\n',
            '好不容易安静了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，学校差不多也该放学了。\n',
            '一会儿温丝也该回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_398D')

    def _loc_3911(): pass

    label('loc_3911')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '工房周围\n',
            '好不容易安静了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在主日学校放学前，\n',
            '骚乱能够结束真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不想让孩子们\n',
            '看见那样的骚动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_398D(): pass

    label('loc_398D')

    Jump('loc_3CAE')

    def _loc_3990(): pass

    label('loc_3990')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_3AE6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_39FF',
    )

    ChrTalk(
        0x00FE,
        (
            '当然啦，\n',
            '也不是耶鲁克一个人的错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟技术人员的那种\n',
            '仅仅追求性能的态度也是个问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AE3')

    def _loc_39FF(): pass

    label('loc_39FF')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '店长耶鲁克虽说人很热心，\n',
            '维修武器的技术也相当不错，\n',
            '却有一种只关心武器性能的癖好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，无论武器的性能如何优秀，\n',
            '如果难以自如运用就变得没意义了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反反复复地跟他说，\n',
            '不要单单追求性能……\n',
            '怎么就不能理解一下呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AE3(): pass

    label('loc_3AE3')

    Jump('loc_3CAE')

    def _loc_3AE6(): pass

    label('loc_3AE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_3B65',
    )

    ChrTalk(
        0x00FE,
        (
            '身为一个有尊严的原技师，\n',
            '我在武器进货的时候，\n',
            '也是特别用心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我准备了很多不错的商品，\n',
            '请一定要来看看哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CAE')

    def _loc_3B65(): pass

    label('loc_3B65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3C14',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '我家世代都是钟表工匠。\n',
            '我年轻的时候也在\n',
            '中央工房担任过技师的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '和客人交涉可真是一点都没趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当我意识到这点的时候，\n',
            '我的店子已经开张了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CAE')

    def _loc_3C14(): pass

    label('loc_3C14')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '哎，你们是游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要订购武器的话，\n',
            '就交给我们斯坦因武器商会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家的店正好\n',
            '在你们游击士协会对面，\n',
            '有空的话，请你们务必要来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CAE(): pass

    label('loc_3CAE')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x3CB2
@scena.Code('func_0F_3CB2')
def func_0F_3CB2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_3CFD',
    )

    ChrTalk(
        0x00FE,
        (
            '温丝！\n',
            '你又旷课了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么老是那样啊。\n',
            '又不是学不会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E09')

    def _loc_3CFD(): pass

    label('loc_3CFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3E09',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_3D56',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '主日学校一会儿就该放学了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '温丝今天\n',
            '有没有认真上课啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E09')

    def _loc_3D56(): pass

    label('loc_3D56')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '之前知道不是火灾或事故的时候，\n',
            '还松了一口气……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到偏偏是个案件。\n',
            '真是做梦都想不到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……哎呀，\n',
            '主日学校一会儿就该放学了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是不是该去\n',
            '接温丝回家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E09(): pass

    label('loc_3E09')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x3E0D
@scena.Code('func_10_3E0D')
def func_10_3E0D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3F4E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3EB9',
    )

    ChrTalk(
        0x00FE,
        (
            '我将来\n',
            '想成为一名研究员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说从我的性格来看，\n',
            '要将精力集中在某件事上\n',
            '来进行研究是很困难的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是我相信成为研究员\n',
            '对我的发展很有好处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F4B')

    def _loc_3EB9(): pass

    label('loc_3EB9')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '一清早加鲁诺叔叔\n',
            '就来拜访爸爸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '加鲁诺叔叔两眼通红。\n',
            '看起来昨天一夜没睡的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '专注于某件事的研究员\n',
            '看起来还真是光彩耀人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F4B(): pass

    label('loc_3F4B')

    Jump('loc_4008')

    def _loc_3F4E(): pass

    label('loc_3F4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_4008',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3FB7',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈，\n',
            '请不要评价得这么主观哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我并非那种对某一件事\n',
            '可以保持长久兴趣的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4008')

    def _loc_3FB7(): pass

    label('loc_3FB7')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '妈妈，\n',
            '我并不是偷懒不学习哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只不过是，\n',
            '我的兴趣与大家不一样而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4008(): pass

    label('loc_4008')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x400C
@scena.Code('func_11_400C')
def func_11_400C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_4093',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_4041',
    )

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '汤要重新热一下对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4090')

    def _loc_4041(): pass

    label('loc_4041')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '啊，露依赛那家伙\n',
            '好像把汤完全煮干了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来还想叫她\n',
            '吃点什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4090(): pass

    label('loc_4090')

    Jump('loc_4174')

    def _loc_4093(): pass

    label('loc_4093')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_4174',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_40F6',
    )

    ChrTalk(
        0x00FE,
        (
            '得赶快做好饭，\n',
            '回店里干活去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光老板一个人的话，\n',
            '无论如何都不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4174')

    def _loc_40F6(): pass

    label('loc_40F6')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    ChrTurnDirection(0x0011, 0x0009, 400)

    ChrTalk(
        0x00FE,
        (
            '给你做午饭\n',
            '倒是没什么问题啦……\n',
            '不过我说乌缇，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算我是她的男友，\n',
            '为什么非要我给她收拾床铺不可啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 263, 0)

    def _loc_4174(): pass

    label('loc_4174')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

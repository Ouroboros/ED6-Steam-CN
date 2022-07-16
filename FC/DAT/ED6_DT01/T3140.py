import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3140_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3140   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '露依赛'),
    TXT(0x02, '乌缇'),
    TXT(0x03, '鲁特尔'),
    TXT(0x04, '索黛丽娅'),
    TXT(0x05, '米优'),
    TXT(0x06, '兰达'),
    TXT(0x07, '斯坦因'),
    TXT(0x08, '阿利瑟'),
    TXT(0x09, '温丝'),
    TXT(0x0A, '乌尔斯'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3140.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4069
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
        ('ED6_DT07/CH01433._CH', 'ED6_DT07/CH01433P._CP'),
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

# id: 0x10002 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -1900,
            z                   = 250,
            y                   = 23230,
            direction           = 254,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
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
            x                   = 23410,
            z                   = 0,
            y                   = 740,
            direction           = 308,
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
            x                   = 27980,
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

# id: 0x10003 offset: 0x23A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x23A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x23A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x23A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_249',
    )

    SetChrFlags(0x000A, 0x0080)

    Jump('loc_42D')

    def _loc_249(): pass

    label('loc_249')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_286',
    )

    CreateThread(0x0009, 0x00, 0x00, 0x0003)
    SetChrFlags(0x000A, 0x0080)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    SetChrPos(0x000C, 21930, 0, 2180, 138)
    SetChrFlags(0x000C, 0x0010)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0010)

    Jump('loc_42D')

    def _loc_286(): pass

    label('loc_286')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2A6',
    )

    CreateThread(0x0009, 0x00, 0x00, 0x0003)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)

    Jump('loc_42D')

    def _loc_2A6(): pass

    label('loc_2A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2DC',
    )

    CreateThread(0x0009, 0x00, 0x00, 0x0003)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 28080, 0, 25700, 170)

    Jump('loc_42D')

    def _loc_2DC(): pass

    label('loc_2DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_387',
    )

    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -1800, 0, 21070, 263)
    SetChrPos(0x0009, 750, 0, 24620, 270)
    SetChrPos(0x0008, -1720, 220, 24700, 270)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -160, 0, -100, 315)
    SetChrFlags(0x000D, 0x0010)
    SetChrFlags(0x000F, 0x0010)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 26330, 4000, 25200, 76)
    SetChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 27970, 4000, 25230, 275)
    SetChrPos(0x000A, 21330, 0, 3950, 352)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    Jump('loc_42D')

    def _loc_387(): pass

    label('loc_387')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3BA',
    )

    CreateThread(0x0009, 0x00, 0x00, 0x0003)
    SetChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, -3830, 0, 330, 269)
    CreateThread(0x000F, 0x00, 0x00, 0x0007)

    Jump('loc_42D')

    def _loc_3BA(): pass

    label('loc_3BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_3D3',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)

    Jump('loc_42D')

    def _loc_3D3(): pass

    label('loc_3D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_404',
    )

    CreateThread(0x0009, 0x00, 0x00, 0x0003)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -1800, 0, 21070, 263)

    Jump('loc_42D')

    def _loc_404(): pass

    label('loc_404')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_41A',
    )

    CreateThread(0x0009, 0x00, 0x00, 0x0003)
    SetChrFlags(0x000E, 0x0080)

    Jump('loc_42D')

    def _loc_41A(): pass

    label('loc_41A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_42D',
    )

    CreateThread(0x0009, 0x00, 0x00, 0x0003)
    SetChrFlags(0x000E, 0x0080)

    def _loc_42D(): pass

    label('loc_42D')

    Return()

# id: 0x0001 offset: 0x42E
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x42F
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_444',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_444(): pass

    label('loc_444')

    Return()

# id: 0x0003 offset: 0x445
@scena.Code('func_03_445')
def func_03_445():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_468',
    )

    OP_8D(0x00FE, 290, 22470, 1800, 25300, 2000)

    Jump('func_03_445')

    def _loc_468(): pass

    label('loc_468')

    Return()

# id: 0x0004 offset: 0x469
@scena.Code('func_04_469')
def func_04_469():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_48C',
    )

    OP_8D(0x00FE, -1920, 1860, 2170, -2770, 2000)

    Jump('func_04_469')

    def _loc_48C(): pass

    label('loc_48C')

    Return()

# id: 0x0005 offset: 0x48D
@scena.Code('func_05_48D')
def func_05_48D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4B0',
    )

    OP_8D(0x00FE, -4730, 3760, -1290, 1770, 2000)

    Jump('func_05_48D')

    def _loc_4B0(): pass

    label('loc_4B0')

    Return()

# id: 0x0006 offset: 0x4B1
@scena.Code('func_06_4B1')
def func_06_4B1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4D4',
    )

    OP_8D(0x00FE, 20960, 3050, 25510, -530, 2000)

    Jump('func_06_4B1')

    def _loc_4D4(): pass

    label('loc_4D4')

    Return()

# id: 0x0007 offset: 0x4D5
@scena.Code('func_07_4D5')
def func_07_4D5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4F8',
    )

    OP_8D(0x00FE, -5320, 520, -1440, 630, 2000)

    Jump('func_07_4D5')

    def _loc_4F8(): pass

    label('loc_4F8')

    Return()

# id: 0x0008 offset: 0x4F9
@scena.Code('func_08_4F9')
def func_08_4F9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_556',
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

    Jump('loc_FD8')

    def _loc_556(): pass

    label('loc_556')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_68E',
    )

    SetChrFlags(0x00FE, 0x0010)
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_5F1',
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

    Jump('loc_688')

    def _loc_5F1(): pass

    label('loc_5F1')

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

    def _loc_688(): pass

    label('loc_688')

    TalkEnd(0x0008)

    Jump('loc_FD8')

    def _loc_68E(): pass

    label('loc_68E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_7B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_710',
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

    Jump('loc_7AD')

    def _loc_710(): pass

    label('loc_710')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetChrFlags(0x00FE, 0x0010)
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

    def _loc_7AD(): pass

    label('loc_7AD')

    TalkEnd(0x0008)

    Jump('loc_FD8')

    def _loc_7B3(): pass

    label('loc_7B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_831',
    )

    SetChrFlags(0x00FE, 0x0010)
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

    Jump('loc_FD8')

    def _loc_831(): pass

    label('loc_831')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_9C8',
    )

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_899',
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

    Jump('loc_9C2')

    def _loc_899(): pass

    label('loc_899')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

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

    ChrTalk(
        0x0107,
        (
            '#060F呜呜……',
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

    def _loc_9C2(): pass

    label('loc_9C2')

    TalkEnd(0x0008)

    Jump('loc_FD8')

    def _loc_9C8(): pass

    label('loc_9C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_E36',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_A77',
    )

    SetChrFlags(0x00FE, 0x0010)
    TalkBegin(0x0008)

    ChrTalk(
        0x00FE,
        (
            '……嗯，\n',
            '结晶光学论集……结晶光学论集……',
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

    Jump('loc_E33')

    def _loc_A77(): pass

    label('loc_A77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 3, 0x573)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DC4',
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
        'loc_AB4',
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

    Jump('loc_AE8')

    def _loc_AB4(): pass

    label('loc_AB4')

    ChrTalk(
        0x00FE,
        (
            '哎？',
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

    def _loc_AE8(): pass

    label('loc_AE8')

    ChrTalk(
        0x0107,
        (
            '#060F露依赛姐姐\n',
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
            '#060F是呀，没错。\n',
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
            '#000F爆、爆炸？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#060F那、那个……虽说是爆炸，\n',
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
            '#000F唔……\n',
            '那个已经十分严重了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……就是啊。',
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

    Jump('loc_E33')

    def _loc_DC4(): pass

    label('loc_DC4')

    TalkBegin(0x0008)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DFC',
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

    Jump('loc_E06')

    def _loc_DFC(): pass

    label('loc_DFC')

    ChrTalk(
        0x00FE,
        (
            '哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E06(): pass

    label('loc_E06')

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
    TalkEnd(0x0008)

    def _loc_E33(): pass

    label('loc_E33')

    Jump('loc_FD8')

    def _loc_E36(): pass

    label('loc_E36')

    SetChrFlags(0x00FE, 0x0010)
    TalkBegin(0x0008)
    TerminateThread(0x0009, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ED9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetChrFlags(0x0009, 0x0020)
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

    Jump('loc_FCB')

    def _loc_ED9(): pass

    label('loc_ED9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F71',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
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

    SetChrDirection(0x00FE, 254, 400)
    CloseMessageWindow()

    Jump('loc_FCB')

    def _loc_F71(): pass

    label('loc_F71')

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

    def _loc_FCB(): pass

    label('loc_FCB')

    SetChrDirection(0x0009, 263, 400)
    OP_85(0x0009)
    TalkEnd(0x0008)

    def _loc_FD8(): pass

    label('loc_FD8')

    Return()

# id: 0x0009 offset: 0xFD9
@scena.Code('func_09_FD9')
def func_09_FD9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1095',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1042',
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

    Jump('loc_108F')

    def _loc_1042(): pass

    label('loc_1042')

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

    def _loc_108F(): pass

    label('loc_108F')

    TalkEnd(0x00FE)

    Jump('loc_19D2')

    def _loc_1095(): pass

    label('loc_1095')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_115B',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10FD',
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

    Jump('loc_1155')

    def _loc_10FD(): pass

    label('loc_10FD')

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

    def _loc_1155(): pass

    label('loc_1155')

    TalkEnd(0x00FE)

    Jump('loc_19D2')

    def _loc_115B(): pass

    label('loc_115B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1256',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1204',
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

    Jump('loc_1250')

    def _loc_1204(): pass

    label('loc_1204')

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

    def _loc_1250(): pass

    label('loc_1250')

    TalkEnd(0x00FE)

    Jump('loc_19D2')

    def _loc_1256(): pass

    label('loc_1256')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1354',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12F8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetChrName('民家１')

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

    Jump('loc_134E')

    def _loc_12F8(): pass

    label('loc_12F8')

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

    def _loc_134E(): pass

    label('loc_134E')

    TalkEnd(0x00FE)

    Jump('loc_19D2')

    def _loc_1354(): pass

    label('loc_1354')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1442',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13D7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

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
            '#060F啊……',
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

    Jump('loc_143C')

    def _loc_13D7(): pass

    label('loc_13D7')

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

    def _loc_143C(): pass

    label('loc_143C')

    TalkEnd(0x00FE)

    Jump('loc_19D2')

    def _loc_1442(): pass

    label('loc_1442')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1536',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14C6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

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

    Jump('loc_1530')

    def _loc_14C6(): pass

    label('loc_14C6')

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

    def _loc_1530(): pass

    label('loc_1530')

    TalkEnd(0x00FE)

    Jump('loc_19D2')

    def _loc_1536(): pass

    label('loc_1536')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_158E',
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

    Jump('loc_19D2')

    def _loc_158E(): pass

    label('loc_158E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_16E6',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_168C',
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
            '#060F早上好，乌缇。',
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

    Jump('loc_16E0')

    def _loc_168C(): pass

    label('loc_168C')

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

    def _loc_16E0(): pass

    label('loc_16E0')

    TalkEnd(0x00FE)

    Jump('loc_19D2')

    def _loc_16E6(): pass

    label('loc_16E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_18A6',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 4, 0x574)),
            Expr.Return,
        ),
        'loc_1755',
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

    Jump('loc_18A0')

    def _loc_1755(): pass

    label('loc_1755')

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
            '#060F哎……！？',
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
            '#060F啊，嗯，不好意思。\n',
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

    def _loc_18A0(): pass

    label('loc_18A0')

    TalkEnd(0x00FE)

    Jump('loc_19D2')

    def _loc_18A6(): pass

    label('loc_18A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18B3',
    )

    SetChrFlags(0x00FE, 0x0010)

    def _loc_18B3(): pass

    label('loc_18B3')

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_197E',
    )

    TerminateThread(0x0008, 0xFF)
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

    ChrTalk(
        0x0008,
        (
            '是吗。\n',
            '嗯，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在有点忙，一会儿收拾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的～要快点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 263, 400)
    ClearChrFlags(0x00FE, 0x0010)

    Jump('loc_19CC')

    def _loc_197E(): pass

    label('loc_197E')

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

    def _loc_19CC(): pass

    label('loc_19CC')

    OP_85(0x0008)
    TalkEnd(0x0009)

    def _loc_19D2(): pass

    label('loc_19D2')

    Return()

# id: 0x000A offset: 0x19D3
@scena.Code('func_0A_19D3')
def func_0A_19D3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1B52',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1A47',
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

    Jump('loc_1B4F')

    def _loc_1A47(): pass

    label('loc_1A47')

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

    def _loc_1B4F(): pass

    label('loc_1B4F')

    Jump('loc_22C2')

    def _loc_1B52(): pass

    label('loc_1B52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1C1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1BC5',
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

    Jump('loc_1C1C')

    def _loc_1BC5(): pass

    label('loc_1BC5')

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

    def _loc_1C1C(): pass

    label('loc_1C1C')

    Jump('loc_22C2')

    def _loc_1C1F(): pass

    label('loc_1C1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1D56',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1CC3',
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

    Jump('loc_1D53')

    def _loc_1CC3(): pass

    label('loc_1CC3')

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

    def _loc_1D53(): pass

    label('loc_1D53')

    Jump('loc_22C2')

    def _loc_1D56(): pass

    label('loc_1D56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1E78',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1DAF',
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

    Jump('loc_1E75')

    def _loc_1DAF(): pass

    label('loc_1DAF')

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

    def _loc_1E75(): pass

    label('loc_1E75')

    Jump('loc_22C2')

    def _loc_1E78(): pass

    label('loc_1E78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_1FDF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1F0A',
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

    Jump('loc_1FDC')

    def _loc_1F0A(): pass

    label('loc_1F0A')

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

    def _loc_1FDC(): pass

    label('loc_1FDC')

    Jump('loc_22C2')

    def _loc_1FDF(): pass

    label('loc_1FDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_20EE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2044',
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

    Jump('loc_20EB')

    def _loc_2044(): pass

    label('loc_2044')

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

    def _loc_20EB(): pass

    label('loc_20EB')

    Jump('loc_22C2')

    def _loc_20EE(): pass

    label('loc_20EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2119',
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

    Jump('loc_22C2')

    def _loc_2119(): pass

    label('loc_2119')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_221D',
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

    Jump('loc_22C2')

    def _loc_221D(): pass

    label('loc_221D')

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

    def _loc_22C2(): pass

    label('loc_22C2')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x22C6
@scena.Code('func_0B_22C6')
def func_0B_22C6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_238A',
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

    Jump('loc_2907')

    def _loc_238A(): pass

    label('loc_238A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_242B',
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

    Jump('loc_2907')

    def _loc_242B(): pass

    label('loc_242B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_24E0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_247C',
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

    Jump('loc_24DD')

    def _loc_247C(): pass

    label('loc_247C')

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

    def _loc_24DD(): pass

    label('loc_24DD')

    Jump('loc_2907')

    def _loc_24E0(): pass

    label('loc_24E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_251E',
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

    Jump('loc_2907')

    def _loc_251E(): pass

    label('loc_251E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2632',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2566',
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

    Jump('loc_262F')

    def _loc_2566(): pass

    label('loc_2566')

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

    def _loc_262F(): pass

    label('loc_262F')

    Jump('loc_2907')

    def _loc_2632(): pass

    label('loc_2632')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_26C3',
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

    Jump('loc_2907')

    def _loc_26C3(): pass

    label('loc_26C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_279D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2728',
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

    Jump('loc_279A')

    def _loc_2728(): pass

    label('loc_2728')

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

    def _loc_279A(): pass

    label('loc_279A')

    Jump('loc_2907')

    def _loc_279D(): pass

    label('loc_279D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2877',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_27F5',
    )

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

    Jump('loc_2874')

    def _loc_27F5(): pass

    label('loc_27F5')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

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

    def _loc_2874(): pass

    label('loc_2874')

    Jump('loc_2907')

    def _loc_2877(): pass

    label('loc_2877')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_28B0',
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

    Jump('loc_2907')

    def _loc_28B0(): pass

    label('loc_28B0')

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

    def _loc_2907(): pass

    label('loc_2907')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x290B
@scena.Code('func_0C_290B')
def func_0C_290B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2990',
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

    Jump('loc_2F8C')

    def _loc_2990(): pass

    label('loc_2990')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_29FD',
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

    Jump('loc_2F8C')

    def _loc_29FD(): pass

    label('loc_29FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2ABD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2A60',
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

    Jump('loc_2ABA')

    def _loc_2A60(): pass

    label('loc_2A60')

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

    def _loc_2ABA(): pass

    label('loc_2ABA')

    Jump('loc_2F8C')

    def _loc_2ABD(): pass

    label('loc_2ABD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2B9A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2B1E',
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

    Jump('loc_2B97')

    def _loc_2B1E(): pass

    label('loc_2B1E')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

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
            '#060F嗯？\n',
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
            '#060F…………',
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

    def _loc_2B97(): pass

    label('loc_2B97')

    Jump('loc_2F8C')

    def _loc_2B9A(): pass

    label('loc_2B9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_2CAE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2C06',
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

    Jump('loc_2CAB')

    def _loc_2C06(): pass

    label('loc_2C06')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上\n',
            '真是好刺激啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力停止了，\n',
            '街上一片漆黑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '站在阳台往上看，\n',
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

    def _loc_2CAB(): pass

    label('loc_2CAB')

    Jump('loc_2F8C')

    def _loc_2CAE(): pass

    label('loc_2CAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2E01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2D34',
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
            '我就到阳台上看了一下，\n',
            '周围一片漆黑的，\n',
            '那时侯可真急死我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DFE')

    def _loc_2D34(): pass

    label('loc_2D34')

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
            '我慌慌张张地跑到阳台上去看，\n',
            '外面一片漆黑，真是急死我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊呀呀……\n',
            '对不起，米优。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

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

    def _loc_2DFE(): pass

    label('loc_2DFE')

    Jump('loc_2F8C')

    def _loc_2E01(): pass

    label('loc_2E01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2F32',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2E5C',
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

    Jump('loc_2F2F')

    def _loc_2E5C(): pass

    label('loc_2E5C')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

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
        0x0107,
        (
            '#060F啊，米优。\n',
            '到卢安旅行好玩吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

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
        0x0107,
        (
            '#060F啊、啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F2F(): pass

    label('loc_2F2F')

    Jump('loc_2F8C')

    def _loc_2F32(): pass

    label('loc_2F32')

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

    def _loc_2F8C(): pass

    label('loc_2F8C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x2F90
@scena.Code('func_0D_2F90')
def func_0D_2F90():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3079',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3001',
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

    Jump('loc_3076')

    def _loc_3001(): pass

    label('loc_3001')

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

    def _loc_3076(): pass

    label('loc_3076')

    Jump('loc_30D3')

    def _loc_3079(): pass

    label('loc_3079')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_30D3',
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

    def _loc_30D3(): pass

    label('loc_30D3')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x30D7
@scena.Code('func_0E_30D7')
def func_0E_30D7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3276',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3188',
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

    Jump('loc_3273')

    def _loc_3188(): pass

    label('loc_3188')

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

    def _loc_3273(): pass

    label('loc_3273')

    Jump('loc_3B2D')

    def _loc_3276(): pass

    label('loc_3276')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_33BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_32FB',
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

    Jump('loc_33B8')

    def _loc_32FB(): pass

    label('loc_32FB')

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

    def _loc_33B8(): pass

    label('loc_33B8')

    Jump('loc_3B2D')

    def _loc_33BB(): pass

    label('loc_33BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3532',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3471',
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

    Jump('loc_352F')

    def _loc_3471(): pass

    label('loc_3471')

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

    def _loc_352F(): pass

    label('loc_352F')

    Jump('loc_3B2D')

    def _loc_3532(): pass

    label('loc_3532')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_3725',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3630',
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

    Jump('loc_3722')

    def _loc_3630(): pass

    label('loc_3630')

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

    def _loc_3722(): pass

    label('loc_3722')

    Jump('loc_3B2D')

    def _loc_3725(): pass

    label('loc_3725')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_380F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3790',
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

    Jump('loc_380C')

    def _loc_3790(): pass

    label('loc_3790')

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

    def _loc_380C(): pass

    label('loc_380C')

    Jump('loc_3B2D')

    def _loc_380F(): pass

    label('loc_380F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_3965',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_387E',
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

    Jump('loc_3962')

    def _loc_387E(): pass

    label('loc_387E')

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

    def _loc_3962(): pass

    label('loc_3962')

    Jump('loc_3B2D')

    def _loc_3965(): pass

    label('loc_3965')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_39E4',
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

    Jump('loc_3B2D')

    def _loc_39E4(): pass

    label('loc_39E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3A93',
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

    Jump('loc_3B2D')

    def _loc_3A93(): pass

    label('loc_3A93')

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

    def _loc_3B2D(): pass

    label('loc_3B2D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x3B31
@scena.Code('func_0F_3B31')
def func_0F_3B31():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_3BE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_3B83',
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

    Jump('loc_3BE0')

    def _loc_3B83(): pass

    label('loc_3B83')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    OP_62(0x000F, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    PlaySE(47, 0x00, 0x64)
    Sleep(1000)

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

    def _loc_3BE0(): pass

    label('loc_3BE0')

    Jump('loc_3CEF')

    def _loc_3BE3(): pass

    label('loc_3BE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3CEF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_3C3C',
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

    Jump('loc_3CEF')

    def _loc_3C3C(): pass

    label('loc_3C3C')

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

    def _loc_3CEF(): pass

    label('loc_3CEF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x3CF3
@scena.Code('func_10_3CF3')
def func_10_3CF3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3E34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3D9F',
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

    Jump('loc_3E31')

    def _loc_3D9F(): pass

    label('loc_3D9F')

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

    def _loc_3E31(): pass

    label('loc_3E31')

    Jump('loc_3EEE')

    def _loc_3E34(): pass

    label('loc_3E34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_3EEE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3E9D',
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

    Jump('loc_3EEE')

    def _loc_3E9D(): pass

    label('loc_3E9D')

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

    def _loc_3EEE(): pass

    label('loc_3EEE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x3EF2
@scena.Code('func_11_3EF2')
def func_11_3EF2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_3F79',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3F27',
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

    Jump('loc_3F76')

    def _loc_3F27(): pass

    label('loc_3F27')

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

    def _loc_3F76(): pass

    label('loc_3F76')

    Jump('loc_4041')

    def _loc_3F79(): pass

    label('loc_3F79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_4041',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3FDC',
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

    Jump('loc_4041')

    def _loc_3FDC(): pass

    label('loc_3FDC')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

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
            '为什么非要\n',
            '我给你的姐姐\n',
            '收拾床铺不可啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4041(): pass

    label('loc_4041')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

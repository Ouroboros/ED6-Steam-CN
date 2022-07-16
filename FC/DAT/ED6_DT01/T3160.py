import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3160_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3160   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乌缇'),
    TXT(0x02, '米优'),
    TXT(0x03, '加雷利'),
    TXT(0x04, '艾妲'),
    TXT(0x05, '呆呆'),
    TXT(0x06, '库诺'),
    TXT(0x07, '皮克塞恩教区长'),
    TXT(0x08, '修女琪爱拉'),
    TXT(0x09, '莱恩'),
    TXT(0x0A, '西加罗'),
    TXT(0x0B, '艾德尔'),
    TXT(0x0C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3160.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x32BF
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
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01400._CH', 'ED6_DT07/CH01400P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
    ]

# id: 0x10002 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 61430,
            z                   = 0,
            y                   = 45130,
            direction           = 345,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 54510,
            z                   = 0,
            y                   = 43560,
            direction           = 345,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
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
            talkScenaIndex      = 0x000E,
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
            talkScenaIndex      = 0x0005,
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
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x262
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x262
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x262
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 58950,
            triggerZ            = 1000,
            triggerY            = 50290,
            triggerRange        = 400,
            actorX              = 58800,
            actorZ              = 2500,
            actorY              = 52200,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x286
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2BC',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)

    Jump('loc_636')

    def _loc_2BC(): pass

    label('loc_2BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2F2',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)

    Jump('loc_636')

    def _loc_2F2(): pass

    label('loc_2F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_328',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)

    Jump('loc_636')

    def _loc_328(): pass

    label('loc_328')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_394',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 2, 0x552)),
            Expr.Return,
        ),
        'loc_365',
    )

    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 15690, 4000, 42960, 96)

    Jump('loc_37B')

    def _loc_365(): pass

    label('loc_365')

    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 60250, 1000, 51160, 270)

    def _loc_37B(): pass

    label('loc_37B')

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 61930, 0, 46550, 4)

    Jump('loc_636')

    def _loc_394(): pass

    label('loc_394')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3CA',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 57890, 0, 48010, 82)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 59610, 0, 47980, 274)

    Jump('loc_636')

    def _loc_3CA(): pass

    label('loc_3CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_43B',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 54110, 0, 42050, 20)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 55350, 0, 42050, 1)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    SetChrFlags(0x000E, 0x0010)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)

    Jump('loc_636')

    def _loc_43B(): pass

    label('loc_43B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_4A7',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 63500, 0, 46550, 348)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 62290, 0, 46560, 338)
    SetChrFlags(0x000B, 0x0010)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    SetChrFlags(0x000E, 0x0010)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)

    Jump('loc_636')

    def _loc_4A7(): pass

    label('loc_4A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_529',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 60350, 1000, 51110, 285)
    SetChrFlags(0x000B, 0x0010)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 60270, 1000, 52070, 281)
    SetChrFlags(0x000B, 0x0010)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 56260, 0, 45050, 348)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)

    Jump('loc_636')

    def _loc_529(): pass

    label('loc_529')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_575',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 56260, 0, 45050, 348)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)

    Jump('loc_636')

    def _loc_575(): pass

    label('loc_575')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_5D7',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 61490, 0, 45200, 2)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 62440, 0, 45200, 3)

    Jump('loc_636')

    def _loc_5D7(): pass

    label('loc_5D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_636',
    )

    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 61490, 0, 45200, 2)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 62440, 0, 45200, 3)

    def _loc_636(): pass

    label('loc_636')

    Return()

# id: 0x0001 offset: 0x637
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_641',
    )

    Jump('loc_6A6')

    def _loc_641(): pass

    label('loc_641')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_64B',
    )

    Jump('loc_6A6')

    def _loc_64B(): pass

    label('loc_64B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_655',
    )

    Jump('loc_6A6')

    def _loc_655(): pass

    label('loc_655')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_65F',
    )

    Jump('loc_6A6')

    def _loc_65F(): pass

    label('loc_65F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_66D',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_6A6')

    def _loc_66D(): pass

    label('loc_66D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_677',
    )

    Jump('loc_6A6')

    def _loc_677(): pass

    label('loc_677')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_681',
    )

    Jump('loc_6A6')

    def _loc_681(): pass

    label('loc_681')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_68B',
    )

    Jump('loc_6A6')

    def _loc_68B(): pass

    label('loc_68B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_695',
    )

    Jump('loc_6A6')

    def _loc_695(): pass

    label('loc_695')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_69F',
    )

    Jump('loc_6A6')

    def _loc_69F(): pass

    label('loc_69F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_6A6',
    )

    def _loc_6A6(): pass

    label('loc_6A6')

    Return()

# id: 0x0002 offset: 0x6A7
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6BC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_6BC(): pass

    label('loc_6BC')

    Return()

# id: 0x0003 offset: 0x6BD
@scena.Code('func_03_6BD')
def func_03_6BD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_721',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '终于到达蔡斯的礼拜堂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下我们的巡礼之旅\n',
            '只剩下格兰赛尔的大圣堂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_721(): pass

    label('loc_721')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x725
@scena.Code('func_04_725')
def func_04_725():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_7A5',
    )

    ChrTalk(
        0x00FE,
        (
            '和城里不同，\n',
            '礼拜堂真是出乎意料地简单呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有一些让人吃惊的隐藏功能吗？\n',
            '比如椅子可以自动旋转什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7A5(): pass

    label('loc_7A5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x7A9
@scena.Code('func_05_7A9')
def func_05_7A9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_826',
    )

    ChrTalk(
        0x00FE,
        (
            '你们是来向女神爱德丝请教\n',
            '今天的事情该如何处理的吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '在这种时候来到礼拜堂，\n',
            '你们也有什么烦恼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_826(): pass

    label('loc_826')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x82A
@scena.Code('func_06_82A')
def func_06_82A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_868',
    )

    TalkBegin(0x0008)

    ChrTalk(
        0x00FE,
        (
            '真是的，外面好吵，\n',
            '都没办法集中精神学习了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    def _loc_868(): pass

    label('loc_868')

    Return()

# id: 0x0007 offset: 0x869
@scena.Code('func_07_869')
def func_07_869():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_8F5',
    )

    ChrTalk(
        0x00FE,
        (
            '不管怎么说\n',
            '因为来到主日学校，\n',
            '我意想不到的认真呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，\n',
            '今天外头很热闹哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '人家本来还想好好学习呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8F5(): pass

    label('loc_8F5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x8F9
@scena.Code('func_08_8F9')
def func_08_8F9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_97F',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '接下来要去哪儿呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是个逍遥自在、\n',
            '漫无目的的流浪者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '随心所欲，走遍四方，\n',
            '过着自由的旅行生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EE')

    def _loc_97F(): pass

    label('loc_97F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_9EE',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '早上的祈祷\n',
            '一定要集中精神呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样闭着眼睛的话，\n',
            '就算导力停了都没有关系哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9EE(): pass

    label('loc_9EE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x9F2
@scena.Code('func_09_9F2')
def func_09_9F2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_A8C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_A34',
    )

    ChrTurnDirection(0x00FE, 0x000C, 400)

    ChrTalk(
        0x00FE,
        (
            '我说呆呆。\n',
            '马上就完了，乖一点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A89')

    def _loc_A34(): pass

    label('loc_A34')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '好不容易来一次，\n',
            '最好顺便去祈祷一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空之女神啊……\n',
            '谢谢您赐予的药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A89(): pass

    label('loc_A89')

    Jump('loc_B59')

    def _loc_A8C(): pass

    label('loc_A8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_B59',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_AFF',
    )

    ChrTalk(
        0x00FE,
        (
            '教区长您调制的药相当有效，\n',
            '在附近可是有口皆碑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是这种时候\n',
            '才能感受到教会的恩德呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B59')

    def _loc_AFF(): pass

    label('loc_AFF')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '不好意思，\n',
            '我还想要取些药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为肩部非常酸疼，\n',
            '导致现在连头也疼起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000B, 0x0010)

    def _loc_B59(): pass

    label('loc_B59')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0xB5D
@scena.Code('func_0A_B5D')
def func_0A_B5D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_B87',
    )

    ChrTalk(
        0x00FE,
        (
            '哥哥～\n',
            '这个真没意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BFA')

    def _loc_B87(): pass

    label('loc_B87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_BB2',
    )

    ChrTalk(
        0x00FE,
        (
            '呜呜，妈妈～\n',
            '我已经厌烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BFA')

    def _loc_BB2(): pass

    label('loc_BB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_BFA',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈，没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想，\n',
            '大概是因为肩膀的导力压变低了吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BFA(): pass

    label('loc_BFA')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0xBFE
@scena.Code('func_0B_BFE')
def func_0B_BFE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_C5D',
    )

    ChrTalk(
        0x00FE,
        (
            '呜～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么这些东西\n',
            '摆放得这么混乱呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，我想将它们重新摆一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C5D(): pass

    label('loc_C5D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0xC61
@scena.Code('func_0C_C61')
def func_0C_C61():
    Call(0, 0x000D)

    Return()

# id: 0x000D offset: 0xC66
@scena.Code('func_0D_C66')
def func_0D_C66():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 7, 0x557)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 6, 0x556)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1359',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0107, 57370, 1000, 52020, 90)
    SetChrPos(0x0102, 56420, 1000, 52490, 90)
    SetChrPos(0x0101, 56210, 1000, 51250, 90)
    SetChrPos(0x0108, 57250, 1000, 50620, 45)
    ChrTurnDirection(0x000E, 0x0107, 0)
    CameraMove(58050, 1000, 52120, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010081557V#006F教区长！\n',
            '『塞姆里亚苔藓』采到了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081558V哦哦……真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081559V那太好了。\n',
            '没想到你们这么快就采集到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081560V#560F那、那个……\n',
            '这样就可以做药了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081561V啊啊，当然可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081562V我到里面去配药，\n',
            '你们在此稍等片刻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(16290, 4000, 43670, 0)
    OP_67(0, 6330, -10000, 0)
    CameraSetDistance(3090, 0)
    OP_6C(41000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000E, 15590, 4000, 43000, 90)
    SetChrPos(0x000F, 15690, 4000, 41980, 45)
    OP_4A(0x000F, 255)

    @scena.Lambda('lambda_0E56')
    def lambda_0E56():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0E56')

    DispatchAsync2(0x0000, 0x0001, lambda_0E56)

    @scena.Lambda('lambda_0E67')
    def lambda_0E67():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0E67')

    DispatchAsync2(0x0001, 0x0001, lambda_0E67)

    @scena.Lambda('lambda_0E78')
    def lambda_0E78():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0E78')

    DispatchAsync2(0x0002, 0x0001, lambda_0E78)

    @scena.Lambda('lambda_0E89')
    def lambda_0E89():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0E89')

    DispatchAsync2(0x0003, 0x0001, lambda_0E89)

    SetChrPos(0x0101, 14110, 4000, 44580, 150)
    SetChrPos(0x0102, 14410, 4000, 45600, 176)
    SetChrPos(0x0107, 14890, 4000, 44370, 153)
    SetChrPos(0x0108, 15390, 4000, 45540, 176)
    Sleep(500)

    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#2010081563V#6P万物之根，源自七耀，\n',
            '圣化苍金，汇聚于此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081564V#6P女神圣礼，流转万物，\n',
            '净化活性，相融相成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'magic\\\\mg110_0.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 16260, 4100, 42980, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(
        0x000E,
        (
            '#2010081565V#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081566V#6P嗯……这样就完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0107, 400)

    @scena.Lambda('lambda_0FFF')
    def lambda_0FFF():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0FFF)

    @scena.Lambda('lambda_100D')
    def lambda_100D():
        CameraMove(16290, 4000, 44670, 1000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_100D)

    ChrWalkTo(0x000E, 14920, 4000, 43570, 1000, 0x00)
    ChrTurnDirection(0x000E, 0x0107, 400)

    ChrTalk(
        0x000E,
        (
            '#2010081567V给，拿去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x0365, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '亚鲁福灵药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0366, 1)
    ChrMoveTo(0x000E, 14940, 4000, 43280, 1000, 0x00)

    ChrTalk(
        0x0107,
        (
            '#0070081568V#560F哇……好漂亮的颜色！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081569V#501F这个是喝的药吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081570V啊啊，是内服药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081571V药的作用不在于清除毒的成分，\n',
            '而是通过大幅度提高患者的免疫力\n',
            '从而使之自然痊愈和康复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080081572V#070F哦……原来如此。\n',
            '和东方的医术也有共通之处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081573V这的确是源于东方的医术……\n',
            '可以说两者都是一脉相承的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081574V好了。\n',
            '快点把这药拿给那位伤者服用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081575V#001F嗯，好的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081576V#061F教区长！\n',
            '真的非常谢谢您！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)
    SetChrPos(0x0101, 11980, 2000, 47970, 270)
    SetChrPos(0x0102, 11980, 2000, 47970, 270)
    SetChrPos(0x0107, 11980, 2000, 47970, 270)
    SetChrPos(0x0108, 11980, 2000, 47970, 270)
    SetChrPos(0x000E, 59070, 1000, 52160, 180)
    SetChrPos(0x000F, 15690, 4000, 42960, 90)
    OP_4B(0x000F, 255)
    CameraMove(11980, 2000, 47970, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x00AA, 7, 0x557))
    OP_28(0x0042, 0x01, 0x0100)
    EventEnd(0x00)

    Jump('loc_2B0F')

    def _loc_1359(): pass

    label('loc_1359')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 1, 0x551)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A09',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0107, 57370, 1000, 52020, 90)
    SetChrPos(0x0102, 56420, 1000, 52490, 90)
    SetChrPos(0x0101, 56210, 1000, 51250, 90)
    ChrTurnDirection(0x000E, 0x0107, 0)
    OP_4A(0x000F, 255)
    CameraMove(58050, 1000, 52120, 1000)

    ChrTalk(
        0x000E,
        (
            '#2010081397V哎呀，这不是提妲吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081398V这么晚来这里有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081399V#068F那、那个，教区长！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081400V请您一定要\n',
            '救救阿加特大哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#2010081401V发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081402V#004F提、提妲，\n',
            '稍微冷静一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081403V#012F其实是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向教区长说明了\n',
            '阿加特中毒倒下以及他处于昏迷症状一事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x000F,
        (
            '#2020081404V竟然出了这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081405V唔……\n',
            '这下可伤脑筋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081406V#002F果、果然……\n',
            '很难治疗这种毒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081407V不，并不是这意思。\n',
            '所幸的是七耀教会那种能解\n',
            '所有神经毒药的配方至今仍流传下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081408V那种解药并非含有解毒的成分，\n',
            '而是一种通过增强患者的抵抗力\n',
            '而使其自然痊愈的药……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000F, 400)

    ChrTalk(
        0x000E,
        (
            '#2010081409V#1P琪爱拉修女，\n',
            '那种解药好像……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2020081410V是的……\n',
            '刚好药料已经用完了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081411V#069F怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081412V#012F药料……\n',
            '请问那是什么样的药料？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0107, 400)

    ChrTalk(
        0x000E,
        (
            '#2010081413V是以古代文明的名字为典故，\n',
            '被称为『塞姆里亚苔藓』的发光植物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081414V在蔡斯地区附近，\n',
            '也只有卡鲁迪亚隧道的钟乳洞里\n',
            '有这种珍稀的植物生长着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081415V以前我都是委托\n',
            '游击士协会帮忙采集的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081416V#505F卡鲁迪亚隧道……\n',
            '就是我们来蔡斯时所通过的\n',
            '那条超长地下隧道吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081417V#006F什～么嘛！\n',
            '这样的话不就好办了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081418V#010F我们马上前往钟乳洞\n',
            '采集『塞姆里亚苔藓』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081419V什么……你们要去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081420V#560F那个，教区长。\n',
            '姐姐他们是游击士协会的游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081421V原来如此……\n',
            '那么就交给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081422V总之去钟乳洞前，\n',
            '先去问问协会的负责人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081423V协会应该还保留着\n',
            '以前采集时所做的记录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081424V#006F嗯，知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081425V#010F谢谢您，我们就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00AA, 1, 0x551))
    OP_28(0x0042, 0x01, 0x0004)
    OP_28(0x0042, 0x01, 0x0008)
    OP_28(0x0042, 0x01, 0x0010)
    OP_4B(0x000F, 255)
    EventEnd(0x00)

    Jump('loc_2B0F')

    def _loc_1A09(): pass

    label('loc_1A09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1B89',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1A6C',
    )

    ChrTalk(
        0x000E,
        (
            '无论有什么烦恼，\n',
            '都可以到礼拜堂来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '为市民服务\n',
            '也是七耀教会的宗旨之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B86')

    def _loc_1A6C(): pass

    label('loc_1A6C')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000E,
        (
            '哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我们也要感谢教区长您呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '托教区长您的福，\n',
            '阿加特他现在好了很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F承蒙您的照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不不不，\n',
            '我也只是尽了应尽的义务罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '以后无论有什么烦恼，\n',
            '都可以到礼拜堂来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '为市民服务\n',
            '也是七耀教会的宗旨之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B86(): pass

    label('loc_1B86')

    Jump('loc_2B0F')

    def _loc_1B89(): pass

    label('loc_1B89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1ECA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 1, 0x579)),
            Expr.Return,
        ),
        'loc_1BFA',
    )

    ChrTalk(
        0x000E,
        (
            '虽说身上的毒已经祛除了，\n',
            '但他的身体状况还没有完全恢复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '一定要叮嘱他\n',
            '不要太过勉强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EC7')

    def _loc_1BFA(): pass

    label('loc_1BFA')

    SetScenaFlags(ScenaFlag(0x00AF, 1, 0x579))

    ChrTalk(
        0x0107,
        (
            '#060F啊，教区长大人！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '太感谢您的药了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '哦，是提妲大小姐啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '后来他没什么事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F药……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊……是的，没事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '阿加特大哥哥的药，\n',
            '就是这位皮克塞恩教区长\n',
            '给我们调制的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……给别人添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F真是的，\n',
            '还是不会道声谢呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '为什么不诚恳一些\n',
            '向教区长表示感谢呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔， \n',
            '你也不要总是顶嘴啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '哎呀～\n',
            '竟然已经可以站起来走路了……\n',
            '不愧是游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '但是，毕竟还没有完全恢复。\n',
            '千万不要太勉强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F啊，是自己的身体嘛。\n',
            '我是最了解不过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……说太多话了。\n',
            '我们该走了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊。\n',
            '确实是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那再见了，教区长大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '提妲大小姐……\n',
            '你也要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '………是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EC7(): pass

    label('loc_1EC7')

    Jump('loc_2B0F')

    def _loc_1ECA(): pass

    label('loc_1ECA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_21D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 0, 0x578)),
            Expr.Return,
        ),
        'loc_1F29',
    )

    ChrTalk(
        0x000E,
        (
            '我也会在这里\n',
            '祈愿阿加特早日康复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '再有什么事的话，\n',
            '随时都可以过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D5')

    def _loc_1F29(): pass

    label('loc_1F29')

    SetScenaFlags(ScenaFlag(0x00AF, 0, 0x578))

    ChrTalk(
        0x000E,
        (
            '哦，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '怎么样？药有效果吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是的，病情总算是稳住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '中央工房的米妮亚姆医生说，\n',
            '阿加特兄已经脱离危险期了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '是吗？渡过危险期了？\n',
            '这样一来我也就稍稍安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，我想没问题的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为病人\n',
            '可是那个阿加特呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我也是这么想的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '要是比起体力的话，\n',
            '他一定和金先生有一拼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F不过，\n',
            '这次真的是麻烦教区长您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么晚突然跑过来，\n',
            '还让您给我们配药……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '那个时候，\n',
            '提妲大小姐那么紧张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '一贯内向的那个孩子\n',
            '也会那样拼命地诉说自己的请求，\n',
            '我想不管是谁看到都会帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我也会在这里\n',
            '祈愿阿加特早日康复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160864V#000F嗯，非常感谢您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100495V#010F真是帮了我们大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '呵呵，再有什么事的话，\n',
            '随时都可以过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21D5(): pass

    label('loc_21D5')

    Jump('loc_2B0F')

    def _loc_21D8(): pass

    label('loc_21D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_234E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 7, 0x557)),
            Expr.Return,
        ),
        'loc_2281',
    )

    ChrTalk(
        0x000E,
        (
            '这种解药并非含有解毒的成分，\n',
            '而是一种通过增强患者抵抗力使其自然痊愈的药……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '对于未知的毒药\n',
            '应该也能起到一些作用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '好了，你们赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234B')

    def _loc_2281(): pass

    label('loc_2281')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 2, 0x552)),
            Expr.Return,
        ),
        'loc_22E1',
    )

    ChrTalk(
        0x000E,
        (
            '那么，我们在这边\n',
            '先做一下调药的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '钟乳洞里面十分危险。\n',
            '你们千万要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234B')

    def _loc_22E1(): pass

    label('loc_22E1')

    ChrTalk(
        0x000E,
        (
            '#2010081422V总之去钟乳洞前，\n',
            '先去问问协会的负责人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2010081423V协会应该还保留着\n',
            '以前采集时所做的记录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_234B(): pass

    label('loc_234B')

    Jump('loc_2B0F')

    def _loc_234E(): pass

    label('loc_234E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2415',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_23AE',
    )

    ChrTalk(
        0x000E,
        (
            '事态的发展似乎很严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '正是在这种非常时期，\n',
            '我们更要振作起来才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2412')

    def _loc_23AE(): pass

    label('loc_23AE')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000E,
        (
            '事态的发展似乎很严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽然目前还没收到有伤者的报告，\n',
            '但最好还是准备些药物比较稳妥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2412(): pass

    label('loc_2412')

    Jump('loc_2B0F')

    def _loc_2415(): pass

    label('loc_2415')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_24BB',
    )

    ChrTalk(
        0x000E,
        (
            '……在时间的洪流中，\n',
            '作为『钟表之城』的蔡斯市\n',
            '已经完成了它伟大的使命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '以蔡斯为中心生产的导力器\n',
            '在各地全面普及，\n',
            '给利贝尔王国带来一场导力革命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B0F')

    def _loc_24BB(): pass

    label('loc_24BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2502',
    )

    ChrTalk(
        0x000E,
        (
            '空之女神爱德丝啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '请给予广大民众\n',
            '保佑和引导……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B0F')

    def _loc_2502(): pass

    label('loc_2502')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_266A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_25A5',
    )

    ChrTalk(
        0x000E,
        (
            '虽然我也很明白\n',
            '修女琪爱拉那份要好好爱护\n',
            '礼拜堂这种祈祷之地的心情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '但我想比起别的，\n',
            '教会不就该是个\n',
            '让有困难的人可以安心落脚的地方吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2667')

    def _loc_25A5(): pass

    label('loc_25A5')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000E,
        (
            '向人们提供传统医疗的服务\n',
            '也是礼拜堂的重要职责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '除了医疗，\n',
            '还有大家都头疼的小孩教育问题……\n',
            '教会的使命有很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '对社会做出贡献是\n',
            '未来的七耀教会必须承担的责任。\n',
            '我是这样想的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2667(): pass

    label('loc_2667')

    Jump('loc_2B0F')

    def _loc_266A(): pass

    label('loc_266A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2860',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_26D3',
    )

    ChrTalk(
        0x000E,
        (
            '如果可以的话，\n',
            '就经常来找我谈谈心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '遇到什么麻烦的事情，\n',
            '也可以尽管来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_285D')

    def _loc_26D3(): pass

    label('loc_26D3')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000E,
        (
            '早上好啊，提妲大小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不……\n',
            '你什么都不用说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '总之昨晚真是一团糟啊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F呜……\n',
            '对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '哎呀，你用不着道歉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '为了进步试验是必不可少的，\n',
            '而试验也往往伴随着失败。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这个城市的人们\n',
            '对此都十分地理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '提妲，\n',
            '今后你也要好好协助博士哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F……是，教区长大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '如果可以的话，\n',
            '就经常来找我谈谈心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '遇到什么麻烦的事情，\n',
            '也可以尽管来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_285D(): pass

    label('loc_285D')

    Jump('loc_2B0F')

    def _loc_2860(): pass

    label('loc_2860')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2A8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_28C3',
    )

    ChrTalk(
        0x000E,
        (
            '要是有用得着的地方\n',
            '就尽管到这里来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '教会并不是\n',
            '只为了祈祷而设立的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A8A')

    def _loc_28C3(): pass

    label('loc_28C3')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2904',
    )

    ChrTalk(
        0x000E,
        (
            '嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这个小姑娘\n',
            '不就是提妲大小姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2945')

    def _loc_2904(): pass

    label('loc_2904')

    ChrTalk(
        0x000E,
        (
            '哦哦，提妲大小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我觉得好像有很久\n',
            '都没有见到过你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2945(): pass

    label('loc_2945')

    ChrTalk(
        0x0107,
        (
            '#060F您好，教区长大人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '你也和爷爷一样\n',
            '总是一天到晚地忙碌呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过，工作告一段落之后，\n',
            '还得来主日学校学习哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '你毕竟还是个孩子啊。\n',
            '多花点时间和同龄的朋友\n',
            '一起玩耍也是很有必要的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嗯，是的。\n',
            '我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嗯，如果需要什么帮助的话，\n',
            '就尽管到这里来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '教会并不是只为了\n',
            '祈祷而设立的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A8A(): pass

    label('loc_2A8A')

    Jump('loc_2B0F')

    def _loc_2A8D(): pass

    label('loc_2A8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2B0F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2AC1',
    )

    ChrTalk(
        0x000E,
        (
            '当然，\n',
            '来祈祷的话更是欢迎啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B0F')

    def _loc_2AC1(): pass

    label('loc_2AC1')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000E,
        (
            '欢迎来到七耀教会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '从恋爱的烦恼到胃疼，\n',
            '任何事情都可以找我商量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B0F(): pass

    label('loc_2B0F')

    TalkEnd(0x000E)

    Return()

# id: 0x000E offset: 0x2B13
@scena.Code('func_0E_2B13')
def func_0E_2B13():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2BA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2B68',
    )

    ChrTalk(
        0x00FE,
        (
            '今后也欢迎\n',
            '随时光临教会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只不过， \n',
            '来了就请好好祈祷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BA4')

    def _loc_2B68(): pass

    label('loc_2B68')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '啊，欢迎来到七耀教会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有什么事\n',
            '就请尽管说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BA4(): pass

    label('loc_2BA4')

    Jump('loc_329D')

    def _loc_2BA7(): pass

    label('loc_2BA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2C51',
    )

    ChrTalk(
        0x00FE,
        (
            '药似乎很有效果呢。\n',
            '不愧是皮克塞恩教区长大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拯救别人的生命，\n',
            '果然是件了不起的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我重新考虑了一下，\n',
            '这样做对于传播教会的智慧\n',
            '也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329D')

    def _loc_2C51(): pass

    label('loc_2C51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2DCE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2CF0',
    )

    ChrTalk(
        0x00FE,
        (
            '像昨天晚上那种情况，\n',
            '我不知道教区长的想法\n',
            '到底是不是正确的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我还是认为\n',
            '过来拿药的时候才顺便祈祷一下，\n',
            '这种做法不能原谅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DCB')

    def _loc_2CF0(): pass

    label('loc_2CF0')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '像昨天晚上那种情况，\n',
            '我不知道教区长的想法\n',
            '到底是不是正确的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因为得到了大家信赖，\n',
            '在紧急时刻，\n',
            '大家才会来拜托教会吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，不过我还是认为\n',
            '过来拿药的时候才顺便祈祷一下，\n',
            '这种做法不能原谅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DCB(): pass

    label('loc_2DCB')

    Jump('loc_329D')

    def _loc_2DCE(): pass

    label('loc_2DCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_2F22',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 7, 0x557)),
            Expr.Return,
        ),
        'loc_2E31',
    )

    ChrTalk(
        0x00FE,
        (
            '请不要耽误时间，\n',
            '尽快把药送过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也会祈祷患者\n',
            '能够尽快恢复健康。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F1F')

    def _loc_2E31(): pass

    label('loc_2E31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 2, 0x552)),
            Expr.Return,
        ),
        'loc_2E9F',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '难道你们已经找到材料了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '教区长大人已经做好调药的准备了。\n',
            '请把材料交给教区长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F1F')

    def _loc_2E9F(): pass

    label('loc_2E9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 1, 0x551)),
            Expr.Return,
        ),
        'loc_2EE4',
    )

    ChrTalk(
        0x00FE,
        (
            '我们先进行着\n',
            '调制药水的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各位，路上请当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F1F')

    def _loc_2EE4(): pass

    label('loc_2EE4')

    ChrTalk(
        0x00FE,
        (
            '啊，各位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都已经夜深了，\n',
            '来教会有什么指教吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F1F(): pass

    label('loc_2F1F')

    Jump('loc_329D')

    def _loc_2F22(): pass

    label('loc_2F22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2F72',
    )

    ChrTalk(
        0x00FE,
        (
            '工房那边\n',
            '似乎出了什么事呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过详细的情况\n',
            '我还不太清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329D')

    def _loc_2F72(): pass

    label('loc_2F72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_3058',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2FCF',
    )

    ChrTalk(
        0x00FE,
        (
            '为什么今天\n',
            '城里那么吵闹呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孩子们好像也是\n',
            '一副坐立不安的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3055')

    def _loc_2FCF(): pass

    label('loc_2FCF')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '今天主日学校的课\n',
            '讲的是这个城市的历史。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '从刚才开始就觉得城里就很吵闹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孩子们好像也是\n',
            '一副坐立不安的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3055(): pass

    label('loc_3055')

    Jump('loc_329D')

    def _loc_3058(): pass

    label('loc_3058')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_30CF',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才还以为是有人来祈祷呢，\n',
            '原来是来取药的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '教区长应该对他们说说\n',
            '让他们能更常来祈祷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329D')

    def _loc_30CF(): pass

    label('loc_30CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_31F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3142',
    )

    ChrTalk(
        0x00FE,
        (
            '我想教会毕竟是个\n',
            '怀着虔诚的心祈祷的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去的话，\n',
            '教会都要变成观光地或者药店了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31EE')

    def _loc_3142(): pass

    label('loc_3142')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '蔡斯的市民们\n',
            '每个人都很忙\n',
            '很少有人会来教会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '教区长对于那些\n',
            '来教会却做别的事情的人\n',
            '也会热情地接待……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我还是觉得\n',
            '教会毕竟是个怀着虔诚的心祈祷的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31EE(): pass

    label('loc_31EE')

    Jump('loc_329D')

    def _loc_31F1(): pass

    label('loc_31F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_325B',
    )

    ChrTalk(
        0x00FE,
        (
            '昨晚真是不得了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房\n',
            '好像已经一团糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那种时候\n',
            '就应该静下心来祈祷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329D')

    def _loc_325B(): pass

    label('loc_325B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_329D',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到七耀教会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请各位\n',
            '虔诚地祈祷一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_329D(): pass

    label('loc_329D')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

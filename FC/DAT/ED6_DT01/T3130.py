import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3130_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3130   ._SN')

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
    header.mapModel       = 'T3130.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x23EC
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
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
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

    Jump('loc_63D')

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

    Jump('loc_63D')

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

    Jump('loc_63D')

    def _loc_328(): pass

    label('loc_328')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_374',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 61930, 0, 46550, 4)

    Jump('loc_63D')

    def _loc_374(): pass

    label('loc_374')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3AA',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 57890, 0, 48010, 82)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 59610, 0, 47980, 274)

    Jump('loc_63D')

    def _loc_3AA(): pass

    label('loc_3AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_442',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 61010, 0, 48400, 306)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 60100, 0, 46860, 7)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 57910, 0, 47170, 0)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 56780, 0, 47520, 45)
    SetChrFlags(0x000C, 0x0010)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    SetChrFlags(0x000E, 0x0010)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)

    Jump('loc_63D')

    def _loc_442(): pass

    label('loc_442')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_4AE',
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

    Jump('loc_63D')

    def _loc_4AE(): pass

    label('loc_4AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_530',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 60350, 1000, 51110, 285)
    SetChrFlags(0x000C, 0x0010)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 60270, 1000, 52070, 281)
    SetChrFlags(0x000B, 0x0010)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 56260, 0, 45050, 348)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)

    Jump('loc_63D')

    def _loc_530(): pass

    label('loc_530')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_57C',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 56260, 0, 45050, 348)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)

    Jump('loc_63D')

    def _loc_57C(): pass

    label('loc_57C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_5DE',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 58420, 0, 47750, 0)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 59620, 0, 47750, 0)

    Jump('loc_63D')

    def _loc_5DE(): pass

    label('loc_5DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_63D',
    )

    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 63690, 0, 48900, 231)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 59070, 1000, 52160, 164)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 58420, 0, 47750, 0)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 59620, 0, 47750, 0)

    def _loc_63D(): pass

    label('loc_63D')

    Return()

# id: 0x0001 offset: 0x63E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_656',
    )

    OP_B1('t3130_y')

    Jump('loc_65F')

    def _loc_656(): pass

    label('loc_656')

    OP_B1('t3130_n')

    def _loc_65F(): pass

    label('loc_65F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_669',
    )

    Jump('loc_6CE')

    def _loc_669(): pass

    label('loc_669')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_673',
    )

    Jump('loc_6CE')

    def _loc_673(): pass

    label('loc_673')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_67D',
    )

    Jump('loc_6CE')

    def _loc_67D(): pass

    label('loc_67D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_687',
    )

    Jump('loc_6CE')

    def _loc_687(): pass

    label('loc_687')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_695',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_6CE')

    def _loc_695(): pass

    label('loc_695')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_69F',
    )

    Jump('loc_6CE')

    def _loc_69F(): pass

    label('loc_69F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_6A9',
    )

    Jump('loc_6CE')

    def _loc_6A9(): pass

    label('loc_6A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_6B3',
    )

    Jump('loc_6CE')

    def _loc_6B3(): pass

    label('loc_6B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_6BD',
    )

    Jump('loc_6CE')

    def _loc_6BD(): pass

    label('loc_6BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_6C7',
    )

    Jump('loc_6CE')

    def _loc_6C7(): pass

    label('loc_6C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_6CE',
    )

    def _loc_6CE(): pass

    label('loc_6CE')

    Return()

# id: 0x0002 offset: 0x6CF
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6E4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_6E4(): pass

    label('loc_6E4')

    Return()

# id: 0x0003 offset: 0x6E5
@scena.Code('func_03_6E5')
def func_03_6E5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_740',
    )

    ChrTalk(
        0x00FE,
        (
            '从格兰赛尔开始的利贝尔巡礼之旅\n',
            '到这里就要结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，感慨颇深啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_740(): pass

    label('loc_740')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x744
@scena.Code('func_04_744')
def func_04_744():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_7C4',
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

    def _loc_7C4(): pass

    label('loc_7C4')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x7C8
@scena.Code('func_05_7C8')
def func_05_7C8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_845',
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

    def _loc_845(): pass

    label('loc_845')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x849
@scena.Code('func_06_849')
def func_06_849():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_87C',
    )

    TalkBegin(0x0008)

    ChrTalk(
        0x00FE,
        (
            '……哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '温丝跑到哪里去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    def _loc_87C(): pass

    label('loc_87C')

    Return()

# id: 0x0007 offset: 0x87D
@scena.Code('func_07_87D')
def func_07_87D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_909',
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

    def _loc_909(): pass

    label('loc_909')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x90D
@scena.Code('func_08_90D')
def func_08_90D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_993',
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

    Jump('loc_A02')

    def _loc_993(): pass

    label('loc_993')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_A02',
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

    def _loc_A02(): pass

    label('loc_A02')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xA06
@scena.Code('func_09_A06')
def func_09_A06():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_AA0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_A48',
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

    Jump('loc_A9D')

    def _loc_A48(): pass

    label('loc_A48')

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

    def _loc_A9D(): pass

    label('loc_A9D')

    Jump('loc_B6D')

    def _loc_AA0(): pass

    label('loc_AA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_B6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_B13',
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

    Jump('loc_B6D')

    def _loc_B13(): pass

    label('loc_B13')

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

    def _loc_B6D(): pass

    label('loc_B6D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0xB71
@scena.Code('func_0A_B71')
def func_0A_B71():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_B9B',
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

    Jump('loc_C0E')

    def _loc_B9B(): pass

    label('loc_B9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_BC6',
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

    Jump('loc_C0E')

    def _loc_BC6(): pass

    label('loc_BC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_C0E',
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

    def _loc_C0E(): pass

    label('loc_C0E')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0xC12
@scena.Code('func_0B_C12')
def func_0B_C12():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_C71',
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

    def _loc_C71(): pass

    label('loc_C71')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0xC75
@scena.Code('func_0C_C75')
def func_0C_C75():
    Call(0, 0x000D)

    Return()

# id: 0x000D offset: 0xC7A
@scena.Code('func_0D_C7A')
def func_0D_C7A():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_E02',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_CE0',
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

    Jump('loc_DFF')

    def _loc_CE0(): pass

    label('loc_CE0')

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
            '#001F我们也要感谢教区长您呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#006F托教区长您的福，\n',
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

    def _loc_DFF(): pass

    label('loc_DFF')

    Jump('loc_1CAC')

    def _loc_E02(): pass

    label('loc_E02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_115B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 1, 0x579)),
            Expr.Return,
        ),
        'loc_E73',
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

    Jump('loc_1158')

    def _loc_E73(): pass

    label('loc_E73')

    SetScenaFlags(ScenaFlag(0x00AF, 1, 0x579))
    ChrTurnDirection(0x000E, 0x0107, 0)

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
            '#052F药……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F啊……是的，没事了。',
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
            '#053F是吗……',
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
            '#509F真是的，\n',
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
            '#015F艾丝蒂尔， \n',
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
            '#053F………………',
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
            '#064F………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#061F………是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1158(): pass

    label('loc_1158')

    Jump('loc_1CAC')

    def _loc_115B(): pass

    label('loc_115B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1469',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 0, 0x578)),
            Expr.Return,
        ),
        'loc_11BA',
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

    Jump('loc_1466')

    def _loc_11BA(): pass

    label('loc_11BA')

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
            '#019F我也是这么想的。',
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
            '#506F不过，\n',
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
            '#0010150603V#001F嗯，非常感谢您。',
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

    def _loc_1466(): pass

    label('loc_1466')

    Jump('loc_1CAC')

    def _loc_1469(): pass

    label('loc_1469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_14DD',
    )

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

    Jump('loc_1CAC')

    def _loc_14DD(): pass

    label('loc_14DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_15A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_153D',
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

    Jump('loc_15A1')

    def _loc_153D(): pass

    label('loc_153D')

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

    def _loc_15A1(): pass

    label('loc_15A1')

    Jump('loc_1CAC')

    def _loc_15A4(): pass

    label('loc_15A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_164A',
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

    Jump('loc_1CAC')

    def _loc_164A(): pass

    label('loc_164A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1691',
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

    Jump('loc_1CAC')

    def _loc_1691(): pass

    label('loc_1691')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_17F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1734',
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

    Jump('loc_17F6')

    def _loc_1734(): pass

    label('loc_1734')

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

    def _loc_17F6(): pass

    label('loc_17F6')

    Jump('loc_1CAC')

    def _loc_17F9(): pass

    label('loc_17F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_19F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1862',
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

    Jump('loc_19F3')

    def _loc_1862(): pass

    label('loc_1862')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ChrTurnDirection(0x000E, 0x0107, 0)

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
            '#065F呜……\n',
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
            '#066F……是，教区长大人。',
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

    def _loc_19F3(): pass

    label('loc_19F3')

    Jump('loc_1CAC')

    def _loc_19F6(): pass

    label('loc_19F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1C2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1A59',
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

    Jump('loc_1C27')

    def _loc_1A59(): pass

    label('loc_1A59')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AA1',
    )

    ChrTurnDirection(0x000E, 0x0107, 0)

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

    Jump('loc_1AE2')

    def _loc_1AA1(): pass

    label('loc_1AA1')

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

    def _loc_1AE2(): pass

    label('loc_1AE2')

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

    def _loc_1C27(): pass

    label('loc_1C27')

    Jump('loc_1CAC')

    def _loc_1C2A(): pass

    label('loc_1C2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1CAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1C5E',
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

    Jump('loc_1CAC')

    def _loc_1C5E(): pass

    label('loc_1C5E')

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

    def _loc_1CAC(): pass

    label('loc_1CAC')

    TalkEnd(0x000E)

    Return()

# id: 0x000E offset: 0x1CB0
@scena.Code('func_0E_1CB0')
def func_0E_1CB0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1D44',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1D05',
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

    Jump('loc_1D41')

    def _loc_1D05(): pass

    label('loc_1D05')

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

    def _loc_1D41(): pass

    label('loc_1D41')

    Jump('loc_23CA')

    def _loc_1D44(): pass

    label('loc_1D44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1DEE',
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

    Jump('loc_23CA')

    def _loc_1DEE(): pass

    label('loc_1DEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1F6B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1E8D',
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

    Jump('loc_1F68')

    def _loc_1E8D(): pass

    label('loc_1E8D')

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

    def _loc_1F68(): pass

    label('loc_1F68')

    Jump('loc_23CA')

    def _loc_1F6B(): pass

    label('loc_1F6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_204F',
    )

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

    Jump('loc_23CA')

    def _loc_204F(): pass

    label('loc_204F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_209F',
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

    Jump('loc_23CA')

    def _loc_209F(): pass

    label('loc_209F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2185',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_20FC',
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

    Jump('loc_2182')

    def _loc_20FC(): pass

    label('loc_20FC')

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

    def _loc_2182(): pass

    label('loc_2182')

    Jump('loc_23CA')

    def _loc_2185(): pass

    label('loc_2185')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_21FC',
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

    Jump('loc_23CA')

    def _loc_21FC(): pass

    label('loc_21FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_231E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_226F',
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

    Jump('loc_231B')

    def _loc_226F(): pass

    label('loc_226F')

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

    def _loc_231B(): pass

    label('loc_231B')

    Jump('loc_23CA')

    def _loc_231E(): pass

    label('loc_231E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2388',
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

    Jump('loc_23CA')

    def _loc_2388(): pass

    label('loc_2388')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_23CA',
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

    def _loc_23CA(): pass

    label('loc_23CA')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

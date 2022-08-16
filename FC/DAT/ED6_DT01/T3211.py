import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3211_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3211   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3211.x'
    header.mapIndex       = 1
    header.bgm            = 84
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
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '拜舍尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '艾德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '林',
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
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '莉西亚',
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
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '希利尔',
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
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '艾缇',
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
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '拉克',
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
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '希玛',
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
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '库安',
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
            talkScenaIndex      = 0x000B,
        ),
    )

# id: 0x10002 offset: 0x21A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x21A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x21A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x21A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_255',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 1960, 250, 8900, 0)
    ChrSetFlags(0x000C, 0x0010)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)

    Jump('loc_4AA')

    def _loc_255(): pass

    label('loc_255')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_28B',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 3430, 0, 4050, 11)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)

    Jump('loc_4AA')

    def _loc_28B(): pass

    label('loc_28B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2C1',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -3460, 250, 8840, 350)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)

    Jump('loc_4AA')

    def _loc_2C1(): pass

    label('loc_2C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_32A',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -1330, 250, 8540, 104)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 33700, 250, 7700, 171)
    ChrTurnDirection(0x000A, 0x000B, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 1880, 250, 8350, 276)

    Jump('loc_4AA')

    def _loc_32A(): pass

    label('loc_32A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_3A4',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 3820, 0, 2790, 100)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)
    ChrSetFlags(0x000A, 0x0010)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetChipByIndex(0x000B, 9)
    TerminateThread(0x000B, 0x00)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetPos(0x000B, 29020, 250, 7120, 270)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 2530, 0, 4070, 6)

    Jump('loc_4AA')

    def _loc_3A4(): pass

    label('loc_3A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_3C4',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 29020, 250, 7010, 255)

    Jump('loc_4AA')

    def _loc_3C4(): pass

    label('loc_3C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_410',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 3430, 0, 4050, 11)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 29020, 250, 7010, 255)

    Jump('loc_4AA')

    def _loc_410(): pass

    label('loc_410')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_472',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 27220, 250, 6680, 96)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 29020, 250, 7010, 255)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 3430, 0, 4050, 11)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)

    Jump('loc_4AA')

    def _loc_472(): pass

    label('loc_472')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_4AA',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -2080, 250, 6150, 195)
    ChrSetFlags(0x000C, 0x0010)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)

    def _loc_4AA(): pass

    label('loc_4AA')

    Return()

# id: 0x0001 offset: 0x4AB
@scena.Code('func_01_4AB')
def func_01_4AB():
    Return()

# id: 0x0002 offset: 0x4AC
@scena.Code('func_02_4AC')
def func_02_4AC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4C1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_4AC')

    def _loc_4C1(): pass

    label('loc_4C1')

    Return()

# id: 0x0003 offset: 0x4C2
@scena.Code('func_03_4C2')
def func_03_4C2():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x4C9
@scena.Code('func_04_4C9')
def func_04_4C9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_4D6',
    )

    Jump('loc_545')

    def _loc_4D6(): pass

    label('loc_4D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_4E0',
    )

    Jump('loc_545')

    def _loc_4E0(): pass

    label('loc_4E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_4EA',
    )

    Jump('loc_545')

    def _loc_4EA(): pass

    label('loc_4EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_4F4',
    )

    Jump('loc_545')

    def _loc_4F4(): pass

    label('loc_4F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_4FE',
    )

    Jump('loc_545')

    def _loc_4FE(): pass

    label('loc_4FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_508',
    )

    Jump('loc_545')

    def _loc_508(): pass

    label('loc_508')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_512',
    )

    Jump('loc_545')

    def _loc_512(): pass

    label('loc_512')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_53E',
    )

    ChrTalk(
        0x00FE,
        (
            '喂～～林。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '给我杯茶～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_545')

    def _loc_53E(): pass

    label('loc_53E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_545',
    )

    def _loc_545(): pass

    label('loc_545')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x549
@scena.Code('func_05_549')
def func_05_549():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_656',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_5E8',
    )

    ChrTalk(
        0x00FE,
        (
            '村子里这么安静\n',
            '是因为今天没有观光的客人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是因为这样\n',
            '我女儿一直睡到现在才起床。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真是的，\n',
            '要不要给她找点活干干呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_653')

    def _loc_5E8(): pass

    label('loc_5E8')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '是因为今天没有观光的客人吗。\n',
            '村子里这么安静……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望在诞辰庆典之前\n',
            '不要再发生什么事情就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_653(): pass

    label('loc_653')

    Jump('loc_ADB')

    def _loc_656(): pass

    label('loc_656')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_767',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_6DB',
    )

    ChrTalk(
        0x00FE,
        (
            '对家庭主妇来说，\n',
            '比起关心外面的事，\n',
            '今晩要做的菜才更重要呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管外面发生什么，\n',
            '女儿一到晚上\n',
            '肚子都会饿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_764')

    def _loc_6DB(): pass

    label('loc_6DB')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '马上就是女王的诞辰庆典了。\n',
            '可是，最近到处都不太平啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……算了， \n',
            '在意这种事也没用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是想想\n',
            '今天晚上做什么饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_764(): pass

    label('loc_764')

    Jump('loc_ADB')

    def _loc_767(): pass

    label('loc_767')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_7E2',
    )

    ChrTalk(
        0x00FE,
        (
            '蔡斯那边好像\n',
            '发生了不得了的大事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近外边那么乱，\n',
            '真是可怕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还好这个村子\n',
            '什么事都没发生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADB')

    def _loc_7E2(): pass

    label('loc_7E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_832',
    )

    ChrTalk(
        0x00FE,
        (
            '我说，莉西亚。\n',
            '你也稍微精神点呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我忍着睡意\n',
            '给你做早饭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADB')

    def _loc_832(): pass

    label('loc_832')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_8F4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_88D',
    )

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '真是散漫的女儿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直和年轻时的丈夫一样，\n',
            '真让人头疼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8F1')

    def _loc_88D(): pass

    label('loc_88D')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrSetDirection(0x000A, 0, 400)

    ChrTalk(
        0x00FE,
        (
            '莉西亚！\n',
            '别光喊肚子饿，\n',
            '你也来帮帮忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不然还要\n',
            '等很久才能把饭做完。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 400)

    def _loc_8F1(): pass

    label('loc_8F1')

    Jump('loc_ADB')

    def _loc_8F4(): pass

    label('loc_8F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_8FE',
    )

    Jump('loc_ADB')

    def _loc_8FE(): pass

    label('loc_8FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_A07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_963',
    )

    ChrTalk(
        0x00FE,
        (
            '为什么非要让\n',
            '忙得不可开交的我来倒茶啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要喝茶，\n',
            '就不能自己去倒吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A04')

    def _loc_963(): pass

    label('loc_963')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '我还以为丈夫和女儿吃完了饭\n',
            '就会没事了的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们吃完后谁也不收拾，\n',
            '结果洗盘子的活儿还是由我来做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……总是这样，\n',
            '就不能放过我一次吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A04(): pass

    label('loc_A04')

    Jump('loc_ADB')

    def _loc_A07(): pass

    label('loc_A07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_ADB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_A67',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '该开始准备中午饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '调味料快要用完了。\n',
            '一会儿去买点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADB')

    def _loc_A67(): pass

    label('loc_A67')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '我的丈夫\n',
            '是旅馆里的厨师哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他做的东方料理\n',
            '在旅行者中很受欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连旅游指南里面\n',
            '也有这方面的记载。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ADB(): pass

    label('loc_ADB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xADF
@scena.Code('func_06_ADF')
def func_06_ADF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_AEC',
    )

    Jump('loc_CDD')

    def _loc_AEC(): pass

    label('loc_AEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_AF6',
    )

    Jump('loc_CDD')

    def _loc_AF6(): pass

    label('loc_AF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_B00',
    )

    Jump('loc_CDD')

    def _loc_B00(): pass

    label('loc_B00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_B7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_B39',
    )

    ChrTalk(
        0x00FE,
        (
            '呼啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是没有睡够呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B79')

    def _loc_B39(): pass

    label('loc_B39')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '呼啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸从早上开始什么都不干，\n',
            '也不起床。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B79(): pass

    label('loc_B79')

    Jump('loc_CDD')

    def _loc_B7C(): pass

    label('loc_B7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_BE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_BC4',
    )

    ChrTalk(
        0x00FE,
        (
            '妈～妈，我肚子饿了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我已经\n',
            '快要饿死了啦～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE6')

    def _loc_BC4(): pass

    label('loc_BC4')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '妈妈～～\n',
            '饭还没做好吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE6(): pass

    label('loc_BE6')

    Jump('loc_CDD')

    def _loc_BE9(): pass

    label('loc_BE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_C84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_C36',
    )

    ChrTalk(
        0x00FE,
        (
            '呜，已经晚上啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～讨厌～\n',
            '天变黑了。\n',
            '好可怕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C81')

    def _loc_C36(): pass

    label('loc_C36')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '呜，好寂寞啊。\n',
            '可是还要看家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，好饿啊。\n',
            '妈妈快点回来吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C81(): pass

    label('loc_C81')

    Jump('loc_CDD')

    def _loc_C84(): pass

    label('loc_C84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_C8E',
    )

    Jump('loc_CDD')

    def _loc_C8E(): pass

    label('loc_C8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_CD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_CB7',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，还有饭后点心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD3')

    def _loc_CB7(): pass

    label('loc_CB7')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '妈妈～\n',
            '我也要喝茶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD3(): pass

    label('loc_CD3')

    Jump('loc_CDD')

    def _loc_CD6(): pass

    label('loc_CD6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_CDD',
    )

    def _loc_CDD(): pass

    label('loc_CDD')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xCE1
@scena.Code('func_07_CE1')
def func_07_CE1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_D76',
    )

    ChrTalk(
        0x00FE,
        (
            '今天真难得，\n',
            '都没有客人啊。\n',
            '我也可以休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这样一来\n',
            '『红叶亭』就更冷清了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下的诞辰庆典\n',
            '真是很吸引游客啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1155')

    def _loc_D76(): pass

    label('loc_D76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_D80',
    )

    Jump('loc_1155')

    def _loc_D80(): pass

    label('loc_D80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_E4F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_DDD',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '我差不多该去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，无论如何，\n',
            '希望早日抓住那些犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E4C')

    def _loc_DDD(): pass

    label('loc_DDD')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '关于蔡斯的事件，\n',
            '听说犯人好像还没抓到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蔡斯市离军队的要塞很近，\n',
            '本来以为那里会很安全的，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E4C(): pass

    label('loc_E4C')

    Jump('loc_1155')

    def _loc_E4F(): pass

    label('loc_E4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_EB6',
    )

    ChrTurnDirection(0x00FE, 0x000E, 0)

    ChrTalk(
        0x00FE,
        (
            '好了，拉克。\n',
            '赶快吃早饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再这么磨磨蹭蹭的话，\n',
            '爸爸连你的那份也要吃了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1155')

    def _loc_EB6(): pass

    label('loc_EB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_FEC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_F16',
    )

    ChrTurnDirection(0x00FE, 0x000E, 0)

    ChrTalk(
        0x00FE,
        (
            '好，拉克。\n',
            '那么面包就交给你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为接下来\n',
            '爸爸要准备炖菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE9')

    def _loc_F16(): pass

    label('loc_F16')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我以前也在蔡斯住，\n',
            '不过我还是\n',
            '更喜欢这个村子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '生下这个孩子的时候，\n',
            '我和妻子艾缇搬到这里住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蔡斯那边确实便利，\n',
            '但是我觉得自己\n',
            '还是适合这边的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每天能泡温泉\n',
            '也是这里的一大魅力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FE9(): pass

    label('loc_FE9')

    Jump('loc_1155')

    def _loc_FEC(): pass

    label('loc_FEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_FF6',
    )

    Jump('loc_1155')

    def _loc_FF6(): pass

    label('loc_FF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_1000',
    )

    Jump('loc_1155')

    def _loc_1000(): pass

    label('loc_1000')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_100A',
    )

    Jump('loc_1155')

    def _loc_100A(): pass

    label('loc_100A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1155',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_10C3',
    )

    ChrTalk(
        0x00FE,
        (
            '其实我也是\n',
            '『红叶亭』的客房工作人员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那真是个很好的旅馆啊。\n',
            '希望你们有机会一定来住住看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，\n',
            '这种话由我这个工作人员说出来，\n',
            '听起来就像在打广告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1155')

    def _loc_10C3(): pass

    label('loc_10C3')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '你们是想找住宿的地方吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『红叶亭』旅馆就在贮水池那边，\n',
            '村子的另一头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那真是个很好的旅馆啊。\n',
            '希望你们有机会一定来住住看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1155(): pass

    label('loc_1155')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1159
@scena.Code('func_08_1159')
def func_08_1159():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1166',
    )

    Jump('loc_1335')

    def _loc_1166(): pass

    label('loc_1166')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1250',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_11C0',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '要开始准备晚饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊……这么说来， \n',
            '今天做什么菜好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_124D')

    def _loc_11C0(): pass

    label('loc_11C0')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '刚才在外边\n',
            '看见拉克他们了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小孩子就是有精神啊。\n',
            '发生了那样的事件，\n',
            '也还在外边活蹦乱跳的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得\n',
            '自己也被他们感染了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_124D(): pass

    label('loc_124D')

    Jump('loc_1335')

    def _loc_1250(): pass

    label('loc_1250')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_125A',
    )

    Jump('loc_1335')

    def _loc_125A(): pass

    label('loc_125A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1264',
    )

    Jump('loc_1335')

    def _loc_1264(): pass

    label('loc_1264')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_126E',
    )

    Jump('loc_1335')

    def _loc_126E(): pass

    label('loc_126E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_1278',
    )

    Jump('loc_1335')

    def _loc_1278(): pass

    label('loc_1278')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_132E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_12D3',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，\n',
            '炖菜需要重新热一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '再多加一种蔬菜进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_132B')

    def _loc_12D3(): pass

    label('loc_12D3')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '午休的时候必须要预先准备晚饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我们家两个大人平时都要外出工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_132B(): pass

    label('loc_132B')

    Jump('loc_1335')

    def _loc_132E(): pass

    label('loc_132E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1335',
    )

    def _loc_1335(): pass

    label('loc_1335')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1339
@scena.Code('func_09_1339')
def func_09_1339():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1346',
    )

    Jump('loc_1493')

    def _loc_1346(): pass

    label('loc_1346')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1350',
    )

    Jump('loc_1493')

    def _loc_1350(): pass

    label('loc_1350')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_135A',
    )

    Jump('loc_1493')

    def _loc_135A(): pass

    label('loc_135A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_13B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1393',
    )

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……呼唔唔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13B5')

    def _loc_1393(): pass

    label('loc_1393')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '呼唔～……\n',
            '还是很瞌睡啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13B5(): pass

    label('loc_13B5')

    Jump('loc_1493')

    def _loc_13B8(): pass

    label('loc_13B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_146E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1417',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸很不擅长家务活。\n',
            '做起来毛手毛脚的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样也能\n',
            '在旅馆里工作吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_146B')

    def _loc_1417(): pass

    label('loc_1417')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ChrTurnDirection(0x00FE, 0x000C, 0)

    ChrTalk(
        0x00FE,
        (
            '喂，爸爸。\n',
            '先把炖菜热一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后趁那段时间\n',
            '做面包不就好了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_146B(): pass

    label('loc_146B')

    Jump('loc_1493')

    def _loc_146E(): pass

    label('loc_146E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_1478',
    )

    Jump('loc_1493')

    def _loc_1478(): pass

    label('loc_1478')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_1482',
    )

    Jump('loc_1493')

    def _loc_1482(): pass

    label('loc_1482')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_148C',
    )

    Jump('loc_1493')

    def _loc_148C(): pass

    label('loc_148C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1493',
    )

    def _loc_1493(): pass

    label('loc_1493')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1497
@scena.Code('func_0A_1497')
def func_0A_1497():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x149E
@scena.Code('func_0B_149E')
def func_0B_149E():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

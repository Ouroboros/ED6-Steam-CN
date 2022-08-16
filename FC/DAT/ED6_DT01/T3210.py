import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3210_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3210   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3210.x'
    header.mapIndex       = 1
    header.bgm            = 15
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
        ('ED6_DT07/CH01273._CH', 'ED6_DT07/CH01273P._CP'),
        ('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP'),
    ]

# id: 0x10001 offset: 0x102
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

# id: 0x10002 offset: 0x222
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x222
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x222
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x222
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_258',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 1750, 250, 8900, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)

    Jump('loc_4C0')

    def _loc_258(): pass

    label('loc_258')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_28E',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 3430, 0, 4050, 11)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)

    Jump('loc_4C0')

    def _loc_28E(): pass

    label('loc_28E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2C4',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -3460, 250, 8840, 350)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)

    Jump('loc_4C0')

    def _loc_2C4(): pass

    label('loc_2C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_32D',
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

    Jump('loc_4C0')

    def _loc_32D(): pass

    label('loc_32D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_394',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 3820, 0, 2790, 100)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)
    ChrSetFlags(0x000A, 0x0010)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 29020, 250, 7010, 255)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 2530, 0, 4070, 6)

    Jump('loc_4C0')

    def _loc_394(): pass

    label('loc_394')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_3B4',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 28000, 250, 5350, 0)

    Jump('loc_4C0')

    def _loc_3B4(): pass

    label('loc_3B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_413',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 3430, 0, 4050, 11)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetChipByIndex(0x000B, 10)
    TerminateThread(0x000B, 0x00)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetPos(0x000B, 29020, 250, 7120, 270)

    Jump('loc_4C0')

    def _loc_413(): pass

    label('loc_413')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_48D',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0010)
    ChrSetPos(0x0009, 28090, 0, 8600, 180)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetChipByIndex(0x000B, 10)
    TerminateThread(0x000B, 0x00)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetPos(0x000B, 29020, 250, 7120, 270)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 3430, 0, 4050, 11)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)

    Jump('loc_4C0')

    def _loc_48D(): pass

    label('loc_48D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_4C0',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -3600, 250, 8850, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 27020, 0, 2570, 277)

    def _loc_4C0(): pass

    label('loc_4C0')

    Return()

# id: 0x0001 offset: 0x4C1
@scena.Code('func_01_4C1')
def func_01_4C1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4D9',
    )

    OP_B1('t3210_y')

    Jump('loc_4E2')

    def _loc_4D9(): pass

    label('loc_4D9')

    OP_B1('t3210_n')

    def _loc_4E2(): pass

    label('loc_4E2')

    Return()

# id: 0x0002 offset: 0x4E3
@scena.Code('func_02_4E3')
def func_02_4E3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4F8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_4E3')

    def _loc_4F8(): pass

    label('loc_4F8')

    Return()

# id: 0x0003 offset: 0x4F9
@scena.Code('func_03_4F9')
def func_03_4F9():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x500
@scena.Code('func_04_500')
def func_04_500():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_50D',
    )

    Jump('loc_57C')

    def _loc_50D(): pass

    label('loc_50D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_517',
    )

    Jump('loc_57C')

    def _loc_517(): pass

    label('loc_517')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_521',
    )

    Jump('loc_57C')

    def _loc_521(): pass

    label('loc_521')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_52B',
    )

    Jump('loc_57C')

    def _loc_52B(): pass

    label('loc_52B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_535',
    )

    Jump('loc_57C')

    def _loc_535(): pass

    label('loc_535')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_53F',
    )

    Jump('loc_57C')

    def _loc_53F(): pass

    label('loc_53F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_549',
    )

    Jump('loc_57C')

    def _loc_549(): pass

    label('loc_549')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_575',
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

    Jump('loc_57C')

    def _loc_575(): pass

    label('loc_575')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_57C',
    )

    def _loc_57C(): pass

    label('loc_57C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x580
@scena.Code('func_05_580')
def func_05_580():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_68D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_61F',
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

    Jump('loc_68A')

    def _loc_61F(): pass

    label('loc_61F')

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

    def _loc_68A(): pass

    label('loc_68A')

    Jump('loc_B5F')

    def _loc_68D(): pass

    label('loc_68D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_79E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_712',
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

    Jump('loc_79B')

    def _loc_712(): pass

    label('loc_712')

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

    def _loc_79B(): pass

    label('loc_79B')

    Jump('loc_B5F')

    def _loc_79E(): pass

    label('loc_79E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_819',
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

    Jump('loc_B5F')

    def _loc_819(): pass

    label('loc_819')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_870',
    )

    ChrTurnDirection(0x00FE, 0x000B, 0)

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

    Jump('loc_B5F')

    def _loc_870(): pass

    label('loc_870')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_924',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_8CB',
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

    Jump('loc_921')

    def _loc_8CB(): pass

    label('loc_8CB')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

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

    def _loc_921(): pass

    label('loc_921')

    Jump('loc_B5F')

    def _loc_924(): pass

    label('loc_924')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_92E',
    )

    Jump('loc_B5F')

    def _loc_92E(): pass

    label('loc_92E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 0, 0x520)),
            Expr.Return,
        ),
        'loc_961',
    )

    ChrTalk(
        0x00FE,
        (
            '真希望丈夫\n',
            '吃完饭能把盘子收拾一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B5F')

    def _loc_961(): pass

    label('loc_961')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_A8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_9C6',
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

    Jump('loc_A88')

    def _loc_9C6(): pass

    label('loc_9C6')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
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
    OP_62(0x000A, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '……干脆我就放着不收拾算了，\n',
            '看他们父女俩怎么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A88(): pass

    label('loc_A88')

    Jump('loc_B5F')

    def _loc_A8B(): pass

    label('loc_A8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_B5F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_AEB',
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

    Jump('loc_B5F')

    def _loc_AEB(): pass

    label('loc_AEB')

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

    def _loc_B5F(): pass

    label('loc_B5F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xB63
@scena.Code('func_06_B63')
def func_06_B63():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_B70',
    )

    Jump('loc_D89')

    def _loc_B70(): pass

    label('loc_B70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_B7A',
    )

    Jump('loc_D89')

    def _loc_B7A(): pass

    label('loc_B7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_B84',
    )

    Jump('loc_D89')

    def _loc_B84(): pass

    label('loc_B84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_C00',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_BBD',
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

    Jump('loc_BFD')

    def _loc_BBD(): pass

    label('loc_BBD')

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

    def _loc_BFD(): pass

    label('loc_BFD')

    Jump('loc_D89')

    def _loc_C00(): pass

    label('loc_C00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_C6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_C48',
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

    Jump('loc_C6A')

    def _loc_C48(): pass

    label('loc_C48')

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

    def _loc_C6A(): pass

    label('loc_C6A')

    Jump('loc_D89')

    def _loc_C6D(): pass

    label('loc_C6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_D08',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_CBA',
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

    Jump('loc_D05')

    def _loc_CBA(): pass

    label('loc_CBA')

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

    def _loc_D05(): pass

    label('loc_D05')

    Jump('loc_D89')

    def _loc_D08(): pass

    label('loc_D08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 0, 0x520)),
            Expr.Return,
        ),
        'loc_D3A',
    )

    ChrTalk(
        0x00FE,
        (
            '那～么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在要玩点什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D89')

    def _loc_D3A(): pass

    label('loc_D3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_D82',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_D63',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，还有饭后点心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D7F')

    def _loc_D63(): pass

    label('loc_D63')

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

    def _loc_D7F(): pass

    label('loc_D7F')

    Jump('loc_D89')

    def _loc_D82(): pass

    label('loc_D82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_D89',
    )

    def _loc_D89(): pass

    label('loc_D89')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xD8D
@scena.Code('func_07_D8D')
def func_07_D8D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_E22',
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

    Jump('loc_1200')

    def _loc_E22(): pass

    label('loc_E22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_E2C',
    )

    Jump('loc_1200')

    def _loc_E2C(): pass

    label('loc_E2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_EFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_E89',
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

    Jump('loc_EF8')

    def _loc_E89(): pass

    label('loc_E89')

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

    def _loc_EF8(): pass

    label('loc_EF8')

    Jump('loc_1200')

    def _loc_EFB(): pass

    label('loc_EFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_F62',
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

    Jump('loc_1200')

    def _loc_F62(): pass

    label('loc_F62')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_1098',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_FC2',
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

    Jump('loc_1095')

    def _loc_FC2(): pass

    label('loc_FC2')

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

    def _loc_1095(): pass

    label('loc_1095')

    Jump('loc_1200')

    def _loc_1098(): pass

    label('loc_1098')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_10A2',
    )

    Jump('loc_1200')

    def _loc_10A2(): pass

    label('loc_10A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_10AC',
    )

    Jump('loc_1200')

    def _loc_10AC(): pass

    label('loc_10AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_10B6',
    )

    Jump('loc_1200')

    def _loc_10B6(): pass

    label('loc_10B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1200',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_116E',
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
            '哈哈，这种话由我这个工作人员说出来，\n',
            '听起来就像在打广告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1200')

    def _loc_116E(): pass

    label('loc_116E')

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

    def _loc_1200(): pass

    label('loc_1200')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1204
@scena.Code('func_08_1204')
def func_08_1204():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1211',
    )

    Jump('loc_13E0')

    def _loc_1211(): pass

    label('loc_1211')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_12FB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_126B',
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

    Jump('loc_12F8')

    def _loc_126B(): pass

    label('loc_126B')

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

    def _loc_12F8(): pass

    label('loc_12F8')

    Jump('loc_13E0')

    def _loc_12FB(): pass

    label('loc_12FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1305',
    )

    Jump('loc_13E0')

    def _loc_1305(): pass

    label('loc_1305')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_130F',
    )

    Jump('loc_13E0')

    def _loc_130F(): pass

    label('loc_130F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_1319',
    )

    Jump('loc_13E0')

    def _loc_1319(): pass

    label('loc_1319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_1323',
    )

    Jump('loc_13E0')

    def _loc_1323(): pass

    label('loc_1323')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_13D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_137E',
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

    Jump('loc_13D6')

    def _loc_137E(): pass

    label('loc_137E')

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

    def _loc_13D6(): pass

    label('loc_13D6')

    Jump('loc_13E0')

    def _loc_13D9(): pass

    label('loc_13D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_13E0',
    )

    def _loc_13E0(): pass

    label('loc_13E0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x13E4
@scena.Code('func_09_13E4')
def func_09_13E4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_13F1',
    )

    Jump('loc_153E')

    def _loc_13F1(): pass

    label('loc_13F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_13FB',
    )

    Jump('loc_153E')

    def _loc_13FB(): pass

    label('loc_13FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1405',
    )

    Jump('loc_153E')

    def _loc_1405(): pass

    label('loc_1405')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1463',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_143E',
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

    Jump('loc_1460')

    def _loc_143E(): pass

    label('loc_143E')

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

    def _loc_1460(): pass

    label('loc_1460')

    Jump('loc_153E')

    def _loc_1463(): pass

    label('loc_1463')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_1519',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_14C2',
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

    Jump('loc_1516')

    def _loc_14C2(): pass

    label('loc_14C2')

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

    def _loc_1516(): pass

    label('loc_1516')

    Jump('loc_153E')

    def _loc_1519(): pass

    label('loc_1519')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_1523',
    )

    Jump('loc_153E')

    def _loc_1523(): pass

    label('loc_1523')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_152D',
    )

    Jump('loc_153E')

    def _loc_152D(): pass

    label('loc_152D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1537',
    )

    Jump('loc_153E')

    def _loc_1537(): pass

    label('loc_1537')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_153E',
    )

    def _loc_153E(): pass

    label('loc_153E')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1542
@scena.Code('func_0A_1542')
def func_0A_1542():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1549
@scena.Code('func_0B_1549')
def func_0B_1549():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

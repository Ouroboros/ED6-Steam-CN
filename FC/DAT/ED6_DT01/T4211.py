import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4211_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4211   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4211.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
    ]

# id: 0x10001 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '理查德上校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '凯诺娜上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '杜南公爵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '管家菲利普',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '克劳斯市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '科林兹校长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '索蕾拉',
            x                   = -1020,
            z                   = 0,
            y                   = 85000,
            direction           = 175,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '妮舒',
            x                   = -2500,
            z                   = 0,
            y                   = 76500,
            direction           = 53,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '布莉姆',
            x                   = 2500,
            z                   = 0,
            y                   = 81150,
            direction           = 255,
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
            name                = '艾科尔',
            x                   = -5950,
            z                   = 0,
            y                   = 68110,
            direction           = 272,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x2B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2B2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2B2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_2C0',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_07_985)

    def _loc_2C0(): pass

    label('loc_2C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2EA',
    )

    ChrSetChipByIndex(0x0000, 9)
    ChrSetChipByIndex(0x0001, 10)
    ChrSetChipByIndex(0x0138, 11)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_2EA(): pass

    label('loc_2EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_308',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_369')

    def _loc_308(): pass

    label('loc_308')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_31C',
    )

    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)

    Jump('loc_369')

    def _loc_31C(): pass

    label('loc_31C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_33A',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_369')

    def _loc_33A(): pass

    label('loc_33A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_358',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_369')

    def _loc_358(): pass

    label('loc_358')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_362',
    )

    Jump('loc_369')

    def _loc_362(): pass

    label('loc_362')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_369',
    )

    def _loc_369(): pass

    label('loc_369')

    Return()

# id: 0x0001 offset: 0x36A
@scena.Code('func_01_36A')
def func_01_36A():
    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x374
@scena.Code('func_02_374')
def func_02_374():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_389',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_374')

    def _loc_389(): pass

    label('loc_389')

    Return()

# id: 0x0003 offset: 0x38A
@scena.Code('func_03_38A')
def func_03_38A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_397',
    )

    Jump('loc_49B')

    def _loc_397(): pass

    label('loc_397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3F7',
    )

    ChrTalk(
        0x00FE,
        (
            '因为诞辰庆典，\n',
            '今天大街上很热闹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要不是还有工作，\n',
            '也会出去好好玩玩的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49B')

    def _loc_3F7(): pass

    label('loc_3F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_401',
    )

    Jump('loc_49B')

    def _loc_401(): pass

    label('loc_401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_40B',
    )

    Jump('loc_49B')

    def _loc_40B(): pass

    label('loc_40B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_440',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '茜亚和希尔丹夫人到哪儿去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49B')

    def _loc_440(): pass

    label('loc_440')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_49B',
    )

    ChrTalk(
        0x00FE,
        (
            '还要让客人们专程\n',
            '来陪公爵他消磨时间，\n',
            '真是够麻烦的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明大家都那么忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49B(): pass

    label('loc_49B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x49F
@scena.Code('func_04_49F')
def func_04_49F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_4AC',
    )

    Jump('loc_5E7')

    def _loc_4AC(): pass

    label('loc_4AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4B6',
    )

    Jump('loc_5E7')

    def _loc_4B6(): pass

    label('loc_4B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_4C0',
    )

    Jump('loc_5E7')

    def _loc_4C0(): pass

    label('loc_4C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_4CA',
    )

    Jump('loc_5E7')

    def _loc_4CA(): pass

    label('loc_4CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_520',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '理查德上校实在是帅呆了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和那个公爵相比\n',
            '根本就是天壤之别嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E7')

    def _loc_520(): pass

    label('loc_520')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_5E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_579',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '公爵用那双讨厌的眼睛\n',
            '在我身上转来转去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，太无礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E7')

    def _loc_579(): pass

    label('loc_579')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '刚才在走廊上\n',
            '和杜南公爵擦肩而过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公爵他用\n',
            '那双讨厌的眼睛\n',
            '在我身上转来转去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，太无礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E7(): pass

    label('loc_5E7')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x5EB
@scena.Code('func_05_5EB')
def func_05_5EB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_5F8',
    )

    Jump('loc_69D')

    def _loc_5F8(): pass

    label('loc_5F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_602',
    )

    Jump('loc_69D')

    def _loc_602(): pass

    label('loc_602')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_60C',
    )

    Jump('loc_69D')

    def _loc_60C(): pass

    label('loc_60C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_616',
    )

    Jump('loc_69D')

    def _loc_616(): pass

    label('loc_616')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_657',
    )

    ChrTalk(
        0x00FE,
        (
            '终于结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快收拾好东西，\n',
            '早点回家去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_69D')

    def _loc_657(): pass

    label('loc_657')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_69D',
    )

    ChrTalk(
        0x00FE,
        (
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对不起呀，\n',
            '我现在正忙着晚宴的准备工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_69D(): pass

    label('loc_69D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x6A1
@scena.Code('func_06_6A1')
def func_06_6A1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_6AE',
    )

    Jump('loc_981')

    def _loc_6AE(): pass

    label('loc_6AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_77E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_710',
    )

    ChrTalk(
        0x00FE,
        (
            '特务部队的队长\n',
            '取下面具之后，\n',
            '真是帅呆了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，\n',
            '为何他要戴面具呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77B')

    def _loc_710(): pass

    label('loc_710')

    ChrTalk(
        0x00FE,
        (
            '我悄悄对你们说哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特务部队的队长\n',
            '取下面具之后，\n',
            '真是帅呆了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，\n',
            '为何他要戴面具呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_77B(): pass

    label('loc_77B')

    Jump('loc_981')

    def _loc_77E(): pass

    label('loc_77E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_788',
    )

    Jump('loc_981')

    def _loc_788(): pass

    label('loc_788')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_792',
    )

    Jump('loc_981')

    def _loc_792(): pass

    label('loc_792')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_884',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_805',
    )

    ChrTalk(
        0x00FE,
        (
            '公爵喝醉之后\n',
            '会变得更加无耻下流……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直不敢相信他和女王陛下\n',
            '还有公主殿下是同一血脉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_881')

    def _loc_805(): pass

    label('loc_805')

    ChrTalk(
        0x00FE,
        (
            '我悄悄对你们说哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公爵喝醉之后\n',
            '会变得更加无耻下流……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直不敢相信他和女王陛下\n',
            '还有公主殿下是同一血脉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_881(): pass

    label('loc_881')

    Jump('loc_981')

    def _loc_884(): pass

    label('loc_884')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_981',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8FE',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然人手已经足够了，\n',
            '但公爵还要叫希尔丹夫人\n',
            '不断增加侍女的数量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正他肯定是\n',
            '不怀什么好意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_981')

    def _loc_8FE(): pass

    label('loc_8FE')

    ChrTalk(
        0x00FE,
        (
            '我悄悄对你们说哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然人手已经足够了，\n',
            '但公爵还要叫希尔丹夫人\n',
            '不断增加侍女的数量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正他肯定是\n',
            '不怀什么好意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_981(): pass

    label('loc_981')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x985
@scena.Code('func_07_985')
def func_07_985():
    EventBegin(0x00)
    CameraMove(1430, 30, 80070, 0)
    OP_67(0, 5440, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(44000, 0)
    OP_6E(371, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000C, -2450, 0, 82370, 90)
    ChrSetPos(0x000D, -2450, 0, 79820, 90)
    ChrSetPos(0x000E, -2450, 0, 77340, 90)
    ChrSetPos(0x0010, -2450, 0, 74860, 90)
    ChrSetPos(0x000F, -3070, 0, 74030, 90)
    ChrSetPos(0x0108, 2490, 0, 79820, 270)
    ChrSetPos(0x0102, 2490, 0, 74860, 270)
    ChrSetPos(0x0101, 2490, 0, 77340, 270)

    ChrTalk(
        0x0101,
        (
            '#000F啊……\n',
            '这就是晚餐会了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120612V可是为什么餐具是摆放好了的，\n',
            '关键的料理却没有呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120613V为何刀子和叉子\n',
            '要这样并排放在一起呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F因为这是很正式的晚宴啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120615V先是凉菜，然后接着\n',
            '就上各种各样的料理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120616V还有就是刀子和叉子\n',
            '要从侧边来拿着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F麻烦……\n',
            '这就是所谓的餐桌礼仪吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我还有些紧张了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#610F嘻嘻……\n',
            '不用那么在意的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120620V因为品尝料理的\n',
            '美味才是最重要的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120621V礼仪啊，礼貌的做法都是其次的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#600F对呀对呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120623V再说了，你们两人对\n',
            '在场出席的各位不都是\n',
            '很熟悉的吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120624V没有必要那么拘束嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F啊，说的也是啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这样一来就没办法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0361290003V#610F嘻嘻……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，那位朋友对于\n',
            '刀子和叉子习惯吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120628V我听说东方那边\n',
            '主要是使用筷子的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哦，您知道的很清楚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过俗话说得好，\n',
            '入乡随俗嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120631V虽说用的不好，但还是会一点\n',
            '用刀子和叉子的方法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#610F啊……很了不起呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120633V不愧是取得武术大会优胜的达人，\n',
            '说起话来都和普通人不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哈～哈～哈。\n',
            '哪里，您过奖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（确实是对美人没有抵抗力呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（可是我并不觉得\n',
            '他是一个喜好女色的人……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#800F话说回来……\n',
            '公爵大人真慢呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120638V究竟想要做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0340120639V#600F嗯……的确。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120640V而且如果说上座是公爵大人的，\n',
            '那么那边的座位又是谁的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0530850027V#780F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850028V科洛蒂娅公主座那里\n',
            '的可能性会比较高……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, -250, 0, 62670, 0)
    ChrSetPos(0x0009, 460, 0, 62290, 0)
    ChrSetPos(0x000A, -110, 0, 64099, 0)
    ChrSetPos(0x000B, 10, 0, 62670, 0)

    @scena.Lambda('lambda_1097')
    def lambda_1097():
        CameraMove(370, 0, 72370, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1097)

    Sleep(1000)

    @scena.Lambda('lambda_10B4')
    def lambda_10B4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_10B4)

    @scena.Lambda('lambda_10C6')
    def lambda_10C6():
        ChrWalkTo(0x00FE, 10, 0, 66950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_10C6)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_10E6')
    def lambda_10E6():
        ChrWalkTo(0x00FE, -2190, 0, 67060, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_10E6)

    WaitForThreadExit(0x000B, 0x0001)
    ChrSetDirection(0x000B, 0, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x000B,
        (
            '#720F各位……\n',
            '让你们久等了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '公爵大人大驾光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    @scena.Lambda('lambda_114D')
    def lambda_114D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_114D)

    @scena.Lambda('lambda_115F')
    def lambda_115F():
        ChrWalkTo(0x00FE, -140, 0, 69090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_115F)

    Sleep(300)

    @scena.Lambda('lambda_117F')
    def lambda_117F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_117F)

    @scena.Lambda('lambda_1191')
    def lambda_1191():
        ChrWalkTo(0x00FE, 1080, 0, 68670, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1191)

    Sleep(600)

    @scena.Lambda('lambda_11B1')
    def lambda_11B1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_11B1)

    @scena.Lambda('lambda_11C3')
    def lambda_11C3():
        ChrWalkTo(0x00FE, 400, 0, 67340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_11C3)

    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0640120645V#220F哎呀，诸位，\n',
            '让你们等那么久真是不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120646V因为稍稍协商了一下，\n',
            '所以拖延了一会儿时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0008, 400)

    ChrTalk(
        0x000A,
        (
            '#220F这位是理查德上校。\n',
            '王国军情报部的负责人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120648V为了解决恐怖事件，\n',
            '他日夜操劳，尽心尽力，\n',
            '作为礼节我就邀请他来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0130120649V#110F初次与大家见面。\n',
            '我是王国军情报部的理查德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120650V承蒙公爵大人的好意，\n',
            '邀请我来参加晚宴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120651V这身与这里不相称的军服有些失礼了，\n',
            '但还请允许我与各位同席。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000A, 0x01, 0x00, func_0A_2E29)
    Sleep(300)

    Sleep(100)

    @scena.Lambda('lambda_13BF')
    def lambda_13BF():
        CameraMove(330, 60, 81510, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13BF)

    CreateThread(0x0008, 0x01, 0x00, func_08_2DB5)
    Sleep(200)

    CreateThread(0x000B, 0x01, 0x00, func_0B_2E81)
    Sleep(200)

    CreateThread(0x0009, 0x01, 0x00, func_09_2DF9)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#000F（竟、竟然会和上校一起\n',
            '在餐桌上用餐……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（虽然猜到了几分，\n',
            '但果然还是些紧张……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    CameraMove(50, 1210, 79220, 0)
    OP_67(0, 2920, -10000, 0)
    CameraSetDistance(2090, 0)
    OP_6C(0, 0)
    OP_6E(424, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#220F哈～哈～哈，哎呀，愉快愉快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '怎么样，梅贝尔市长。\n',
            '王城格兰赛尔这儿的厨艺如何？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120656V与柏斯的『安特洛丝』\n',
            '相比也毫不逊色对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#610F嗯，很精妙的厨艺呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120658V搭配上葡萄酒可以说是完美了，\n',
            '出乎预料的出类拔萃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F哈～哈～哈，既然都这么说\n',
            '肯定就不是吹牛的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如何，你是叫金对吧，\n',
            '东方人对于这些感觉不大合胃口吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120661V#070F哪里，非常美味啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120662V虽说在下的舌头很迟钝，\n',
            '但也感觉得出其中蕴涵的美味。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120663V品味出了利贝尔\n',
            '料理的精髓所在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F嗯嗯，说得好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '怎么样啊，两位年轻的游击士？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120666V这样豪华的料理\n',
            '今天还是第一次吃到吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F唔－嗯，的确\n',
            '非常非常美味啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120668V邀请的人姑且不论如何，\n',
            '就这个料理真的很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F哈～哈～哈。\n',
            '说的好，说的好啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#010F哦，实在是\n',
            '很棒的料理呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120672V而且至今为止我们还没有\n',
            '这样正式的被邀请入席的机会，\n',
            '还很是有些不习惯呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '承蒙您的款待，\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F哈～哈～哈。\n',
            '你很会说话嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过经管家的提醒，\n',
            '我总算是想起来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120676V你们两位曾经在卢安的事件中\n',
            '和我见过一面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120677V缘分这个东西真是奇妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哈、哈哈……是－是呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（管家没有提醒之前\n',
            '难道就没有想起来吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F好啊，今晚不醉不归！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120681V料理和酒都是绰绰有余，\n',
            '不用有顾虑，想吃就尽管说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#110F公爵大人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0131090003V我们把之前谈到的内容\n',
            '先了结了如何呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F……哦哦！\n',
            '对啊，还有那些内容呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120685V#220F事实上把作为王国代表的诸位\n',
            '集中在这里没有什么别的意思……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120686V就是借这个晚宴的机会\n',
            '宣布一件重要的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#600F重大的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#800F这究竟……\n',
            '是什么样的事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120690V在这里先由理查德上校\n',
            '替我说明相关内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#110F……惶恐之至。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '女王陛下身体欠佳，\n',
            '是各位之前已知的事实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120693V不过陛下正在缓缓的康复中，\n',
            '很快就会以健康的状态与人民见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#600F哦……这就好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#610F那去探望陛下\n',
            '也是可以的了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#110F真对不起，照陛下的意向，\n',
            '还是希望暂时先谢绝探望。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0131090008V然而这几天扰乱王都周边\n',
            '秩序的恐怖组织，要先予以铲除。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120698V这件事成功之后，女王陛下\n',
            '的诞辰庆典才能按预定顺利进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0530850029V#780F嗯……这样能让市民们\n',
            '安居乐业，愉快的生活，\n',
            '真是值得庆贺的事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850030V不过，想要说的\n',
            '应该不止是这些吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#800F……是啊，如果只是这些的话，\n',
            '联络我们并说明就可以了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#110F呵呵，能察觉到就好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '女王陛下的健康状况正在恢复，\n',
            '之前也已经说到了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120704V陛下因为这次身体欠佳\n',
            '而下了一个决定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120705V那个决定就是——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#110F陛下自身退位，让在座的\n',
            '杜南公爵大人继承王位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(300)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(300)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(300)

    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(300)

    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x000E,
        (
            '#800F什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#610F真、真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（约修亚，这是……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（嗯……\n',
            '阴谋终于浮出水面了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F……我虽比较愚钝，\n',
            '不过很意外，陛下并没有轻视我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120712V并非是勉强，在这近４０年间，\n',
            '经历了动荡时期的利贝尔\n',
            '都是由一位女性来领导的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '基于这一点，在诞辰庆典之后\n',
            ' ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120714V转交王位的继承权\n',
            '的决定就是出于这样的原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0341330001V#600F竟然……陛下一直为此\n',
            '而深感苦恼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120716V每年见到她的时候\n',
            '都没能感觉到，是我们的不对啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#610F可、可是……\n',
            '怎能在这样一个觥筹交错的宴席\n',
            '宣布如此重大的决议呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120718V冒昧的问一句，这些究竟\n',
            '算不算数呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#110F哼哼，梅贝尔市长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120721V大人的话毫无信用可言，\n',
            '……这就你的本意吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#610F我、我没有那么说过！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360120723V可是通过市长的选举\n',
            '来表决王位的继承人\n',
            '的这项程序竟然会没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#800F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120725V可以的话，我们想直接\n',
            '向陛下询问一下刚才那些决议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F呜、呜－嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#110F各位的情绪动摇我很理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120728V不过还请冷静下来，\n',
            '暂且先知道就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0131090004V更进一步的来说，\n',
            '在诞辰庆典时将会由陛下自身\n',
            '来公布这项决议。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120730V是真是假到那时就可以\n',
            '见分晓了对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#800F这、这……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#110F问题在于公布这项决议时\n',
            '会给普通市民带来什么样的影响。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120733V为了避免无益的混乱，\n',
            '所以才把各地的负责人也就是在座的\n',
            '各位召集到这里来传达这项决议……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120734V公爵大人也是这么认为的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F咳咳……\n',
            '嗯，就是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#110F而且陛下如果退位了的话，\n',
            '这个消息肯定不止是滞留在国内。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120737V大陆各国，尤其是作为威胁的北方\n',
            '埃雷波尼亚肯定会注意到这个变动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120738V正因为如此，在座的各位\n',
            '应该扶植新的国王陛下，\n',
            '如果不团结起来是绝对不行的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120739V特别是在这样一个关键时期即将来临的时刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000C, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0010, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000D, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    ChrTalk(
        0x0101,
        (
            '#000F（居、居然说的如此\n',
            '冠冕堂皇……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（嗯……\n',
            '好一个煽动者啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000E)

    ChrTalk(
        0x000E,
        (
            '#800F正式的决定可以在诞辰庆典时\n',
            '向陛下直接请示……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120743V不过要事先做好心里准备，\n',
            '就是这样的对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0131090005V#110F哼哼……\n',
            '能够理解真是万幸啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000C)

    ChrTalk(
        0x000C,
        (
            '#600F唔－嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120746V一旦这件事情落实了，\n',
            '我们就有的忙碌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0010)

    ChrTalk(
        0x0010,
        (
            '#610F是呢……\n',
            '还要向市民们宣布。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000D)

    ChrTalk(
        0x000D,
        (
            '#0530850031V#780F……我还有一事相问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0530850032V#780F公爵大人具有王位的继承权\n',
            '这点我也承认……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850033V我认为具有同样资格的继承者\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#110F还有陛下的孙女\n',
            '科洛蒂娅殿下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120753V的确，依据王室典范的规定，\n',
            '她和公爵大人拥有同等资格……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120754V因为她的年纪还比较小，\n',
            '所以陛下就推选了公爵大人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且之前也说到过……\n',
            '对于女性都过于沉重的责任\n',
            '要一位小姑娘来承担是不行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F对呀对呀，就是这样的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，正在打算为科洛蒂娅\n',
            '公主寻找良缘佳偶。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120758V虽然是非正式的，但是之前其他国家\n',
            '的王家已经提出过了相关的事宜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120759V如果可能的话准备在\n',
            '今年年中实现这个婚约。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#610F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#780F……唔，您说的话我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850034V这么以来就可以让\n',
            '好事成双了对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#600F唔……公主殿下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340120764V要此时结婚似乎\n',
            '也太过年幼了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120765V#070F……打搅一下。\n',
            '我问个问题好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F金、金大哥？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640120767V#220F呵……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640120768V没关系，但说无妨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F很抱歉，但刚才听到的那番话，\n',
            '对于我们这几个与此事无关的人\n',
            '是不应该提及的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120770V况且我并非是王国的国民。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因此，为何还要特地要在\n',
            '这样的酒席间发表决议呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#110F这是因为取得优胜的几位\n',
            '恰好就是游击士的缘故。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120773V陛下退位这个重大的事情\n',
            '也要传达给游击士协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120774V所以我才给公爵提议\n',
            '让你们得知这件事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040017V在利贝尔军队和协会\n',
            '有着良好的关系的传言\n',
            '看来果真不假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0131090006V#110F哈哈，和帝国及共和国相比，\n',
            '我国的军力不是很充实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120778V只有携起手来，\n',
            '才能面对苛刻的现实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '总之就是这样的，\n',
            '你明白其中的意思了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120780V#070F呼……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120781V我会把今天从宴席中得知的情况\n',
            '转达给王都支部的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4222._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x2DB5
@scena.Code('func_08_2DB5')
def func_08_2DB5():
    ChrWalkTo(0x00FE, 4310, 0, 69570, 3000, 0x00)
    ChrWalkTo(0x00FE, 4470, 0, 83040, 3000, 0x00)
    ChrWalkTo(0x00FE, 2550, 0, 82360, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)

    Return()

# id: 0x0009 offset: 0x2DF9
@scena.Code('func_09_2DF9')
def func_09_2DF9():
    ChrWalkTo(0x00FE, 4310, 0, 69570, 3000, 0x00)
    ChrWalkTo(0x00FE, 4470, 0, 83040, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x000A offset: 0x2E29
@scena.Code('func_0A_2E29')
def func_0A_2E29():
    ChrWalkTo(0x00FE, -4380, 0, 71660, 3000, 0x00)
    ChrWalkTo(0x00FE, -4280, 0, 85250, 3000, 0x00)
    ChrWalkTo(0x00FE, -1030, 0, 85250, 3000, 0x00)
    ChrWalkTo(0x00FE, 10, 0, 85000, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 0)

    Return()

# id: 0x000B offset: 0x2E81
@scena.Code('func_0B_2E81')
def func_0B_2E81():
    ChrWalkTo(0x00FE, -4380, 0, 71660, 3000, 0x00)
    ChrWalkTo(0x00FE, -4280, 0, 85250, 3000, 0x00)
    ChrWalkTo(0x00FE, -910, 0, 86310, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

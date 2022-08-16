import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3132_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3132   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3132.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3132_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '玛尔奇娜主管',
            x                   = -1700,
            z                   = 0,
            y                   = 2400,
            direction           = 192,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '艾玛',
            x                   = 36440,
            z                   = 0,
            y                   = 50580,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '诺蒂亚',
            x                   = 68210,
            z                   = 0,
            y                   = 92140,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '多杰',
            x                   = 68100,
            z                   = 0,
            y                   = 56310,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
    )

# id: 0x10002 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x14A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x14A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -1290,
            triggerZ            = 0,
            triggerY            = 550,
            triggerRange        = 400,
            actorX              = -1700,
            actorZ              = 1500,
            actorY              = 2400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4000,
            triggerZ            = 0,
            triggerY            = 4000,
            triggerRange        = 800,
            actorX              = -4000,
            actorZ              = 1000,
            actorY              = 4000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x192
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1C3',
    )

    ChrClearFlags(0x000B, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1B9',
    )

    ChrSetPos(0x0009, 33350, 0, 55500, 0)

    Jump('loc_1C0')

    def _loc_1B9(): pass

    label('loc_1B9')

    CreateThread(0x0009, 0x00, 0x00, func_02_205)

    def _loc_1C0(): pass

    label('loc_1C0')

    Jump('loc_203')

    def _loc_1C3(): pass

    label('loc_1C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1DE',
    )

    ChrSetPos(0x0009, 5590, 0, 134800, 348)

    Jump('loc_203')

    def _loc_1DE(): pass

    label('loc_1DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1ED',
    )

    ChrClearFlags(0x000A, 0x0080)

    Jump('loc_203')

    def _loc_1ED(): pass

    label('loc_1ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1F7',
    )

    Jump('loc_203')

    def _loc_1F7(): pass

    label('loc_1F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_203',
    )

    ChrClearFlags(0x000A, 0x0080)

    def _loc_203(): pass

    label('loc_203')

    Return()

# id: 0x0001 offset: 0x204
@scena.Code('func_01_204')
def func_01_204():
    Return()

# id: 0x0002 offset: 0x205
@scena.Code('func_02_205')
def func_02_205():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_228',
    )

    OP_8D(0x00FE, 33380, 54030, 36670, 49190, 2000)

    Jump('func_02_205')

    def _loc_228(): pass

    label('loc_228')

    Return()

# id: 0x0003 offset: 0x229
@scena.Code('func_03_229')
def func_03_229():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x22E
@scena.Code('func_04_22E')
def func_04_22E():
    TalkBegin(0x0008)
    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_248',
    )

    OP_A9(0x99)
    TalkEnd(0x0008)

    Return()

    def _loc_248(): pass

    label('loc_248')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_259',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_259(): pass

    label('loc_259')

    If(
        (
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x40)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x02)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0071, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_285',
    )

    Call(1, 0x0001)

    Jump('loc_289')

    def _loc_285(): pass

    label('loc_285')

    Call(1, 0x0000)

    def _loc_289(): pass

    label('loc_289')

    Jump('loc_A3E')

    def _loc_28C(): pass

    label('loc_28C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_2E4',
    )

    ChrTalk(
        0x0008,
        (
            '现在这种情况，\n',
            '客人也越来越少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '到定期船恢复之前\n',
            '只能先忍耐了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A3E')

    def _loc_2E4(): pass

    label('loc_2E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_421',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D2',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_373',
    )

    ChrTalk(
        0x0008,
        (
            '啊，各位游击士。\n',
            '好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '蔡恩拉德酒店\n',
            '还像平常一样正常营业哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然有些不便之处，\n',
            '请多担待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CC')

    def _loc_373(): pass

    label('loc_373')

    ChrTalk(
        0x0008,
        (
            '欢迎光临。\n',
            '蔡恩拉德酒店\n',
            '还像平常一样正常营业哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然有些不便之处，\n',
            '请多担待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CC(): pass

    label('loc_3CC')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_41E')

    def _loc_3D2(): pass

    label('loc_3D2')

    ChrTalk(
        0x0008,
        (
            '蔡恩拉德酒店\n',
            '还像平常一样正常营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然有些不便之处，\n',
            '请多担待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_41E(): pass

    label('loc_41E')

    Jump('loc_A3E')

    def _loc_421(): pass

    label('loc_421')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_772',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_705',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_68F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C8, 3, 0x1643)),
            Expr.Return,
        ),
        'loc_61F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_501',
    )

    ChrTalk(
        0x0008,
        (
            '艾玛听到地震不会再来的消息之后\n',
            '恢复得和以前一样活泼了，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '像她那个样子…\n',
            '实在是活泼过头了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼～不是精力过剩就是缩成一团，\n',
            '就不能正常一点吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BD')

    def _loc_501(): pass

    label('loc_501')

    ChrTalk(
        0x0008,
        (
            '中央工房发表过安全宣言了，\n',
            '说是地震已经不会再出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '多亏如此，我们的艾玛也\n',
            '恢复得和以前一样活泼了，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '像她那个样子…\n',
            '实在是活泼过头了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼～真是担心死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_5BD(): pass

    label('loc_5BD')

    Jump('loc_61C')

    def _loc_5C0(): pass

    label('loc_5C0')

    ChrTalk(
        0x0008,
        (
            '大家辛苦了，\n',
            '吉米刚才已经回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他回来就一副急急忙忙的样子，\n',
            '马上就退房离开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_61C(): pass

    label('loc_61C')

    Jump('loc_68C')

    def _loc_61F(): pass

    label('loc_61F')

    ChrTalk(
        0x0008,
        (
            '啊，各位。\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '刚才吉米已经\n',
            '平安回来了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼～胸中的一块大石头\n',
            '总算是落地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C8, 3, 0x1643))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    def _loc_68C(): pass

    label('loc_68C')

    Jump('loc_702')

    def _loc_68F(): pass

    label('loc_68F')

    ChrTalk(
        0x0008,
        (
            '行踪不明的客人\n',
            '好像是去了钟乳洞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们虽然努力\n',
            '劝阻过他了，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那么，那位客人的事\n',
            '就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_702(): pass

    label('loc_702')

    Jump('loc_76F')

    def _loc_705(): pass

    label('loc_705')

    ChrTalk(
        0x0008,
        (
            '地震的安全宣言放出了，\n',
            '本来是值得高兴的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但还有一件事情\n',
            '让我很担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼，怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_76F(): pass

    label('loc_76F')

    Jump('loc_A3E')

    def _loc_772(): pass

    label('loc_772')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_866',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7D9',
    )

    ChrTalk(
        0x0008,
        (
            '店员艾玛\n',
            '还在害怕地震会再来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看她那种魂不守舍的模样，\n',
            '还真是让人担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_863')

    def _loc_7D9(): pass

    label('loc_7D9')

    ChrTalk(
        0x0008,
        (
            '店员艾玛\n',
            '还在担心地震再来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过她平时活泼过头了，\n',
            '现在这样反而更好吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看她那种魂不守舍的模样，\n',
            '还真是让人担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_863(): pass

    label('loc_863')

    Jump('loc_A3E')

    def _loc_866(): pass

    label('loc_866')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_957',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8D9',
    )

    ChrTalk(
        0x0008,
        (
            '别看艾玛现在很乖巧，\n',
            '但平时的她可不是这个样子的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '之前总是一副大嗓门，\n',
            '经常把客人吓到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_954')

    def _loc_8D9(): pass

    label('loc_8D9')

    ChrTalk(
        0x0008,
        (
            '这次地震\n',
            '让店员艾玛\n',
            '变得有些没精神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过也许她现在这个样子\n',
            '反而更好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '平时的她实在是\n',
            '活泼得过头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_954(): pass

    label('loc_954')

    Jump('loc_A3E')

    def _loc_957(): pass

    label('loc_957')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_A3E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9B2',
    )

    ChrTalk(
        0x0008,
        (
            '这家酒店的抗震性\n',
            '是没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '中央工房也给我们\n',
            '颁布了合格证书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A3E')

    def _loc_9B2(): pass

    label('loc_9B2')

    ChrTalk(
        0x0008,
        (
            '欢迎光临。\n',
            '欢迎光临蔡恩拉德酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然被地震吓了一大跳，\n',
            '不过还真是好久没遇到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '地震并没造成什么重大影响，\n',
            '请放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_A3E(): pass

    label('loc_A3E')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xA42
@scena.Code('func_05_A42')
def func_05_A42():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_B14',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AC9',
    )

    ChrTalk(
        0x00FE,
        (
            '油灯这种东西\n',
            '还真是麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不经常清洁的话\n',
            '墙壁就会被弄得污黑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～果然还是导力灯\n',
            '最便利啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_B11')

    def _loc_AC9(): pass

    label('loc_AC9')

    ChrTalk(
        0x00FE,
        (
            '这油灯才用了没几天\n',
            '就搞得这么脏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是导力灯\n',
            '最便利啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B11(): pass

    label('loc_B11')

    Jump('loc_F8B')

    def _loc_B14(): pass

    label('loc_B14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_BFF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BB4',
    )

    ChrTalk(
        0x00FE,
        (
            '现在导力灯没法使用了，\n',
            '只能点油灯应急……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但还是好暗，\n',
            '到了晚上真是好可怕呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时候还会和客人撞到一起，\n',
            '都快吓出心脏病了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_BFC')

    def _loc_BB4(): pass

    label('loc_BB4')

    ChrTalk(
        0x00FE,
        (
            '油灯的光实在是\n',
            '太昏暗了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '夜、夜里来到走廊时\n',
            '真是好害怕啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BFC(): pass

    label('loc_BFC')

    Jump('loc_F8B')

    def _loc_BFF(): pass

    label('loc_BFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_D00',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_C48',
    )

    ChrTalk(
        0x00FE,
        (
            '好了～先来做扫除吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天也要鼓足干劲才行～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CFD')

    def _loc_C48(): pass

    label('loc_C48')

    ChrTalk(
        0x00FE,
        (
            '欢迎光临！\n',
            '欢迎光临蔡恩拉德酒店！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿！！听说了吗！？\n',
            '已经不会发生地震了啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是客人告诉我\n',
            '这件超级好消息的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈！这样的话，\n',
            '我艾玛就彻底复活了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_CFD(): pass

    label('loc_CFD')

    Jump('loc_F8B')

    def _loc_D00(): pass

    label('loc_D00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_DEB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_D63',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～一想起地震的事\n',
            '就连食欲也没有了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概以后\n',
            '会发展成失眠也说不定啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE8')

    def _loc_D63(): pass

    label('loc_D63')

    ChrTalk(
        0x00FE,
        (
            '啊，欢迎光临……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～一想起地震的事\n',
            '就连食欲也没有了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概以后\n',
            '会发展成失眠也说不定啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊、啊哈哈哈～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_DE8(): pass

    label('loc_DE8')

    Jump('loc_F8B')

    def _loc_DEB(): pass

    label('loc_DEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_ED3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_E56',
    )

    ChrTalk(
        0x00FE,
        (
            '老想着会不会再有地震，\n',
            '都没办法投入工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但不知为什么主管\n',
            '就可以那么轻松……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ED0')

    def _loc_E56(): pass

    label('loc_E56')

    ChrTalk(
        0x00FE,
        (
            '啊，客人……\n',
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老想着会不会再有地震，\n',
            '都没办法投入工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但不知为什么主管\n',
            '就可以那么轻松……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_ED0(): pass

    label('loc_ED0')

    Jump('loc_F8B')

    def _loc_ED3(): pass

    label('loc_ED3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_F8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_F30',
    )

    ChrTalk(
        0x00FE,
        (
            '要、要是再有地震\n',
            '的话该怎么办啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜～害怕得我\n',
            '都没办法工作了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F8B')

    def _loc_F30(): pass

    label('loc_F30')

    ChrTalk(
        0x00FE,
        (
            '欢、欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜～总觉得地面\n',
            '还在摇晃呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好可怕啊～\n',
            '都没办法工作了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_F8B(): pass

    label('loc_F8B')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0xF8F
@scena.Code('func_06_F8F')
def func_06_F8F():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1051',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_FFB',
    )

    ChrTalk(
        0x00FE,
        (
            '中央工房的报道\n',
            '大家都很感兴趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～在坐上回航的船之前\n',
            '先把稿子整理一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104E')

    def _loc_FFB(): pass

    label('loc_FFB')

    ChrTalk(
        0x00FE,
        (
            '中央工房的报道\n',
            '大家都很感兴趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是有着王国的大脑\n',
            '之称的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_104E(): pass

    label('loc_104E')

    Jump('loc_114D')

    def _loc_1051(): pass

    label('loc_1051')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_114D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_10CA',
    )

    ChrTalk(
        0x00FE,
        (
            '身为利贝尔通讯的记者，\n',
            '绝对不能错过地震的报道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有关新型导力照相机\n',
            '想听听专业人士的意见吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_114D')

    def _loc_10CA(): pass

    label('loc_10CA')

    ChrTalk(
        0x00FE,
        (
            '呼～地震还真是少见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为利贝尔通讯的记者，\n',
            '这种新闻当然不能错过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有关新型导力照相机\n',
            '想听听专业人士的意见吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_114D(): pass

    label('loc_114D')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x1151
@scena.Code('func_07_1151')
def func_07_1151():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_124B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11E8',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器瘫痪的原因\n',
            '好像还不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房现在已经是那种状态了，\n',
            '肯定不可能再进行研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想想也知道\n',
            '事态有多严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1248')

    def _loc_11E8(): pass

    label('loc_11E8')

    ChrTalk(
        0x00FE,
        (
            '导力器瘫痪的原因\n',
            '好像还不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房现在已经是那种状态了，\n',
            '肯定不可能再进行研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1248(): pass

    label('loc_1248')

    Jump('loc_1371')

    def _loc_124B(): pass

    label('loc_124B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1371',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12FF',
    )

    ChrTalk(
        0x00FE,
        (
            '我从共和国特意赶来，就是为了\n',
            '购买新型导力器，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为、为什么城里所有的导力器\n',
            '都瘫痪了呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房也是一团漆黑，\n',
            '想进行商谈似乎很困难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1371')

    def _loc_12FF(): pass

    label('loc_12FF')

    ChrTalk(
        0x00FE,
        (
            '我从共和国特意赶来，就是为了\n',
            '购买新型导力器，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照现在的形势来看的话，\n',
            '这次的商讨算是彻底泡汤了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1371(): pass

    label('loc_1371')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1375
@scena.Code('func_08_1375')
def func_08_1375():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　　工作人员室　　　　　　　\n',
            '        ※无关人员请勿入内',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

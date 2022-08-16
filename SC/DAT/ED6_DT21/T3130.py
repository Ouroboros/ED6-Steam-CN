import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3130_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3130   ._SN')

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
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01400._CH', 'ED6_DT07/CH01400P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '皮克塞恩教区长',
            x                   = 59010,
            z                   = 1000,
            y                   = 52150,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '修女琪爱拉',
            x                   = 56310,
            z                   = 1000,
            y                   = 50360,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '莱恩',
            x                   = 59970,
            z                   = 0,
            y                   = 43850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '艾妲',
            x                   = 59010,
            z                   = 1000,
            y                   = 50160,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
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
            triggerX            = 58950,
            triggerZ            = 1000,
            triggerY            = 50290,
            triggerRange        = 400,
            actorX              = 58800,
            actorZ              = 2500,
            actorY              = 52200,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x16E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_17D',
    )

    ChrSetFlags(0x000A, 0x0080)

    Jump('loc_1F0')

    def _loc_17D(): pass

    label('loc_17D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_198',
    )

    ChrSetPos(0x000A, 62680, 0, 45050, 0)

    Jump('loc_1F0')

    def _loc_198(): pass

    label('loc_198')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1D3',
    )

    ChrSetFlags(0x0008, 0x0010)
    ChrSetPos(0x000B, 56190, 0, 46550, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetPos(0x000A, 62680, 0, 45050, 0)

    Jump('loc_1F0')

    def _loc_1D3(): pass

    label('loc_1D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1F0',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000A, 62680, 0, 45050, 0)

    def _loc_1F0(): pass

    label('loc_1F0')

    Return()

# id: 0x0001 offset: 0x1F1
@scena.Code('func_01_1F1')
def func_01_1F1():
    Return()

# id: 0x0002 offset: 0x1F2
@scena.Code('func_02_1F2')
def func_02_1F2():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x1F7
@scena.Code('func_03_1F7')
def func_03_1F7():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_338',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D7',
    )

    ChrTalk(
        0x0008,
        (
            '导力器无法使用的话，\n',
            '保安方面也有很大问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如你所知，导力灯具有\n',
            '驱散魔兽的效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '以前遭到魔兽侵犯时\n',
            '王国军都会替我们击退魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但那个时候导力器可以使用，\n',
            '和现在的情况不同啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_335')

    def _loc_2D7(): pass

    label('loc_2D7')

    ChrTalk(
        0x0008,
        (
            '导力器无法使用的话，\n',
            '保安方面也有很大问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如你所知，导力灯具有\n',
            '驱散魔兽的效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_335(): pass

    label('loc_335')

    Jump('loc_10EB')

    def _loc_338(): pass

    label('loc_338')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_49C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_434',
    )

    ChrTalk(
        0x0008,
        (
            '异变发生之后\n',
            '引起了很大的混乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过城里的状况总算是\n',
            '稍微安定下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '对城里的居民来说，导力器的意义\n',
            '已经不止是一个普通的机械了，\n',
            '因此出现这么大的骚乱也不奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然技术力的不断进步，\n',
            '这里也发展得越来越快了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_499')

    def _loc_434(): pass

    label('loc_434')

    ChrTalk(
        0x0008,
        (
            '对城里的居民来说，导力器的意义\n',
            '已经不止是一个普通的机械了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因此引发这么大的混乱也不奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_499(): pass

    label('loc_499')

    Jump('loc_10EB')

    def _loc_49C(): pass

    label('loc_49C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0285, 0, 0x1428)),
            Expr.Return,
        ),
        'loc_998',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_94D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_58F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_518',
    )

    ChrTalk(
        0x0008,
        (
            '清楚认识到自己能力的不足\n',
            '也是迈上成功之道的第一步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '只要相信神\n',
            '一切就都会有希望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58C')

    def _loc_518(): pass

    label('loc_518')

    ChrTalk(
        0x0008,
        (
            '愿女神可以保佑\n',
            '别再发生地震了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '希望我的祈祷\n',
            '能管用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们要清楚地认识到\n',
            '自己能力的不足才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_58C(): pass

    label('loc_58C')

    Jump('loc_94A')

    def _loc_58F(): pass

    label('loc_58F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_5CC',
    )

    ChrTalk(
        0x0008,
        (
            '空之女神啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '愿女神永远\n',
            '引导保护我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94A')

    def _loc_5CC(): pass

    label('loc_5CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_781',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_629',
    )

    ChrTurnDirection(0x0008, 0x0107, 0)

    ChrTalk(
        0x0008,
        (
            '那么，你们就加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果有什么困难的话\n',
            '随时可以到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77E')

    def _loc_629(): pass

    label('loc_629')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_660',
    )

    ChrTalk(
        0x0008,
        (
            '啊，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '又在帮博士的忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A7')

    def _loc_660(): pass

    label('loc_660')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0107, 0)

    ChrTalk(
        0x0008,
        (
            '呀，提妲也在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '又在帮博士的忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6A7(): pass

    label('loc_6A7')

    ChrTalk(
        0x0107,
        (
            '#560F啊…嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '只是设置测量仪而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，真让人佩服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '下次主日学校的课\n',
            '一定要再来听哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '只要有你在，\n',
            '大家就都充满活力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F嘿嘿嘿……\n',
            '是，我知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那么，你就\n',
            '继续加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_77E(): pass

    label('loc_77E')

    Jump('loc_94A')

    def _loc_781(): pass

    label('loc_781')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_879',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7E0',
    )

    ChrTalk(
        0x0008,
        (
            '最近修女琪爱拉\n',
            '一直很热心帮忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '她似乎理解了社会活动\n',
            '的重要性了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_876')

    def _loc_7E0(): pass

    label('loc_7E0')

    ChrTalk(
        0x0008,
        (
            '提供医疗服务\n',
            '是礼拜堂的重要作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不管是心中的苦闷还是身体上的伤痛\n',
            '都需要别人来抚平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '只有将这两种痛苦全部消除\n',
            '才能算是真正的拯救。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_876(): pass

    label('loc_876')

    Jump('loc_94A')

    def _loc_879(): pass

    label('loc_879')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_94A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_8D8',
    )

    ChrTalk(
        0x0008,
        (
            '虽然只是小型地震，\n',
            '但也许会有人受伤，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还是要事先把伤药\n',
            '准备好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94A')

    def _loc_8D8(): pass

    label('loc_8D8')

    ChrTalk(
        0x0008,
        (
            '嗯，刚才的摇晃\n',
            '似乎是地震啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然震动不算大，\n',
            '但也许会有人受伤，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还是要事先把伤药\n',
            '准备好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_94A(): pass

    label('loc_94A')

    Jump('loc_995')

    def _loc_94D(): pass

    label('loc_94D')

    ChrTalk(
        0x0008,
        (
            '如果有事\n',
            '那就请再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果有需要的话，\n',
            '随时可以来找我商谈哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_995(): pass

    label('loc_995')

    Jump('loc_10EB')

    def _loc_998(): pass

    label('loc_998')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_CCB',
    )

    ChrTalk(
        0x0008,
        (
            '啊，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F啊～教区长先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F那……那个时候\n',
            '真是～多亏了您的帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#552F……多亏您的照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0106, 400)

    ChrTalk(
        0x0008,
        (
            '喔喔，看样子你已经\n',
            '完全康复了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '没想到竟然恢复得这么快，\n',
            '看来完全不用担心你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过，以后也不要蛮干啊。\n',
            '要小心身体才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F嗯，我一定会铭记在心的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#555F真是的，我又不是小孩子了。\n',
            '不用那么担心啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，虽然如此，不过呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你能得救也是多亏了女神的守护，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今后一定还有需要你完成的\n',
            '使命在等着你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '所以，你可是有用之身，\n',
            '不能轻易就犯险乱来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这也是\n',
            '我对你的一点希望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#552F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '……哎呀，我这人真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '只是救过你一次，\n',
            '就非要让你听这么多说教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 500)

    ChrTalk(
        0x0008,
        (
            '那么，欢迎以后再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果有需要的话，\n',
            '有问题随时都可以找我商量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那再见啦，教区长先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10E5')

    def _loc_CCB(): pass

    label('loc_CCB')

    ChrTalk(
        0x0008,
        (
            '啊，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F啊～教区长先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F阿加特受伤的时候\n',
            '真是～多亏了您的帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#023F受……伤？\n',
            '有那种事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DE6',
    )

    ChrTalk(
        0x0107,
        (
            '#561F嗯、是的……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#1003F中了特务兵的毒弹，\n',
            '情况非常危险呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯，多亏了教区长的药\n',
            '才能顺利脱险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ED5')

    def _loc_DE6(): pass

    label('loc_DE6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E7B',
    )

    @scena.Lambda('lambda_0DFA')
    def lambda_0DFA():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DFA)

    ChrTurnDirection(0x0108, 0x0103, 400)

    ChrTalk(
        0x0108,
        (
            '#072F嗯，他被有毒的子弹\n',
            '射中，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '当时的情况好像很危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，多亏了教区长的药\n',
            '才能顺利脱险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ED5')

    def _loc_E7B(): pass

    label('loc_E7B')

    ChrTalk(
        0x0101,
        (
            '#1003F嗯，被毒弹击伤，\n',
            '情况非常危险呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯，多亏了教区长的药\n',
            '才能顺利脱险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ED5(): pass

    label('loc_ED5')

    ChrTalk(
        0x0008,
        (
            '啊，我也只是帮了\n',
            '一点小忙而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '对了，他现在怎么样了？\n',
            '已经彻底痊愈了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F4E',
    )

    @scena.Lambda('lambda_0F46')
    def lambda_0F46():
        ChrTurnDirection(0x0108, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0F46)

    def _loc_F4E(): pass

    label('loc_F4E')

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，已经完全恢复了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他现在和我们\n',
            '分头行动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯…希望他不要再像\n',
            '以前那么乱来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他能获救都是因为女神的意志。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这也说明他以后还有\n',
            '自己应尽的使命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '……哎呀，我这人真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '只是救了他一次，\n',
            '就要让你们听这么多说教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那么，欢迎以后再来，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果有需要的话，\n',
            '有问题随时都可以找我商量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那，再见啦，教区长先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10E5(): pass

    label('loc_10E5')

    SetScenaFlags(ScenaFlag(0x0285, 0, 0x1428))
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    def _loc_10EB(): pass

    label('loc_10EB')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x10EF
@scena.Code('func_04_10EF')
def func_04_10EF():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1166',
    )

    ChrTalk(
        0x00FE,
        (
            '为了预防紧急事态\n',
            '必须要多制作一些药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果可能的话，我倒更希望\n',
            '自己的这些努力全部变成无用劳动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1609')

    def _loc_1166(): pass

    label('loc_1166')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_12A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1241',
    )

    ChrTalk(
        0x00FE,
        (
            '因为导力器停止而受惊的市民们\n',
            '都聚集在了中央工房……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '转眼之间，\n',
            '城里就变得一片混乱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但即使大家都聚在一起\n',
            '也都完全做不了什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过这样一来，\n',
            '也可以认识到自己力量的不足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_12A3')

    def _loc_1241(): pass

    label('loc_1241')

    ChrTalk(
        0x00FE,
        (
            '因为导力器停止而受惊的市民们\n',
            '都聚集在了中央工房……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '转眼之间，\n',
            '城里好像已经一片骚乱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12A3(): pass

    label('loc_12A3')

    Jump('loc_1609')

    def _loc_12A6(): pass

    label('loc_12A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1394',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1303',
    )

    ChrTalk(
        0x00FE,
        (
            '在教区长看来，\n',
            '只要求神保佑就ＯＫ了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，女神未免也太\n',
            '宽容了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1391')

    def _loc_1303(): pass

    label('loc_1303')

    ChrTalk(
        0x00FE,
        (
            '在教区长看来，\n',
            '只要求神保佑就ＯＫ了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然从某种意义上说\n',
            '我可以理解他们的做法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是、不管怎么说\n',
            '从心情上也没办法接受呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1391(): pass

    label('loc_1391')

    Jump('loc_1609')

    def _loc_1394(): pass

    label('loc_1394')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1497',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_13E7',
    )

    ChrTalk(
        0x00FE,
        (
            '只有在遇到困难的时候\n',
            '才来祈祷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '未免也太\n',
            '不虔诚了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1494')

    def _loc_13E7(): pass

    label('loc_13E7')

    ChrTalk(
        0x00FE,
        (
            '来做礼拜的人\n',
            '最近急剧增多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都是希望地震不要再来\n',
            '才来向女神祈祷的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然教区长总是一脸笑容\n',
            '地欢迎他们，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是觉得这样子\n',
            '太不虔诚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1494(): pass

    label('loc_1494')

    Jump('loc_1609')

    def _loc_1497(): pass

    label('loc_1497')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1560',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_14FC',
    )

    ChrTalk(
        0x00FE,
        (
            '不管任何困难也要克服，\n',
            '努力为他人解决困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '教区长这种想法\n',
            '实在是很伟大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_155D')

    def _loc_14FC(): pass

    label('loc_14FC')

    ChrTalk(
        0x00FE,
        (
            '研制药品的处方\n',
            '也是教会的重要职责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '开始的时候还有些抵触，\n',
            '但现在已经完全没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_155D(): pass

    label('loc_155D')

    Jump('loc_1609')

    def _loc_1560(): pass

    label('loc_1560')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_1609',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_15B6',
    )

    ChrTalk(
        0x00FE,
        (
            '城里那边没什么问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，比起那个\n',
            '我更加担心中央工房呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1609')

    def _loc_15B6(): pass

    label('loc_15B6')

    ChrTalk(
        0x00FE,
        (
            '虽然震动很小，\n',
            '但毕竟也是场地震啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我来到这里之后\n',
            '还是第一次发生呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1609(): pass

    label('loc_1609')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0x160D
@scena.Code('func_05_160D')
def func_05_160D():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1724',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_167A',
    )

    ChrTalk(
        0x00FE,
        (
            '呜～今天要通宵工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，果然，对宗教的热情\n',
            '和现实社会的生活是密不可分的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1721')

    def _loc_167A(): pass

    label('loc_167A')

    ChrTalk(
        0x00FE,
        (
            '听过中央工房发表的声明了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要虔诚祈祷的话\n',
            '地震就会停止的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喔，还有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在祈祷的时候，\n',
            '我的工作就要先放下了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，工作怎么办呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1721(): pass

    label('loc_1721')

    Jump('loc_193B')

    def _loc_1724(): pass

    label('loc_1724')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_17DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1787',
    )

    ChrTalk(
        0x00FE,
        (
            '大家都来祈祷\n',
            '地震不要再发生呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然要耽误工作，\n',
            '但我也不能自己先回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17DA')

    def _loc_1787(): pass

    label('loc_1787')

    ChrTalk(
        0x00FE,
        (
            '大家都来祈祷\n',
            '地震不要再发生呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这种时候，\n',
            '情绪也受到大家的影响了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_17DA(): pass

    label('loc_17DA')

    Jump('loc_193B')

    def _loc_17DD(): pass

    label('loc_17DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1882',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_183A',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，在回去工作之前\n',
            '先认真祈祷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～希望地震\n',
            '不要再来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_187F')

    def _loc_183A(): pass

    label('loc_183A')

    ChrTalk(
        0x00FE,
        (
            '今天来礼拜堂的人\n',
            '好像很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都来祈祷\n',
            '真让人吃惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_187F(): pass

    label('loc_187F')

    Jump('loc_193B')

    def _loc_1882(): pass

    label('loc_1882')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_193B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_18D8',
    )

    ChrTalk(
        0x00FE,
        (
            '难得来一次教会，\n',
            '却都在祈祷同一件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让地震不要再来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_193B')

    def _loc_18D8(): pass

    label('loc_18D8')

    ChrTalk(
        0x00FE,
        (
            '呼，看来是被刚才的地震\n',
            '吓得太厉害吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然还在工作中，但想也没想\n',
            '就直接跑到教会来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_193B(): pass

    label('loc_193B')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x193F
@scena.Code('func_06_193F')
def func_06_193F():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_199E',
    )

    ChrTalk(
        0x00FE,
        (
            '伟大的女神啊……\n',
            '请让地震不要再发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有，感谢您\n',
            '总是赐予我们良药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA0')

    def _loc_199E(): pass

    label('loc_199E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1AA0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1A09',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，今天就好好\n',
            '祈祷一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望地震不要再发生，\n',
            '女神一定能听到我们的祈愿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA0')

    def _loc_1A09(): pass

    label('loc_1A09')

    ChrTalk(
        0x00FE,
        (
            '教区长的药\n',
            '非常管用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的肩膀也\n',
            '彻底治好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，今天就好好\n',
            '祈祷一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望地震不要再发生，\n',
            '女神一定能听到我们的祈愿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1AA0(): pass

    label('loc_1AA0')

    TalkEnd(0x000B)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C2219_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2219_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C2210.x'
    header.mapIndex       = 84
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10000 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1048',
    )

    OP_28(0x001D, 0x04, 0x10)
    OP_28(0x001D, 0x01, 0x0080)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    Fade(1000)
    ChrSetPos(0x0101, -970, 0, 201500, 270)
    ChrSetPos(0x0102, -120, 0, 201000, 270)
    ChrSetPos(0x0105, 330, 0, 202500, 270)
    OP_69(0x0008, 1000)
    TalkBegin(0x0008)

    ChrTalk(
        0x0101,
        (
            '#0010160382V#001F谢谢惠顾～\n',
            '这是给您送来的东西～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160383V嗯？\n',
            '你们不是前些时候的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160384V#001F嘿嘿，好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160385V#006F今天我们是为了任务而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160386V#010F从游击士协会接到的委托，\n',
            '把维修工具箱给您送来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160387V#000F没错，请收下。\n',
            '啊，要小心，比较重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '维修工具箱',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0326, 1)

    ChrTalk(
        0x0008,
        (
            '#1730160388V唔，没错，就是这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160389V那么大老远的跑来，\n',
            '真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x0004)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x019A)"),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5B9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010160390V#000F没有啦，小事一桩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160391V比起这个，\n',
            '城里的人们也都很关心老人家您呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160392V工作这么辛苦，\n',
            '一定要保重身体才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160393V唔～真是谢谢他们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160394V……你们现在也总算明白了\n',
            '这种为某人某事操心的艰难了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160395V#506F嗯，怎么说好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160396V虽然明白这些道理，\n',
            '不过要做好果然还是挺难的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160397V没关系，慢慢来，\n',
            '总有一天可以做到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160398V当然，\n',
            '现在还是差得很远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160399V……就这样吧。\n',
            '今天真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160400V我也该继续工作了。\n',
            '还要进行定期检查呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160401V#000F好吧。\n',
            '多多保重了，老爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160402V#010F打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【运送维修工具箱】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    EventEnd(0x00)
    TalkEnd(0x0008)

    Jump('loc_1045')

    def _loc_5B9(): pass

    label('loc_5B9')

    ChrTalk(
        0x0101,
        (
            '#0010160390V#000F没有啦，小事一桩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160404V而且我们今天\n',
            '还带了其他的东西来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160405V哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0105, -800, 0, 0, 2000, 0x00)
    OP_92(0x0105, 0x0008, 1000, 2000, 0x00)

    ChrTalk(
        0x0105,
        (
            '#0060160406V#040F弗科特老爷爷，请收下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160407V这是『拉旺塔尔』的\n',
            '普莱米奥老板捎给您的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0105, 400)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '亚瑟利亚葡萄酒',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x019A, 1)
    OP_28(0x001D, 0x01, 0x0020)
    ChrMoveToRelativeAsync(0x0105, 400, 0, 400, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#1730160408V哦哦！\n',
            '这不是『亚瑟利亚葡萄酒』吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160409V让我回忆起了\n',
            '以前用辣鳀鱼作为下酒菜，\n',
            '通宵痛饮的时代啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_40(0x0391)"),
            Expr.Return,
        ),
        'loc_99D',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【交出辣鳀鱼】\n'),
            TXT(0x01, '【什么也不做】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_817'),
        (0x00000001, 'loc_957'),
        (-1, 'loc_99A'),
    )

    def _loc_817(): pass

    label('loc_817')

    ChrTalk(
        0x0101,
        (
            '#0010160410V#001F嘿嘿嘿⊙\n',
            '事实上我们一起带来了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '辣鳀鱼',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0391, 1)
    OP_28(0x001D, 0x01, 0x0040)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#1730160411V哦哦！哦哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160412V还专门弄来了下酒菜，\n',
            '真是准备得很周全啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160413V唉～\n',
            '真让人怀念啊。\n',
            '普莱米奥他们还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99A')

    def _loc_957(): pass

    label('loc_957')

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160414V唉，真让人怀念啊，\n',
            '普莱米奥他们还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99A')

    def _loc_99A(): pass

    label('loc_99A')

    Jump('loc_9DD')

    def _loc_99D(): pass

    label('loc_99D')

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160414V唉，真让人怀念啊，\n',
            '普莱米奥他们还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_9DD(): pass

    label('loc_9DD')

    ChrTalk(
        0x0101,
        (
            '#0010160416V#000F很好的，\n',
            '大家也都很关心老人家您呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160392V工作这么辛苦，\n',
            '一定要保重身体才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160418V嗯，你们捎来东西我就已经很感激了，\n',
            '这么说让我更加感激啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160419V……你们现在\n',
            '也总算明白了这种\n',
            '为某人某事操心的艰难了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160395V#506F嗯，怎么说好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160396V虽然明白这些道理，\n',
            '不过要做好果然还是挺难的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160422V没关系，慢慢来，\n',
            '你们很快就能做到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160423V当然，\n',
            '现在还是差得很远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160424V……哦，对了。\n',
            '稍等片刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BD6')
    def lambda_0BD6():
        ChrTurnDirection(0x0102, 0x0008, 400)
        Yield()

        Jump('lambda_0BD6')

    DispatchAsync2(0x0102, 0x0001, lambda_0BD6)

    @scena.Lambda('lambda_0BE7')
    def lambda_0BE7():
        ChrTurnDirection(0x0101, 0x0008, 400)
        Yield()

        Jump('lambda_0BE7')

    DispatchAsync2(0x0101, 0x0001, lambda_0BE7)

    @scena.Lambda('lambda_0BF8')
    def lambda_0BF8():
        ChrTurnDirection(0x0105, 0x0008, 400)
        Yield()

        Jump('lambda_0BF8')

    DispatchAsync2(0x0105, 0x0001, lambda_0BF8)

    ChrWalkTo(0x0008, -2080, 0, 203320, 2000, 0x00)
    ChrWalkTo(0x0008, -3570, 0, 204220, 2000, 0x00)
    ChrWalkTo(0x0008, -5930, 0, 203930, 2000, 0x00)
    ChrSetDirection(0x0008, 315, 0)
    Sleep(1000)

    ChrWalkTo(0x0008, -5930, 0, 203930, 2000, 0x00)
    ChrWalkTo(0x0008, -3570, 0, 204220, 2000, 0x00)
    ChrWalkTo(0x0008, -2080, 0, 203320, 2000, 0x00)
    ChrWalkTo(0x0008, -2140, 0, 201500, 2000, 0x00)
    ChrTurnDirection(0x0008, 0x0101, 400)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#1730160425V这是很久以前\n',
            '我用过的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160426V让你们那么辛苦地送东西来，\n',
            '这就算我的一点心意。\n',
            '你们就别客气，收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160427V虽然有些旧了，\n',
            '不过品质可是勿庸置疑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_DF1',
    )

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '工作安全帽',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '斗魂扎头巾',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0148, 1)
    AddItem(0x0146, 1)

    Jump('loc_E3E')

    def _loc_DF1(): pass

    label('loc_DF1')

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '工作安全帽',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0148, 1)

    def _loc_E3E(): pass

    label('loc_E3E')

    ChrTalk(
        0x0101,
        (
            '#0010160428V#001F哇啊，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160429V#014F这样好吗？\n',
            '那么珍贵的物品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160430V没关系没关系，\n',
            '反正我也不可能再次出海了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1730160431V……就这样吧。\n',
            '今天真是辛苦你们了。\n',
            '我也该继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160432V拿到你们捎来的东西，\n',
            '我真的非常高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160433V#040F请您一定要注意身体哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160434V#000F那么，\n',
            '多多保重了，老爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160435V#010F我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【运送维修工具箱】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    EventEnd(0x00)
    TalkEnd(0x0008)

    def _loc_1045(): pass

    label('loc_1045')

    Jump('loc_1824')

    def _loc_1048(): pass

    label('loc_1048')

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 2, 0x442)),
            Expr.Return,
        ),
        'loc_1302',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008B, 0, 0x458)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_120E',
    )

    SetScenaFlags(ScenaFlag(0x008B, 0, 0x458))
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '噢，是小姑娘你们啊。\n',
            '昨晚真是谢谢你们了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F老爷爷您才是呢，\n',
            '已经没事了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '不久前头还稍微有点晕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在已经没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#013F看来麻醉药的作用已经过去了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '药本身是无毒的，\n',
            '这样的话就不用担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F太好了，\n',
            '那我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，\n',
            '那我这就恢复工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F不要太过勉强了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然已经恢复了，\n',
            '但是毕竟遭遇了那样的惊吓啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，说的有道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那就比平时\n',
            '多休息一会儿再工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12FF')

    def _loc_120E(): pass

    label('loc_120E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12A9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '噢，是小姑娘你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '药的效果终于已经过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '头晕的感觉也已经消失了，\n',
            '跟平常没什么两样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吧，\n',
            '我这就恢复工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12FF')

    def _loc_12A9(): pass

    label('loc_12A9')

    ChrTalk(
        0x00FE,
        (
            '药的效果\n',
            '终于已经过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '跟平常没什么两样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吧，\n',
            '我这就恢复工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12FF(): pass

    label('loc_12FF')

    Jump('loc_1821')

    def _loc_1302(): pass

    label('loc_1302')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_15DA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008B, 0, 0x458)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14B6',
    )

    SetScenaFlags(ScenaFlag(0x008B, 0, 0x458))
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '噢，是小姑娘你们啊。\n',
            '昨晚真是谢谢你们了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F老爷爷您才是呢，\n',
            '已经没事了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，没什么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '还是稍微有点头晕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#013F看来麻醉药的作用\n',
            '还没有完全消退。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过这药没有毒，\n',
            '应该很快就可以恢复的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F太好了，\n',
            '那我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，那么我稍微休息一会儿，\n',
            '然后再去工作好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，\n',
            '休息是最重要的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F请您千万不要勉强自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吧，\n',
            '那我这就去休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15D7')

    def _loc_14B6(): pass

    label('loc_14B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1566',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上\n',
            '真是谢谢你们了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我记不清楚\n',
            '昨天晚上到底发生过什么事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉真的就像\n',
            '在一瞬间发生的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜……\n',
            '我的头好像又有点晕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15D7')

    def _loc_1566(): pass

    label('loc_1566')

    ChrTalk(
        0x00FE,
        (
            '昨晚的事情\n',
            '我怎么也记不清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉真的就像\n',
            '在一瞬间发生的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '我的头好像又有点晕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15D7(): pass

    label('loc_15D7')

    Jump('loc_1821')

    def _loc_15DA(): pass

    label('loc_15DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_175B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_169C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_164B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哦，是你们啊。\n',
            '真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从今往后也要记得\n',
            '把关心别人放在首位哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1699')

    def _loc_164B(): pass

    label('loc_164B')

    ChrTalk(
        0x00FE,
        (
            '呼，休息一下\n',
            '就开始进行检查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '这个工作对腰真是不好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1699(): pass

    label('loc_1699')

    Jump('loc_1758')

    def _loc_169C(): pass

    label('loc_169C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1702',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哦，是你们啊。\n',
            '辛苦你们消灭魔兽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不要忘记关心人的心，\n',
            '从今往后也要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1758')

    def _loc_1702(): pass

    label('loc_1702')

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '我差不多该去进行定期检查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在货物运来之前\n',
            '要去进行工作的准备才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1758(): pass

    label('loc_1758')

    Jump('loc_1821')

    def _loc_175B(): pass

    label('loc_175B')

    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1821',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17CB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哦，是你们啊。\n',
            '辛苦你们消灭魔兽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不要忘记关心人的心，\n',
            '从今往后也要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1821')

    def _loc_17CB(): pass

    label('loc_17CB')

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '我差不多该去进行定期检查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在货物运来之前\n',
            '要去进行工作的准备才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1821(): pass

    label('loc_1821')

    TalkEnd(0x0008)
    def _loc_1824(): pass

    label('loc_1824')

    Return()

# id: 0x0001 offset: 0x1825
@scena.Code('func_01_1825')
def func_01_1825():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrClearFlags(0x0008, 0x0080)
    TalkBegin(0x0008)
    ChrSetPos(0x0008, 300, 0, 202000, 180)
    ChrSetPos(0x0101, 1750, 0, 203500, 180)
    ChrSetPos(0x0102, 2650, 0, 203000, 180)
    ChrSetPos(0x0105, 2550, 0, 205000, 180)
    OP_69(0x0101, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_188E')
    def lambda_188E():
        ChrWalkTo(0x0008, -2140, 0, 201500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_188E)

    @scena.Lambda('lambda_18A9')
    def lambda_18A9():
        CameraMove(-970, 0, 201500, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_18A9)

    CreateThread(0x0101, 0x01, 0x01, 0x0002)
    Sleep(200)

    CreateThread(0x0102, 0x01, 0x01, 0x0003)
    Sleep(200)

    CreateThread(0x0105, 0x01, 0x01, 0x0004)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetDirection(0x0008, 270, 400)
    Sleep(400)

    ChrSetDirection(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160436V呼，我这是怎么了，\n',
            '突然感觉自己\n',
            '好像离开这里好久了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160437V#010F艾丝蒂尔，\n',
            '先把任务完成了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160438V#000F嗯，说得对呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)
    OP_92(0x0101, 0x0008, 1000, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010160439V#001F谢谢惠顾～\n',
            '这是给您送来的东西～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160440V有点重，要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '维修工具箱',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0326, 1)

    ChrTalk(
        0x0008,
        (
            '#1730160388V唔，没错，就是这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160389V那么大老远的跑来，\n',
            '真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x0004)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x019A)"),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2084',
    )

    ChrTalk(
        0x0101,
        (
            '#0010160390V#000F没有啦，小事一桩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160391V比起这个，\n',
            '城里的人也都很关心老人家您呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160392V工作这么辛苦，\n',
            '一定要保重身体才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160393V唔～真是谢谢他们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160394V……你们现在也总算明白了这种\n',
            '为某人某事操心的艰难了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160395V#506F嗯，怎么说好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160396V虽然明白这些道理，\n',
            '不过要做好果然还是挺难的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160397V没关系，慢慢来，\n',
            '总有一天可以做到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160451V当然，\n',
            '如果和那位游击士相比，\n',
            '不足的地方还是很多的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160452V#000F请问，您说的那位游击士\n',
            '究竟是个什么样的人呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160453V听您刚才那么说，\n',
            '他好像是个很了不起的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160167V七八年前，我承蒙过他的关照。\n',
            '但是很遗憾，我并不知道他的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160455V他可真是一个了不起的男子汉啊。\n',
            '现在的你们\n',
            '还是无法和他相提并论的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160456V唔，但是小姑娘头发的颜色倒是和他很相似，\n',
            '那个游击士的头发也恰好是\n',
            '红色中带有一丝茶色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#1730160457V……怎么回事，仔细一看，\n',
            '眼睛的颜色也挺相似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160172V#014F……红色的头发，\n',
            '和艾丝蒂尔相同的眼睛颜色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160459V#004F那、那个游击士难道是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160174V#044F？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160176V你们还远远没有\n',
            '达到他那样的水平啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160462V……把理想定得太高，\n',
            '就容易忽视一些细小的方面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160463V哦，话说回来，\n',
            '今天真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160400V我也该继续工作了。\n',
            '还要进行定期检查呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160465V#000F啊……嗯，那么，\n',
            '多多保重了，老爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160466V#010F打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/C2209._SN', 101, 0, 0)
    IdleLoop()
    TalkEnd(0x0008)

    Jump('loc_2E0B')

    def _loc_2084(): pass

    label('loc_2084')

    ChrTalk(
        0x0101,
        (
            '#0010160390V#000F没有啦，小事一桩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160404V而且我们今天还\n',
            '带了其他的东西来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160405V哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0105, -800, 0, 0, 2000, 0x00)
    OP_92(0x0105, 0x0008, 1000, 2000, 0x00)

    ChrTalk(
        0x0105,
        (
            '#0060160406V#040F弗科特老爷爷，请收下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160407V这是『拉旺塔尔』的\n',
            '普莱米奥老板捎给您的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0105, 400)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '亚瑟利亚葡萄酒',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x019A, 1)
    OP_28(0x001D, 0x01, 0x0020)
    ChrMoveToRelativeAsync(0x0105, 400, 0, 400, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#1730160408V哦哦！\n',
            '这不是『亚瑟利亚葡萄酒』吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160409V让我回忆起了\n',
            '以前用辣鳀鱼作为下酒菜，\n',
            '通宵痛饮的时代啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_40(0x0391)"),
            Expr.Return,
        ),
        'loc_2468',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【交出辣鳀鱼】\n'),
            TXT(0x01, '【什么也不做】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_22E2'),
        (0x00000001, 'loc_2422'),
        (-1, 'loc_2465'),
    )

    def _loc_22E2(): pass

    label('loc_22E2')

    ChrTalk(
        0x0101,
        (
            '#0010160410V#001F嘿嘿嘿⊙\n',
            '事实上我们一起带来了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '辣鳀鱼',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0391, 1)
    OP_28(0x001D, 0x01, 0x0040)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#1730160411V哦哦！哦哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160412V还专门弄来了下酒菜，\n',
            '真是准备得很周全啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160413V唉～\n',
            '真让人怀念啊。\n',
            '普莱米奥他们还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2465')

    def _loc_2422(): pass

    label('loc_2422')

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160414V唉，真让人怀念啊，\n',
            '普莱米奥他们还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2465')

    def _loc_2465(): pass

    label('loc_2465')

    Jump('loc_24A8')

    def _loc_2468(): pass

    label('loc_2468')

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160414V唉，真让人怀念啊，\n',
            '普莱米奥他们还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_24A8(): pass

    label('loc_24A8')

    ChrTalk(
        0x0101,
        (
            '#0010160416V#000F很好的，\n',
            '大家也都很关心老人家您呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160392V工作这么辛苦，\n',
            '一定要保重身体才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160418V嗯，你们捎来东西我就已经很感激了，\n',
            '这么说让我更加感激啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160419V……你们现在\n',
            '也总算明白了这种\n',
            '为某人某事操心的艰难了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160395V#506F嗯，怎么说好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160396V虽然明白这些道理，\n',
            '不过要做好果然还是挺难的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160397V没关系，慢慢来，\n',
            '总有一天可以做到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160451V当然，\n',
            '如果和那位游击士相比，\n',
            '不足的地方还是比较多的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160452V#000F请问，您说的那位游击士\n',
            '究竟是个什么样的人呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160453V听您刚才那么说，\n',
            '他好像是个很了不起的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160167V七八年前，我承蒙过他的关照。\n',
            '但是很遗憾，我并不知道他的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160455V他可真是一个了不起的男子汉啊。\n',
            '现在的你们\n',
            '还是无法和他相提并论的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160456V唔，但是小姑娘头发的颜色倒是和他很相似，\n',
            '那个游击士的头发也恰好是\n',
            '红色中带有一丝茶色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#1730160457V……怎么回事，仔细一看，\n',
            '眼睛的颜色也挺相似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160172V#014F……红色的头发，\n',
            '和艾丝蒂尔相同的眼睛颜色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160459V#004F那、那个游击士难道是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160174V#044F？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160176V你们还远远没有\n',
            '达到他那样的水平啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160462V……把理想定得太高，\n',
            '就容易忽视一些细小的方面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160463V哦，话说回来，\n',
            '今天真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160500V除了工作用品，\n',
            '你们还特地送了这些东西来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160501V……哦，对了。\n',
            '稍等片刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A22')
    def lambda_2A22():
        ChrTurnDirection(0x0102, 0x0008, 400)
        Yield()

        Jump('lambda_2A22')

    DispatchAsync2(0x0102, 0x0001, lambda_2A22)

    @scena.Lambda('lambda_2A33')
    def lambda_2A33():
        ChrTurnDirection(0x0101, 0x0008, 400)
        Yield()

        Jump('lambda_2A33')

    DispatchAsync2(0x0101, 0x0001, lambda_2A33)

    @scena.Lambda('lambda_2A44')
    def lambda_2A44():
        ChrTurnDirection(0x0105, 0x0008, 400)
        Yield()

        Jump('lambda_2A44')

    DispatchAsync2(0x0105, 0x0001, lambda_2A44)

    ChrWalkTo(0x0008, -2080, 0, 203320, 2000, 0x00)
    ChrWalkTo(0x0008, -3570, 0, 204220, 2000, 0x00)
    ChrWalkTo(0x0008, -5930, 0, 203930, 2000, 0x00)
    ChrSetDirection(0x0008, 315, 0)
    Sleep(1000)

    ChrWalkTo(0x0008, -5930, 0, 203930, 2000, 0x00)
    ChrWalkTo(0x0008, -3570, 0, 204220, 2000, 0x00)
    ChrWalkTo(0x0008, -2080, 0, 203320, 2000, 0x00)
    ChrWalkTo(0x0008, -2140, 0, 201500, 2000, 0x00)
    ChrTurnDirection(0x0008, 0x0101, 400)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#1730160425V这是很久以前\n',
            '我用过的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160503V这就算我的一点心意。\n',
            '你们就别客气，收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160427V虽然有些旧了，\n',
            '不过品质可是勿庸置疑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_2C22',
    )

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '工作安全帽',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '斗魂扎头巾',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0148, 1)
    AddItem(0x0146, 1)

    Jump('loc_2C6F')

    def _loc_2C22(): pass

    label('loc_2C22')

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '工作安全帽',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0148, 1)

    def _loc_2C6F(): pass

    label('loc_2C6F')

    ChrTalk(
        0x0101,
        (
            '#0010160428V#001F哇啊，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160429V#014F这样好吗？\n',
            '那么珍贵的物品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160430V没关系没关系，\n',
            '反正我也不可能再次出海了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1730160508V……那么，\n',
            '我也该继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1730160432V拿到你们捎来的东西，\n',
            '我真的非常高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160433V#040F请您一定要注意身体哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160434V#000F那么，\n',
            '多多保重了，老爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160512V#010F我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/C2209._SN', 101, 0, 0)
    IdleLoop()
    TalkEnd(0x0008)

    def _loc_2E0B(): pass

    label('loc_2E0B')

    EventEnd(0x00)
    MapSetFlags(0x00000001)

    Return()

# id: 0x0002 offset: 0x2E13
@scena.Code('func_02_2E13')
def func_02_2E13():
    @scena.Lambda('lambda_2E19')
    def lambda_2E19():
        ChrWalkTo(0x0101, -970, 0, 201500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2E19)

    WaitForThreadExit(0x0101, 0x0002)
    ChrSetDirection(0x0101, 270, 400)

    Return()

# id: 0x0003 offset: 0x2E3B
@scena.Code('func_03_2E3B')
def func_03_2E3B():
    @scena.Lambda('lambda_2E41')
    def lambda_2E41():
        ChrWalkTo(0x0102, -120, 0, 201000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2E41)

    WaitForThreadExit(0x0102, 0x0002)
    ChrSetDirection(0x0102, 270, 400)

    Return()

# id: 0x0004 offset: 0x2E63
@scena.Code('func_04_2E63')
def func_04_2E63():
    @scena.Lambda('lambda_2E69')
    def lambda_2E69():
        ChrWalkTo(0x0105, 330, 0, 202800, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_2E69)

    WaitForThreadExit(0x0105, 0x0002)
    ChrSetDirection(0x0105, 270, 400)

    Return()

# id: 0x0005 offset: 0x2E8B
@scena.Code('func_05_2E8B')
def func_05_2E8B():
    EventBegin(0x01)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽全部消灭干净了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x01)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

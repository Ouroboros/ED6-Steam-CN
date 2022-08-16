import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0130_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0130_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0130.x'
    header.mapIndex       = 3
    header.bgm            = 10
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
    TalkBegin(0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x0007, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E9',
    )

    OP_28(0x0007, 0x01, 0x8000)

    ChrTalk(
        0x0008,
        (
            '#1080150770V哦，看你们的样子……\n',
            '是要出去旅行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150771V#000F嗯，是啊。\n',
            '我们要去柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150772V原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150773V如果可以的话，\n',
            '能不能帮我一个忙呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150774V我这有一封给柏斯的豪尔斯教区长的信，\n',
            '因为定期船停航的缘故没法寄出，\n',
            '正在为这事发愁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150775V如果方便的话，\n',
            '请在旅途中顺便帮我送去好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32F')

    def _loc_1E9(): pass

    label('loc_1E9')

    ChrTalk(
        0x0008,
        (
            '#1080150776V……对了。\n',
            '你们说要去柏斯吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150777V#000F是啊，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150778V这样的话我还有一件事要拜托你们，\n',
            '能不能帮个忙呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150779V我有一封给柏斯的豪尔斯教区长的信，\n',
            '因为定期船停航的缘故没法寄出，\n',
            '正在为这事发愁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150775V如果方便的话，\n',
            '请在旅途中顺便帮我送去好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32F(): pass

    label('loc_32F')

    Call(1, 0x0003)
    TalkEnd(0x0008)

    Return()

# id: 0x0001 offset: 0x337
@scena.Code('func_01_337')
def func_01_337():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    Fade(1000)

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0xE678),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_38E',
    )

    ChrSetPos(0x0101, 60600, 1000, 52500, 270)
    ChrSetPos(0x0102, 60600, 1000, 51300, 315)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_38B',
    )

    ChrSetPos(0x0103, 61600, 1000, 50200, 315)

    def _loc_38B(): pass

    label('loc_38B')

    Jump('loc_3C8')

    def _loc_38E(): pass

    label('loc_38E')

    ChrSetPos(0x0101, 57400, 1000, 52500, 90)
    ChrSetPos(0x0102, 57400, 1000, 51300, 45)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_3C8',
    )

    ChrSetPos(0x0103, 56400, 1000, 50200, 45)

    def _loc_3C8(): pass

    label('loc_3C8')

    OP_69(0x0101, 2000)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x0007, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C0',
    )

    OP_28(0x0007, 0x01, 0x8000)
    OP_4A(0x0008, 255)
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150770V哦，看你们的样子……\n',
            '是要出去旅行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150782V#000F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150783V虽然我们马上要去柏斯了，\n',
            '不过在出发前有些东西\n',
            '必须要交给教区长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150784V给我……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_582')

    def _loc_4C0(): pass

    label('loc_4C0')

    OP_4A(0x0008, 255)
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150785V哦，看你们的样子……\n',
            '你们还没出发吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150782V#000F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150787V其实在出发前有些东西\n',
            '必须要交给教区长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150784V给我……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_582(): pass

    label('loc_582')

    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '魔兽羽翼',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#1080150266V这不就是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150267V#010F『熊刺草』和『魔兽羽翼』。\n',
            '您需要的药材。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150268V是您委托游击士协会去采集的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150269V哦，确实是我委托的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150270V不过，\n',
            '没想到是由你们去采集的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150794V艾丝蒂尔、约修亚。\n',
            '真的十分感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150795V你们两个，\n',
            '都能尽心尽力去完成工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150796V这样我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150797V#000F嗯⊙\n',
            '以后我们也会全心全意努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150798V这样我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150799V以后的旅途中，\n',
            '也一定要小心谨慎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150800V愿你们能\n',
            '常受女神的保佑。',
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
            '任务【采集药材】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0386, 1)
    RemoveItem(0x039F, 1)
    OP_28(0x0007, 0x04, 0x10)
    OP_28(0x0007, 0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrSetDirection(0x0008, 180, 0)
    EventEnd(0x00)
    OP_4B(0x0008, 255)

    Return()

# id: 0x0002 offset: 0x8E8
@scena.Code('func_02_8E8')
def func_02_8E8():
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#1080150801V哦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150802V难道是有空帮我送信了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_933(): pass

    label('loc_933')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CEB',
    )

    FadeOut(300, 0, 100)

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
        100,
        0,
        (
            TXT(0x00, '【接受】\n'),
            TXT(0x01, '【拒绝】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_997'),
        (0x00000001, 'loc_BCB'),
        (-1, 'loc_CE8'),
    )

    def _loc_997(): pass

    label('loc_997')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_28(0x000D, 0x04, 0x08)
    OP_28(0x000D, 0x01, 0x0001)
    AddItem(0x0329, 1)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150803V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_A1B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030150804V#020F反正也是举手之劳，\n',
            '您就别客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A1B(): pass

    label('loc_A1B')

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150805V谢谢你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150806V嗯，\n',
            '那么就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '教区长的亲笔信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150807V#010F交给柏斯的豪尔斯教区长\n',
            '就可以了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150808V是的。\n',
            '教会在柏斯市的东侧，\n',
            '进城后很容易就可以找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150809V周游各地的时候\n',
            '增长的见识和经历，\n',
            '可以变为自身的财富。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150800V愿你们能\n',
            '常受女神的保佑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE8')

    def _loc_BCB(): pass

    label('loc_BCB')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_28(0x000D, 0x01, 0x8000)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150811V#003F嗯～对不起，\n',
            '现在有些困难……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150812V是这样啊。\n',
            '那就只能先不送了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150813V……但是，你们越是着急，\n',
            '就越容易发生危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150814V所以在旅途中\n',
            '一定要小心谨慎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150815V那么，\n',
            '愿你们常受女神的保佑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE8')

    def _loc_CE8(): pass

    label('loc_CE8')

    Jump('loc_933')

    def _loc_CEB(): pass

    label('loc_CEB')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkEnd(0x0008)

    Return()

# id: 0x0003 offset: 0xCF9
@scena.Code('func_03_CF9')
def func_03_CF9():
    OP_28(0x000D, 0x04, 0x04)
    OP_28(0x000D, 0x04, 0x02)
    def _loc_D03(): pass

    label('loc_D03')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10DC',
    )

    FadeOut(300, 0, 100)

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
        100,
        0,
        (
            TXT(0x00, '【接受】\n'),
            TXT(0x01, '【拒绝】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_D67'),
        (0x00000001, 'loc_F86'),
        (-1, 'loc_10D9'),
    )

    def _loc_D67(): pass

    label('loc_D67')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_28(0x000D, 0x04, 0x08)
    OP_28(0x000D, 0x01, 0x0001)
    AddItem(0x0329, 1)

    ChrTalk(
        0x0101,
        (
            '#0010150803V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_DE4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030150804V#020F反正也是举手之劳，\n',
            '您就别客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DE4(): pass

    label('loc_DE4')

    ChrTalk(
        0x0008,
        (
            '#1080150805V谢谢你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150806V嗯，\n',
            '那么就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '教区长的亲笔信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#0020150807V#010F交给柏斯的豪尔斯教区长\n',
            '就可以了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 0)

    ChrTalk(
        0x0008,
        (
            '#1080150808V是的。\n',
            '教会在柏斯市的东侧，\n',
            '进城后很容易就可以找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150809V周游各地的时候\n',
            '增长的见识和经历，\n',
            '可以变为自身的财富。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150800V愿你们能\n',
            '常受女神的保佑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D9')

    def _loc_F86(): pass

    label('loc_F86')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_28(0x000D, 0x01, 0x8000)

    ChrTalk(
        0x0101,
        (
            '#0010150824V#003F对不起，教区长。\n',
            '我们还有很急的事情要去办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150825V是这样啊。\n',
            '那就只能先不送了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150813V……但是，你们越是着急，\n',
            '就越容易发生危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150814V所以在旅途中\n',
            '一定要小心谨慎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150828V#000F……嗯，我们会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150815V那么，\n',
            '愿你们常受女神的保佑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D9')

    def _loc_10D9(): pass

    label('loc_10D9')

    Jump('loc_D03')

    def _loc_10DC(): pass

    label('loc_10DC')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x10EA
@scena.Code('func_04_10EA')
def func_04_10EA():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    Fade(1000)

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0xE678),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_119D',
    )

    ChrSetPos(0x0101, 60600, 1000, 52500, 270)
    ChrSetPos(0x0102, 60600, 1000, 51300, 315)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1159',
    )

    ChrSetPos(0x0002, 61600, 1000, 51500, 270)
    ChrSetPos(0x0003, 61600, 1000, 50200, 315)

    Jump('loc_119A')

    def _loc_1159(): pass

    label('loc_1159')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_117B',
    )

    ChrSetPos(0x0002, 61600, 1000, 51500, 270)

    Jump('loc_119A')

    def _loc_117B(): pass

    label('loc_117B')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_119A',
    )

    ChrSetPos(0x0103, 61600, 1000, 51500, 270)

    def _loc_119A(): pass

    label('loc_119A')

    Jump('loc_1233')

    def _loc_119D(): pass

    label('loc_119D')

    ChrSetPos(0x0101, 57400, 1000, 52500, 90)
    ChrSetPos(0x0102, 57400, 1000, 51300, 45)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11F2',
    )

    ChrSetPos(0x0002, 56400, 1000, 51500, 90)
    ChrSetPos(0x0003, 56400, 1000, 50200, 45)

    Jump('loc_1233')

    def _loc_11F2(): pass

    label('loc_11F2')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1214',
    )

    ChrSetPos(0x0002, 56400, 1000, 51500, 90)

    Jump('loc_1233')

    def _loc_1214(): pass

    label('loc_1214')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1233',
    )

    ChrSetPos(0x0103, 56400, 1000, 51500, 90)

    def _loc_1233(): pass

    label('loc_1233')

    OP_69(0x0101, 2000)
    OP_0D()
    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_4A(0x0008, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12B1',
    )

    ChrTalk(
        0x0008,
        (
            '#1080150260V哦？是艾丝蒂尔啊。\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150261V#000F请收下这些，教区长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1361')

    def _loc_12B1(): pass

    label('loc_12B1')

    ChrTalk(
        0x0008,
        (
            '#1080150262V哦？是艾丝蒂尔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150263V今天依旧是\n',
            '那么的活泼开朗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010150264V#001F嘿嘿嘿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150265V请收下这些，教区长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1361(): pass

    label('loc_1361')

    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '魔兽羽翼',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#1080150266V这不就是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150267V#010F『熊刺草』和『魔兽羽翼』。\n',
            '您需要的药材。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150268V是您委托游击士协会去采集的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150269V哦，确实是我委托的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150270V不过，\n',
            '没想到是由你们去采集的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150271V艾丝蒂尔、约修亚，\n',
            '你们没有受伤吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0005)

    Return()

# id: 0x0005 offset: 0x1539
@scena.Code('func_05_1539')
def func_05_1539():
    ChrTalk(
        0x0101,
        (
            '#0010150272V#001F没事，完好无损⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150273V#000F……不信您看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150274V……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150275V……你们的状况\n',
            '让我有些担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150276V#004F啊～～！？\n',
            '不用担心、不用担心啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150277V我以前应该也对你们说过的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150278V一件事情若能顺利的进行，\n',
            '固然很令人高兴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150279V但是在这种时候，\n',
            '尤其要提高警觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150280V#007F好～～的。\n',
            '我以后会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150281V唔……\n',
            '时间还很充裕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150282V机会难得，我就给你们来一堂特别讲义如何……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010150283V#004F（不会吧……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150284V#506F对、对不起啊教区长。\n',
            '我们现在必须得走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_180B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020150285V#010F抱歉，教区长。\n',
            '其实我们还有紧急任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18C1')

    def _loc_180B(): pass

    label('loc_180B')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150286V#506F对吧，约修亚。\n',
            '我们还有其他工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150287V#017F（……真拿她没办法。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150288V#010F抱歉，教区长。\n',
            '我们得回游击士协会了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_18B9')
    def lambda_18B9():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18B9)

    def _loc_18C1(): pass

    label('loc_18C1')

    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1080150289V是这样啊，真是太遗憾了。\n',
            '不过工作是一定要完成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150290V艾丝蒂尔、约修亚，\n',
            '辛苦了，真是非常感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080150291V在你们二人走过的蓝天之下，\n',
            '空之女神会常伴左右。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【采集药材】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0386, 1)
    RemoveItem(0x039F, 1)
    OP_28(0x0007, 0x04, 0x10)
    OP_28(0x0007, 0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrSetDirection(0x0008, 180, 0)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x19FD
@scena.Code('func_06_19FD')
def func_06_19FD():
    EventBegin(0x00)
    MapSetFlags(0x00400000)
    MapClearFlags(0x00000001)
    ChrSetPos(0x000E, 59100, 0, 45800, 0)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetPos(0x0101, 59800, 0, 41000, 0)
    ChrSetPos(0x0102, 58700, 0, 40000, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A74',
    )

    ChrSetPos(0x0002, 59600, 0, 39000, 0)
    ChrSetPos(0x0003, 58600, 0, 38500, 0)

    Jump('loc_1A93')

    def _loc_1A74(): pass

    label('loc_1A74')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A93',
    )

    ChrSetPos(0x0002, 59600, 0, 39000, 0)

    def _loc_1A93(): pass

    label('loc_1A93')

    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)
    CameraMove(59100, 0, 45800, 3000)
    ChrTurnDirection(0x000E, 0x0101, 0)
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x000E, 0, 0, 0, 800, 12000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010150731V#507F嘿嘿嘿嘿……\n',
            '这下逃不掉了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150732V老老实实束手就擒吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrSetDirection(0x000E, 135, 400)
    Sleep(500)

    ChrSetDirection(0x000E, 225, 400)
    Sleep(500)

    ChrSetPos(0x000D, 59100, 0, 45800, 180)
    ChrClearFlags(0x000D, 0x0008)
    ChrSetFlags(0x000E, 0x0008)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000D, 0x0008)
    ChrSetFlags(0x000D, 0x0040)
    ChrMoveTo(0x000D, 59100, 0, 46800, 3000, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C36',
    )

    @scena.Lambda('lambda_1BBC')
    def lambda_1BBC():
        ChrTurnDirection(0x0101, 0x000D, 0)
        Yield()

        Jump('lambda_1BBC')

    DispatchAsync2(0x0101, 0x0001, lambda_1BBC)

    @scena.Lambda('lambda_1BCD')
    def lambda_1BCD():
        ChrTurnDirection(0x0102, 0x000D, 0)
        Yield()

        Jump('lambda_1BCD')

    DispatchAsync2(0x0102, 0x0001, lambda_1BCD)

    @scena.Lambda('lambda_1BDE')
    def lambda_1BDE():
        ChrTurnDirection(0x0008, 0x000D, 0)
        Yield()

        Jump('lambda_1BDE')

    DispatchAsync2(0x0008, 0x0001, lambda_1BDE)

    @scena.Lambda('lambda_1BEF')
    def lambda_1BEF():
        ChrTurnDirection(0x010F, 0x000D, 0)
        Yield()

        Jump('lambda_1BEF')

    DispatchAsync2(0x010F, 0x0001, lambda_1BEF)

    @scena.Lambda('lambda_1C00')
    def lambda_1C00():
        ChrTurnDirection(0x0110, 0x000D, 0)
        Yield()

        Jump('lambda_1C00')

    DispatchAsync2(0x0110, 0x0001, lambda_1C00)

    ChrWalkTo(0x000D, 49700, 0, 51400, 7000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x010F, 0xFF)
    TerminateThread(0x0110, 0xFF)

    Jump('loc_1CFB')

    def _loc_1C36(): pass

    label('loc_1C36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_1CA8',
    )

    @scena.Lambda('lambda_1C43')
    def lambda_1C43():
        ChrTurnDirection(0x0101, 0x000D, 0)
        Yield()

        Jump('lambda_1C43')

    DispatchAsync2(0x0101, 0x0001, lambda_1C43)

    @scena.Lambda('lambda_1C54')
    def lambda_1C54():
        ChrTurnDirection(0x0102, 0x000D, 0)
        Yield()

        Jump('lambda_1C54')

    DispatchAsync2(0x0102, 0x0001, lambda_1C54)

    @scena.Lambda('lambda_1C65')
    def lambda_1C65():
        ChrTurnDirection(0x0008, 0x000D, 0)
        Yield()

        Jump('lambda_1C65')

    DispatchAsync2(0x0008, 0x0001, lambda_1C65)

    @scena.Lambda('lambda_1C76')
    def lambda_1C76():
        ChrTurnDirection(0x010F, 0x000D, 0)
        Yield()

        Jump('lambda_1C76')

    DispatchAsync2(0x010F, 0x0001, lambda_1C76)

    ChrWalkTo(0x000D, 49700, 0, 51400, 7000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x010F, 0xFF)

    Jump('loc_1CFB')

    def _loc_1CA8(): pass

    label('loc_1CA8')

    @scena.Lambda('lambda_1CAE')
    def lambda_1CAE():
        ChrTurnDirection(0x0101, 0x000D, 0)
        Yield()

        Jump('lambda_1CAE')

    DispatchAsync2(0x0101, 0x0001, lambda_1CAE)

    @scena.Lambda('lambda_1CBF')
    def lambda_1CBF():
        ChrTurnDirection(0x0102, 0x000D, 0)
        Yield()

        Jump('lambda_1CBF')

    DispatchAsync2(0x0102, 0x0001, lambda_1CBF)

    @scena.Lambda('lambda_1CD0')
    def lambda_1CD0():
        ChrTurnDirection(0x0008, 0x000D, 0)
        Yield()

        Jump('lambda_1CD0')

    DispatchAsync2(0x0008, 0x0001, lambda_1CD0)

    ChrWalkTo(0x000D, 49700, 0, 51400, 7000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)

    def _loc_1CFB(): pass

    label('loc_1CFB')

    ChrSetPos(0x000D, 0, 0, 0, 180)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D52',
    )

    @scena.Lambda('lambda_1D1D')
    def lambda_1D1D():
        OP_92(0x010F, 0x0000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_1D1D)

    @scena.Lambda('lambda_1D32')
    def lambda_1D32():
        OP_92(0x0110, 0x0000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0110, 0x0001, lambda_1D32)

    OP_92(0x0001, 0x0000, 0, 3000, 0x00)

    Jump('loc_1D8D')

    def _loc_1D52(): pass

    label('loc_1D52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_1D7F',
    )

    @scena.Lambda('lambda_1D5F')
    def lambda_1D5F():
        OP_92(0x010F, 0x0000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_1D5F)

    OP_92(0x0001, 0x0000, 0, 3000, 0x00)

    Jump('loc_1D8D')

    def _loc_1D7F(): pass

    label('loc_1D7F')

    OP_92(0x0001, 0x0000, 0, 3000, 0x00)

    def _loc_1D8D(): pass

    label('loc_1D8D')

    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x0102, 0x0040)
    OP_85(0x0008)
    MapClearFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1DA2
@scena.Code('func_07_1DA2')
def func_07_1DA2():
    EventBegin(0x00)
    MapSetFlags(0x00400000)
    MapClearFlags(0x00000001)
    FadeIn(1000, 0)
    CameraMove(46700, 5000, 49700, 0)
    ChrSetPos(0x000E, 52100, 5000, 48000, 90)
    ChrSetFlags(0x000E, 0x0040)
    ChrClearFlags(0x000E, 0x0008)
    ChrSetPos(0x0101, 51700, 5000, 50300, 180)
    ChrSetPos(0x0102, 52100, 5000, 50800, 180)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E38',
    )

    ChrSetPos(0x0002, 51500, 5000, 51300, 180)
    ChrSetPos(0x0003, 52100, 5000, 51700, 180)

    Jump('loc_1E57')

    def _loc_1E38(): pass

    label('loc_1E38')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E57',
    )

    ChrSetPos(0x0002, 51500, 5000, 51300, 180)

    def _loc_1E57(): pass

    label('loc_1E57')

    CameraMove(51500, 5000, 49200, 3000)
    ChrTurnDirection(0x000E, 0x0101, 0)
    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x000E, 0, 0, 0, 800, 12000)

    ChrTalk(
        0x0101,
        (
            '#0010150733V#002F好孩子～\n',
            '要乖乖地听话哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrWalkTo(0x0101, 51700, 5000, 50200, 2000, 0x00)
    ChrMoveTo(0x000E, 52100, 5000, 47700, 3000, 0x00)
    Sleep(1000)

    @scena.Lambda('lambda_1F05')
    def lambda_1F05():
        ChrWalkTo(0x0101, 51700, 5000, 49900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F05)

    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(200)

    @scena.Lambda('lambda_1F37')
    def lambda_1F37():
        ChrMoveTo(0x000E, 52100, 5000, 47400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1F37)

    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010150734V#002F不要动哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F78')
    def lambda_1F78():
        ChrWalkTo(0x0101, 51700, 5000, 49500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F78)

    OP_63(0x000E)
    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(200)

    @scena.Lambda('lambda_1FAD')
    def lambda_1FAD():
        ChrMoveTo(0x000E, 52100, 5000, 46500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1FAD)

    OP_63(0x000E)
    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x000E, 45, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 90, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 135, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 180, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 225, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 270, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 315, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 0, 0)
    ChrSetDirection(0x000E, 315, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 270, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 225, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 180, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 135, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 90, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 45, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 0, 0)
    ChrSetDirection(0x000E, 45, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 90, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 135, 0)
    Sleep(50)

    ChrSetDirection(0x000E, 180, 0)
    Sleep(200)

    CreateThread(0x000E, 0x01, 0x01, 0x0008)
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020150735V#014F艾丝蒂尔，\n',
            '不要把它逼急了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150736V如果它从这里跳下去，\n',
            '那可怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150737V#009F我、我知道啦，\n',
            '可是它怎么也不听话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2178')
    def lambda_2178():
        ChrTurnDirection(0x0101, 0x0102, 0)
        Yield()

        Jump('lambda_2178')

    DispatchAsync2(0x0101, 0x0001, lambda_2178)

    ChrWalkTo(0x0102, 52100, 5000, 48400, 1000, 0x00)
    TerminateThread(0x0101, 0xFF)
    Sleep(400)

    Fade(500)
    ChrSetChipByIndex(0x0102, 13)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020150738V#011F小安莉尔，乖，到我这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    Sleep(800)

    ChrTurnDirection(0x000E, 0x0102, 600)
    Sleep(200)

    OP_62(0x000E, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(600)

    ChrTalk(
        0x0102,
        (
            '#0020150739V#011F真是对不起，吓着你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150740V#009F（哼。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150741V#019F乖，别跑。\n',
            '和我们回阿姨那里去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    OP_62(0x000E, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1500)

    @scena.Lambda('lambda_22CC')
    def lambda_22CC():
        ChrWalkTo(0x000E, 52000, 5000, 47500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_22CC)

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000E,
        (
            '#1100150742V喵喵～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(600)

    ChrTalk(
        0x0102,
        (
            '#0020150743V#019F对，就是这样。安莉尔真是乖孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150744V我们回家吧，\n',
            '阿姨在等着你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapClearFlags(0x00400000)
    FadeOut(500, 0, -1)
    NewScene('ED6_DT01/T0100._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x2380
@scena.Code('func_08_2380')
def func_08_2380():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_23A5',
    )

    OP_63(0x000E)
    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(600)

    Yield()

    Jump('func_08_2380')

    def _loc_23A5(): pass

    label('loc_23A5')

    Return()

# id: 0x0009 offset: 0x23A6
@scena.Code('func_09_23A6')
def func_09_23A6():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2411',
    )

    ChrTalk(
        0x0101,
        (
            '#0010150725V#006F先把那只小猫抓住再说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150726V好不容易把它追进这里来了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2489')

    def _loc_2411(): pass

    label('loc_2411')

    ChrTurnDirection(0x0102, 0x0001, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150727V#010F既然来到这里了，\n',
            '还是先把小猫抓住比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150728V如果这样放着不管，\n',
            '会惹出麻烦来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2489(): pass

    label('loc_2489')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

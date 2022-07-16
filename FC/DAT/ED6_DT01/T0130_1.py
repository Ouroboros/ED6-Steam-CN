import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0130_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0130_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

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

# id: 0xFFFF offset: 0x2293
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    TalkBegin(0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x0007, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CB',
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

    Jump('loc_2F8')

    def _loc_1CB(): pass

    label('loc_1CB')

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

    def _loc_2F8(): pass

    label('loc_2F8')

    Call(1, 0x0003)
    TalkEnd(0x0008)

    Return()

# id: 0x0001 offset: 0x300
@scena.Code('Init')
def Init():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    Fade(1000)

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0xE678),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_357',
    )

    SetChrPos(0x0101, 60600, 1000, 52500, 270)
    SetChrPos(0x0102, 60600, 1000, 51300, 315)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_354',
    )

    SetChrPos(0x0103, 61600, 1000, 50200, 315)

    def _loc_354(): pass

    label('loc_354')

    Jump('loc_391')

    def _loc_357(): pass

    label('loc_357')

    SetChrPos(0x0101, 57400, 1000, 52500, 90)
    SetChrPos(0x0102, 57400, 1000, 51300, 45)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_391',
    )

    SetChrPos(0x0103, 56400, 1000, 50200, 45)

    def _loc_391(): pass

    label('loc_391')

    OP_69(0x0101, 2000)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x0007, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_475',
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

    Jump('loc_523')

    def _loc_475(): pass

    label('loc_475')

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

    def _loc_523(): pass

    label('loc_523')

    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
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
    SetChrName('')
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
    SetChrName('')

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
    SetChrDirection(0x0008, 180, 0)
    EventEnd(0x00)
    OP_4B(0x0008, 255)

    Return()

# id: 0x0002 offset: 0x84D
@scena.Code('ReInit')
def ReInit():
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
    def _loc_88E(): pass

    label('loc_88E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C05',
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
        (0x00000000, 'loc_8F2'),
        (0x00000001, 'loc_AFE'),
        (-1, 'loc_C02'),
    )

    def _loc_8F2(): pass

    label('loc_8F2')

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
        'loc_96C',
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

    def _loc_96C(): pass

    label('loc_96C')

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
    SetChrName('')

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

    Jump('loc_C02')

    def _loc_AFE(): pass

    label('loc_AFE')

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

    Jump('loc_C02')

    def _loc_C02(): pass

    label('loc_C02')

    Jump('loc_88E')

    def _loc_C05(): pass

    label('loc_C05')

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

# id: 0x0003 offset: 0xC13
@scena.Code('func_03_C13')
def func_03_C13():
    OP_28(0x000D, 0x04, 0x04)
    OP_28(0x000D, 0x04, 0x02)
    def _loc_C1D(): pass

    label('loc_C1D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FB0',
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
        (0x00000000, 'loc_C81'),
        (0x00000001, 'loc_E78'),
        (-1, 'loc_FAD'),
    )

    def _loc_C81(): pass

    label('loc_C81')

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
        'loc_CF4',
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

    def _loc_CF4(): pass

    label('loc_CF4')

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
    SetChrName('')

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

    Jump('loc_FAD')

    def _loc_E78(): pass

    label('loc_E78')

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

    Jump('loc_FAD')

    def _loc_FAD(): pass

    label('loc_FAD')

    Jump('loc_C1D')

    def _loc_FB0(): pass

    label('loc_FB0')

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

# id: 0x0004 offset: 0xFBE
@scena.Code('func_04_FBE')
def func_04_FBE():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    Fade(1000)

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0xE678),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1071',
    )

    SetChrPos(0x0101, 60600, 1000, 52500, 270)
    SetChrPos(0x0102, 60600, 1000, 51300, 315)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_102D',
    )

    SetChrPos(0x0002, 61600, 1000, 51500, 270)
    SetChrPos(0x0003, 61600, 1000, 50200, 315)

    Jump('loc_106E')

    def _loc_102D(): pass

    label('loc_102D')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_104F',
    )

    SetChrPos(0x0002, 61600, 1000, 51500, 270)

    Jump('loc_106E')

    def _loc_104F(): pass

    label('loc_104F')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_106E',
    )

    SetChrPos(0x0103, 61600, 1000, 51500, 270)

    def _loc_106E(): pass

    label('loc_106E')

    Jump('loc_1107')

    def _loc_1071(): pass

    label('loc_1071')

    SetChrPos(0x0101, 57400, 1000, 52500, 90)
    SetChrPos(0x0102, 57400, 1000, 51300, 45)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10C6',
    )

    SetChrPos(0x0002, 56400, 1000, 51500, 90)
    SetChrPos(0x0003, 56400, 1000, 50200, 45)

    Jump('loc_1107')

    def _loc_10C6(): pass

    label('loc_10C6')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10E8',
    )

    SetChrPos(0x0002, 56400, 1000, 51500, 90)

    Jump('loc_1107')

    def _loc_10E8(): pass

    label('loc_10E8')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1107',
    )

    SetChrPos(0x0103, 56400, 1000, 51500, 90)

    def _loc_1107(): pass

    label('loc_1107')

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
        'loc_117B',
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

    Jump('loc_1217')

    def _loc_117B(): pass

    label('loc_117B')

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

    def _loc_1217(): pass

    label('loc_1217')

    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
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
    SetChrName('')
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

# id: 0x0005 offset: 0x13D1
@scena.Code('func_05_13D1')
def func_05_13D1():
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
        'loc_165D',
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

    Jump('loc_1704')

    def _loc_165D(): pass

    label('loc_165D')

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

    @scena.Lambda('lambda_16FC')
    def lambda_16FC():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16FC)

    def _loc_1704(): pass

    label('loc_1704')

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
    SetChrName('')

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
    SetChrDirection(0x0008, 180, 0)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x1831
@scena.Code('func_06_1831')
def func_06_1831():
    EventBegin(0x00)
    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    SetChrPos(0x000E, 59100, 0, 45800, 0)
    SetChrFlags(0x000D, 0x0040)
    SetChrPos(0x0101, 59800, 0, 41000, 0)
    SetChrPos(0x0102, 58700, 0, 40000, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18A8',
    )

    SetChrPos(0x0002, 59600, 0, 39000, 0)
    SetChrPos(0x0003, 58600, 0, 38500, 0)

    Jump('loc_18C7')

    def _loc_18A8(): pass

    label('loc_18A8')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18C7',
    )

    SetChrPos(0x0002, 59600, 0, 39000, 0)

    def _loc_18C7(): pass

    label('loc_18C7')

    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0102, 0x0040)
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

    SetChrDirection(0x000E, 135, 400)
    Sleep(500)

    SetChrDirection(0x000E, 225, 400)
    Sleep(500)

    SetChrPos(0x000D, 59100, 0, 45800, 180)
    ClearChrFlags(0x000D, 0x0008)
    SetChrFlags(0x000E, 0x0008)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000D, 0x0008)
    SetChrFlags(0x000D, 0x0040)
    ChrMoveTo(0x000D, 59100, 0, 46800, 3000, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A60',
    )

    @scena.Lambda('lambda_19E6')
    def lambda_19E6():
        ChrTurnDirection(0x0101, 0x000D, 0)
        Yield()

        Jump('lambda_19E6')

    DispatchAsync2(0x0101, 0x0001, lambda_19E6)

    @scena.Lambda('lambda_19F7')
    def lambda_19F7():
        ChrTurnDirection(0x0102, 0x000D, 0)
        Yield()

        Jump('lambda_19F7')

    DispatchAsync2(0x0102, 0x0001, lambda_19F7)

    @scena.Lambda('lambda_1A08')
    def lambda_1A08():
        ChrTurnDirection(0x0008, 0x000D, 0)
        Yield()

        Jump('lambda_1A08')

    DispatchAsync2(0x0008, 0x0001, lambda_1A08)

    @scena.Lambda('lambda_1A19')
    def lambda_1A19():
        ChrTurnDirection(0x010F, 0x000D, 0)
        Yield()

        Jump('lambda_1A19')

    DispatchAsync2(0x010F, 0x0001, lambda_1A19)

    @scena.Lambda('lambda_1A2A')
    def lambda_1A2A():
        ChrTurnDirection(0x0110, 0x000D, 0)
        Yield()

        Jump('lambda_1A2A')

    DispatchAsync2(0x0110, 0x0001, lambda_1A2A)

    ChrWalkTo(0x000D, 49700, 0, 51400, 7000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x010F, 0xFF)
    TerminateThread(0x0110, 0xFF)

    Jump('loc_1B25')

    def _loc_1A60(): pass

    label('loc_1A60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_1AD2',
    )

    @scena.Lambda('lambda_1A6D')
    def lambda_1A6D():
        ChrTurnDirection(0x0101, 0x000D, 0)
        Yield()

        Jump('lambda_1A6D')

    DispatchAsync2(0x0101, 0x0001, lambda_1A6D)

    @scena.Lambda('lambda_1A7E')
    def lambda_1A7E():
        ChrTurnDirection(0x0102, 0x000D, 0)
        Yield()

        Jump('lambda_1A7E')

    DispatchAsync2(0x0102, 0x0001, lambda_1A7E)

    @scena.Lambda('lambda_1A8F')
    def lambda_1A8F():
        ChrTurnDirection(0x0008, 0x000D, 0)
        Yield()

        Jump('lambda_1A8F')

    DispatchAsync2(0x0008, 0x0001, lambda_1A8F)

    @scena.Lambda('lambda_1AA0')
    def lambda_1AA0():
        ChrTurnDirection(0x010F, 0x000D, 0)
        Yield()

        Jump('lambda_1AA0')

    DispatchAsync2(0x010F, 0x0001, lambda_1AA0)

    ChrWalkTo(0x000D, 49700, 0, 51400, 7000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x010F, 0xFF)

    Jump('loc_1B25')

    def _loc_1AD2(): pass

    label('loc_1AD2')

    @scena.Lambda('lambda_1AD8')
    def lambda_1AD8():
        ChrTurnDirection(0x0101, 0x000D, 0)
        Yield()

        Jump('lambda_1AD8')

    DispatchAsync2(0x0101, 0x0001, lambda_1AD8)

    @scena.Lambda('lambda_1AE9')
    def lambda_1AE9():
        ChrTurnDirection(0x0102, 0x000D, 0)
        Yield()

        Jump('lambda_1AE9')

    DispatchAsync2(0x0102, 0x0001, lambda_1AE9)

    @scena.Lambda('lambda_1AFA')
    def lambda_1AFA():
        ChrTurnDirection(0x0008, 0x000D, 0)
        Yield()

        Jump('lambda_1AFA')

    DispatchAsync2(0x0008, 0x0001, lambda_1AFA)

    ChrWalkTo(0x000D, 49700, 0, 51400, 7000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)

    def _loc_1B25(): pass

    label('loc_1B25')

    SetChrPos(0x000D, 0, 0, 0, 180)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B7C',
    )

    @scena.Lambda('lambda_1B47')
    def lambda_1B47():
        OP_92(0x010F, 0x0000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_1B47)

    @scena.Lambda('lambda_1B5C')
    def lambda_1B5C():
        OP_92(0x0110, 0x0000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0110, 0x0001, lambda_1B5C)

    OP_92(0x0001, 0x0000, 0, 3000, 0x00)

    Jump('loc_1BB7')

    def _loc_1B7C(): pass

    label('loc_1B7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_1BA9',
    )

    @scena.Lambda('lambda_1B89')
    def lambda_1B89():
        OP_92(0x010F, 0x0000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010F, 0x0001, lambda_1B89)

    OP_92(0x0001, 0x0000, 0, 3000, 0x00)

    Jump('loc_1BB7')

    def _loc_1BA9(): pass

    label('loc_1BA9')

    OP_92(0x0001, 0x0000, 0, 3000, 0x00)

    def _loc_1BB7(): pass

    label('loc_1BB7')

    ClearChrFlags(0x0101, 0x0040)
    ClearChrFlags(0x0102, 0x0040)
    OP_85(0x0008)
    ClearMapFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1BCC
@scena.Code('func_07_1BCC')
def func_07_1BCC():
    EventBegin(0x00)
    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    FadeIn(1000, 0)
    CameraMove(46700, 5000, 49700, 0)
    SetChrPos(0x000E, 52100, 5000, 48000, 90)
    SetChrFlags(0x000E, 0x0040)
    ClearChrFlags(0x000E, 0x0008)
    SetChrPos(0x0101, 51700, 5000, 50300, 180)
    SetChrPos(0x0102, 52100, 5000, 50800, 180)

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C62',
    )

    SetChrPos(0x0002, 51500, 5000, 51300, 180)
    SetChrPos(0x0003, 52100, 5000, 51700, 180)

    Jump('loc_1C81')

    def _loc_1C62(): pass

    label('loc_1C62')

    If(
        (
            (Expr.Eval, "OP_42(0x000E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C81',
    )

    SetChrPos(0x0002, 51500, 5000, 51300, 180)

    def _loc_1C81(): pass

    label('loc_1C81')

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

    @scena.Lambda('lambda_1D2A')
    def lambda_1D2A():
        ChrWalkTo(0x0101, 51700, 5000, 49900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D2A)

    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(200)

    @scena.Lambda('lambda_1D5C')
    def lambda_1D5C():
        ChrMoveTo(0x000E, 52100, 5000, 47400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1D5C)

    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010150734V#002F不要动哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D98')
    def lambda_1D98():
        ChrWalkTo(0x0101, 51700, 5000, 49500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D98)

    OP_63(0x000E)
    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(200)

    @scena.Lambda('lambda_1DCD')
    def lambda_1DCD():
        ChrMoveTo(0x000E, 52100, 5000, 46500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1DCD)

    OP_63(0x000E)
    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrDirection(0x000E, 45, 0)
    Sleep(50)

    SetChrDirection(0x000E, 90, 0)
    Sleep(50)

    SetChrDirection(0x000E, 135, 0)
    Sleep(50)

    SetChrDirection(0x000E, 180, 0)
    Sleep(50)

    SetChrDirection(0x000E, 225, 0)
    Sleep(50)

    SetChrDirection(0x000E, 270, 0)
    Sleep(50)

    SetChrDirection(0x000E, 315, 0)
    Sleep(50)

    SetChrDirection(0x000E, 0, 0)
    SetChrDirection(0x000E, 315, 0)
    Sleep(50)

    SetChrDirection(0x000E, 270, 0)
    Sleep(50)

    SetChrDirection(0x000E, 225, 0)
    Sleep(50)

    SetChrDirection(0x000E, 180, 0)
    Sleep(50)

    SetChrDirection(0x000E, 135, 0)
    Sleep(50)

    SetChrDirection(0x000E, 90, 0)
    Sleep(50)

    SetChrDirection(0x000E, 45, 0)
    Sleep(50)

    SetChrDirection(0x000E, 0, 0)
    SetChrDirection(0x000E, 45, 0)
    Sleep(50)

    SetChrDirection(0x000E, 90, 0)
    Sleep(50)

    SetChrDirection(0x000E, 135, 0)
    Sleep(50)

    SetChrDirection(0x000E, 180, 0)
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

    @scena.Lambda('lambda_1F89')
    def lambda_1F89():
        ChrTurnDirection(0x0101, 0x0102, 0)
        Yield()

        Jump('lambda_1F89')

    DispatchAsync2(0x0101, 0x0001, lambda_1F89)

    ChrWalkTo(0x0102, 52100, 5000, 48400, 1000, 0x00)
    TerminateThread(0x0101, 0xFF)
    Sleep(400)

    Fade(500)
    SetChrChipByIndex(0x0102, 13)
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

    @scena.Lambda('lambda_20C9')
    def lambda_20C9():
        ChrWalkTo(0x000E, 52000, 5000, 47500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_20C9)

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
    ClearMapFlags(0x00400000)
    FadeOut(500, 0, -1)
    NewScene('ED6_DT01/T0100._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x216E
@scena.Code('func_08_216E')
def func_08_216E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2193',
    )

    OP_63(0x000E)
    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(600)

    Yield()

    Jump('func_08_216E')

    def _loc_2193(): pass

    label('loc_2193')

    Return()

# id: 0x0009 offset: 0x2194
@scena.Code('func_09_2194')
def func_09_2194():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21F5',
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

    Jump('loc_2263')

    def _loc_21F5(): pass

    label('loc_21F5')

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

    def _loc_2263(): pass

    label('loc_2263')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

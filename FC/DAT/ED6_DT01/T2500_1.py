import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2500_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2500_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2500.x'
    header.mapIndex       = 1
    header.bgm            = 12
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
    EventBegin(0x00)
    Fade(1000)
    OP_6C(135000, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1920171061V呼，难办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1920171062V这样下去校园的装饰\n',
            '就完成不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1920171063V想要找人帮忙，\n',
            '但是学生们现在都很忙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 135, 400)

    ChrTalk(
        0x00FE,
        (
            '#1920171064V你们看吧，\n',
            '还有一些没能装饰到的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0147')
    def lambda_0147():
        CameraMove(49960, 1500, 53870, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0147)

    Sleep(100)

    ChrTurnDirectionByPos(0x0101, 49960, 53870, 400)
    Sleep(150)

    ChrTurnDirectionByPos(0x0105, 49960, 53870, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_198',
    )

    ChrTurnDirectionByPos(0x013B, 49960, 53870, 400)

    def _loc_198(): pass

    label('loc_198')

    WaitForThreadExit(0x00FE, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010171065V#004F哎呀……\n',
            '正中间没有垂幕啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171066V#003F唔～\n',
            '的确有些不好看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1920171067V对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_021C')
    def lambda_021C():
        OP_69(0x0000, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_021C)

    Sleep(100)

    ChrTurnDirection(0x0101, 0x00FE, 400)
    Sleep(100)

    ChrTurnDirection(0x0105, 0x00FE, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_251',
    )

    ChrTurnDirection(0x013B, 0x00FE, 400)

    def _loc_251(): pass

    label('loc_251')

    WaitForThreadExit(0x00FE, 0x0001)

    ChrTalk(
        0x00FE,
        (
            '#1920171068V如果看到没有装饰的地方，\n',
            '还请告诉我一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1920171069V我会很快过去，\n',
            '把它给弄好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1920171070V只要稍微注意一下\n',
            '应该就可以发现的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010171071V#000F这么说，\n',
            '只要找到像这样\n',
            '还没装饰的地方就可以了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171072V嗯，明白了。\n',
            '如果看到了就回来告诉您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1920171073V啊，那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0027, 0x01, 0x0001)
    OP_65(0x03, 0x0001)
    OP_65(0x04, 0x0001)
    OP_65(0x05, 0x0001)
    EventEnd(0x01)

    Return()

# id: 0x0001 offset: 0x3A8
@scena.Code('func_01_3A8')
def func_01_3A8():
    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0002)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E29',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6C(225000, 0)
    ChrSetPos(0x0101, 21320, 250, 26540, 180)
    ChrSetPos(0x0105, 21880, 0, 27550, 180)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_405',
    )

    ChrSetPos(0x013B, 20790, 0, 27100, 180)

    def _loc_405(): pass

    label('loc_405')

    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010171106V#004F哎……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171144V这里没有彩旗吗……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_477',
    )

    ChrTurnDirection(0x0101, 0x013B, 400)

    Jump('loc_47E')

    def _loc_477(): pass

    label('loc_477')

    ChrTurnDirection(0x0101, 0x0105, 400)

    def _loc_47E(): pass

    label('loc_47E')

    ChrTalk(
        0x0101,
        (
            '#0010171145V#002F你看，其他建筑物的门口\n',
            '不都有挂上彩旗的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_571',
    )

    ChrTalk(
        0x013B,
        (
            '#0510171146V#643F啊，\n',
            '这样说的话好像真的是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510171147V这个地方应该是还没有装饰好。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171148V#040F我们去告诉\n',
            '勤务员巴克斯师傅吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    Jump('loc_5DB')

    def _loc_571(): pass

    label('loc_571')

    ChrTalk(
        0x0105,
        (
            '#0060171149V#044F啊，真的呢。\n',
            '好像还没有装饰到呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171148V#040F我们去告诉\n',
            '勤务员巴克斯师傅吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5DB(): pass

    label('loc_5DB')

    ChrTalk(
        0x0101,
        (
            '#0010171151V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0015, 30130, 0, 28910, 270)
    ChrSetPos(0x0101, 22450, 0, 27570, 180)
    ChrSetPos(0x0105, 21590, 0, 28160, 180)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_659',
    )

    ChrSetPos(0x013B, 20300, 0, 27960, 90)

    def _loc_659(): pass

    label('loc_659')

    ChrSetDirection(0x0101, 90, 0)
    ChrSetDirection(0x0105, 90, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_67C',
    )

    ChrSetDirection(0x013B, 90, 0)

    def _loc_67C(): pass

    label('loc_67C')

    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    ChrSetFlags(0x0015, 0x0040)
    ChrWalkTo(0x0015, 24380, 0, 27840, 3000, 0x00)
    ChrWalkTo(0x0015, 23530, 0, 27230, 3000, 0x00)
    OP_4A(0x0015, 255)
    Sleep(400)

    ChrSetDirection(0x0015, 225, 400)
    OP_62(0x0015, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0015,
        (
            '#1920171152V啊，果然。\n',
            '很会观察嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0015, 0x0101, 400)

    ChrTalk(
        0x0015,
        (
            '#1920171153V好，\n',
            '我这就开始装饰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_78A',
    )

    ChrTurnDirection(0x013B, 0x0101, 400)

    ChrTalk(
        0x013B,
        (
            '#0510171154V#644F我们也来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0778')
    def lambda_0778():
        ChrTurnDirection(0x0105, 0x013B, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0778)

    ChrTurnDirection(0x0101, 0x013B, 400)

    Jump('loc_7BB')

    def _loc_78A(): pass

    label('loc_78A')

    ChrTalk(
        0x0105,
        (
            '#0060171155V#040F我们也来帮忙吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    def _loc_7BB(): pass

    label('loc_7BB')

    ChrTalk(
        0x0101,
        (
            '#0010171156V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1920171157V啊，谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0800')
    def lambda_0800():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0800)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_824',
    )

    @scena.Lambda('lambda_081C')
    def lambda_081C():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_081C)

    def _loc_824(): pass

    label('loc_824')

    ChrTurnDirection(0x0101, 0x0015, 400)

    ChrTalk(
        0x0015,
        (
            '#1920171158V那么就\n',
            '有劳你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0856')
    def lambda_0856():
        ChrWalkTo(0x0101, 22450, 0, 26200, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0856)

    @scena.Lambda('lambda_0871')
    def lambda_0871():
        ChrWalkTo(0x0105, 21590, 0, 26400, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0871)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8AF',
    )

    @scena.Lambda('lambda_089A')
    def lambda_089A():
        ChrWalkTo(0x013B, 20820, 250, 26020, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_089A)

    def _loc_8AF(): pass

    label('loc_8AF')

    @scena.Lambda('lambda_08B5')
    def lambda_08B5():
        ChrWalkTo(0x0015, 23220, 250, 26040, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_08B5)

    @scena.Lambda('lambda_08D0')
    def lambda_08D0():
        OP_6C(135000, 2500)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_08D0)

    CameraMove(22030, 3500, 24930, 1500)
    FadeOut(1000, 0, -1)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0105, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_913',
    )

    WaitForThreadExit(0x013B, 0x0001)

    def _loc_913(): pass

    label('loc_913')

    WaitForThreadExit(0x0015, 0x0001)
    Sleep(400)

    OP_72(0x001E, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    Sleep(400)

    OP_28(0x0027, 0x01, 0x0002)

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0002)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0004)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0008)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CA9',
    )

    ChrTalk(
        0x0015,
        (
            '#1920171088V……好。\n',
            '这样就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0101, 1500)
    ChrTurnDirection(0x0015, 0x0101, 400)

    ChrTalk(
        0x0015,
        (
            '#1920171089V呼……\n',
            '总算是全部解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1920171090V哎呀～\n',
            '让你们费心了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09E6')
    def lambda_09E6():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_09E6)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A0A',
    )

    @scena.Lambda('lambda_0A02')
    def lambda_0A02():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0A02)

    def _loc_A0A(): pass

    label('loc_A0A')

    ChrTurnDirection(0x0101, 0x0015, 400)

    ChrTalk(
        0x0101,
        (
            '#0010171091V#000F没什么，不用介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171092V好不容易才有一次学园祭，\n',
            '不好好准备一下怎么能行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171093V#040F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171094V既然是我们大家的节日，\n',
            '帮帮忙那是应该的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B26',
    )

    ChrTurnDirection(0x013B, 0x0105, 400)

    ChrTalk(
        0x013B,
        (
            '#0510171095V#644F不愧是科洛丝。\n',
            '真是说出了我们的心声啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B26(): pass

    label('loc_B26')

    ChrTalk(
        0x0015,
        (
            '#1920171096V哈哈～\n',
            '的确如此啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x013B, 0x0015, 400)

    ChrTalk(
        0x0015,
        (
            '#1920171097V我们也很期待\n',
            '明天的学园祭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101168V#006F嗯！交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BE9',
    )

    ChrTalk(
        0x013B,
        (
            '#0510171099V#649F呵呵，\n',
            '那就请拭目以待了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C12')

    def _loc_BE9(): pass

    label('loc_BE9')

    ChrTalk(
        0x0105,
        (
            '#0060171100V#040F我们会竭尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C12(): pass

    label('loc_C12')

    ChrTalk(
        0x0015,
        (
            '#1920171101V那么，\n',
            '你们要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0027, 0x01, 0x0010)
    OP_28(0x003D, 0x01, 0x0200)
    OP_2C(0x003D, 0x01F4)
    OP_2B(0x003D, 0x0001)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '学园祭的校园任务\n',
            '【装饰校园】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    WaitEffect(0x02, 0x02)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_D86')

    def _loc_CA9(): pass

    label('loc_CA9')

    ChrTalk(
        0x0015,
        (
            '#1920171088V……好。\n',
            '这样就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0101, 1500)
    ChrTurnDirection(0x0015, 0x0101, 400)

    ChrTalk(
        0x0015,
        (
            '#1920171103V那，如果再看到的话，\n',
            '也麻烦告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D19')
    def lambda_0D19():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0D19)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D3D',
    )

    @scena.Lambda('lambda_0D35')
    def lambda_0D35():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0D35)

    def _loc_D3D(): pass

    label('loc_D3D')

    ChrTurnDirection(0x0101, 0x0015, 400)

    ChrTalk(
        0x0101,
        (
            '#0010171104V#006F嗯，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171105V#040F知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_D86(): pass

    label('loc_D86')

    @scena.Lambda('lambda_0D8C')
    def lambda_0D8C():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_0D8C')

    DispatchAsync2(0x0000, 0x0001, lambda_0D8C)

    @scena.Lambda('lambda_0D9D')
    def lambda_0D9D():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_0D9D')

    DispatchAsync2(0x0001, 0x0001, lambda_0D9D)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DC7',
    )

    @scena.Lambda('lambda_0DBC')
    def lambda_0DBC():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_0DBC')

    DispatchAsync2(0x0002, 0x0001, lambda_0DBC)

    def _loc_DC7(): pass

    label('loc_DC7')

    ChrWalkTo(0x0015, 24710, 0, 28270, 3000, 0x00)
    ChrWalkTo(0x0015, 31280, 0, 28000, 3000, 0x00)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E09',
    )

    TerminateThread(0x0002, 0xFF)

    def _loc_E09(): pass

    label('loc_E09')

    ChrSetPos(0x0015, 47880, 0, 56070, 135)
    ChrClearFlags(0x0015, 0x0040)
    OP_4B(0x0015, 255)
    OP_64(0x03, 0x0001)
    EventEnd(0x00)

    def _loc_E29(): pass

    label('loc_E29')

    TalkEnd(0x00FF)

    Return()

# id: 0x0002 offset: 0xE2D
@scena.Code('func_02_E2D')
def func_02_E2D():
    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_196D',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6C(45000, 0)
    ChrSetPos(0x0101, 38970, 0, 68950, 90)
    ChrSetPos(0x0105, 40770, 0, 68550, 45)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E8A',
    )

    ChrSetPos(0x013B, 38560, 0, 70140, 90)

    def _loc_E8A(): pass

    label('loc_E8A')

    OP_0D()
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0105,
        (
            '#0060171074V#044F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EDD',
    )

    @scena.Lambda('lambda_0ED5')
    def lambda_0ED5():
        ChrTurnDirection(0x013B, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0ED5)

    def _loc_EDD(): pass

    label('loc_EDD')

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150036V#000F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060171076V#044F这里……\n',
            '按理说这也应该是挂垂幕的地方啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171077V门的另外一边是挂好了的……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 0, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F9B',
    )

    @scena.Lambda('lambda_0F93')
    def lambda_0F93():
        ChrSetDirection(0x013B, 0, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0F93)

    def _loc_F9B(): pass

    label('loc_F9B')

    ChrSetDirection(0x0101, 0, 400)
    CameraMove(41580, 2000, 73990, 1500)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FE7',
    )

    ChrTalk(
        0x013B,
        (
            '#0510171078V#643F啊，没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_100A')

    def _loc_FE7(): pass

    label('loc_FE7')

    ChrTalk(
        0x0101,
        (
            '#0010171079V#004F啊，真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_100A(): pass

    label('loc_100A')

    OP_69(0x0105, 1500)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1032',
    )

    Sleep(100)

    @scena.Lambda('lambda_102A')
    def lambda_102A():
        ChrTurnDirection(0x013B, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_102A)

    def _loc_1032(): pass

    label('loc_1032')

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010171080V#000F那好，\n',
            '我们去告诉巴克斯师傅吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060171081V#040F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0015, 45200, 0, 65300, 270)
    ChrSetPos(0x0101, 39140, 0, 69780, 135)
    ChrSetPos(0x0105, 38830, 0, 68410, 135)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10F9',
    )

    Sleep(100)

    ChrSetPos(0x013B, 37730, 0, 69120, 135)

    def _loc_10F9(): pass

    label('loc_10F9')

    OP_69(0x0101, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_1115')
    def lambda_1115():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1115')

    DispatchAsync2(0x0000, 0x0001, lambda_1115)

    @scena.Lambda('lambda_1126')
    def lambda_1126():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1126')

    DispatchAsync2(0x0001, 0x0001, lambda_1126)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1150',
    )

    @scena.Lambda('lambda_1145')
    def lambda_1145():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1145')

    DispatchAsync2(0x0002, 0x0001, lambda_1145)

    def _loc_1150(): pass

    label('loc_1150')

    ChrSetFlags(0x0015, 0x0040)
    ChrWalkTo(0x0015, 40930, 0, 66670, 3000, 0x00)
    ChrWalkTo(0x0015, 40770, 0, 68550, 3000, 0x00)
    OP_4A(0x0015, 255)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_119B',
    )

    TerminateThread(0x0002, 0xFF)

    def _loc_119B(): pass

    label('loc_119B')

    Sleep(400)

    ChrSetDirection(0x0015, 45, 400)
    OP_62(0x0015, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0015,
        (
            '#1920171082V啊，\n',
            '这里很明显呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0015, 0x0101, 400)

    ChrTalk(
        0x0015,
        (
            '#1920171083V那么我这就\n',
            '开始装饰吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1254',
    )

    ChrTalk(
        0x013B,
        (
            '#0510171084V#644F好，我们也来帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0015, 0x013B, 400)

    Jump('loc_1289')

    def _loc_1254(): pass

    label('loc_1254')

    ChrTurnDirection(0x0101, 0x0015, 400)

    ChrTalk(
        0x0101,
        (
            '#0010171085V#000F我们也来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0015, 0x0101, 400)

    def _loc_1289(): pass

    label('loc_1289')

    ChrTalk(
        0x0015,
        (
            '#1920171086V哦，有劳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1920171087V那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_12CB')
    def lambda_12CB():
        OP_6C(135000, 4000)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_12CB)

    @scena.Lambda('lambda_12DB')
    def lambda_12DB():
        ChrWalkTo(0x0101, 41000, 0, 70140, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12DB)

    @scena.Lambda('lambda_12F6')
    def lambda_12F6():
        ChrWalkTo(0x0105, 40770, 0, 68550, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_12F6)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1334',
    )

    @scena.Lambda('lambda_131F')
    def lambda_131F():
        ChrWalkTo(0x013B, 40130, 0, 69380, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_131F)

    def _loc_1334(): pass

    label('loc_1334')

    @scena.Lambda('lambda_133A')
    def lambda_133A():
        CameraMove(41770, 3500, 69260, 4000)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_133A)

    ChrWalkTo(0x0015, 40930, 0, 67500, 2000, 0x00)
    ChrWalkTo(0x0015, 38150, 0, 68000, 2000, 0x00)
    FadeOut(1000, 0, -1)
    ChrWalkTo(0x0015, 38300, 0, 72350, 3000, 0x00)
    OP_72(0x0005, 0x0002)
    OP_6F(0x0005, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0105, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13BC',
    )

    WaitForThreadExit(0x013B, 0x0001)

    def _loc_13BC(): pass

    label('loc_13BC')

    WaitForThreadExit(0x0015, 0x0001)
    WaitForThreadExit(0x0015, 0x0002)
    OP_72(0x0012, 0x0004)
    ChrSetFlags(0x0015, 0x0040)
    ChrSetPos(0x0015, 43990, 0, 73850, 270)
    OP_6F(0x0005, 60)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1407',
    )

    ChrSetPos(0x013B, 41160, 0, 69290, 90)

    def _loc_1407(): pass

    label('loc_1407')

    FadeIn(1000, 0)
    ChrWalkTo(0x0015, 41560, 500, 74220, 3000, 0x00)
    OP_72(0x0005, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)
    ChrWalkTo(0x0015, 38300, 0, 72350, 3000, 0x00)
    ChrWalkTo(0x0015, 38000, 0, 68550, 3000, 0x00)
    ChrSetDirection(0x0015, 90, 400)
    OP_71(0x0005, 0x0800)
    Sleep(400)

    OP_28(0x0027, 0x01, 0x0004)

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0002)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0004)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0008)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17E8',
    )

    ChrTalk(
        0x0015,
        (
            '#1920171088V……好。\n',
            '这样就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0015, 0x0101, 400)

    @scena.Lambda('lambda_14CA')
    def lambda_14CA():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_14CA)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14EE',
    )

    @scena.Lambda('lambda_14E6')
    def lambda_14E6():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_14E6)

    def _loc_14EE(): pass

    label('loc_14EE')

    ChrTurnDirection(0x0101, 0x0015, 400)
    OP_69(0x0101, 1500)

    ChrTalk(
        0x0015,
        (
            '#1920171089V呼……\n',
            '总算是全部解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1920171090V哎呀～\n',
            '让你们费心了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010171091V#000F没什么，不用介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171092V好不容易才有一次学园祭，\n',
            '不好好准备一下怎么能行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171093V#040F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171094V既然是我们大家的节日，\n',
            '帮帮忙那是应该的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1665',
    )

    ChrTurnDirection(0x013B, 0x0105, 400)

    ChrTalk(
        0x013B,
        (
            '#0510171095V#644F不愧是科洛丝。\n',
            '真是说出了我们的心声啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1665(): pass

    label('loc_1665')

    ChrTalk(
        0x0015,
        (
            '#1920171096V哈哈～\n',
            '的确如此啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x013B, 0x0015, 400)

    ChrTalk(
        0x0015,
        (
            '#1920171097V我们也很期待\n',
            '明天的学园祭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101168V#006F嗯！交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1728',
    )

    ChrTalk(
        0x013B,
        (
            '#0510171099V#649F呵呵，\n',
            '那就请拭目以待了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1751')

    def _loc_1728(): pass

    label('loc_1728')

    ChrTalk(
        0x0105,
        (
            '#0060171100V#040F我们会竭尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1751(): pass

    label('loc_1751')

    ChrTalk(
        0x0015,
        (
            '#1920171101V那么，\n',
            '你们要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0027, 0x01, 0x0010)
    OP_28(0x003D, 0x01, 0x0200)
    OP_2C(0x003D, 0x01F4)
    OP_2B(0x003D, 0x0001)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '学园祭的校园任务\n',
            '【装饰校园】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    WaitEffect(0x02, 0x02)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_18C5')

    def _loc_17E8(): pass

    label('loc_17E8')

    ChrTalk(
        0x0015,
        (
            '#1920171088V……好。\n',
            '这样就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1815')
    def lambda_1815():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1815)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1839',
    )

    @scena.Lambda('lambda_1831')
    def lambda_1831():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_1831)

    def _loc_1839(): pass

    label('loc_1839')

    ChrTurnDirection(0x0101, 0x0015, 400)
    OP_69(0x0101, 1500)
    ChrTurnDirection(0x0015, 0x0101, 400)

    ChrTalk(
        0x0015,
        (
            '#1920171103V那，如果再看到的话，\n',
            '也麻烦告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010171104V#006F嗯，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171105V#040F知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_18C5(): pass

    label('loc_18C5')

    @scena.Lambda('lambda_18CB')
    def lambda_18CB():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_18CB')

    DispatchAsync2(0x0000, 0x0001, lambda_18CB)

    @scena.Lambda('lambda_18DC')
    def lambda_18DC():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_18DC')

    DispatchAsync2(0x0001, 0x0001, lambda_18DC)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1906',
    )

    @scena.Lambda('lambda_18FB')
    def lambda_18FB():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_18FB')

    DispatchAsync2(0x0002, 0x0001, lambda_18FB)

    def _loc_1906(): pass

    label('loc_1906')

    ChrSetFlags(0x0015, 0x0040)
    ChrWalkTo(0x0015, 39790, 0, 65330, 3000, 0x00)
    ChrWalkTo(0x0015, 46280, 0, 65340, 3000, 0x00)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_194D',
    )

    TerminateThread(0x0002, 0xFF)

    def _loc_194D(): pass

    label('loc_194D')

    ChrSetPos(0x0015, 47880, 0, 56070, 135)
    ChrClearFlags(0x0015, 0x0040)
    OP_4B(0x0015, 255)
    OP_64(0x04, 0x0001)
    EventEnd(0x00)

    def _loc_196D(): pass

    label('loc_196D')

    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0x1971
@scena.Code('func_03_1971')
def func_03_1971():
    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25CC',
    )

    OP_28(0x0027, 0x01, 0x0008)
    EventBegin(0x00)
    Fade(1000)
    OP_6C(270000, 0)
    ChrSetPos(0x0101, 53860, 0, 28500, 90)
    ChrSetPos(0x0105, 53290, 0, 29520, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19D4',
    )

    ChrSetPos(0x013B, 52540, 0, 30290, 90)

    def _loc_19D4(): pass

    label('loc_19D4')

    OP_69(0x0101, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010171106V#004F哎……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171107V啊，难道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    OP_94(0x01, 0x0101, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A63',
    )

    @scena.Lambda('lambda_1A56')
    def lambda_1A56():
        ChrTurnDirection(0x013B, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_1A56)

    Sleep(150)

    def _loc_1A63(): pass

    label('loc_1A63')

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060171108V#040F怎么了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010171109V#002F这里没有彩旗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_1ABB')
    def lambda_1ABB():
        ChrTurnDirection(0x0105, 0x0101, 0)
        Yield()

        Jump('lambda_1ABB')

    DispatchAsync2(0x0105, 0x0001, lambda_1ABB)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AE5',
    )

    @scena.Lambda('lambda_1ADA')
    def lambda_1ADA():
        ChrTurnDirection(0x013B, 0x0101, 0)
        Yield()

        Jump('lambda_1ADA')

    DispatchAsync2(0x013B, 0x0001, lambda_1ADA)

    def _loc_1AE5(): pass

    label('loc_1AE5')

    ChrWalkTo(0x0101, 51210, 0, 27710, 6000, 0x00)
    Sleep(100)

    Fade(1000)
    OP_6C(135000, 0)
    CameraMove(51210, 0, 27710, 0)
    Sleep(100)

    ChrSetDirection(0x0101, 90, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010171110V#000F你看，反面却是有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0105, 0x01)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B8A',
    )

    TerminateThread(0x013B, 0x01)

    @scena.Lambda('lambda_1B75')
    def lambda_1B75():
        ChrWalkTo(0x013B, 52630, 0, 29600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_1B75)

    def _loc_1B8A(): pass

    label('loc_1B8A')

    ChrWalkTo(0x0105, 52430, 0, 27750, 3000, 0x00)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BBA',
    )

    @scena.Lambda('lambda_1BB2')
    def lambda_1BB2():
        ChrSetDirection(0x013B, 315, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_1BB2)

    def _loc_1BBA(): pass

    label('loc_1BBA')

    ChrSetDirection(0x0105, 315, 400)
    Sleep(200)

    ChrSetDirection(0x0105, 180, 400)
    Sleep(200)

    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0105, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C63',
    )

    ChrTalk(
        0x0105,
        (
            '#0060171111V#044F啊，真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x013B, 0x0101, 400)

    ChrTalk(
        0x013B,
        (
            '#0510171112V#643F不愧是游击士，\n',
            '观察得这么仔细。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x013B, 400)

    Jump('loc_1CB4')

    def _loc_1C63(): pass

    label('loc_1C63')

    ChrTalk(
        0x0105,
        (
            '#0060171113V#044F啊，真的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171114V艾丝蒂尔，\n',
            '你很会观察啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    def _loc_1CB4(): pass

    label('loc_1CB4')

    ChrTalk(
        0x0101,
        (
            '#0010171115V#001F嘿嘿，还好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171116V那好，\n',
            '我们去告诉巴克斯师傅吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171117V#041F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0015, 49850, 0, 28600, 90)
    ChrSetPos(0x0101, 55720, 0, 29180, 270)
    ChrSetPos(0x0105, 55170, 0, 30090, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D84',
    )

    ChrSetPos(0x013B, 56220, 0, 30860, 270)

    def _loc_1D84(): pass

    label('loc_1D84')

    Sleep(1000)

    FadeIn(1000, 0)
    OP_6C(270000, 0)
    CameraMove(54350, 0, 28820, 0)
    OP_0D()

    @scena.Lambda('lambda_1DB3')
    def lambda_1DB3():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1DB3')

    DispatchAsync2(0x0000, 0x0001, lambda_1DB3)

    @scena.Lambda('lambda_1DC4')
    def lambda_1DC4():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1DC4')

    DispatchAsync2(0x0001, 0x0001, lambda_1DC4)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DEE',
    )

    @scena.Lambda('lambda_1DE3')
    def lambda_1DE3():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1DE3')

    DispatchAsync2(0x0002, 0x0001, lambda_1DE3)

    def _loc_1DEE(): pass

    label('loc_1DEE')

    ChrSetFlags(0x0015, 0x0040)
    ChrWalkTo(0x0015, 54680, 0, 28420, 3000, 0x00)
    OP_4A(0x0015, 255)
    Sleep(400)

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E2A',
    )

    TerminateThread(0x0002, 0xFF)

    def _loc_1E2A(): pass

    label('loc_1E2A')

    ChrSetDirection(0x0015, 270, 400)
    OP_62(0x0015, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0015,
        (
            '#1920171118V哦，\n',
            '这样的细节也能发现啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0015, 0x0101, 400)

    ChrTalk(
        0x0015,
        (
            '#1920171119V真是很不起眼的地方呢。\n',
            '我这就开始装饰吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F2E',
    )

    ChrTalk(
        0x013B,
        (
            '#0510171120V#644F那我们也来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1EF4')
    def lambda_1EF4():
        ChrTurnDirection(0x0105, 0x013B, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1EF4)

    ChrTurnDirection(0x0101, 0x013B, 400)

    ChrTalk(
        0x0105,
        (
            '#0060171121V#040F嗯，当然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0015, 0x013B, 400)

    Jump('loc_1F8A')

    def _loc_1F2E(): pass

    label('loc_1F2E')

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010171122V#000F好的，我们也来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060171081V#040F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F8A(): pass

    label('loc_1F8A')

    ChrTalk(
        0x0015,
        (
            '#1920171124V抱歉，又麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1FB6')
    def lambda_1FB6():
        ChrWalkTo(0x0015, 55140, 0, 24660, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_1FB6)

    @scena.Lambda('lambda_1FD1')
    def lambda_1FD1():
        ChrWalkTo(0x0101, 56060, 0, 31960, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FD1)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_202D',
    )

    @scena.Lambda('lambda_1FFA')
    def lambda_1FFA():
        ChrWalkTo(0x013B, 55210, 0, 32119, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_1FFA)

    @scena.Lambda('lambda_2015')
    def lambda_2015():
        ChrWalkTo(0x0105, 56020, 0, 25710, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2015)

    Jump('loc_2048')

    def _loc_202D(): pass

    label('loc_202D')

    @scena.Lambda('lambda_2033')
    def lambda_2033():
        ChrWalkTo(0x0105, 55210, 0, 32119, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2033)

    def _loc_2048(): pass

    label('loc_2048')

    CameraMove(54350, 1500, 28820, 1000)
    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0015, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0105, 0x01)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2082',
    )

    TerminateThread(0x013B, 0x01)

    def _loc_2082(): pass

    label('loc_2082')

    OP_72(0x001A, 0x0004)
    ChrSetPos(0x0101, 55720, 0, 29180, 270)
    ChrSetPos(0x0105, 55170, 0, 30090, 270)
    ChrSetPos(0x0015, 56700, 0, 27700, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20D9',
    )

    ChrSetPos(0x013B, 57090, 0, 30560, 270)

    def _loc_20D9(): pass

    label('loc_20D9')

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_28(0x0027, 0x01, 0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0002)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0004)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0008)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_245B',
    )

    ChrTalk(
        0x0015,
        (
            '#1920171088V……好。\n',
            '这样就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0015, 0x0101, 400)

    @scena.Lambda('lambda_213D')
    def lambda_213D():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_213D)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2161',
    )

    @scena.Lambda('lambda_2159')
    def lambda_2159():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_2159)

    def _loc_2161(): pass

    label('loc_2161')

    ChrTurnDirection(0x0101, 0x0015, 400)
    OP_69(0x0101, 1500)

    ChrTalk(
        0x0015,
        (
            '#1920171089V呼……\n',
            '总算是全部解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1920171090V哎呀～\n',
            '让你们费心了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010171091V#000F没什么，不用介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171092V好不容易才有一次学园祭，\n',
            '不好好准备一下怎么能行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171093V#040F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171094V既然是我们大家的节日，\n',
            '帮帮忙那是应该的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22D8',
    )

    ChrTurnDirection(0x013B, 0x0105, 400)

    ChrTalk(
        0x013B,
        (
            '#0510171095V#644F不愧是科洛丝。\n',
            '真是说出了我们的心声啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22D8(): pass

    label('loc_22D8')

    ChrTalk(
        0x0015,
        (
            '#1920171096V哈哈～\n',
            '的确如此啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x013B, 0x0015, 400)

    ChrTalk(
        0x0015,
        (
            '#1920171097V我们也很期待\n',
            '明天的学园祭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101168V#006F嗯！交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_239B',
    )

    ChrTalk(
        0x013B,
        (
            '#0510171099V#649F呵呵，\n',
            '那就请拭目以待了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C4')

    def _loc_239B(): pass

    label('loc_239B')

    ChrTalk(
        0x0105,
        (
            '#0060171100V#040F我们会竭尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23C4(): pass

    label('loc_23C4')

    ChrTalk(
        0x0015,
        (
            '#1920171101V那么，\n',
            '你们要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0027, 0x01, 0x0010)
    OP_28(0x003D, 0x01, 0x0200)
    OP_2C(0x003D, 0x01F4)
    OP_2B(0x003D, 0x0001)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '学园祭的校园任务\n',
            '【装饰校园】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    WaitEffect(0x02, 0x02)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_2538')

    def _loc_245B(): pass

    label('loc_245B')

    ChrTalk(
        0x0015,
        (
            '#1920171088V……好。\n',
            '这样就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0101, 1500)
    ChrTurnDirection(0x0015, 0x0101, 400)

    @scena.Lambda('lambda_2496')
    def lambda_2496():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2496)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24BA',
    )

    @scena.Lambda('lambda_24B2')
    def lambda_24B2():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_24B2)

    def _loc_24BA(): pass

    label('loc_24BA')

    ChrTurnDirection(0x0101, 0x0015, 400)

    ChrTalk(
        0x0015,
        (
            '#1920171103V那，如果再看到的话，\n',
            '也麻烦告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010171104V#006F嗯，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171105V#040F知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2538(): pass

    label('loc_2538')

    @scena.Lambda('lambda_253E')
    def lambda_253E():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_253E')

    DispatchAsync2(0x0000, 0x0001, lambda_253E)

    @scena.Lambda('lambda_254F')
    def lambda_254F():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_254F')

    DispatchAsync2(0x0001, 0x0001, lambda_254F)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2579',
    )

    @scena.Lambda('lambda_256E')
    def lambda_256E():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_256E')

    DispatchAsync2(0x0002, 0x0001, lambda_256E)

    def _loc_2579(): pass

    label('loc_2579')

    ChrSetFlags(0x0015, 0x0040)
    ChrWalkTo(0x0015, 45250, 0, 28110, 3000, 0x00)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25AC',
    )

    TerminateThread(0x0002, 0xFF)

    def _loc_25AC(): pass

    label('loc_25AC')

    ChrSetPos(0x0015, 47880, 0, 56070, 135)
    ChrClearFlags(0x0015, 0x0040)
    OP_4B(0x0015, 255)
    OP_64(0x05, 0x0001)
    EventEnd(0x00)

    def _loc_25CC(): pass

    label('loc_25CC')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

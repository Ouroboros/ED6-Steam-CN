import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2500_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2500_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

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

# id: 0xFFFF offset: 0x2394
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
    SetChrDirection(0x00FE, 135, 400)

    ChrTalk(
        0x00FE,
        (
            '#1920171064V你们看吧，\n',
            '还有一些没能装饰到的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0133')
    def lambda_0133():
        CameraMove(49960, 1500, 53870, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0133)

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
        'loc_184',
    )

    ChrTurnDirectionByPos(0x013B, 49960, 53870, 400)

    def _loc_184(): pass

    label('loc_184')

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

    @scena.Lambda('lambda_01F9')
    def lambda_01F9():
        OP_69(0x0000, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_01F9)

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
        'loc_22E',
    )

    ChrTurnDirection(0x013B, 0x00FE, 400)

    def _loc_22E(): pass

    label('loc_22E')

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

# id: 0x0001 offset: 0x367
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0002)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D3E',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6C(225000, 0)
    SetChrPos(0x0101, 21320, 250, 26540, 180)
    SetChrPos(0x0105, 21880, 0, 27550, 180)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C4',
    )

    SetChrPos(0x013B, 20790, 0, 27100, 180)

    def _loc_3C4(): pass

    label('loc_3C4')

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
        'loc_42C',
    )

    ChrTurnDirection(0x0101, 0x013B, 400)

    Jump('loc_433')

    def _loc_42C(): pass

    label('loc_42C')

    ChrTurnDirection(0x0101, 0x0105, 400)

    def _loc_433(): pass

    label('loc_433')

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
        'loc_512',
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

    Jump('loc_572')

    def _loc_512(): pass

    label('loc_512')

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

    def _loc_572(): pass

    label('loc_572')

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
    SetChrPos(0x0015, 30130, 0, 28910, 270)
    SetChrPos(0x0101, 22450, 0, 27570, 180)
    SetChrPos(0x0105, 21590, 0, 28160, 180)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5EB',
    )

    SetChrPos(0x013B, 20300, 0, 27960, 90)

    def _loc_5EB(): pass

    label('loc_5EB')

    SetChrDirection(0x0101, 90, 0)
    SetChrDirection(0x0105, 90, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_60E',
    )

    SetChrDirection(0x013B, 90, 0)

    def _loc_60E(): pass

    label('loc_60E')

    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    SetChrFlags(0x0015, 0x0040)
    ChrWalkTo(0x0015, 24380, 0, 27840, 3000, 0x00)
    ChrWalkTo(0x0015, 23530, 0, 27230, 3000, 0x00)
    OP_4A(0x0015, 255)
    Sleep(400)

    SetChrDirection(0x0015, 225, 400)
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
        'loc_70D',
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

    @scena.Lambda('lambda_06FB')
    def lambda_06FB():
        ChrTurnDirection(0x0105, 0x013B, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_06FB)

    ChrTurnDirection(0x0101, 0x013B, 400)

    Jump('loc_739')

    def _loc_70D(): pass

    label('loc_70D')

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

    def _loc_739(): pass

    label('loc_739')

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

    @scena.Lambda('lambda_0774')
    def lambda_0774():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0774)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_798',
    )

    @scena.Lambda('lambda_0790')
    def lambda_0790():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0790)

    def _loc_798(): pass

    label('loc_798')

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

    @scena.Lambda('lambda_07C5')
    def lambda_07C5():
        ChrWalkTo(0x0101, 22450, 0, 26200, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07C5)

    @scena.Lambda('lambda_07E0')
    def lambda_07E0():
        ChrWalkTo(0x0105, 21590, 0, 26400, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_07E0)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_81E',
    )

    @scena.Lambda('lambda_0809')
    def lambda_0809():
        ChrWalkTo(0x013B, 20820, 250, 26020, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0809)

    def _loc_81E(): pass

    label('loc_81E')

    @scena.Lambda('lambda_0824')
    def lambda_0824():
        ChrWalkTo(0x0015, 23220, 250, 26040, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_0824)

    @scena.Lambda('lambda_083F')
    def lambda_083F():
        OP_6C(135000, 2500)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_083F)

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
        'loc_882',
    )

    WaitForThreadExit(0x013B, 0x0001)

    def _loc_882(): pass

    label('loc_882')

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
        'loc_BD2',
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

    @scena.Lambda('lambda_0946')
    def lambda_0946():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0946)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_96A',
    )

    @scena.Lambda('lambda_0962')
    def lambda_0962():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0962)

    def _loc_96A(): pass

    label('loc_96A')

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
        'loc_A6D',
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

    def _loc_A6D(): pass

    label('loc_A6D')

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
        'loc_B1C',
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

    Jump('loc_B40')

    def _loc_B1C(): pass

    label('loc_B1C')

    ChrTalk(
        0x0105,
        (
            '#0060171100V#040F我们会竭尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B40(): pass

    label('loc_B40')

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
    SetChrName('')

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

    Jump('loc_C9B')

    def _loc_BD2(): pass

    label('loc_BD2')

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

    @scena.Lambda('lambda_0C38')
    def lambda_0C38():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0C38)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C5C',
    )

    @scena.Lambda('lambda_0C54')
    def lambda_0C54():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0C54)

    def _loc_C5C(): pass

    label('loc_C5C')

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
    def _loc_C9B(): pass

    label('loc_C9B')

    @scena.Lambda('lambda_0CA1')
    def lambda_0CA1():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_0CA1')

    DispatchAsync2(0x0000, 0x0001, lambda_0CA1)

    @scena.Lambda('lambda_0CB2')
    def lambda_0CB2():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_0CB2')

    DispatchAsync2(0x0001, 0x0001, lambda_0CB2)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CDC',
    )

    @scena.Lambda('lambda_0CD1')
    def lambda_0CD1():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_0CD1')

    DispatchAsync2(0x0002, 0x0001, lambda_0CD1)

    def _loc_CDC(): pass

    label('loc_CDC')

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
        'loc_D1E',
    )

    TerminateThread(0x0002, 0xFF)

    def _loc_D1E(): pass

    label('loc_D1E')

    SetChrPos(0x0015, 47880, 0, 56070, 135)
    ClearChrFlags(0x0015, 0x0040)
    OP_4B(0x0015, 255)
    OP_64(0x03, 0x0001)
    EventEnd(0x00)

    def _loc_D3E(): pass

    label('loc_D3E')

    TalkEnd(0x00FF)

    Return()

# id: 0x0002 offset: 0xD42
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17E2',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6C(45000, 0)
    SetChrPos(0x0101, 38970, 0, 68950, 90)
    SetChrPos(0x0105, 40770, 0, 68550, 45)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D9F',
    )

    SetChrPos(0x013B, 38560, 0, 70140, 90)

    def _loc_D9F(): pass

    label('loc_D9F')

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
        'loc_DED',
    )

    @scena.Lambda('lambda_0DE5')
    def lambda_0DE5():
        ChrTurnDirection(0x013B, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0DE5)

    def _loc_DED(): pass

    label('loc_DED')

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
    SetChrDirection(0x0105, 0, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E9C',
    )

    @scena.Lambda('lambda_0E94')
    def lambda_0E94():
        SetChrDirection(0x013B, 0, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0E94)

    def _loc_E9C(): pass

    label('loc_E9C')

    SetChrDirection(0x0101, 0, 400)
    CameraMove(41580, 2000, 73990, 1500)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EE3',
    )

    ChrTalk(
        0x013B,
        (
            '#0510171078V#643F啊，没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F01')

    def _loc_EE3(): pass

    label('loc_EE3')

    ChrTalk(
        0x0101,
        (
            '#0010171079V#004F啊，真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F01(): pass

    label('loc_F01')

    OP_69(0x0105, 1500)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F29',
    )

    Sleep(100)

    @scena.Lambda('lambda_0F21')
    def lambda_0F21():
        ChrTurnDirection(0x013B, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0F21)

    def _loc_F29(): pass

    label('loc_F29')

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
    SetChrPos(0x0015, 45200, 0, 65300, 270)
    SetChrPos(0x0101, 39140, 0, 69780, 135)
    SetChrPos(0x0105, 38830, 0, 68410, 135)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FE6',
    )

    Sleep(100)

    SetChrPos(0x013B, 37730, 0, 69120, 135)

    def _loc_FE6(): pass

    label('loc_FE6')

    OP_69(0x0101, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_1002')
    def lambda_1002():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1002')

    DispatchAsync2(0x0000, 0x0001, lambda_1002)

    @scena.Lambda('lambda_1013')
    def lambda_1013():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1013')

    DispatchAsync2(0x0001, 0x0001, lambda_1013)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_103D',
    )

    @scena.Lambda('lambda_1032')
    def lambda_1032():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1032')

    DispatchAsync2(0x0002, 0x0001, lambda_1032)

    def _loc_103D(): pass

    label('loc_103D')

    SetChrFlags(0x0015, 0x0040)
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
        'loc_1088',
    )

    TerminateThread(0x0002, 0xFF)

    def _loc_1088(): pass

    label('loc_1088')

    Sleep(400)

    SetChrDirection(0x0015, 45, 400)
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
        'loc_1132',
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

    Jump('loc_1162')

    def _loc_1132(): pass

    label('loc_1132')

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

    def _loc_1162(): pass

    label('loc_1162')

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

    @scena.Lambda('lambda_119A')
    def lambda_119A():
        OP_6C(135000, 4000)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_119A)

    @scena.Lambda('lambda_11AA')
    def lambda_11AA():
        ChrWalkTo(0x0101, 41000, 0, 70140, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11AA)

    @scena.Lambda('lambda_11C5')
    def lambda_11C5():
        ChrWalkTo(0x0105, 40770, 0, 68550, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_11C5)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1203',
    )

    @scena.Lambda('lambda_11EE')
    def lambda_11EE():
        ChrWalkTo(0x013B, 40130, 0, 69380, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_11EE)

    def _loc_1203(): pass

    label('loc_1203')

    @scena.Lambda('lambda_1209')
    def lambda_1209():
        CameraMove(41770, 3500, 69260, 4000)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_1209)

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
        'loc_128B',
    )

    WaitForThreadExit(0x013B, 0x0001)

    def _loc_128B(): pass

    label('loc_128B')

    WaitForThreadExit(0x0015, 0x0001)
    WaitForThreadExit(0x0015, 0x0002)
    OP_72(0x0012, 0x0004)
    SetChrFlags(0x0015, 0x0040)
    SetChrPos(0x0015, 43990, 0, 73850, 270)
    OP_6F(0x0005, 60)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12D6',
    )

    SetChrPos(0x013B, 41160, 0, 69290, 90)

    def _loc_12D6(): pass

    label('loc_12D6')

    FadeIn(1000, 0)
    ChrWalkTo(0x0015, 41560, 500, 74220, 3000, 0x00)
    OP_72(0x0005, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)
    ChrWalkTo(0x0015, 38300, 0, 72350, 3000, 0x00)
    ChrWalkTo(0x0015, 38000, 0, 68550, 3000, 0x00)
    SetChrDirection(0x0015, 90, 400)
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
        'loc_1671',
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

    @scena.Lambda('lambda_1394')
    def lambda_1394():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1394)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13B8',
    )

    @scena.Lambda('lambda_13B0')
    def lambda_13B0():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_13B0)

    def _loc_13B8(): pass

    label('loc_13B8')

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
        'loc_150C',
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

    def _loc_150C(): pass

    label('loc_150C')

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
        'loc_15BB',
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

    Jump('loc_15DF')

    def _loc_15BB(): pass

    label('loc_15BB')

    ChrTalk(
        0x0105,
        (
            '#0060171100V#040F我们会竭尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15DF(): pass

    label('loc_15DF')

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
    SetChrName('')

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

    Jump('loc_173A')

    def _loc_1671(): pass

    label('loc_1671')

    ChrTalk(
        0x0015,
        (
            '#1920171088V……好。\n',
            '这样就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1699')
    def lambda_1699():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1699)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16BD',
    )

    @scena.Lambda('lambda_16B5')
    def lambda_16B5():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_16B5)

    def _loc_16BD(): pass

    label('loc_16BD')

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
    def _loc_173A(): pass

    label('loc_173A')

    @scena.Lambda('lambda_1740')
    def lambda_1740():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1740')

    DispatchAsync2(0x0000, 0x0001, lambda_1740)

    @scena.Lambda('lambda_1751')
    def lambda_1751():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1751')

    DispatchAsync2(0x0001, 0x0001, lambda_1751)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_177B',
    )

    @scena.Lambda('lambda_1770')
    def lambda_1770():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1770')

    DispatchAsync2(0x0002, 0x0001, lambda_1770)

    def _loc_177B(): pass

    label('loc_177B')

    SetChrFlags(0x0015, 0x0040)
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
        'loc_17C2',
    )

    TerminateThread(0x0002, 0xFF)

    def _loc_17C2(): pass

    label('loc_17C2')

    SetChrPos(0x0015, 47880, 0, 56070, 135)
    ClearChrFlags(0x0015, 0x0040)
    OP_4B(0x0015, 255)
    OP_64(0x04, 0x0001)
    EventEnd(0x00)

    def _loc_17E2(): pass

    label('loc_17E2')

    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0x17E6
@scena.Code('func_03_17E6')
def func_03_17E6():
    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2388',
    )

    OP_28(0x0027, 0x01, 0x0008)
    EventBegin(0x00)
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x0101, 53860, 0, 28500, 90)
    SetChrPos(0x0105, 53290, 0, 29520, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1849',
    )

    SetChrPos(0x013B, 52540, 0, 30290, 90)

    def _loc_1849(): pass

    label('loc_1849')

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
    SetChrDirection(0x0101, 270, 400)
    OP_94(0x01, 0x0101, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18CE',
    )

    @scena.Lambda('lambda_18C1')
    def lambda_18C1():
        ChrTurnDirection(0x013B, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_18C1)

    Sleep(150)

    def _loc_18CE(): pass

    label('loc_18CE')

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

    @scena.Lambda('lambda_191C')
    def lambda_191C():
        ChrTurnDirection(0x0105, 0x0101, 0)
        Yield()

        Jump('lambda_191C')

    DispatchAsync2(0x0105, 0x0001, lambda_191C)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1946',
    )

    @scena.Lambda('lambda_193B')
    def lambda_193B():
        ChrTurnDirection(0x013B, 0x0101, 0)
        Yield()

        Jump('lambda_193B')

    DispatchAsync2(0x013B, 0x0001, lambda_193B)

    def _loc_1946(): pass

    label('loc_1946')

    ChrWalkTo(0x0101, 51210, 0, 27710, 6000, 0x00)
    Sleep(100)

    Fade(1000)
    OP_6C(135000, 0)
    CameraMove(51210, 0, 27710, 0)
    Sleep(100)

    SetChrDirection(0x0101, 90, 400)
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
        'loc_19E6',
    )

    TerminateThread(0x013B, 0x01)

    @scena.Lambda('lambda_19D1')
    def lambda_19D1():
        ChrWalkTo(0x013B, 52630, 0, 29600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_19D1)

    def _loc_19E6(): pass

    label('loc_19E6')

    ChrWalkTo(0x0105, 52430, 0, 27750, 3000, 0x00)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A16',
    )

    @scena.Lambda('lambda_1A0E')
    def lambda_1A0E():
        SetChrDirection(0x013B, 315, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_1A0E)

    def _loc_1A16(): pass

    label('loc_1A16')

    SetChrDirection(0x0105, 315, 400)
    Sleep(200)

    SetChrDirection(0x0105, 180, 400)
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
        'loc_1AB5',
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

    Jump('loc_1AFC')

    def _loc_1AB5(): pass

    label('loc_1AB5')

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

    def _loc_1AFC(): pass

    label('loc_1AFC')

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
    SetChrPos(0x0015, 49850, 0, 28600, 90)
    SetChrPos(0x0101, 55720, 0, 29180, 270)
    SetChrPos(0x0105, 55170, 0, 30090, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BBD',
    )

    SetChrPos(0x013B, 56220, 0, 30860, 270)

    def _loc_1BBD(): pass

    label('loc_1BBD')

    Sleep(1000)

    FadeIn(1000, 0)
    OP_6C(270000, 0)
    CameraMove(54350, 0, 28820, 0)
    OP_0D()

    @scena.Lambda('lambda_1BEC')
    def lambda_1BEC():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1BEC')

    DispatchAsync2(0x0000, 0x0001, lambda_1BEC)

    @scena.Lambda('lambda_1BFD')
    def lambda_1BFD():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1BFD')

    DispatchAsync2(0x0001, 0x0001, lambda_1BFD)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C27',
    )

    @scena.Lambda('lambda_1C1C')
    def lambda_1C1C():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_1C1C')

    DispatchAsync2(0x0002, 0x0001, lambda_1C1C)

    def _loc_1C27(): pass

    label('loc_1C27')

    SetChrFlags(0x0015, 0x0040)
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
        'loc_1C63',
    )

    TerminateThread(0x0002, 0xFF)

    def _loc_1C63(): pass

    label('loc_1C63')

    SetChrDirection(0x0015, 270, 400)
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
        'loc_1D53',
    )

    ChrTalk(
        0x013B,
        (
            '#0510171120V#644F那我们也来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D1E')
    def lambda_1D1E():
        ChrTurnDirection(0x0105, 0x013B, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1D1E)

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

    Jump('loc_1DA5')

    def _loc_1D53(): pass

    label('loc_1D53')

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

    def _loc_1DA5(): pass

    label('loc_1DA5')

    ChrTalk(
        0x0015,
        (
            '#1920171124V抱歉，又麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1DCC')
    def lambda_1DCC():
        ChrWalkTo(0x0015, 55140, 0, 24660, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_1DCC)

    @scena.Lambda('lambda_1DE7')
    def lambda_1DE7():
        ChrWalkTo(0x0101, 56060, 0, 31960, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1DE7)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E43',
    )

    @scena.Lambda('lambda_1E10')
    def lambda_1E10():
        ChrWalkTo(0x013B, 55210, 0, 32119, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_1E10)

    @scena.Lambda('lambda_1E2B')
    def lambda_1E2B():
        ChrWalkTo(0x0105, 56020, 0, 25710, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1E2B)

    Jump('loc_1E5E')

    def _loc_1E43(): pass

    label('loc_1E43')

    @scena.Lambda('lambda_1E49')
    def lambda_1E49():
        ChrWalkTo(0x0105, 55210, 0, 32119, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1E49)

    def _loc_1E5E(): pass

    label('loc_1E5E')

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
        'loc_1E98',
    )

    TerminateThread(0x013B, 0x01)

    def _loc_1E98(): pass

    label('loc_1E98')

    OP_72(0x001A, 0x0004)
    SetChrPos(0x0101, 55720, 0, 29180, 270)
    SetChrPos(0x0105, 55170, 0, 30090, 270)
    SetChrPos(0x0015, 56700, 0, 27700, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EEF',
    )

    SetChrPos(0x013B, 57090, 0, 30560, 270)

    def _loc_1EEF(): pass

    label('loc_1EEF')

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
        'loc_222B',
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

    @scena.Lambda('lambda_1F4E')
    def lambda_1F4E():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1F4E)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F72',
    )

    @scena.Lambda('lambda_1F6A')
    def lambda_1F6A():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_1F6A)

    def _loc_1F72(): pass

    label('loc_1F72')

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
        'loc_20C6',
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

    def _loc_20C6(): pass

    label('loc_20C6')

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
        'loc_2175',
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

    Jump('loc_2199')

    def _loc_2175(): pass

    label('loc_2175')

    ChrTalk(
        0x0105,
        (
            '#0060171100V#040F我们会竭尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2199(): pass

    label('loc_2199')

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
    SetChrName('')

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

    Jump('loc_22F4')

    def _loc_222B(): pass

    label('loc_222B')

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

    @scena.Lambda('lambda_2261')
    def lambda_2261():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2261)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2285',
    )

    @scena.Lambda('lambda_227D')
    def lambda_227D():
        ChrTurnDirection(0x013B, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_227D)

    def _loc_2285(): pass

    label('loc_2285')

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
    def _loc_22F4(): pass

    label('loc_22F4')

    @scena.Lambda('lambda_22FA')
    def lambda_22FA():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_22FA')

    DispatchAsync2(0x0000, 0x0001, lambda_22FA)

    @scena.Lambda('lambda_230B')
    def lambda_230B():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_230B')

    DispatchAsync2(0x0001, 0x0001, lambda_230B)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2335',
    )

    @scena.Lambda('lambda_232A')
    def lambda_232A():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_232A')

    DispatchAsync2(0x0002, 0x0001, lambda_232A)

    def _loc_2335(): pass

    label('loc_2335')

    SetChrFlags(0x0015, 0x0040)
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
        'loc_2368',
    )

    TerminateThread(0x0002, 0xFF)

    def _loc_2368(): pass

    label('loc_2368')

    SetChrPos(0x0015, 47880, 0, 56070, 135)
    ClearChrFlags(0x0015, 0x0040)
    OP_4B(0x0015, 255)
    OP_64(0x05, 0x0001)
    EventEnd(0x00)

    def _loc_2388(): pass

    label('loc_2388')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

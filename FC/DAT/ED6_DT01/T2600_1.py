import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2600_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2600_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2600.x'
    header.mapIndex       = 1
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x11C6
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
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x2000)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x8000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_81',
    )

    Return()

    def _loc_81(): pass

    label('loc_81')

    EventBegin(0x00)
    Fade(1000)
    OP_6C(45000, 0)
    CameraMove(200, 0, 3500, 0)
    SetChrPos(0x0101, 200, 0, 3500, 0)
    SetChrPos(0x0105, -600, 0, 2500, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E3',
    )

    SetChrPos(0x013B, 1000, 0, 1500, 0)

    def _loc_E3(): pass

    label('loc_E3')

    OP_0D()
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_00EF')
    def lambda_00EF():
        CameraMove(-180, 1000, 7200, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_00EF)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15E',
    )

    Sleep(150)

    OP_62(0x013B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_15E(): pass

    label('loc_15E')

    WaitForThreadExit(0x0009, 0x0001)
    SetChrPos(0x0009, 20, 1000, 12000, 180)
    ClearChrFlags(0x0009, 0x0080)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 45)
    OP_73(0x0000)

    @scena.Lambda('lambda_0190')
    def lambda_0190():
        ChrMoveTo(0x0009, 80, 1000, 10800, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0190)

    SetChrDirection(0x0009, 0, 800)
    OP_72(0x0000, 0x0800)
    PlaySE(211, 0x00, 0x64)
    OP_6F(0x0000, 45)
    OP_70(0x0000, 0)
    WaitForThreadExit(0x0009, 0x0002)
    OP_94(0x01, 0x0009, 0x00B4, 0x00000578, 0x00001770, 0x00)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    CreateThread(0x0009, 0x01, 0x01, 0x0001)
    OP_97(0x0009, -750, 9480, 180000, 5000, 0x0001)
    SetChrDirection(0x0009, 45, 400)
    TerminateThread(0x0009, 0x01)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#1900171003V哈～呼～哈～呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1900171004V可恶……\n',
            '到底是怎么回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0101, 1500)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010171005V#002F……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171006V#045F是啊，怎么了呢……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171007V好像不太寻常的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 0, 400)
    OP_6A(0x0101)

    @scena.Lambda('lambda_02F0')
    def lambda_02F0():
        ChrMoveToRelativeAsync(0x0101, 0, 0, 2700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_02F0)

    Sleep(150)

    @scena.Lambda('lambda_0310')
    def lambda_0310():
        ChrMoveToRelativeAsync(0x0105, 0, 0, 2600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0310)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34A',
    )

    ChrMoveToRelativeAsync(0x013B, 0, 0, 2600, 2000, 0x00)

    Jump('loc_34F')

    def _loc_34A(): pass

    label('loc_34A')

    WaitForThreadExit(0x0105, 0x0001)

    def _loc_34F(): pass

    label('loc_34F')

    ChrTurnDirection(0x0101, 0x0009, 400)
    ClearMapFlags(0x00000001)

    ChrTalk(
        0x0101,
        (
            '#0010171008V#002F请问发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x0009, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#1900171009V喂、喂，\n',
            '你们最好别站在门口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1900171010V说不定什么时候\n',
            '怪物就会跳出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010171011V#004F怪、怪物？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171012V这座建筑物里面有魔兽吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1900171013V啊，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1900171014V体型相当巨大，\n',
            '而且有很多只聚集在一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060171015V#042F这座古老的建筑物\n',
            '是学院以前的校舍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171016V不过一般情况下，\n',
            '入口应该是用钥匙锁住了的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0105, 400)

    ChrTalk(
        0x0009,
        (
            '#1900171017V是我从艾福托老师那里\n',
            '把钥匙借来的。',
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
        'loc_569',
    )

    @scena.Lambda('lambda_055C')
    def lambda_055C():
        ChrTurnDirection(0x013B, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_055C)

    Sleep(100)

    def _loc_569(): pass

    label('loc_569')

    ChrTurnDirection(0x0105, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '#1900171018V校舍里因为准备学园祭太吵了，\n',
            '所以我想到安静的地方休息。',
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
        'loc_6DC',
    )

    ChrTalk(
        0x0101,
        (
            '#0010171019V#004F到安静的地方休息……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013B,
        (
            '#0510171020V#647F这是有意在逃避工作啊。\n',
            '也就是说你是在偷懒了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510171021V#659F哼哼～米克。\n',
            '你还真是有胆量啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x013B, 400)

    ChrTalk(
        0x0009,
        (
            '#1900171022V哼，\n',
            '我本来就不想参加啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1900171023V为什么非要\n',
            '让我出演那样的舞台剧啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1900171024V我都烦死了，\n',
            '不想再参与了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_76D')

    def _loc_6DC(): pass

    label('loc_6DC')

    ChrTalk(
        0x0101,
        (
            '#0010171025V#004F到安静的地方休息……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171026V这么说来，\n',
            '你不就是来这里偷懒的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#1900171027V准备工作实在太烦人了，\n',
            '让愿意做的人去做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_76D(): pass

    label('loc_76D')

    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010171028V#009F这、这是什么态度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171029V在大家拼命努力的时候，\n',
            '你却说出这种事不关己的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060171030V#045F算了，算了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171031V现在更为重要的是\n',
            '确定魔兽的情况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010171032V#004F啊……哦，\n',
            '说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171033V#002F的确，\n',
            '魔兽可不能就这么放任不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171034V#043F嗯，\n',
            '明天就是学园祭了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0105, 400)

    ChrTalk(
        0x0009,
        (
            '#1900171035V不过，\n',
            '这些应该和我没有什么关系了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1900171036V总之，我现在去还钥匙，\n',
            '然后把事情告诉艾福托老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0009, 0x0040)
    ChrTurnDirection(0x0009, 0x0101, 400)

    @scena.Lambda('lambda_0965')
    def lambda_0965():
        ChrTurnDirection(0x0101, 0x0009, 0)
        Yield()

        Jump('lambda_0965')

    DispatchAsync2(0x0101, 0x0001, lambda_0965)

    @scena.Lambda('lambda_0976')
    def lambda_0976():
        ChrTurnDirection(0x0105, 0x0009, 0)
        Yield()

        Jump('lambda_0976')

    DispatchAsync2(0x0105, 0x0001, lambda_0976)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9A0',
    )

    @scena.Lambda('lambda_0995')
    def lambda_0995():
        ChrTurnDirection(0x013B, 0x0009, 0)
        Yield()

        Jump('lambda_0995')

    DispatchAsync2(0x013B, 0x0001, lambda_0995)

    def _loc_9A0(): pass

    label('loc_9A0')

    ChrTalk(
        0x0009,
        (
            '#1900171037V真的很危险，\n',
            '不要接近门口哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0009, -1170, 1000, 6740, 5000, 0x00)

    @scena.Lambda('lambda_09E4')
    def lambda_09E4():
        ChrMoveToRelativeAsync(0x0105, 1000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_09E4)

    ChrWalkTo(0x0009, 130, 1000, -4210, 5000, 0x00)
    SetChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0009, 0x0040)
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
        'loc_A31',
    )

    TerminateThread(0x013B, 0x01)

    def _loc_A31(): pass

    label('loc_A31')

    OP_28(0x0027, 0x01, 0x2000)
    OP_64(0x00, 0x0001)
    OP_71(0x0000, 0x0010)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0xA43
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A67',
    )

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(2000)

    Yield()

    Jump('Init')

    def _loc_A67(): pass

    label('loc_A67')

    Return()

# id: 0x0002 offset: 0xA68
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0105, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A87',
    )

    SetChrFlags(0x013B, 0x0080)

    def _loc_A87(): pass

    label('loc_A87')

    SetMapFlags(0x00400000)
    SetChrPos(0x0101, -500, 1000, 11470, 96)
    SetChrPos(0x0105, 500, 1000, 11470, 96)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ACD',
    )

    SetChrPos(0x013B, 0, 1000, 11470, 96)

    def _loc_ACD(): pass

    label('loc_ACD')

    OP_6C(45000, 0)
    CameraMove(0, 1000, 6110, 0)
    OP_6F(0x0000, 60)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0105, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B0B',
    )

    ClearChrFlags(0x013B, 0x0080)

    def _loc_B0B(): pass

    label('loc_B0B')

    @scena.Lambda('lambda_0B11')
    def lambda_0B11():
        ChrWalkTo(0x0101, -500, 1000, 6500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B11)

    Sleep(200)

    @scena.Lambda('lambda_0B31')
    def lambda_0B31():
        ChrWalkTo(0x0105, 550, 1000, 6200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0B31)

    @scena.Lambda('lambda_0B4C')
    def lambda_0B4C():
        ChrWalkTo(0x000A, 300, 500, 4110, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B4C)

    Sleep(400)

    ClearChrFlags(0x000A, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B9C',
    )

    @scena.Lambda('lambda_0B7F')
    def lambda_0B7F():
        ChrWalkTo(0x013B, 300, 1000, 7500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0B7F)

    WaitForThreadExit(0x013B, 0x0001)

    Jump('loc_BA1')

    def _loc_B9C(): pass

    label('loc_B9C')

    WaitForThreadExit(0x0105, 0x0001)

    def _loc_BA1(): pass

    label('loc_BA1')

    OP_72(0x0000, 0x0800)
    PlaySE(211, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x000A, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF1',
    )

    @scena.Lambda('lambda_0BE9')
    def lambda_0BE9():
        ChrTurnDirection(0x013B, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x013B, 0x0001, lambda_0BE9)

    def _loc_BF1(): pass

    label('loc_BF1')

    ChrTurnDirection(0x0105, 0x000A, 400)
    OP_71(0x0000, 0x0800)

    ChrTalk(
        0x0105,
        (
            '#0060171038V#040F啊，艾福托老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0105, 400)

    ChrTalk(
        0x000A,
        (
            '#1910171039V哦，你们没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1910171040V旧校舍有魔兽出没的情况，\n',
            '米克都告诉我了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171041V#040F啊，是有这么一回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010171042V#000F已经不用担心了哦。\n',
            '魔兽全都被消灭掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#1910171043V哦，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1910171044V说起来，艾丝蒂尔，\n',
            '你是游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1910171045V哎呀，真是帮了大忙啊。\n',
            '要是等到学园祭当天\n',
            '发生了什么事情那可就糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171046V#040F嗯，的确。',
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
        'loc_E5C',
    )

    ChrTalk(
        0x013B,
        (
            '#0510171047V#640F如果这样想的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510171048V那个懒虫米克\n',
            '也算帮了一个大忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510171049V先不说他的动机如何，\n',
            '总之发现了魔兽这个隐患。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E2D')
    def lambda_0E2D():
        ChrTurnDirection(0x0105, 0x013B, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0E2D)

    ChrTurnDirection(0x0101, 0x013B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111179V#000F嗯，说的也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E5C(): pass

    label('loc_E5C')

    ChrTalk(
        0x000A,
        (
            '#1910171051V好的，为了谨慎起见，\n',
            '还是把门给锁上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E96')
    def lambda_0E96():
        ChrTurnDirection(0x0105, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0E96)

    Sleep(100)

    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x000A,
        (
            '#1910171052V我以后会留心的，\n',
            '不会让这种事情再次发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171053V#040F嗯，那样就最好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000A, 0x0040)

    @scena.Lambda('lambda_0F13')
    def lambda_0F13():
        ChrTurnDirection(0x0101, 0x000A, 0)
        Yield()

        Jump('lambda_0F13')

    DispatchAsync2(0x0101, 0x0001, lambda_0F13)

    @scena.Lambda('lambda_0F24')
    def lambda_0F24():
        ChrTurnDirection(0x0105, 0x000A, 0)
        Yield()

        Jump('lambda_0F24')

    DispatchAsync2(0x0105, 0x0001, lambda_0F24)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F4E',
    )

    @scena.Lambda('lambda_0F43')
    def lambda_0F43():
        ChrTurnDirection(0x013B, 0x000A, 0)
        Yield()

        Jump('lambda_0F43')

    DispatchAsync2(0x013B, 0x0001, lambda_0F43)

    def _loc_F4E(): pass

    label('loc_F4E')

    @scena.Lambda('lambda_0F54')
    def lambda_0F54():
        ChrMoveToRelativeAsync(0x0105, 700, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_0F54)

    @scena.Lambda('lambda_0F6F')
    def lambda_0F6F():
        ChrMoveToRelativeAsync(0x0101, -700, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F6F)

    If(
        (
            (Expr.Eval, "OP_42(0x003A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FAD',
    )

    @scena.Lambda('lambda_0F98')
    def lambda_0F98():
        ChrMoveToRelativeAsync(0x013B, 1000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x013B, 0x0002, lambda_0F98)

    def _loc_FAD(): pass

    label('loc_FAD')

    @scena.Lambda('lambda_0FB3')
    def lambda_0FB3():
        CameraMove(-20, 1000, 9150, 1500)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0FB3)

    ChrWalkTo(0x000A, -20, 1000, 9150, 2000, 0x00)
    WaitForThreadExit(0x000A, 0x0001)
    Sleep(300)

    PlaySE(115, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x000A,
        (
            '#1910171054V……唔，没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 180, 400)

    ChrTalk(
        0x000A,
        (
            '#1910171055V那么，\n',
            '我就回值班室去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1910171056V平常到了这个时间\n',
            '也该关门了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1910171057V对了，\n',
            '你们也不要玩到太晚了。',
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
        'loc_10C0',
    )

    ChrTalk(
        0x013B,
        (
            '#0510171058V#640F嗯～不用担心啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10E6')

    def _loc_10C0(): pass

    label('loc_10C0')

    ChrTalk(
        0x0105,
        (
            '#0060171059V#040F好的，我们会小心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10E6(): pass

    label('loc_10E6')

    ChrTalk(
        0x0101,
        (
            '#0010171060V#000F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_110A')
    def lambda_110A():
        CameraMove(0, 1000, 6110, 1500)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_110A)

    ChrWalkTo(0x000A, 300, 0, -4310, 3000, 0x00)
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
        'loc_114A',
    )

    TerminateThread(0x013B, 0x01)

    def _loc_114A(): pass

    label('loc_114A')

    ClearChrFlags(0x000A, 0x0040)
    SetChrFlags(0x000A, 0x0080)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '学园祭的校园任务\n',
            '【剿灭旧校舍的魔兽】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    WaitEffect(0x02, 0x01)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ClearMapFlags(0x00400000)
    OP_65(0x00, 0x0001)
    OP_72(0x0000, 0x0010)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

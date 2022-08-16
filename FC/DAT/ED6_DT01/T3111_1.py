import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3111_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3111_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3111.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T3111._SN', 'ED6_DT01/T3111_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_231',
    )

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_12F',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_98',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_9F')

    def _loc_98(): pass

    label('loc_98')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_9F(): pass

    label('loc_9F')

    ChrTalk(
        0x0102,
        (
            '#0020181092V#010F（刚才已经问过话了，\n',
            '　安东尼一点反应也没有。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181093V#010F（那么，我们就去\n',
            '　二楼工房长的房间调查看看吧。）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_226')

    def _loc_12F(): pass

    label('loc_12F')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181088V#010F（刚才调查过了，\n',
            '　一点反应也没有。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181085V#010F（我们再到工房里面调查一下吧。）\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181086V#010F（照米妮亚姆医生说的，\n',
            '　在某个地方也许会有线索的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181091V#003F（唔……也只有这样了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_226(): pass

    label('loc_226')

    TalkEnd(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)

    Jump('loc_801')

    def _loc_231(): pass

    label('loc_231')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D6',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(-10040, 0, -1620, 0)
    ChrSetPos(0x0101, -8960, 0, -1680, 228)
    ChrSetPos(0x0102, -8920, 0, -530, 225)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_298',
    )

    ChrSetPos(0x0107, -7480, 0, -1290, 224)

    def _loc_298(): pass

    label('loc_298')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B7',
    )

    ChrSetPos(0x0106, -7720, 0, -160, 225)

    def _loc_2B7(): pass

    label('loc_2B7')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D6',
    )

    ChrSetPos(0x013C, -8770, 0, -2870, 290)

    def _loc_2D6(): pass

    label('loc_2D6')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2F0',
    )

    @scena.Lambda('lambda_02E8')
    def lambda_02E8():
        ChrTurnDirection(0x0000, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_02E8)

    def _loc_2F0(): pass

    label('loc_2F0')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_30A',
    )

    @scena.Lambda('lambda_0302')
    def lambda_0302():
        ChrTurnDirection(0x0001, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0302)

    def _loc_30A(): pass

    label('loc_30A')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_324',
    )

    @scena.Lambda('lambda_031C')
    def lambda_031C():
        ChrTurnDirection(0x0002, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_031C)

    def _loc_324(): pass

    label('loc_324')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_33E',
    )

    @scena.Lambda('lambda_0336')
    def lambda_0336():
        ChrTurnDirection(0x0003, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0336)

    def _loc_33E(): pass

    label('loc_33E')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_358',
    )

    @scena.Lambda('lambda_0350')
    def lambda_0350():
        ChrTurnDirection(0x0004, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_0350)

    def _loc_358(): pass

    label('loc_358')

    OP_0D()
    Sleep(400)

    OP_4A(0x000A, 255)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000A, 0x0000, 400)
    Sleep(800)

    ChrTalk(
        0x000A,
        (
            '#2110181072V怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2110181073V不好意思，\n',
            '我现在正在谈重要的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2110181074V有事的话请等一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 0, 400)
    OP_4B(0x000A, 255)

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_740',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010181078V#003F（唔～\n',
            '　没机会向他提问啊～）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181079V#004F（啊，对了，\n',
            '　安东尼有什么反应吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_049C')
    def lambda_049C():
        ChrTurnDirection(0x0102, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_049C)

    @scena.Lambda('lambda_04AA')
    def lambda_04AA():
        ChrTurnDirection(0x0107, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_04AA)

    ChrTurnDirection(0x0101, 0x013C, 400)

    ChrTalk(
        0x013C,
        (
            '#2030181038V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTurnDirection(0x013C, 0x0101, 400)

    ChrTalk(
        0x013C,
        (
            '#2030181039V………………喵噢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070181082V#063F（没有反应呢～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002C, 0x01, 0x0010)

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_736',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_60F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010181068V#505F唔～对两个人都没有反应呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181069V果然还是去刚才\n',
            '安东尼有反应的地方调查一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181070V#010F是二楼工房长的房间对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181071V我们赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_736')

    def _loc_60F(): pass

    label('loc_60F')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181083V#004F（咦，\n',
            '　这么说对这两人都没有反应了？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181084V#013F（也就是说没有线索了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181085V#010F（我们再到工房里面调查一下吧。）\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181086V#010F（照米妮亚姆医生说的，\n',
            '　在某个地方也许会有线索的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181087V#003F（唔……也只有这样了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002C, 0x01, 0x0080)

    def _loc_736(): pass

    label('loc_736')

    Sleep(50)

    EventEnd(0x04)

    Jump('loc_801')

    def _loc_740(): pass

    label('loc_740')

    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010181075V#003F（完、完全插不上嘴……）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181076V#017F（好像在商谈重要事情。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181077V（现在还是不要问他了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002C, 0x01, 0x0008)
    MapClearFlags(0x00000080)
    def _loc_801(): pass

    label('loc_801')

    Return()

# id: 0x0001 offset: 0x802
@scena.Code('func_01_802')
def func_01_802():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -115940, -4000, -111340, 180)
    ChrSetPos(0x0102, -116620, -4000, -110300, 180)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_84A',
    )

    ChrSetPos(0x0107, -115430, -4000, -109960, 180)

    def _loc_84A(): pass

    label('loc_84A')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_869',
    )

    ChrSetPos(0x0106, -116050, -4000, -109140, 180)

    def _loc_869(): pass

    label('loc_869')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_888',
    )

    ChrSetPos(0x0108, -116050, -4000, -109140, 180)

    def _loc_888(): pass

    label('loc_888')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8A7',
    )

    ChrSetPos(0x0110, -116740, -4000, -108860, 180)

    def _loc_8A7(): pass

    label('loc_8A7')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8C6',
    )

    ChrSetPos(0x013C, -116740, -4000, -108860, 180)

    def _loc_8C6(): pass

    label('loc_8C6')

    CameraMove(-116920, -4000, -112310, 2000)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010180441V#000F菲小姐，打扰一下好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000E, 0x0010)
    TalkBegin(0x000E)
    OP_4A(0x000E, 255)
    ChrClearFlags(0x000E, 0x0010)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1980180442V嗯？什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180443V#000F这是某人托我们带给您的东西。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180444V这个，请您收下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '给菲的情书',
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

    RemoveItem(0x035E, 1)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1980180445V这封信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180446V…………难道说，\n',
            '是沃尔费堡垒的布拉姆写的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160314V#000F嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180448V#002F（好！\n',
            '　这就把礼物拿给她。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B53',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180482V#008F（……哎呀，虽然心里一直惦记着，\n',
            '　最后还是忘记买礼物了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_F6F')

    def _loc_B53(): pass

    label('loc_B53')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BDD',
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
            TXT(0x00, '【工作手套】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_BCE'),
        (0x00000001, 'loc_BD4'),
        (-1, 'loc_BDA'),
    )

    def _loc_BCE(): pass

    label('loc_BCE')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_BDA')

    def _loc_BD4(): pass

    label('loc_BD4')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_BDA')

    def _loc_BDA(): pass

    label('loc_BDA')

    Jump('loc_F6F')

    def _loc_BDD(): pass

    label('loc_BDD')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C65',
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
            TXT(0x00, '【果馅饼】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_C56'),
        (0x00000001, 'loc_C5C'),
        (-1, 'loc_C62'),
    )

    def _loc_C56(): pass

    label('loc_C56')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_C62')

    def _loc_C5C(): pass

    label('loc_C5C')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_C62')

    def _loc_C62(): pass

    label('loc_C62')

    Jump('loc_F6F')

    def _loc_C65(): pass

    label('loc_C65')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CF1',
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
            TXT(0x00, '【绒毛编织帽】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_CE2'),
        (0x00000001, 'loc_CE8'),
        (-1, 'loc_CEE'),
    )

    def _loc_CE2(): pass

    label('loc_CE2')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_CEE')

    def _loc_CE8(): pass

    label('loc_CE8')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_CEE')

    def _loc_CEE(): pass

    label('loc_CEE')

    Jump('loc_F6F')

    def _loc_CF1(): pass

    label('loc_CF1')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D8F',
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
            TXT(0x00, '【工作手套】\n'),
            TXT(0x01, '【果馅饼】\n'),
            TXT(0x02, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_D7A'),
        (0x00000001, 'loc_D80'),
        (0x00000002, 'loc_D86'),
        (-1, 'loc_D8C'),
    )

    def _loc_D7A(): pass

    label('loc_D7A')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_D8C')

    def _loc_D80(): pass

    label('loc_D80')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_D8C')

    def _loc_D86(): pass

    label('loc_D86')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_D8C')

    def _loc_D8C(): pass

    label('loc_D8C')

    Jump('loc_F6F')

    def _loc_D8F(): pass

    label('loc_D8F')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E31',
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
            TXT(0x00, '【工作手套】\n'),
            TXT(0x01, '【绒毛编织帽】\n'),
            TXT(0x02, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_E1C'),
        (0x00000001, 'loc_E22'),
        (0x00000002, 'loc_E28'),
        (-1, 'loc_E2E'),
    )

    def _loc_E1C(): pass

    label('loc_E1C')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_E2E')

    def _loc_E22(): pass

    label('loc_E22')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_E2E')

    def _loc_E28(): pass

    label('loc_E28')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_E2E')

    def _loc_E2E(): pass

    label('loc_E2E')

    Jump('loc_F6F')

    def _loc_E31(): pass

    label('loc_E31')

    If(
        (
            (Expr.Eval, "OP_40(0x014D)"),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x01B2)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x014A)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_ED1',
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
            TXT(0x00, '【果馅饼】\n'),
            TXT(0x01, '【绒毛编织帽】\n'),
            TXT(0x02, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_EBC'),
        (0x00000001, 'loc_EC2'),
        (0x00000002, 'loc_EC8'),
        (-1, 'loc_ECE'),
    )

    def _loc_EBC(): pass

    label('loc_EBC')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_ECE')

    def _loc_EC2(): pass

    label('loc_EC2')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_ECE')

    def _loc_EC8(): pass

    label('loc_EC8')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_ECE')

    def _loc_ECE(): pass

    label('loc_ECE')

    Jump('loc_F6F')

    def _loc_ED1(): pass

    label('loc_ED1')

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
            TXT(0x00, '【工作手套】\n'),
            TXT(0x01, '【果馅饼】\n'),
            TXT(0x02, '【绒毛编织帽】\n'),
            TXT(0x03, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_F5A'),
        (0x00000001, 'loc_F5D'),
        (0x00000002, 'loc_F63'),
        (0x00000003, 'loc_F69'),
        (-1, 'loc_F6F'),
    )

    def _loc_F5A(): pass

    label('loc_F5A')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_F5D(): pass

    label('loc_F5D')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_F6F')

    def _loc_F63(): pass

    label('loc_F63')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_F6F')

    def _loc_F69(): pass

    label('loc_F69')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_F6F')

    def _loc_F6F(): pass

    label('loc_F6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_122E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180449V#000F对了，\n',
            '这是他送你的礼物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '工作手套',
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

    OP_62(0x00FE, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1980180450V……礼物？\n',
            '工作手套？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180451V好、好吧，\n',
            '我收下了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 270, 200)

    ChrTalk(
        0x00FE,
        (
            '#1980180452V哼，真是的，\n',
            '那个家伙到底在想什么，\n',
            '我一点都不明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180453V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180454V#509F（唔…………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180455V（这、这个礼物\n',
            '　好像失败了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrSetDirection(0x00FE, 0, 400)

    ChrTalk(
        0x00FE,
        (
            '#1980180456V……哎呀，对、对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180457V谢谢你们\n',
            '特地给我送过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180458V那…………\n',
            '我要继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180459V#506F啊……嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x014D, 1)
    OP_28(0x0031, 0x01, 0x0040)
    OP_2B(0x0031, 0x0002)

    Jump('loc_19A0')

    def _loc_122E(): pass

    label('loc_122E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_1521',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180449V#000F对了，\n',
            '这是他送你的礼物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '果馅饼',
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

    OP_62(0x00FE, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1980180461V谢、谢谢了。\n',
            '我很高兴…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180462V不过我最近要\n',
            '控制甜食的数量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180463V尽管这样，\n',
            '却送这样的礼物给我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 270, 200)

    ChrTalk(
        0x00FE,
        (
            '#1980180464V哼！看来他不懂得体贴别人这点\n',
            '还是完全没变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180453V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180454V#509F（唔…………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180455V（这、这个礼物\n',
            '　好像失败了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrSetDirection(0x00FE, 0, 400)

    ChrTalk(
        0x00FE,
        (
            '#1980180456V……哎呀，对、对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180457V谢谢你们\n',
            '特地给我送过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180458V那…………\n',
            '我要继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180459V#506F啊……嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x01B2, 1)
    OP_28(0x0031, 0x01, 0x0080)
    OP_2B(0x0031, 0x0002)

    Jump('loc_19A0')

    def _loc_1521(): pass

    label('loc_1521')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_175B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180449V#000F对了，\n',
            '这是他送你的礼物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '绒毛编织帽',
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

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1980180473V哇，好可爱呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180474V哎呀，\n',
            '他总算是稍微……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180475V……开始为我着想了呢。\n',
            '呵呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180476V不过既然知道该这样，\n',
            '为什么不早点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180453V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1980180456V……哎呀，对、对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180457V谢谢你们\n',
            '特地给我送过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180458V那…………\n',
            '我要继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160346V#506F啊……嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x014A, 1)
    OP_28(0x0031, 0x01, 0x0020)
    OP_2B(0x0031, 0x0004)

    Jump('loc_19A0')

    def _loc_175B(): pass

    label('loc_175B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_179C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180483V#505F（……唔～\n',
            '　没有看到合适的礼物。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_179C(): pass

    label('loc_179C')

    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1980180484V呼～这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180485V那家伙啊，\n',
            '肯定是已经反省过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 270, 200)

    ChrTalk(
        0x00FE,
        (
            '#1980180486V不过，\n',
            '就算他现在想到要写封信给我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180453V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180454V#509F（唔…………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180489V（果然还是应该送点礼物才行……）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrSetDirection(0x00FE, 0, 400)

    ChrTalk(
        0x00FE,
        (
            '#1980180456V……哎呀，对、对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180457V谢谢你们\n',
            '特地给我送过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980180458V那…………\n',
            '我要继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180459V#506F啊……嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0031, 0x01, 0x0100)

    def _loc_19A0(): pass

    label('loc_19A0')

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【爱之使者】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x0031, 0x04, 0x10)
    OP_28(0x0031, 0x01, 0x0010)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    EventEnd(0x00)
    OP_4B(0x000E, 255)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

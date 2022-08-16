import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3115_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3115_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3115.x'
    header.mapIndex       = 1
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('func_01_A9')
def func_01_A9():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('func_02_AA')
def func_02_AA():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(2300, 0, 2540, 0)
    ChrSetPos(0x0101, 1850, 0, 1780, 0)
    ChrSetPos(0x0102, 3300, 0, 2100, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_103',
    )

    ChrSetPos(0x0107, 2650, 0, 1120, 0)

    def _loc_103(): pass

    label('loc_103')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_122',
    )

    ChrSetPos(0x013C, 2530, 0, 3050, 359)

    def _loc_122(): pass

    label('loc_122')

    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0550181117V#800F咦，怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x013C,
        (
            '#2030181001V喵呀～～噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550181119V#802F哦，安东尼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181120V你那样叫，\n',
            '是想说些什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x013C,
        (
            '#2030181121V喵～噢，\n',
            '喵呀～～噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(120)

    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010181122V#509F唔，这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181123V#017F怎么看都很有嫌疑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070181124V#561F是啊～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0008,
        (
            '#0550181125V#802F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181126V你们在说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181127V#002F工房长先生，\n',
            '今天你去过医务室吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0550181128V#802F啊…………！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181129V#805F没、没有……\n',
            '没有去过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181130V#012F我们正在寻找\n',
            '被人从医务室里带走的香烟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181131V让我们对这个房间\n',
            '进行一下调查好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550181132V#806F唔，哦，\n',
            '倒是没什么不行的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181133V#507F那就不用顾虑了，\n',
            '让我们好好调查一番吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002C, 0x01, 0x0200)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x485
@scena.Code('func_03_485')
def func_03_485():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-102680, 0, 106860, 0)
    ChrSetPos(0x0101, -103170, 0, 107210, 90)
    ChrSetPos(0x0102, -102910, 0, 106140, 40)
    ChrSetPos(0x0107, -104120, 0, 106520, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4EF',
    )

    ChrSetPos(0x013C, -104780, 0, 107680, 90)

    def _loc_4EF(): pass

    label('loc_4EF')

    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010180648V#000F不好意思，可以打扰一下吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180649V您是普罗梅笛先生……吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0013, 0x0010)
    TalkBegin(0x0013)
    ChrClearFlags(0x0013, 0x0010)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    OP_4A(0x00FE, 255)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2080180650V嗯，\n',
            '我就是普罗梅笛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180651V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180652V#006F嗯，有点小事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180653V是这样的，\n',
            '我们在找运输车用的导力引擎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180654V想问一下普罗梅笛先生，\n',
            '如果您知道放在哪里的话，\n',
            '可以告诉我们吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180655V运输车用的\n',
            '导力引擎吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180656V实在很抱歉，\n',
            '我完全不知道放在哪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180657V#004F咦？怎么会呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180658V#014F我们听说普罗梅笛先生您\n',
            '是负责管理运输车的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2080180659V啊～～\n',
            '那是很久以前的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180660V那个职务是轮流担当的，\n',
            '会定期更换人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180661V而且………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180662V如果问我现在的负责人是谁，\n',
            '老实说我也不知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180663V#007F呼………………\n',
            '想问的他都抢先回答了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180664V那么，这样就行了吧？\n',
            '我还有很多事情要做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180665V#010F非常抱歉，\n',
            '在您百忙之中前来打扰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180666V嗯，那我先去忙别的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0013, 360, 400)
    OP_4B(0x00FE, 255)

    @scena.Lambda('lambda_0907')
    def lambda_0907():
        CameraMove(-103770, 0, 106670, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0907)

    ChrSetDirection(0x0101, 223, 400)
    ChrSetDirection(0x0102, 286, 400)
    WaitForThreadExit(0x00FE, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0029, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_B3B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180667V#003F唔……\n',
            '怎么和之前说的不一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180668V#561F不、不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180669V因为设备的管理\n',
            '是件相当麻烦的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180670V#013F普罗梅笛先生不知道的话……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180671V就只剩在『卡佩尔』上\n',
            '看到过的那个线索了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180672V#505F嗯，\n',
            '应该在地下工场的入口……\n',
            '资料上面是这么记载的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180673V#060F啊，\n',
            '那是卡鲁迪亚隧道的出口。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180674V那片区域放置了各种各样的零部件。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180675V#010F好，\n',
            '那么我们就到地下去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180676V#006F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1028')

    def _loc_B3B(): pass

    label('loc_B3B')

    ChrTalk(
        0x0101,
        (
            '#0010180677V#003F唔……这下麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180678V怎么和之前说的不一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180668V#561F不、不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180669V因为设备的管理\n',
            '是件相当麻烦的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180681V#010F算了，这也是没办法事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180682V我们还是想想其他办法\n',
            '去调查一下运输车的事情吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180683V我想应该会有其他线索的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0029, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_F04',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180684V#505F别的办法……吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180685V…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180686V#004F……啊，我想起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D12')
    def lambda_0D12():
        ChrTurnDirection(0x0107, 0x0101, 0)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0D12)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180687V#014F什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180688V#002F你想想，\n',
            '不久之前我们不是利用了一个\n',
            '什么导力器收集了不少信息吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180689V#060F是演算导力器『卡佩尔』对吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180690V#000F对对，就是它。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180691V#505F我记得那个时候\n',
            '好像看到了有关运输车的事项……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0107, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180692V#014F对啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180693V『卡佩尔』里面的确应该有\n',
            '运输车的相关记录。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180694V#010F我们立刻就去调查吧，\n',
            '演算室在五楼哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180695V#508F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0029, 0x01, 0x0004)

    Jump('loc_1028')

    def _loc_F04(): pass

    label('loc_F04')

    ChrTalk(
        0x0101,
        (
            '#0010180696V#505F找其他的方法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180697V话是这么说，\n',
            '可应该不会那么简单的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180698V#010F不过，\n',
            '在这里干着急也不是办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180699V也许会有线索的。\n',
            '总之先在工房里转转看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180700V#060F嗯，好～的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180701V#006F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180702V那我们走吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1028(): pass

    label('loc_1028')

    Sleep(400)

    OP_28(0x0029, 0x01, 0x0001)
    OP_28(0x0029, 0x01, 0x0002)
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x103F
@scena.Code('func_04_103F')
def func_04_103F():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -102420, 0, 3650, 45)
    ChrSetPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10C4',
    )

    ChrSetPos(0x0107, -102560, 0, 2630, 45)

    def _loc_10C4(): pass

    label('loc_10C4')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10E3',
    )

    ChrSetPos(0x0106, -103730, 0, 3450, 45)

    def _loc_10E3(): pass

    label('loc_10E3')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1102',
    )

    ChrSetPos(0x013C, -103730, 0, 3450, 45)

    def _loc_1102(): pass

    label('loc_1102')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1121',
    )

    ChrSetPos(0x0110, -103380, 0, 2360, 45)

    def _loc_1121(): pass

    label('loc_1121')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_113B',
    )

    @scena.Lambda('lambda_1133')
    def lambda_1133():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1133)

    def _loc_113B(): pass

    label('loc_113B')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1155',
    )

    @scena.Lambda('lambda_114D')
    def lambda_114D():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_114D)

    def _loc_1155(): pass

    label('loc_1155')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_116F',
    )

    @scena.Lambda('lambda_1167')
    def lambda_1167():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1167)

    def _loc_116F(): pass

    label('loc_116F')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1189',
    )

    @scena.Lambda('lambda_1181')
    def lambda_1181():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1181)

    def _loc_1189(): pass

    label('loc_1189')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_11A3',
    )

    @scena.Lambda('lambda_119B')
    def lambda_119B():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_119B)

    def _loc_11A3(): pass

    label('loc_11A3')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_142E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010181239V#000F嗯～打扰一下好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181240V我们两个是看了公告板而来的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_129A',
    )

    ChrTalk(
        0x00FE,
        (
            '#2120181248V啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181249V来得好晚呀。\n',
            '我还以为你们不来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181247V#506F对不起啊，\n',
            '因为有重要任务在身。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13F6')

    def _loc_129A(): pass

    label('loc_129A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_134B',
    )

    ChrTalk(
        0x00FE,
        (
            '#2120181245V啊……\n',
            '你们终于来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181246V唉，游击士协会\n',
            '哪个支部都是人手不足，\n',
            '这也是没办法的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181247V#506F对不起啊，\n',
            '因为有重要任务在身。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13F6')

    def _loc_134B(): pass

    label('loc_134B')

    ChrTalk(
        0x00FE,
        (
            '#2120181241V啊……\n',
            '来得好快呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181242V我刚刚才\n',
            '把委托贴上去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150561V#001F呵呵呵⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181244V#006F我们也是刚调到这里来的，\n',
            '所以干劲十足呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13F6(): pass

    label('loc_13F6')

    ChrTalk(
        0x00FE,
        (
            '#2120181251V我这就把任务内容予以说明，\n',
            '可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_148E')

    def _loc_142E(): pass

    label('loc_142E')

    ChrTalk(
        0x00FE,
        (
            '#2120181256V咦，是你们。\n',
            '终于来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181257V我这就把任务内容予以说明，\n',
            '可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_148E(): pass

    label('loc_148E')

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
        10,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_159C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010181252V#501F啊，对不起。\n',
            '现在还不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181253V啊，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181254V那么等你们办完事了\n',
            '就再到这里来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170025V#006F嗯，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002D, 0x01, 0x4000)

    @scena.Lambda('lambda_1591')
    def lambda_1591():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1591)

    EventEnd(0x00)

    Return()

    def _loc_159C(): pass

    label('loc_159C')

    ChrTalk(
        0x0101,
        (
            '#0010150317V#006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181259V#010F募集临时图书馆员……\n',
            '没错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181260V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181261V有一些让人\n',
            '束手无策的麻烦事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181262V#004F束手无策？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181263V啊，这个我们之后再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181264V在此之前，\n',
            '还有件事情想让你们解决。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181265V我先拜托你们\n',
            '这件事情好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181266V#010F是什么样的事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181267V工房的研究室\n',
            '经常从资料室这里借书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181268V可是有时期限到了，\n',
            '书却还没有归还。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181269V首先你们就去\n',
            '把那些书找回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181270V#000F这样啊，很简单嘛。\n',
            '大致到哪里去找呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181271V嗯，借书人的所在地有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181272V三楼的设计室以及\n',
            '四楼的实验室和医务室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181273V#000F三楼的设计室以及\n',
            '四楼的实验室和医务室……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181274V………………就这些吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181275V嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181276V请尽快地找回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181277V#001F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181278V#010F我们会很快找回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002D, 0x04, 0x04)
    OP_28(0x002D, 0x04, 0x08)
    OP_28(0x002D, 0x01, 0x0001)
    OP_28(0x002D, 0x01, 0x0002)
    Call(1, 0x000D)

    @scena.Lambda('lambda_1980')
    def lambda_1980():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1980)

    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x198B
@scena.Code('func_05_198B')
def func_05_198B():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -102420, 0, 3650, 45)
    ChrSetPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A10',
    )

    ChrSetPos(0x0107, -102560, 0, 2630, 45)

    def _loc_1A10(): pass

    label('loc_1A10')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A2F',
    )

    ChrSetPos(0x0106, -103730, 0, 3450, 45)

    def _loc_1A2F(): pass

    label('loc_1A2F')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A4E',
    )

    ChrSetPos(0x013C, -103730, 0, 3450, 45)

    def _loc_1A4E(): pass

    label('loc_1A4E')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A6D',
    )

    ChrSetPos(0x0110, -103380, 0, 2360, 45)

    def _loc_1A6D(): pass

    label('loc_1A6D')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1A87',
    )

    @scena.Lambda('lambda_1A7F')
    def lambda_1A7F():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1A7F)

    def _loc_1A87(): pass

    label('loc_1A87')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1AA1',
    )

    @scena.Lambda('lambda_1A99')
    def lambda_1A99():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1A99)

    def _loc_1AA1(): pass

    label('loc_1AA1')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1ABB',
    )

    @scena.Lambda('lambda_1AB3')
    def lambda_1AB3():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1AB3)

    def _loc_1ABB(): pass

    label('loc_1ABB')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1AD5',
    )

    @scena.Lambda('lambda_1ACD')
    def lambda_1ACD():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1ACD)

    def _loc_1AD5(): pass

    label('loc_1AD5')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1AEF',
    )

    @scena.Lambda('lambda_1AE7')
    def lambda_1AE7():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_1AE7)

    def _loc_1AEF(): pass

    label('loc_1AEF')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181310V怎么样？\n',
            '任务进展的如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181311V#001F呵呵呵～⊙\n',
            '拿来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Return,
        ),
        'loc_1BAA',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '结晶光学论集',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0342, 1)

    def _loc_1BAA(): pass

    label('loc_1BAA')

    If(
        (
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Return,
        ),
        'loc_1BFF',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '明日料理',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0341, 1)

    def _loc_1BFF(): pass

    label('loc_1BFF')

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Return,
        ),
        'loc_1C5C',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '猫语日常会话入门',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0340, 1)

    def _loc_1C5C(): pass

    label('loc_1C5C')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0004)"),
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0008)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0010)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26BF',
    )

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '全部的书都归还了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【募集临时图书馆员】',
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

    ChrTalk(
        0x00FE,
        (
            '#2120181282V嗯……没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181283V这么一来，\n',
            '所有的书都找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181284V辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181315V#502F哼哼，这种工作简直轻而易举。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181316V#019F的确是小事一桩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181317V哎呀，果然很靠得住呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181318V那么我就立刻\n',
            '把正式的任务拜托给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181319V#501F啊，这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181320V就是刚才所说的\n',
            '让人束手无策的麻烦事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181321V#014F究竟是什么样的任务呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181322V基本的目的还是和刚才一样，\n',
            '找回过了归还期限的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181323V需要去寻找的书名为\n',
            '《艾尔贝啄木鸟的生态》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181324V#015F先记录下来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181325V#000F啊，好的好的…………\n',
            '《啄木鸟的生态》……对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181326V#505F与鸟有关的书……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_204C',
    )

    ChrTalk(
        0x0107,
        (
            '#0070181327V#060F嗯。\n',
            '也许是～吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070181328V因为艾尔贝啄木鸟是\n',
            '在很久很久以前出现过的鸟的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20BB')

    def _loc_204C(): pass

    label('loc_204C')

    ChrTalk(
        0x0107,
        (
            '#0070181329V#060F啊，是的。\n',
            '我觉得没错～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070181330V因为艾尔贝啄木鸟是\n',
            '在很久很久以前出现过的鸟的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20BB(): pass

    label('loc_20BB')

    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181331V#000F呼～原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20EB(): pass

    label('loc_20EB')

    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181332V#010F那么，有什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181333V嗯，线索是有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181334V……请看这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)
    Sleep(100)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            '#2130181335V',
            (TxtCtl.SetColor, 0x0),
            '到山村的　池中伫立的　石人\n',
            '旁边看看吧　会有收获的',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010181336V#505F虽然记下来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181337V…………这是什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181338V是这本书的借书卡\n',
            '上面写的文字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181339V总而言之，\n',
            '这个好像就是书的隐藏地点的相关提示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181340V#004F隐藏地点的提示……吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181341V这么说来，\n',
            '一开始借书时就打算把书藏起来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181342V嗯，好像是的。\n',
            '这是过去的研究员所做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181343V至于为什么要把书藏起来，\n',
            '我就怎么也想不明白了……\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181344V不过，奇怪的人是很多的，\n',
            '这已经可算是这里的传统了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2439',
    )

    OP_62(0x0107, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070181345V#067F啊、啊哈哈…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2439(): pass

    label('loc_2439')

    ChrTalk(
        0x00FE,
        (
            '#2120181346V那么接下来就拜托你们了。\n',
            '好好加油去找吧。',
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
            '#0010181347V#004F等、等一下，\n',
            '就只有这点线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181348V啊，就只有这些哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181349V正因为如此，\n',
            '我才会委托游击士协会嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010181350V#007F呼………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181351V这、这么一说，\n',
            '我就觉得没希望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181352V#010F……我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181353V困难的任务更要\n',
            '加倍地努力去做才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181354V就在蔡斯周围的地区调查，\n',
            '一定可以找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181355V我会在这里等着的。\n',
            '找到书之后就把它拿来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181356V#007F呼…………\n',
            '只有加油干了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181357V哦呵呵，我很期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_271F')

    def _loc_26BF(): pass

    label('loc_26BF')

    ChrTalk(
        0x00FE,
        (
            '#2120181282V嗯……没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181359V那么，\n',
            '剩下的书也拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x000D)

    @scena.Lambda('lambda_2714')
    def lambda_2714():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2714)

    EventEnd(0x00)

    Return()

    def _loc_271F(): pass

    label('loc_271F')

    Call(1, 0x000D)

    @scena.Lambda('lambda_2729')
    def lambda_2729():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2729)

    OP_28(0x002D, 0x04, 0x10)
    OP_28(0x002D, 0x01, 0x0020)
    OP_28(0x002E, 0x04, 0x02)
    OP_28(0x002E, 0x04, 0x04)
    OP_28(0x002E, 0x04, 0x08)
    OP_28(0x002E, 0x01, 0x0001)
    OP_28(0x002E, 0x01, 0x0002)
    OP_28(0x002E, 0x01, 0x0004)
    OP_28(0x002E, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x2766
@scena.Code('func_06_2766')
def func_06_2766():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -102420, 0, 3650, 45)
    ChrSetPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27EB',
    )

    ChrSetPos(0x0107, -102560, 0, 2630, 45)

    def _loc_27EB(): pass

    label('loc_27EB')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_280A',
    )

    ChrSetPos(0x0106, -103730, 0, 3450, 45)

    def _loc_280A(): pass

    label('loc_280A')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2829',
    )

    ChrSetPos(0x013C, -103730, 0, 3450, 45)

    def _loc_2829(): pass

    label('loc_2829')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2848',
    )

    ChrSetPos(0x0110, -103380, 0, 2360, 45)

    def _loc_2848(): pass

    label('loc_2848')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2862',
    )

    @scena.Lambda('lambda_285A')
    def lambda_285A():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_285A)

    def _loc_2862(): pass

    label('loc_2862')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_287C',
    )

    @scena.Lambda('lambda_2874')
    def lambda_2874():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2874)

    def _loc_287C(): pass

    label('loc_287C')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2896',
    )

    @scena.Lambda('lambda_288E')
    def lambda_288E():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_288E)

    def _loc_2896(): pass

    label('loc_2896')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28B0',
    )

    @scena.Lambda('lambda_28A8')
    def lambda_28A8():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_28A8)

    def _loc_28B0(): pass

    label('loc_28B0')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_28CA',
    )

    @scena.Lambda('lambda_28C2')
    def lambda_28C2():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_28C2)

    def _loc_28CA(): pass

    label('loc_28CA')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181279V哎呀……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181280V把书拿回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181281V#508F嗯，拿来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Return,
        ),
        'loc_299B',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '结晶光学论集',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0342, 1)

    def _loc_299B(): pass

    label('loc_299B')

    If(
        (
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Return,
        ),
        'loc_29F0',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '明日料理',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0341, 1)

    def _loc_29F0(): pass

    label('loc_29F0')

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Return,
        ),
        'loc_2A4D',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '猫语日常会话入门',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0340, 1)

    def _loc_2A4D(): pass

    label('loc_2A4D')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0004)"),
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0008)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0010)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CF3',
    )

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '全部的书都归还了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【募集临时图书馆员】',
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

    ChrTalk(
        0x00FE,
        (
            '#2120181282V嗯……没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181283V这么一来，\n',
            '所有的书都找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181284V辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181285V#010F对不起，\n',
            '这么晚才来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181286V没关系，\n',
            '你们还有别的重要工作嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181287V在你们最忙的时候\n',
            '还是能坚持完成了任务，\n',
            '我已经很感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181288V#001F嗯……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181289V彼此彼此，非常感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181290V那你们以后也要继续努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181291V#010F感谢最近一段时间\n',
            '您对我们的诸多照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151344V#000F再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002D, 0x04, 0x10)
    OP_28(0x002D, 0x01, 0x0020)

    Jump('loc_3011')

    def _loc_2CF3(): pass

    label('loc_2CF3')

    ChrTalk(
        0x00FE,
        (
            '#2120181293V嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181294V对了，\n',
            '剩下的书我已经收回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181295V所以，\n',
            '委托就此中止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181211V#004F咦……怎么会？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181297V我从协会那里听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181298V你们马上就要\n',
            '调到别的支部去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181299V所以调离之前，\n',
            '必须将委托的事宜整理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181300V#013F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181301V对不起。\n',
            '工作半途而废了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181302V#003F真的很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181303V哎呀，不用在意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181304V你们还有别的重要工作嘛。\n',
            '这也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181305V#000F嗯……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181306V感谢你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181307V要打起精神哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181291V#010F感谢最近一段时间\n',
            '您对我们的诸多照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181309V#508F再见了。',
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
            '任务【募集临时图书馆员】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x002D, 0x04, 0x10)
    OP_28(0x002D, 0x01, 0x0040)
    Call(1, 0x000D)

    def _loc_3011(): pass

    label('loc_3011')

    OP_28(0x002D, 0x04, 0x10)
    OP_28(0x002D, 0x01, 0x4000)
    Call(1, 0x000D)

    @scena.Lambda('lambda_3026')
    def lambda_3026():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3026)

    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x3031
@scena.Code('func_07_3031')
def func_07_3031():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -102420, 0, 3650, 45)
    ChrSetPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30B6',
    )

    ChrSetPos(0x0107, -102560, 0, 2630, 45)

    def _loc_30B6(): pass

    label('loc_30B6')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30D5',
    )

    ChrSetPos(0x0106, -103730, 0, 3450, 45)

    def _loc_30D5(): pass

    label('loc_30D5')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30F4',
    )

    ChrSetPos(0x013C, -103730, 0, 3450, 45)

    def _loc_30F4(): pass

    label('loc_30F4')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3113',
    )

    ChrSetPos(0x0110, -103380, 0, 2360, 45)

    def _loc_3113(): pass

    label('loc_3113')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_312D',
    )

    @scena.Lambda('lambda_3125')
    def lambda_3125():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3125)

    def _loc_312D(): pass

    label('loc_312D')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3147',
    )

    @scena.Lambda('lambda_313F')
    def lambda_313F():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_313F)

    def _loc_3147(): pass

    label('loc_3147')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3161',
    )

    @scena.Lambda('lambda_3159')
    def lambda_3159():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3159)

    def _loc_3161(): pass

    label('loc_3161')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_317B',
    )

    @scena.Lambda('lambda_3173')
    def lambda_3173():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3173)

    def _loc_317B(): pass

    label('loc_317B')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3195',
    )

    @scena.Lambda('lambda_318D')
    def lambda_318D():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_318D)

    def _loc_3195(): pass

    label('loc_3195')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181360V啊……\n',
            '有什么进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181361V#001F嗯，很顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181362V#006F书已经带回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181363V#010F请您确认一下。',
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
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '艾尔贝啄木鸟的生态',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【临时图书馆员的加班】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0343, 1)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181364V……哎呀，真让我惊讶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181365V的确是这本书呢。\n',
            '终于找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181366V#502F呵呵呵。\n',
            '我们还只是小试牛刀而已呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181367V说实话，\n',
            '我一直认为已经不可能找回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181368V能够找回来\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181369V这样一来，我就可以放心地\n',
            '把剩下的任务交给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010181370V#004F啊……………！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181371V……什么，剩下的任务？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181372V#014F……还有其他的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181373V那个研究员隐藏起来的书\n',
            '一共有三本呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181374V就是说，\n',
            '还剩下后面的两本哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181375V……我之前没有说过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181376V#509F完全没有，根本就是头一次听说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181377V哎呀，这可真是奇怪了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181378V不过这样也不错嘛。\n',
            '现在你们已经是骑虎难下了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181379V就请你们\n',
            '坚持到最后吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181380V#505F好吧，\n',
            '这倒是没什么关系…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181381V只要别再出现那种含义不明的文字就行了，\n',
            '那东西真是让人摸不着头脑呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_36D0',
    )

    ChrTalk(
        0x0102,
        (
            '#0020181382V#017F说起来，\n',
            '在卢安也遇到过这样的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36D0(): pass

    label('loc_36D0')

    ChrTalk(
        0x00FE,
        (
            '#2120181383V哎呀，\n',
            '你们不用担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181384V这本书的提示\n',
            '并不是什么文字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181385V#004F啊，真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181386V事实胜于雄辩，\n',
            '我这就让你们看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '　● 　 ●　\n',
            '　　 ×\n',
            '　● 　 ●　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010181387V#509F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181388V……我、我无话可说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181389V#014F……一点说明都没有呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3939',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_38DD',
    )

    ChrTalk(
        0x0107,
        (
            '#0070181390V#063F……●和×吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070181391V唔～是说×记号的地方\n',
            '就是书的所在地吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3939')

    def _loc_38DD(): pass

    label('loc_38DD')

    ChrTalk(
        0x0107,
        (
            '#0070181392V#063F……●和×吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070181393V唔～是说×记号的地方\n',
            '就是书的所在地吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3939(): pass

    label('loc_3939')

    ChrTalk(
        0x00FE,
        (
            '#2120181394V要寻找的这本书名为\n',
            '《哈茨少年冒险记·下》哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181395V#000F好的好的，\n',
            '《哈茨少年冒险记·下》对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181396V资料室里只留有上卷，\n',
            '『下卷在哪里？』想看的人经常这么嚷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181397V好了，\n',
            '你们就鼓足干劲去找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181398V#013F话虽如此，\n',
            '这次的更难解决啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181399V#007F与现在这个相比，\n',
            '反而觉得有文字的要简单一些呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181400V……算了，不管写了什么，\n',
            '都还是要去找啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181401V那么，\n',
            '就请你们继续努力寻找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181402V和刚才一样，\n',
            '我会在这里等着的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181403V#010F那么我们就出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181404V#006F好的，加油干吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002E, 0x04, 0x10)
    OP_28(0x002E, 0x01, 0x0020)
    OP_28(0x002F, 0x04, 0x02)
    OP_28(0x002F, 0x04, 0x04)
    OP_28(0x002F, 0x04, 0x08)
    OP_28(0x002F, 0x01, 0x0001)
    OP_28(0x002F, 0x01, 0x0002)
    OP_28(0x002F, 0x01, 0x0004)
    Call(1, 0x000D)

    @scena.Lambda('lambda_3BC9')
    def lambda_3BC9():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3BC9)

    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x3BD4
@scena.Code('func_08_3BD4')
def func_08_3BD4():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -102420, 0, 3650, 45)
    ChrSetPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C59',
    )

    ChrSetPos(0x0107, -102560, 0, 2630, 45)

    def _loc_3C59(): pass

    label('loc_3C59')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C78',
    )

    ChrSetPos(0x0106, -103730, 0, 3450, 45)

    def _loc_3C78(): pass

    label('loc_3C78')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C97',
    )

    ChrSetPos(0x013C, -103730, 0, 3450, 45)

    def _loc_3C97(): pass

    label('loc_3C97')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3CB6',
    )

    ChrSetPos(0x0110, -103380, 0, 2360, 45)

    def _loc_3CB6(): pass

    label('loc_3CB6')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3CD0',
    )

    @scena.Lambda('lambda_3CC8')
    def lambda_3CC8():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3CC8)

    def _loc_3CD0(): pass

    label('loc_3CD0')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3CEA',
    )

    @scena.Lambda('lambda_3CE2')
    def lambda_3CE2():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3CE2)

    def _loc_3CEA(): pass

    label('loc_3CEA')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3D04',
    )

    @scena.Lambda('lambda_3CFC')
    def lambda_3CFC():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3CFC)

    def _loc_3D04(): pass

    label('loc_3D04')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3D1E',
    )

    @scena.Lambda('lambda_3D16')
    def lambda_3D16():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3D16)

    def _loc_3D1E(): pass

    label('loc_3D1E')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3D38',
    )

    @scena.Lambda('lambda_3D30')
    def lambda_3D30():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_3D30)

    def _loc_3D38(): pass

    label('loc_3D38')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181405V啊……\n',
            '你们把书拿来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181406V#006F嗯，对啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181363V#010F请您确认一下。',
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
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '艾尔贝啄木鸟的生态',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【临时图书馆员的加班】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0343, 1)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181364V……哎呀，真让我惊讶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181365V的确是这本书呢。\n',
            '终于找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181285V#010F对不起，\n',
            '这么晚才来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181286V没关系，\n',
            '你们还有别的重要工作嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181287V在你们最忙的时候\n',
            '还是能完成了任务，\n',
            '我已经很感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181305V#000F嗯……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181414V那再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181307V各位请慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181291V#010F感谢最近一段时间\n',
            '您对我们的诸多照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181309V#508F再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002E, 0x04, 0x10)
    OP_28(0x002E, 0x01, 0x0020)
    OP_28(0x002D, 0x01, 0x4000)
    Call(1, 0x000D)

    @scena.Lambda('lambda_402D')
    def lambda_402D():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_402D)

    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x4038
@scena.Code('func_09_4038')
def func_09_4038():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -102420, 0, 3650, 45)
    ChrSetPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40BD',
    )

    ChrSetPos(0x0107, -102560, 0, 2630, 45)

    def _loc_40BD(): pass

    label('loc_40BD')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40DC',
    )

    ChrSetPos(0x0106, -103730, 0, 3450, 45)

    def _loc_40DC(): pass

    label('loc_40DC')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40FB',
    )

    ChrSetPos(0x013C, -103730, 0, 3450, 45)

    def _loc_40FB(): pass

    label('loc_40FB')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_411A',
    )

    ChrSetPos(0x0110, -103380, 0, 2360, 45)

    def _loc_411A(): pass

    label('loc_411A')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4134',
    )

    @scena.Lambda('lambda_412C')
    def lambda_412C():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_412C)

    def _loc_4134(): pass

    label('loc_4134')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_414E',
    )

    @scena.Lambda('lambda_4146')
    def lambda_4146():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_4146)

    def _loc_414E(): pass

    label('loc_414E')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4168',
    )

    @scena.Lambda('lambda_4160')
    def lambda_4160():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_4160)

    def _loc_4168(): pass

    label('loc_4168')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4182',
    )

    @scena.Lambda('lambda_417A')
    def lambda_417A():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_417A)

    def _loc_4182(): pass

    label('loc_4182')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_419C',
    )

    @scena.Lambda('lambda_4194')
    def lambda_4194():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_4194)

    def _loc_419C(): pass

    label('loc_419C')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181418V哎呀…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181419V……难道，\n',
            '你们已经找到书了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181420V#502F呵呵呵，的确找到了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181421V#010F请您确认一下。',
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
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '哈茨少年冒险记·下',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【续·临时图书馆员的加班】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0344, 1)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181422V……嗯，确实是这本呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181423V那么，\n',
            '这样就只剩最后一本了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181424V#007F呼，好歹也让我喘口气吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181425V#006F那么，\n',
            '接下来要找的是什么书呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181426V哦呵呵，不要着急，\n',
            '我这就告诉你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181427V最后要找的是名为\n',
            '《３１棵丝柏树》的书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181428V……这是它对应的借书卡，\n',
            '在这上面又写着\n',
            '一些含义不明的文字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            '#2130181429V',
            (TxtCtl.SetColor, 0x0),
            '　去问风景今何在\n',
            '　呀，山上耸立３\n',
            '　１棵丝柏。钟楼\n',
            '　宁远音，隔世的\n',
            '　饱经之苦如斜木\n',
            '　之坡上滚落酒桶\n',
            '　长阵，接近梦中\n',
            '　沉眠不绝的我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010181430V#509F这次的更古怪啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181431V#007F算了，\n',
            '不管怎么说都只有知难而进了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181432V#010F又是谜语吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_45DC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070181433V#062F嗯，好像是～呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45FF')

    def _loc_45DC(): pass

    label('loc_45DC')

    ChrTalk(
        0x0107,
        (
            '#0070181434V#062F好像是～呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45FF(): pass

    label('loc_45FF')

    ChrTalk(
        0x00FE,
        (
            '#2120181435V已经对这个\n',
            '驾轻就熟了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181436V呵呵……\n',
            '这样就可以一气呵成了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181437V为了彻底达到目标，\n',
            '好好地加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181438V#508F那我们就出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181439V#010F告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002F, 0x04, 0x10)
    OP_28(0x002F, 0x01, 0x0010)
    OP_28(0x0030, 0x04, 0x02)
    OP_28(0x0030, 0x04, 0x04)
    OP_28(0x0030, 0x04, 0x08)
    OP_28(0x0030, 0x01, 0x0001)
    OP_28(0x0030, 0x01, 0x0002)
    Call(1, 0x000D)

    @scena.Lambda('lambda_4706')
    def lambda_4706():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4706)

    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x4711
@scena.Code('func_0A_4711')
def func_0A_4711():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -102420, 0, 3650, 45)
    ChrSetPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4796',
    )

    ChrSetPos(0x0107, -102560, 0, 2630, 45)

    def _loc_4796(): pass

    label('loc_4796')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_47B5',
    )

    ChrSetPos(0x0106, -103730, 0, 3450, 45)

    def _loc_47B5(): pass

    label('loc_47B5')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_47D4',
    )

    ChrSetPos(0x013C, -103730, 0, 3450, 45)

    def _loc_47D4(): pass

    label('loc_47D4')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_47F3',
    )

    ChrSetPos(0x0110, -103380, 0, 2360, 45)

    def _loc_47F3(): pass

    label('loc_47F3')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_480D',
    )

    @scena.Lambda('lambda_4805')
    def lambda_4805():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4805)

    def _loc_480D(): pass

    label('loc_480D')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4827',
    )

    @scena.Lambda('lambda_481F')
    def lambda_481F():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_481F)

    def _loc_4827(): pass

    label('loc_4827')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4841',
    )

    @scena.Lambda('lambda_4839')
    def lambda_4839():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_4839)

    def _loc_4841(): pass

    label('loc_4841')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_485B',
    )

    @scena.Lambda('lambda_4853')
    def lambda_4853():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_4853)

    def _loc_485B(): pass

    label('loc_485B')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4875',
    )

    @scena.Lambda('lambda_486D')
    def lambda_486D():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_486D)

    def _loc_4875(): pass

    label('loc_4875')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181418V哎呀…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181441V你们把书拿来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181442V#508F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181363V#010F请您确认一下。',
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
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '哈茨少年冒险记·下',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【续·临时图书馆员的加班】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0344, 1)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181364V……哎呀，真让我惊讶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181365V的确是这本书呢。\n',
            '终于找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181446V这样嘛，\n',
            '委托就此中止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181447V#004F咦……为什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181448V不是说还有书没有收回来吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181297V我从协会那里听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181298V你们马上就要\n',
            '调到别的支部去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181299V所以调离之前，\n',
            '必须将委托的事宜整理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181300V#013F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181301V对不起。\n',
            '工作半途而废了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181286V你们还有别的重要工作嘛。\n',
            '这也是没办法的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181455V你们能做到这个份上\n',
            '已经足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181456V剩下的工作\n',
            '由蔡斯支部的其他人\n',
            '去完成就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181457V#006F嗯……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181289V彼此彼此，非常感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181290V那你们以后也要继续努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181291V#010F感谢最近一段时间\n',
            '您对我们的诸多照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151344V#000F再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002F, 0x04, 0x10)
    OP_28(0x002F, 0x01, 0x0010)
    OP_28(0x002F, 0x01, 0x0020)
    OP_28(0x002D, 0x01, 0x4000)
    Call(1, 0x000D)

    @scena.Lambda('lambda_4D01')
    def lambda_4D01():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4D01)

    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x4D0C
@scena.Code('func_0B_4D0C')
def func_0B_4D0C():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -102420, 0, 3650, 45)
    ChrSetPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4D91',
    )

    ChrSetPos(0x0107, -102560, 0, 2630, 45)

    def _loc_4D91(): pass

    label('loc_4D91')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4DB0',
    )

    ChrSetPos(0x0106, -103730, 0, 3450, 45)

    def _loc_4DB0(): pass

    label('loc_4DB0')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4DCF',
    )

    ChrSetPos(0x013C, -103730, 0, 3450, 45)

    def _loc_4DCF(): pass

    label('loc_4DCF')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4DEE',
    )

    ChrSetPos(0x0110, -103380, 0, 2360, 45)

    def _loc_4DEE(): pass

    label('loc_4DEE')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4E08',
    )

    @scena.Lambda('lambda_4E00')
    def lambda_4E00():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4E00)

    def _loc_4E08(): pass

    label('loc_4E08')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4E22',
    )

    @scena.Lambda('lambda_4E1A')
    def lambda_4E1A():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_4E1A)

    def _loc_4E22(): pass

    label('loc_4E22')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4E3C',
    )

    @scena.Lambda('lambda_4E34')
    def lambda_4E34():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_4E34)

    def _loc_4E3C(): pass

    label('loc_4E3C')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4E56',
    )

    @scena.Lambda('lambda_4E4E')
    def lambda_4E4E():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_4E4E)

    def _loc_4E56(): pass

    label('loc_4E56')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4E70',
    )

    @scena.Lambda('lambda_4E68')
    def lambda_4E68():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_4E68)

    def _loc_4E70(): pass

    label('loc_4E70')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181418V哎呀…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181486V……难道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181487V#006F嗯，\n',
            '最后一本书也已经找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181488V#010F为了慎重起见，\n',
            '还请您确认一下。',
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
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '３１棵丝柏树',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【再续·临时图书管理员的加班】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0345, 1)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181489V……嗯，就是它没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181490V好厉害呀，\n',
            '真的把３本都找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181491V#001F嘿嘿，\n',
            '因为我们很努力地找啊找啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181492V#000F啊，对了……\n',
            '我们还找到了其他的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181493V#010F是和书放在一起的……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚说明了找到犯人留下的字条\n',
            '和结晶回路的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181494V呼～\n',
            '竟然是出于这样的动机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181495V唉，不管是什么样的理由，\n',
            '也不能给别人制造这么大的麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181496V那个结晶回路\n',
            '你们就拿去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181497V因为让你们费了不少功夫，\n',
            '就算是回报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150603V#001F嗯，非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181499V#010F那么，到现在为止，\n',
            '任务已经做完了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181500V嗯，是呀。\n',
            '任务已经全部完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181501V#007F呼，太好了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181502V我到现在都还觉得\n',
            '会有新任务冒出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_530E',
    )

    ChrTalk(
        0x0107,
        (
            '#0070181503V#061F嘿嘿，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_530E(): pass

    label('loc_530E')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181504V由于你们的努力，\n',
            '麻烦事已经全部解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181505V呵呵，\n',
            '真的很感谢你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181506V托你们的福，\n',
            '最近一段时间我也没事了，太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150156V#501F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181508V……没、没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181509V那么，辛苦你们了。\n',
            '如果再有事情还要麻烦你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181510V#001F嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181511V#010F承蒙您多方的关照，\n',
            '告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    OP_28(0x0030, 0x04, 0x10)
    OP_28(0x0030, 0x01, 0x0008)
    Call(1, 0x000D)

    @scena.Lambda('lambda_54B0')
    def lambda_54B0():
        ChrSetDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_54B0)

    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x54BB
@scena.Code('func_0C_54BB')
def func_0C_54BB():
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '结晶光学论集',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0342, 1)
    ChrSetFlags(0x0018, 0x0080)
    OP_64(0x07, 0x0001)
    OP_28(0x002D, 0x01, 0x0004)
    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x5524
@scena.Code('func_0D_5524')
def func_0D_5524():
    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_5533',
    )

    OP_65(0x0D, 0x0001)

    def _loc_5533(): pass

    label('loc_5533')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_5542',
    )

    OP_65(0x09, 0x0001)

    def _loc_5542(): pass

    label('loc_5542')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_5551',
    )

    OP_65(0x0E, 0x0001)

    def _loc_5551(): pass

    label('loc_5551')

    If(
        (
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0004)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5566',
    )

    OP_65(0x0A, 0x0001)

    def _loc_5566(): pass

    label('loc_5566')

    If(
        (
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0008)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_557B',
    )

    OP_65(0x0B, 0x0001)

    def _loc_557B(): pass

    label('loc_557B')

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0010)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5590',
    )

    OP_65(0x0C, 0x0001)

    def _loc_5590(): pass

    label('loc_5590')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
